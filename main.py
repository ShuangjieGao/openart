import time
import sensor
import image
import json
from machine import UART
from pyb import LED

white = LED(4)
clock = time.clock()
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
        current_error = self.setpoint - current_value
        p_term = current_error - self.error_last
        i_term = current_error
        d_term = current_error - 2 * self.error_last + self.error_prev
        pid_output = self.Kp * p_term + self.Ki * i_term + self.Kd * d_term
        self.output = self.output + pid_output
        self.output = min(self.output_max, max(self.output_min, self.output))
        self.error_prev = self.error_last
        self.error_last = current_error
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


def check_threshold(lightness, a_channel, b_channel, threshold):
    return (
        (threshold[0] <= lightness <= threshold[1])
        and (threshold[2] <= a_channel <= threshold[3])
        and (threshold[4] <= b_channel <= threshold[5])
    )


def max_blob(blobs):
    return max(blobs, key=lambda b: b.pixels(), default=None)


# TODO: calculate-center
def calculate_center(x, y, w, h):
    x_center = x + w // 2
    y_center = y + h // 2
    return (x_center, y_center)


# TODO: color-thresholds
thresholds = {
    "wall": (20, 100, -128, 127, -80, 127),
    "player": (44, 100, -128, -23, -128, 78),
    "player_front": (),
    "player_back": (),
    "box": (50, 100, -50, 50, 50, 127),
    "goal": (40, 100, 85, 127, -75, -50),
    "bomb": (40, 100, 50, 127, -35, 50),
    "floor": (25, 100, 30, 80, -128, -70),
}
# TODO: display-config
display = {
    "wall": False,
    "player": False,
    "box": True,
    "goal": False,
    "bomb": False,
    "floor": True,
    "grid": False,
    "bin": False,
}
# TODO: brightness-pid-inits
brightness_pid = PIDController(
    Kp=1,
    Ki=3,
    Kd=6,
    setpoint=35,
    output_min=10,
    output_max=20000,
)


while True:
    clock.tick()
    img = sensor.snapshot()
    # TODO: overlay-image
    try:
        overlay_img = image.Image("/sd/img3.bmp")
        img.draw_image(overlay_img, 0, 0, x_scale=1, y_scale=1)
    except Exception:
        pass
    color_img = img.copy()
    # TODO: bin-display
    if display["bin"]:
        binary_img = (
            img.copy().binary(
                [
                    # thresholds["floor"],
                    # thresholds["goal"],
                    # thresholds["bomb"],
                    thresholds["player"],
                    # thresholds["box"],
                ]
            )
            # .median(3)
            .mean(1)
            # .dilate(1)
            # .erode(1)
        )
        img.draw_image(binary_img, 0, 0, x_scale=1, y_scale=1)

    # TODO: brightness-control
    current_lightness = color_img.get_statistics().l_median()
    brightness_output = brightness_pid.update(current_lightness)
    sensor.set_brightness(brightness_output)
    img.draw_string(
        0,
        0,
        str(current_lightness) + "," + str(brightness_output),
        color=(255, 255, 255),
    )

    # TODO: packet-init
    packet = {
        "player_coords": [],
        "box_coords": [],
        "goal_coords": [],
        "bomb_coords": [],
        "floor_corners": [],
        "map_grid": [[0] * 14 for _ in range(10)],
        "valid": False,
    }

    # TODO: wall-processing
    # if display["wall"]:
    #     wall_blobs = color_img.find_blobs(
    #         [thresholds["wall"]],
    #         pixels_threshold=100,
    #         merge=True,
    #         margin=1,
    #     )
    #     wall_blob_max = max_blob(wall_blobs)
    #     if wall_blob_max:
    #         blob = wall_blob_max
    #         if display["wall"]:
    #             img.draw_rectangle(*blob.rect(), color=(0, 255, 0), thickness=1)

    floor_blobs = color_img.find_blobs(
        [thresholds["floor"]],
        pixels_threshold=100,
        merge=True,
        margin=1,
    )
    floor_blob_max = max_blob(floor_blobs)
    # TODO: floor-processing
    if floor_blob_max:
        blob = floor_blob_max
        if display["floor"]:
            img.draw_rectangle(*blob.rect(), color=(0, 255, 0), thickness=1)
        floor_binary_img = (
            color_img.copy()
            .binary(
                [
                    thresholds["floor"],
                    thresholds["goal"],
                    thresholds["bomb"],
                    thresholds["player"],
                    thresholds["box"],
                ]
            )
            .mean(1)
            # .erode(1)
        )
        goal_binary_img = (
            color_img.copy()
            .binary(
                [
                    thresholds["goal"],
                ]
            )
            .erode(1)
        )

        x, y, w, h = blob.rect()
        origin_x = x
        origin_y = y
        delta_x = w / 14.0
        delta_y = h / 10.0
        if delta_x < 10 or delta_y < 10:
            packet["valid"] = False
            continue
        img.draw_string(0, 20, f"{int(delta_x)},{int(delta_y)}", color=(255, 255, 255))
        for col in range(14):
            for row in range(10):
                grid_x = int(origin_x + col * delta_x + delta_x * 0.3)
                grid_y = int(origin_y + row * delta_y + delta_y * 0.3)
                grid_w = int(delta_x - 2 * delta_x * 0.3)
                grid_h = int(delta_y - 2 * delta_y * 0.3)
                roi = (grid_x, grid_y, grid_w, grid_h)

                stats_floor = floor_binary_img.get_statistics(roi=roi)
                ratio_floor_white = stats_floor.l_mean() / 100.0
                stats_goal = goal_binary_img.get_statistics(roi=roi)
                ratio_goal_white = stats_goal.l_mean() / 100.0
                detection_threshold = 0.4

                if ratio_goal_white > detection_threshold:
                    packet["goal_coords"].append((row, col))
                    packet["map_grid"][row][col] = 2
                    if display["grid"]:
                        img.draw_rectangle(*roi, color=(255, 255, 0), fill=True)
                elif ratio_floor_white > detection_threshold:
                    packet["map_grid"][row][col] = 1
                    if display["grid"]:
                        img.draw_rectangle(*roi, color=(0, 255, 0), fill=True)
                else:
                    packet["map_grid"][row][col] = 0

    # TODO: player-processing
    player_blobs = color_img.find_blobs(
        [thresholds["player"]],
        pixels_threshold=10,
        merge=True,
        margin=1,
    )
    player_blob_max = max_blob(player_blobs)
    if player_blob_max:
        blob = player_blob_max
        if display["player"]:
            img.draw_rectangle(*blob.rect(), color=(255, 0, 0), thickness=1)
            angle_deg = blob.rotation_deg()
            angle_rad = blob.rotation_rad()
            # print(f"Player angle: {angle_deg:.2f}° ({angle_rad:.3f} rad)")
            x1, y1, x2, y2 = blob.major_axis_line()
            img.draw_line(x1, y1, x2, y2, color=(255, 255, 0), thickness=2)
    # TODO: box-processing
    box_blobs = color_img.find_blobs(
        [thresholds["box"]],
        pixels_threshold=50,
        merge=False,
        margin=5,
    )
    for b in box_blobs:
        img.draw_rectangle(*b.rect(), color=(0, 255, 0), thickness=1)
        img.draw_string(b.x(), b.y() - 10, str(b.pixels()), color=(0, 255, 0))
    box_blob_max = max_blob(box_blobs)
    if box_blob_max:
        blob = box_blob_max
        # if display["box"]:
        #     img.draw_rectangle(*blob.rect(), color=(0, 255, 0), thickness=1)

    # FIXME:removed undefined `goal_coords` variable; use `packet["goal_coords"]` instead
    if player_blob_max and floor_blob_max:
        x_center, y_center = player_blob_max.cx(), player_blob_max.cy()
        packet["player_coords"] = [
            pixel_to_ratio(x_center, y_center, floor_blob_max.rect())
        ]
    if box_blob_max and floor_blob_max:
        x_center, y_center = box_blob_max.cx(), box_blob_max.cy()
        packet["box_coords"] = [
            pixel_to_ratio(x_center, y_center, floor_blob_max.rect())
        ]
    # TODO: publish-results
    json_str = json.dumps(packet, separators=(",", ":"))
    # # uart.write(json_str + "\r\n")
    # print("Sent:", json_str, "\r\n")
    # TODO: fps-draw
    img.draw_string(0, 10, str(int(clock.fps())), color=(102, 204, 255))
