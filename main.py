# import time
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
    x1, y1 = img.width() / 1, img.height() / 1
    x2, y2 = img.width() / 2, img.height() / 2
    # try:
    #     ld_img = image.Image("/sd/firmware_ready.bmp")
    #     img.draw_image(ld_img, 0, 0, x_scale=0.5, y_scale=0.5)
    # except Exception:
    #     pass
    color_img = img.copy()
    img.binary([thresholds_dict["floor"]])
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
        # roi=wall_blob.rect() if wall_blob else [0, 0, img.width(), img.height()],
        pixels_threshold=100,
        merge=True,
        margin=1,
    )
    floor_blob = find_largest_blob(floor_blobs)
    if floor_blob and display_dict["floor"]:
        img.draw_rectangle(floor_blob.rect(), color=(255, 0, 0), thickness=1)

    map_grid = [[0] * 14 for _ in range(10)]
    for row in range(10):
        for col in range(14):
            if row == 0 or row == 9 or col == 0 or col == 13:
                map_grid[row][col] = 3  # 3表示墙

    goal_coords_list = []
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
