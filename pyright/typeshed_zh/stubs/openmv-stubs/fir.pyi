"""
fir 模块用于控制热传感器。
示例用法:
"""

from typing import Tuple
from typing import List
from typing import Optional
from typing import Any
import image

FIR_NONE: int
"""
无FIR传感器类型。
"""

FIR_SHIELD: int
"""
OpenMV Cam 热电堆扩展板板类型（MLX90621）。
"""

FIR_MLX90621: int
"""
FIR_MLX90621 FIR 传感器。
"""

FIR_MLX90640: int
"""
FIR_MLX90640 FIR 传感器。
"""

FIR_MLX90641: int
"""
FIR_MLX90640 FIR 传感器。
"""

FIR_AMG8833: int
"""
FIR_AMG8833 FIR 传感器。
"""

FIR_LEPTON: int
"""
FIR_LEPTON FIR 传感器。
"""

def init(type=-1,refresh: int | None = None,resolution: int | None = None) -> None:
    """
    使用I/O引脚P4和P5（以及P0、P1、P2、P3用于 fir.FIR_LEPTON）初始化已连接的热电堆扩展板
    type 表示热电堆扩展板的类型：
    默认情况下，type 为 -1，这将导致 fir.init() 根据 I2C 地址自动扫描并初始化连接的热传感器。请注意，fir.FIR_MLX90640 和 fir.FIR_MLX90641 具有相同的 I2C 地址，因此您必须将 fir.FIR_MLX90641 传递给 type 来具体初始化它。
    在 OpenMV Cam Pure Thermal 上，fir.FIR_LEPTON 使用内部 I/O 引脚，而不使用 P0-P5。
    refresh 是热电堆传感器的2的幂刷新率（单位：Hz）：
    resolution 是热电堆传感器的测量分辨率：
    对于 fir.FIR_SHIELD 和 fir.FIR_MLX90621：
    对于 fir.FIR_MLX90640 和 fir.FIR_MLX90641：
    对于 fir.FIR_AMG8833：
    对于 fir.FIR_LEPTON：
    """
    pass
    
    
def deinit() -> None:
    """
    反初始化热传感器，释放资源。
    """
    pass
    
    
def width() -> int:
    """
    返回正在使用的热传感器的宽度（水平分辨率）：
    """
    pass
    
    
def height() -> int:
    """
    返回正在使用的热传感器的高度（垂直分辨率）：
    """
    pass
    
    
def type() -> int:
    """
    返回正在使用的热传感器的类型：
    """
    pass
    
    
def refresh() -> int:
    """
    返回在 fir.init() 调用期间设置的当前刷新率。
    """
    pass
    
    
def resolution() -> int:
    """
    返回在 fir.init() 调用期间设置的当前分辨率。
    """
    pass
    
    
def radiometric() -> bool:
    """
    返回热传感器是否报告准确的温度读数（True 或 False）。如果为 False，则意味着热传感器报告基于其环境温度的相对温度读数，可能不是非常准确。
    """
    pass
    
    
def register_vsync_cb(cb) -> None:
    """
    fir.FIR_LEPTON 模式仅适用于OpenMV Cam Pure Thermal。
    注册回调 cb，以在 FLIR Lepton 生成新帧时（但在帧接收之前）执行（在中断上下文中）。
    通常以9Hz触发。
    cb 不接受参数。
    """
    pass
    
    
def register_frame_cb(cb) -> None:
    """
    fir.FIR_LEPTON 模式仅适用于OpenMV Cam Pure Thermal。
    注册回调 cb，以在 FLIR Lepton 生成新帧并准备好通过 fir.read_ir() 或 fir.snapshot() 读取帧时执行（在中断上下文中）。
    通常以9Hz触发。
    cb 不接受参数。
    使用此功能获取中断以稍后使用 micropython.schedule() 读取帧。
    """
    pass
    
    
def get_frame_available() -> bool:
    """
    如果可以通过调用 fir.read_ir() 或 fir.snapshot() 读取帧，则返回 True。
    """
    pass
    
    
def trigger_ffc(timeout=-1) -> None:
    """
    仅适用于 fir.FIR_LEPTON 模式。
    触发 FLIR Lepton 上的平坦场校正过程，该过程校准热像。传感器会自动执行此过程。但是，您可以调用此函数来强制执行该过程。
    timeout 如果不是-1，则等待FFC完成的毫秒数。
    """
    pass
    
    
def read_ta() -> float:
    """
    返回环境温度（即传感器温度）。
    例子:
    返回的值是表示摄氏度的浮点数。
    """
    pass
    
    
def read_ir(hmirror=False,vflip=False,transpose=False,timeout=-1):
    """
    返回一个元组，其中包含环境温度（即传感器温度）、温度列表（宽度*高度）、观察到的最低温度和观察到的最高温度。
    hmirror 如果设置为True，则水平镜像 ir 数组。
    vflip 如果设置为True，则垂直翻转 ir 数组。
    transpose 如果设置为True，则转置 ir 数组。
    timeout 如果不是-1，则等待新帧的毫秒数。
    如果要旋转图像的角度为90的倍数，则传递以下内容:
    例子:
    返回的值时表示摄氏度的浮点数。
    """
    pass
    
    
def draw_ir(image: image.Image,ir,x: int | None = None,y: int | None = None,x_scale=1.0,y_scale=1.0,roi: Tuple[int, int, int, int] | None = None,rgb_channel=-1,alpha=128,color_palette=image.PALETTE_RAINBOW,alpha_palette=-1,hint=0,scale=Optional[Tuple[float, float]]) -> None:
    """
    在 image 上绘制一个 ir 数组，其左上角从位置x、y开始。此方法会自动将传入的图像呈现为图像的正确像素格式，同时无缝处理裁剪。
    x_scale 控制图像在 x 方向的显示比例（float）。如果此值为负，则图像将水平翻转。注意，如果未指定 y_scale，则它将与 x_scale 匹配，以保持纵横比。
    y_scale 控制图像在 y 方向的显示比例（float）。如果此值为负，则图像将垂直翻转。注意，如果未指定 x_scale，则它将与 x_scale 匹配，以保持纵横比。
    roi 是源图像要绘制的感兴趣区域的矩形元组（x、y、w、h）。这允许您仅提取感兴趣区域中的像素以在目标图像上进行缩放和绘制。
    rgb_channel 是要从 RGB565 图像中提取（如果传递）并渲染到目标图像上的 RGB 通道（0=R，G=1，B=2）。例如，如果传递 rgb_channel=1，则会提取源 RGB565 图像的绿色通道，并将其以灰度形式绘制到目标图像上。
    alpha 控制要混合到目标图像中的源图像的程度。256 的值绘制不透明的源图像，而低于 256 的值会在源图像和目标图像之间产生混合。0 表示不对目标图像进行修改。
    color_palette 如果不是 -1 ，可以是 image.PALETTE_RAINBOW 、 image.PALETTE_IRONBOW ，或者总像素 256 的 RGB565 图像，用作对源图像的灰度值进行颜色查找表。如果使用，此操作将在 rgb_channel 提取之后应用。
    alpha_palette 如果不是 -1，可以是总像素256 的 GRAYSCALE 图像，用作调制被绘制到像素级别的源图像的 alpha 值的 alpha 调色板，从而允许您根据它们的灰度值精确控制像素的 alpha 值。在 alpha 查找表中的像素值为 255 时是不透明的，小于 255 的任何值都会变得更透明，直到 0。如果使用，此操作将在 rgb_channel 提取之后应用。
    hint 可以是标志的逻辑 OR：
    scale 是一个两个值的元组，它控制最小和最大温度（一摄氏度为单位）以缩放 ir 图像。默认情况下，它等于图像 ir 的最小值和 ir 的最大值。
    如果未指定x/y，则图像将居中显示在视野中。如果未指定x_scale/y_scale或x_size/y_size，则 ir 数组将被缩放以适应 image 上。
    """
    pass
    
    
def snapshot(hmirror=False,vflip=False,transpose=False,x_scale=1.0,y_scale=1.0,roi: Tuple[int, int, int, int] | None = None,rgb_channel=-1,alpha=128,color_palette=image.PALETTE_RAINBOW,alpha_palette=None,hint=0,scale: Tuple[float, float] | None = None,pixformat=image.RGB565,copy_to_fb=False,timeout=-1) -> image.Image:
    """
    类似于 sensor.snapshot()，返回一个 image 对象，其类型为 image.GRAYSCALE`（灰度）或 `image.RGB565`（彩色）。如果 ``copy_to_fb` 为 False，则在 MicroPython 堆上分配新图像。但是，MicroPython 堆有限，如果耗尽空间，则可能无法存储新图像。相反，将 copy_to_fb 设置为 True，将帧缓冲区设置为新图像，使此函数的工作方式与 sensor.snapshot() 相同。
    hmirror 如果设置为True，则水平镜像新图像。
    vflip 如果设置为True，则垂直翻转新图像。
    transpose 如果设置为True，则转置新图像。
    如果要旋转图像的角度为90的倍数，则传递以下内容:
    x_scale 控制图像在 x 方向的显示比例（float）。如果此值为负，则图像将水平翻转。注意，如果未指定 y_scale，则它将与 x_scale 匹配，以保持纵横比。
    y_scale 控制图像在 y 方向的显示比例（float）。如果此值为负，则图像将垂直翻转。注意，如果未指定 x_scale，则它将与 x_scale 匹配，以保持纵横比。
    roi 是源图像要绘制的感兴趣区域的矩形元组（x、y、w、h）。这允许您仅提取感兴趣区域中的像素以在目标图像上进行缩放和绘制。
    rgb_channel 是要从 RGB565 图像中提取（如果传递）并渲染到目标图像上的 RGB 通道（0=R，G=1，B=2）。例如，如果传递 rgb_channel=1，则会提取源 RGB565 图像的绿色通道，并将其以灰度形式绘制到目标图像上。
    alpha 控制要混合到目标图像中的源图像的程度。256 的值绘制不透明的源图像，而低于 256 的值会在源图像和目标图像之间产生混合。0 表示不对目标图像进行修改。
    color_palette 如果不是 -1 ，可以是 image.PALETTE_RAINBOW 、 image.PALETTE_IRONBOW ，或者总像素 256 的 RGB565 图像，用作对源图像的灰度值进行颜色查找表。如果使用，此操作将在 rgb_channel 提取之后应用。
    alpha_palette 如果不是 -1，可以是总像素256 的 GRAYSCALE 图像，用作调制被绘制到像素级别的源图像的 alpha 值的 alpha 调色板，从而允许您根据它们的灰度值精确控制像素的 alpha 值。在 alpha 查找表中的像素值为 255 时是不透明的，小于 255 的任何值都会变得更透明，直到 0。如果使用，此操作将在 rgb_channel 提取之后应用。
    hint 可以是标志的逻辑 OR：
    scale 是一个两个值的元组，它控制最小和最大温度（一摄氏度为单位）以缩放 ir 图像。默认情况下，它等于图像 ir 的最小值和 ir 的最大值。
    如果指定了 pixformat，则控制最终图像的像素格式。
    timeout 如果不是-1，则等待新帧的毫秒数。
    返回一个图像对象。
    """
    pass
    
    
