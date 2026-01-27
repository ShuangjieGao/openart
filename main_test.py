import image
import sensor

sensor.reset()
sensor.set_pixformat(sensor.RGB565)
sensor.set_framesize(sensor.QQVGA)
sensor.set_auto_gain(False)
sensor.set_auto_whitebal(False)
sensor.set_auto_exposure(False, 1)
sensor.set_brightness(1)


class PIDController:
    """
    标准 PID 控制器 - 增量式实现

    用法：
        pid = PIDController(Kp=1, Ki=3, Kd=6, setpoint=40, output_min=10, output_max=65535)
        output = pid.update(current_value)
    """

    def __init__(self, Kp=1, Ki=3, Kd=6, setpoint=0, output_min=0, output_max=100):
        """
        初始化 PID 控制器

        Args:
            Kp: 比例系数
            Ki: 积分系数
            Kd: 微分系数
            setpoint: 目标值
            output_min: 输出最小值
            output_max: 输出最大值
        """
        self.Kp = Kp
        self.Ki = Ki
        self.Kd = Kd
        self.setpoint = setpoint
        self.output_min = output_min
        self.output_max = output_max

        # 状态变量
        self.error_last = 0
        self.error_prev = 0
        self.output = 0

    def update(self, current_value):
        """
        更新 PID 控制器并返回输出值

        Args:
            current_value: 当前反馈值

        Returns:
            输出值
        """
        # 计算当前误差 e(k) = SP - PV
        error_current = self.setpoint - current_value

        # 计算 PID 三项
        # P项：比例项
        p_term = error_current - self.error_last

        # I项：积分项
        i_term = error_current

        # D项：微分项
        d_term = error_current - 2 * self.error_last + self.error_prev

        # 计算 PID 输出
        pid_output = self.Kp * p_term + self.Ki * i_term + self.Kd * d_term

        # 累加到当前输出值
        self.output = self.output + pid_output

        # 限制输出范围
        self.output = min(self.output_max, max(self.output_min, self.output))

        # 更新误差变量
        self.error_prev = self.error_last
        self.error_last = error_current

        return int(self.output)

    def reset(self):
        """重置 PID 控制器状态"""
        self.error_last = 0
        self.error_prev = 0
        self.output = 0


brightness_pid = PIDController(
    Kp=1,
    Ki=3,
    Kd=6,
    setpoint=40,
    output_min=10,
    output_max=65535,
)


def find_largest_blob(blobs):
    """从blob列表中找到最大的blob"""
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
    "floor": (25, 100, 40, 80, -128, -80)
    #(0, 50, 26, 127, -128, -66),
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
