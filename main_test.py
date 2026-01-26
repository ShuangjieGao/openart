import image
import sensor

sensor.reset()
sensor.set_pixformat(sensor.RGB565)
sensor.set_framesize(sensor.QQVGA)
sensor.set_auto_gain(True)
sensor.set_auto_whitebal(True)
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


while True:
    img = sensor.snapshot()
    # try:
    #     ld_img = image.Image("/sd/img6.bmp")
    #     img.draw_image(ld_img, 0, 0, x_scale=1, y_scale=1)
    # except Exception:
    #     pass
    color_img = img.copy()
    current_lightness = color_img.get_statistics().l_median()
    brightness_output = brightness_pid.update(current_lightness)
    sensor.set_brightness(brightness_output)
    blobs = color_img.find_blobs(
        [(40, 100, -3, 127, -51, 127), (0, 50, 25, 127, -128, -75)],
        pixels_threshold=15,
        merge=True,
        margin=5,
    )
    # img.binary([(40, 100, -3, 127, -51, 127), (0, 50, 25, 127, -128, -75)])
    for blob in blobs:
        x, y, w, h = blob.rect()
        step = w / 16.0
        base_x = x
        base_y = y+h-12*step

        img.draw_rectangle((int(base_x),int(base_y),w,int(12*step)), color=(0, 255, 0), thickness=2)

    print(current_lightness, brightness_output)
