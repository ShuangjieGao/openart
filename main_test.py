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


def max_blob(blobs):
    return max(blobs, key=lambda b: b.pixels(), default=None)


def calculate_center(x, y, w, h):
    center_x = x + w // 2
    center_y = y + h // 2
    return (center_x, center_y)


thresholds = {
    "wall": (20, 100, -128, 127, -80, 127),
    "player": (44, 100, -128, -23, -128, 78),
    "player_front": (),
    "player_back": (),
    "box": (65, 100, -50, 50, 50, 127),
    "goal": (40, 100, 85, 127, -75, -50),
    "bomb": (40, 100, 50, 127, -35, 50),
    "floor": (25, 100, 30, 80, -128, -70),
}

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
        ld_img = image.Image("/sd/img6.bmp")
        img.draw_image(ld_img, 0, 0, x_scale=1, y_scale=1)
    except Exception:
        pass
    color_img = img.copy()
    img.median(1)
    # binary_img = img.binary([thresholds_dict["floor"]])
    current_lightness = color_img.get_statistics().l_median()
    brightness_output = brightness_pid.update(current_lightness)
    sensor.set_brightness(brightness_output)
    print(current_lightness, brightness_output)

    # blobs = color_img.find_blobs(
    #     [thresholds_dict["floor"]],
    #     pixels_threshold=15,
    #     merge=True,
    #     margin=1,
    # )
    # largest_blob = find_largest_blob(blobs)
    # if largest_blob:
    #     blob = largest_blob
    #     img.draw_rectangle(blob.rect(), color=(255, 0, 0), thickness=2)
    #     min_corners = blob.min_corners()
    #     for corner in min_corners:
    #         img.draw_circle(corner[0], corner[1], 3, color=(0, 0, 255), thickness=2)
    #     x, y, w, h = blob.rect()
    #     step_x = w / 14.0
    #     step_y = h / 10.0
    #     base_x = x
    #     base_y = y

    #     for col in range(14):
    #         for row in range(10):
    #             grid_x = int(base_x + col * step_x)
    #             grid_y = int(base_y + row * step_y)
    #             grid_w = int(step_x)
    #             grid_h = int(step_y)

    #             # 边界检查
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

    #             img.draw_rectangle(roi, color=(0, 255, 0), thickness=1)

    print(current_lightness, brightness_output)
