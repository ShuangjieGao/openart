import time
import sensor
import image
import json
from machine import UART

sensor.reset()
sensor.set_pixformat(sensor.RGB565)
sensor.set_framesize(sensor.QQVGA)
sensor.set_auto_gain(False)
sensor.set_auto_whitebal(False)
sensor.set_auto_exposure(False, 1)
sensor.set_brightness(1)
try:
    uart = UART(12, baudrate=115200)
except Exception:
    uart = UART(2, baudrate=115200)


class PIDController:
    def __init__(self, Kp=1, Ki=3, Kd=6, setpoint=0, output_min=0, output_max=100):
        self.Kp = Kp
        self.Ki = Ki
        self.Kd = Kd
        self.setpoint = setpoint
        self.output_min = output_min
        self.output_max = output_max
        self.error_last = 0
        self.error_prev = 0
        self.output = 0

    def update(self, current_value):
        error_current = self.setpoint - current_value
        p_term = error_current - self.error_last
        i_term = error_current
        d_term = error_current - 2 * self.error_last + self.error_prev
        pid_output = self.Kp * p_term + self.Ki * i_term + self.Kd * d_term
        self.output = self.output + pid_output
        self.output = min(self.output_max, max(self.output_min, self.output))
        self.error_prev = self.error_last
        self.error_last = error_current
        return int(self.output)

    def reset(self):
        self.error_last = 0
        self.error_prev = 0
        self.output = 0


def pixel_to_ratio(
    x,
    y,
    reference_rect=None,
    img_width=160,
    img_height=120,
    target_width=320,
    target_height=240,
):

    if reference_rect:
        ref_x, ref_y, ref_w, ref_h = reference_rect
        x_norm = (x - ref_x) / ref_w if ref_w > 0 else 0
        y_norm = (y - ref_y) / ref_h if ref_h > 0 else 0
    else:
        x_norm = x / img_width
        y_norm = y / img_height
    x_norm = max(0, min(1, x_norm))
    y_norm = max(0, min(1, y_norm))
    x_ratio = x_norm * target_width
    y_ratio = y_norm * target_height
    return (x_ratio, y_ratio)


def check_color_in_threshold(L, A, B, threshold):
    return (
        (threshold[0] <= L <= threshold[1])
        and (threshold[2] <= A <= threshold[3])
        and (threshold[4] <= B <= threshold[5])
    )


def process_grid_cell(img, roi, thresholds_dict):
    stats = img.get_statistics(roi=roi)
    l, a, b = stats.l_mode(), stats.a_mode(), stats.b_mode()
    is_goal = check_color_in_threshold(l, a, b, thresholds_dict["goal"])
    is_floor = check_color_in_threshold(l, a, b, thresholds_dict["floor"])
    if is_goal:
        return 2
    elif is_floor:
        return 1
    else:
        return 0


def build_packet(player_blob, box_blob, goal_coords_list, floor_corners):
    packet = {
        "player_coords": None,
        "box_coords": None,
        "goal_coords": None,
        "floor_corners": None,
    }

    if floor_corners:
        packet["floor_corners"] = floor_corners

    if goal_coords_list:
        packet["goal_coords"] = goal_coords_list
    if player_blob:
        center = (player_blob.cx(), player_blob.cy())
        if center:
            packet["player_coords"] = center
    if box_blob:
        center = (box_blob.cx(), box_blob.cy())
        if center:
            packet["box_coords"] = center

    return packet


def find_largest_blob(blobs):
    if not blobs:
        return None

    largest = None
    max_pixels = 0

    for blob in blobs:
        if blob.pixels() > max_pixels:
            max_pixels = blob.pixels()
            largest = blob

    return largest


def extract_floor_corners(blob):
    """
    从floor blob提取四个角点

    Args:
        blob: OpenMV blob对象

    Returns:
        tuple: ((x0, y0), (x1, y1), (x2, y2), (x3, y3))
               分别为左上、右上、右下、左下角点
               如果blob无效则返回None
    """
    if not blob:
        return None

    try:
        x, y, w, h = blob.rect()
        # 左上、右上、右下、左下
        corners = (
            (x, y),  # 左上
            (x + w, y),  # 右上
            (x + w, y + h),  # 右下
            (x, y + h),  # 左下
        )
        return corners
    except Exception:
        return None


def bilinear_interpolate(corners, row, col, grid_rows=10, grid_cols=14):
    """
    使用双线性插值计算网格单元的图像坐标

    Args:
        corners: 四个角点坐标 ((x0,y0), (x1,y1), (x2,y2), (x3,y3))
        row: 网格行索引 (0-9)
        col: 网格列索引 (0-13)
        grid_rows: 网格总行数
        grid_cols: 网格总列数

    Returns:
        tuple: (x, y) 图像像素坐标
    """
    # 归一化网格坐标到[0, 1]
    u = col / (grid_cols - 1)
    v = row / (grid_rows - 1)

    # 提取四个角点
    # P00 = 左上, P10 = 右上, P01 = 左下, P11 = 右下
    x0, y0 = corners[0]  # 左上
    x1, y1 = corners[1]  # 右上
    x2, y2 = corners[2]  # 右下
    x3, y3 = corners[3]  # 左下

    # 双线性插值公式
    # P(u, v) = (1-u)(1-v)P00 + u(1-v)P10 + (1-u)vP01 + uvP11
    x = (1 - u) * (1 - v) * x0 + u * (1 - v) * x1 + (1 - u) * v * x3 + u * v * x2
    y = (1 - u) * (1 - v) * y0 + u * (1 - v) * y1 + (1 - u) * v * y3 + u * v * y2

    return (int(x), int(y))


def sample_grid_cell(img, x, y, sample_size=3):
    """
    在指定像素位置采样颜色

    Args:
        img: OpenMV图像对象
        x: 中心x坐标
        y: 中心y坐标
        sample_size: 采样区域大小（默认3x3像素）

    Returns:
        tuple: (L, A, B) LAB颜色值
               如果采样失败返回None
    """
    # 计算ROI
    roi_x = x - sample_size // 2
    roi_y = y - sample_size // 2
    roi_w = sample_size
    roi_h = sample_size

    # 边界裁剪
    roi_x = max(0, roi_x)
    roi_y = max(0, roi_y)
    roi_w = min(roi_w, img.width() - roi_x)
    roi_h = min(roi_h, img.height() - roi_y)

    # 检查ROI有效性
    if roi_w <= 0 or roi_h <= 0:
        return None

    try:
        # 获取统计值
        stats = img.get_statistics(roi=(roi_x, roi_y, roi_w, roi_h))
        return (stats.l_mode(), stats.a_mode(), stats.b_mode())
    except Exception:
        return None


def classify_color(L, A, B, thresholds_dict):
    """
    分类颜色类型

    Args:
        L, A, B: LAB颜色值
        thresholds_dict: 颜色阈值字典

    Returns:
        int: 2=goal, 1=floor, 0=wall
    """
    if check_color_in_threshold(L, A, B, thresholds_dict["goal"]):
        return 2
    elif check_color_in_threshold(L, A, B, thresholds_dict["floor"]):
        return 1
    else:
        return 0


def build_map_grid(img, floor_blob, thresholds_dict):
    """
    构建完整的10x14地图网格

    Args:
        img: OpenMV图像对象
        floor_blob: 检测到的floor blob
        thresholds_dict: 颜色阈值字典

    Returns:
        tuple: (map_grid, goal_coords_list)
               map_grid: 10x14二维数组
               goal_coords_list: goal单元坐标列表
    """
    # 初始化10x14数组，所有值为0
    map_grid = [[0] * 14 for _ in range(10)]

    # 设置边界为wall (值3)
    for row in range(10):
        for col in range(14):
            if row == 0 or row == 9 or col == 0 or col == 13:
                map_grid[row][col] = 3

    goal_coords_list = []

    # 如果floor_blob为None，返回初始状态
    if not floor_blob:
        print("Warning: Invalid floor blob")
        return (map_grid, goal_coords_list)

    # 提取floor角点
    corners = extract_floor_corners(floor_blob)
    if not corners:
        print("Warning: Invalid corner points")
        return (map_grid, goal_coords_list)

    # 遍历内部网格单元 (1 <= row <= 8, 1 <= col <= 12)
    for row in range(1, 9):
        for col in range(1, 13):
            try:
                # 使用双线性插值计算(x, y)
                x, y = bilinear_interpolate(corners, row, col)

                # 采样颜色获取(L, A, B)
                lab_values = sample_grid_cell(img, x, y)

                # 如果采样失败，跳过该单元
                if not lab_values:
                    continue

                L, A, B = lab_values

                # 分类颜色类型
                cell_type = classify_color(L, A, B, thresholds_dict)

                # 更新map_grid
                map_grid[row][col] = cell_type

                # 如果是goal类型，添加到goal_coords_list
                if cell_type == 2:
                    goal_coords_list.append([row, col])

            except Exception as e:
                print("Warning: Failed to sample cell at ({}, {})".format(row, col))
                continue

    return (map_grid, goal_coords_list)


thresholds_dict = {
    "wall": (40, 100, -3, 127, -51, 127),
    "player": (44, 100, -128, -23, -128, 78),
    "player_front": (),
    "player_back": (),
    "box": (49, 100, -31, 1, 32, 127),
    "goal": (50, 72, 80, 98, -70, -15),
    "bomb": (50, 100, 75, 127, -55, 127),
    # (0, 30, 0, 127, -128, 127) (40, 100, 55, 127, -50, 50)
    "floor": (0, 50, 26, 127, -128, -66),
    # (25, 50, 25, 127, -128, -50)
    #   (0, 50, 25, 127, -128, -75)
}

display_dict = {
    "wall": True,
    "player": False,
    "box": False,
    "goal": True,
    "bomb": False,
    "floor": True,
    "grid": False,
}

brightness_pid = PIDController(
    Kp=1,
    Ki=3,
    Kd=6,
    setpoint=40,
    output_min=10,
    output_max=20000,
)

while True:
    img = sensor.snapshot()
    # try:
    #     ld_img = image.Image("/sd/firmware_ready.bmp")
    #     img.draw_image(ld_img, 0, 0, x_scale=0.5, y_scale=0.5)
    # except Exception:
    #     pass
    color_img = img.copy()
    binary_img = img.binary([thresholds_dict["floor"]])
    current_lightness = color_img.get_statistics().l_median()
    brightness_output = brightness_pid.update(current_lightness)
    sensor.set_brightness(brightness_output)
    print(current_lightness, brightness_output)

    # wall_blobs = color_img.find_blobs(
    #     [thresholds_dict["floor"]], pixels_threshold=15, merge=True, margin=1
    # )
    # wall_blob = find_largest_blob(wall_blobs)
    # if wall_blob and display_dict["wall"]:
    #     img.draw_rectangle(wall_blob.rect(), color=(0, 0, 255), thickness=2)
    #     img.draw_circle(
    #         wall_blob.cx(), wall_blob.cy(), 2, color=(255, 0, 0), thickness=2
    #     )

    floor_blobs = color_img.find_blobs(
        [thresholds_dict["floor"]],
        pixels_threshold=100,
        merge=True,
        margin=1,
    )
    largest_floor_blob = find_largest_blob(floor_blobs)
    if largest_floor_blob and display_dict["floor"]:
        img.draw_rectangle(largest_floor_blob.rect(), color=(255, 0, 0), thickness=1)

    # 使用双线性插值构建地图网格
    map_grid, goal_coords_list = build_map_grid(color_img, largest_floor_blob, thresholds_dict)

    # 可选：绘制网格线用于调试
    if largest_floor_blob and display_dict["grid"]:
        corners = extract_floor_corners(largest_floor_blob)
        if corners:
            # 绘制网格线
            for row in range(10):
                for col in range(14):
                    x, y = bilinear_interpolate(corners, row, col)
                    img.draw_circle(x, y, 1, color=(0, 255, 0))

            # 绘制goal位置
            for goal_row, goal_col in goal_coords_list:
                x, y = bilinear_interpolate(corners, goal_row, goal_col)
                img.draw_cross(x, y, color=(255, 255, 0), size=3, thickness=1)

    floor_cells = []

    # if floor_blob:
    #     x, y, w, h = floor_blob.rect()
    #     step = w / 14.0
    #     base_x = x
    #     base_y = y

    #     # img.draw_rectangle(floor_blob.rect(), color=(0, 255, 0), thickness=1)
    #     for col in range(14):
    #         for row in range(10):
    #             grid_x = int(base_x + col * w / 14.0)
    #             grid_y = int(base_y + row * w / 14.0)
    #             grid_w = int(w / 14.0)
    #             grid_h = int(w / 14.0)

    #             if grid_x < 0:
    #                 grid_x = 0
    #             if grid_y < 0:
    #                 grid_y = 0
    #             if grid_x + grid_w > img.width():
    #                 grid_w = img.width() - grid_x
    #             if grid_y + grid_h > img.height():
    #                 grid_h = img.height() - grid_y

    #             if grid_w <= 0 or grid_h <= 0:
    #                 continue

    #             roi = (grid_x, grid_y, grid_w, grid_h)

    #             # img.draw_rectangle(roi, color=(255, 0, 0), thickness=1)

    #             cell_type, is_goal, is_floor = process_grid_cell(
    #                 img, roi, thresholds_dict
    #             )

    #             map_grid[row][col] = cell_type

    #             if is_goal:
    #                 goal_coords_list.append([row, col])
    #             elif is_floor:
    #                 floor_cells.append((row, col))
    # # 玩家检测
    # player_blob = detect_player(
    #     color_img, thresholds_dict["player"], pixels_threshold=15, merge=True, margin=5
    # )
    # # 箱子检测
    # box_blob = detect_box(
    #     color_img, thresholds_dict["box"], pixels_threshold=5, merge=False, margin=5
    # )

    # # 墙检测
    # wall_blob = detect_wall(
    #     color_img,
    #     thresholds_dict["wall"],
    #     pixels_threshold=15,
    #     merge=True,
    #     margin=5,
    # )

    # map_grid, goal_coords_list, floor_cells, base_x, base_y, step = (
    #     detect_grid_and_floor(color_img, wall_blob, thresholds_dict, display_dict)
    # )

    # if player_blob and display_dict["player"]:
    #     draw_blob_circle(
    #         color_img, player_blob, color=(255, 255, 255), radius=2, thickness=2
    #     )
    # if box_blob and display_dict["box"]:
    #     draw_blob_circle(color_img, box_blob, color=(0, 255, 0), radius=3, thickness=2)

    # # 数据包构建和发送
    # packet = build_packet(player_blob, box_blob, goal_coords_list, stable_floor_corners)
    # json_str = json.dumps(packet, separators=(",", ":"))
    # # uart.write(json_str + "\r\n")
    # print("Sent:", json_str, "\r\n")
