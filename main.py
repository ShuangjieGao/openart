import time
import sensor
import image
import json
from machine import UART
from pyb import LED

white = LED(4)
# white.on()
sensor.reset()
sensor.set_pixformat(sensor.RGB565)
sensor.set_framesize(sensor.QQVGA)
sensor.set_auto_whitebal(False)
sensor.set_auto_gain(False)
sensor.set_auto_exposure(False, 1)
sensor.skip_frames(time=2000)
sensor.set_brightness(1000)
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
        rx, ry, rw, rh = reference_rect
        x_norm = (x - rx) / rw if rw > 0 else 0
        y_norm = (y - ry) / rh if rh > 0 else 0
    else:
        x_norm = x / img_width if img_width > 0 else 0
        y_norm = y / img_height if img_height > 0 else 0
    x_norm = max(0.0, min(1.0, x_norm))
    y_norm = max(0.0, min(1.0, y_norm))
    return (x_norm * target_width, y_norm * target_height)


def check_threshold(L, A, B, threshold):
    return (
        (threshold[0] <= L <= threshold[1])
        and (threshold[2] <= A <= threshold[3])
        and (threshold[4] <= B <= threshold[5])
    )


def build_packet(
    player_blob, box_blob, goal_coords_list, floor_corners, reference_rect=None
):
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
        center_x, center_y = player_blob.cx(), player_blob.cy()
        packet["player_coords"] = pixel_to_ratio(center_x, center_y, reference_rect)

    if box_blob:
        center_x, center_y = box_blob.cx(), box_blob.cy()
        packet["box_coords"] = pixel_to_ratio(center_x, center_y, reference_rect)

    return packet


def find_largest_blob(blobs):
    return max(blobs, key=lambda b: b.pixels(), default=None)


def calculate_center(x, y, w, h):
    center_x = x + w // 2
    center_y = y + h // 2
    return (center_x, center_y)


thresholds_dict = {
    "wall": (20, 100, -128, 127, -80, 127),
    # (40, 100, -3, 127, -51, 127),
    "player": (44, 100, -128, -23, -128, 78),
    "player_front": (),
    "player_back": (),
    "box": (65, 100, -50, 50, 50, 127),
    # (49, 100, -31, 1, 32, 127),
    "goal": (40, 100, 85, 127, -75, -50),
    # (0, 100, 45, 127, -80, -30),
    # (0, 100, 85, 127, -128, -30),
    # (40, 100, 75, 127, -95, -35),
    # (50, 72, 80, 98, -70, -15),
    # (40, 100, 75, 127, -95, -35)
    "bomb": (40, 100, 50, 127, -35, 50),
    # (45, 100, 65, 127, -5, 127),
    # (50, 100, 75, 127, -55, 127),
    # (0, 30, 0, 127, -128, 127),
    # (40, 100, 55, 127, -50, 50)
    "floor": (25, 100, 30, 80, -128, -70),
    # (25, 100, 40, 80, -128, -80),
    # (0, 50, 26, 127, -128, -66),
    # (25, 50, 25, 127, -128, -50)
    # (0, 50, 25, 127, -128, -75)
}

display_dict = {
    "wall": False,
    "player": True,
    "box": False,
    "goal": False,
    "bomb": False,
    "floor": True,
    "grid": False,
    "bin": False,
}

brightness_pid = PIDController(
    Kp=1,
    Ki=3,
    Kd=6,
    setpoint=35,
    output_min=10,
    output_max=20000,
)


while True:
    img = sensor.snapshot()
    try:
        ld_img = image.Image("/sd/img2.bmp")
        img.draw_image(ld_img, 0, 0, x_scale=1, y_scale=1)
    except Exception:
        pass
    color_img = img.copy()  # 保留原始图像
    # flat_field = image.Image("bin.bmp")
    # corrected_img = img.div(flat_field, shift_bits=8)
    if display_dict["bin"]:
        binary_img = (
            img.copy().binary(
                [
                    # thresholds_dict["floor"],
                    # thresholds_dict["goal"],
                    # thresholds_dict["bomb"],
                    thresholds_dict["player"],
                    # thresholds_dict["box"],
                ]
            )
            # .median(3)
            .mean(1)
            # .dilate(1)
            # .erode(1)
        )
        img.draw_image(binary_img, 0, 0, x_scale=1, y_scale=1)
    current_lightness = color_img.get_statistics().l_median()
    brightness_output = brightness_pid.update(current_lightness)
    sensor.set_brightness(brightness_output)
    print(current_lightness, brightness_output)
    if display_dict["wall"]:
        wall_blobs = color_img.find_blobs(
            [thresholds_dict["wall"]],
            pixels_threshold=100,
            merge=True,
            margin=1,
        )
        largest_wall_blob = find_largest_blob(wall_blobs)
        if largest_wall_blob:
            blob = largest_wall_blob
            if display_dict["wall"]:
                img.draw_rectangle(blob.rect(), color=(0, 255, 0), thickness=1)
    floor_blobs = color_img.find_blobs(
        [thresholds_dict["floor"]],
        pixels_threshold=100,
        merge=True,
        margin=1,
    )
    largest_floor_blob = find_largest_blob(floor_blobs)

    if largest_floor_blob:
        blob = largest_floor_blob
        print(blob.pixels())
        if display_dict["floor"]:
            img.draw_rectangle(blob.rect(), color=(0, 255, 0), thickness=1)
        x, y, w, h = blob.rect()
        step_x = w / 14.0
        step_y = h / 10.0
        base_x = x
        base_y = y

        # 创建二值化图像用于快速判断
        floor_binary_img = (
            color_img.copy()
            .binary(
                [
                    thresholds_dict["floor"],
                    thresholds_dict["goal"],
                    thresholds_dict["bomb"],
                    thresholds_dict["player"],
                    thresholds_dict["box"],
                ]
            )
            .mean(1)
            # .erode(1)
        )
        goal_binary_img = (
            color_img.copy()
            .binary(
                [
                    thresholds_dict["goal"],
                ]
            )
            .erode(1)
        )

        map_grid = [[0] * 14 for _ in range(10)]
        goal_coords_list = []
        for col in range(14):
            for row in range(10):
                grid_x = int(base_x + col * step_x + step_x * 0.3)
                grid_y = int(base_y + row * step_y + step_y * 0.3)
                grid_w = int(step_x - step_x * 0.6)
                grid_h = int(step_y - step_y * 0.6)

                # 边界检查
                if grid_x < 0:
                    grid_x = 0
                if grid_y < 0:
                    grid_y = 0
                if grid_x + grid_w > img.width():
                    grid_w = img.width() - grid_x
                if grid_y + grid_h > img.height():
                    grid_h = img.height() - grid_y
                if grid_w <= 0 or grid_h <= 0:
                    continue

                roi = (grid_x, grid_y, grid_w, grid_h)
                floor_stats = floor_binary_img.get_statistics(roi=roi)
                floor_white_ratio = floor_stats.l_mean() / 100.0
                goal_stats = goal_binary_img.get_statistics(roi=roi)
                goal_white_ratio = goal_stats.l_mean() / 100.0
                threshold = 0.4

                if goal_white_ratio > threshold:
                    # Calculate center of the grid cell
                    center_x, center_y = calculate_center(
                        grid_x, grid_y, grid_w, grid_h
                    )
                    # Convert to ratio coordinates using the floor blob as reference
                    goal_coords = pixel_to_ratio(
                        center_x, center_y, reference_rect=blob.rect()
                    )
                    goal_coords_list.append(goal_coords)

                    map_grid[row][col] = 2
                    if display_dict["grid"]:
                        img.draw_rectangle(
                            roi, color=(255, 255, 0), thickness=1, fill=True
                        )
                elif floor_white_ratio > threshold:
                    map_grid[row][col] = 1
                    if display_dict["grid"]:
                        img.draw_rectangle(
                            roi, color=(0, 255, 0), thickness=1, fill=True
                        )
                else:
                    map_grid[row][col] = 0
    # 玩家检测
    player_blobs = color_img.find_blobs(
        [thresholds_dict["player"]],
        pixels_threshold=10,
        merge=True,
        margin=1,
    )
    largest_player_blob = find_largest_blob(player_blobs)
    if largest_player_blob:
        blob = largest_player_blob
        if display_dict["player"]:
            img.draw_rectangle(blob.rect(), color=(255, 0, 0), thickness=1)
            print(blob.pixels())
            angle_deg = blob.rotation_deg()
            angle_rad = blob.rotation_rad()
            print(f"Player angle: {angle_deg:.2f}° ({angle_rad:.3f} rad)")
            x1, y1, x2, y2 = blob.major_axis_line()
            img.draw_line((x1, y1, x2, y2), color=(255, 255, 0), thickness=2)
    # 箱子检测
    box_blobs = color_img.find_blobs(
        [thresholds_dict["box"]],
        pixels_threshold=10,
        merge=True,
        margin=1,
    )
    largest_box_blob = find_largest_blob(box_blobs)
    if largest_box_blob:
        blob = largest_box_blob
        if display_dict["box"]:
            img.draw_rectangle(blob.rect(), color=(0, 255, 0), thickness=1)

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
