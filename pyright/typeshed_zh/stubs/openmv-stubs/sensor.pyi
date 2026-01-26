"""
sensor 模块用于拍照。
示例用法:
"""

from typing import Tuple
from typing import List
from typing import Optional
from typing import Any
import image

BINARY: int
"""
二进制（位图）像素格式。每个像素为1位。
此格式对于掩码存储很有用。可以与 Image() 和 sensor.alloc_extra_fb() 一起使用。
"""

GRAYSCALE: int
"""
灰度像素格式（来自YUV422的Y）。每个像素为8位，1字节。
所有我们的计算机视觉算法在灰度图像上运行速度比RGB565图像快。
"""

RGB565: int
"""
RGB565像素格式。每个像素为16位，即2字节。5位用于红色，6位用于绿色，5位用于蓝色。
所有我们的计算机视觉算法在RGB565图像上运行速度比灰度图像慢。
"""

BAYER: int
"""
RAW BAYER图像像素格式。如果尝试使帧大小过大而无法适应帧缓冲区，则您的OpenMV Cam将像素格式设置为BAYER，以便您可以捕获图像，但只有一些图像处理方法将可用。
"""

YUV422: int
"""
非常容易进行JPEG压缩的像素格式。每个像素都存储为一个灰度8位Y值，后跟交替的8位U/V颜色值，这些值在两个Y值之间共享（8位Y1，8位U，8位Y2，8位V，等等）。只有一些图像处理方法适用于YUV422。
"""

JPEG: int
"""
JPEG模式。摄像头模块输出压缩的jpeg图像。使用 sensor.set_quality() 控制jpeg质量。仅适用于OV2640/OV5640摄像头。
"""

OV2640: int
"""
sensor.get_id() 返回OV2640相机的值。
"""

OV5640: int
"""
sensor.get_id() 返回OV5640相机的值。
"""

OV7690: int
"""
sensor.get_id() 返回OV7690相机的值。
"""

OV7725: int
"""
sensor.get_id() 返回OV7725相机的值。
"""

OV9650: int
"""
sensor.get_id() 返回OV9650相机的值。
"""

MT9V022: int
"""
sensor.get_id() 返回MT9V022相机的值。
"""

MT9V024: int
"""
sensor.get_id() 返回MT9V024相机的值。
"""

MT9V032: int
"""
sensor.get_id() 返回MT9V032相机的值。
"""

MT9V034: int
"""
sensor.get_id() 返回MT9V034相机的值。
"""

MT9M114: int
"""
sensor.get_id() 返回MT9M114相机的值。
"""

LEPTON: int
"""
sensor.get_id() 返回LEPTON1/2/3相机的值。
"""

HM01B0: int
"""
sensor.get_id() 返回HM01B0相机的值。
"""

HM0360: int
"""
sensor.get_id() 返回HM01B0相机的值。
"""

GC2145: int
"""
sensor.get_id() 返回GC2145相机的值。
"""

PAG7920: int
"""
sensor.get_id() 对于 PAG7920 摄像头返回此值。
"""

PAJ6100: int
"""
sensor.get_id() 返回PAJ6100相机的值。
"""

FROGEYE2020: int
"""
sensor.get_id() 返回FROGEYE2020相机的值。
"""

QQCIF: int
"""
88x72分辨率的相机传感器。
"""

QCIF: int
"""
176x144 分辨率的相机传感器。
"""

CIF: int
"""
352x288 分辨率的相机传感器。
"""

QQSIF: int
"""
88x60 分辨率的相机传感器。
"""

QSIF: int
"""
176x120 分辨率的相机传感器。
"""

SIF: int
"""
352x240 分辨率的相机传感器。
"""

QQQQVGA: int
"""
40x30 分辨率的相机传感器。
"""

QQQVGA: int
"""
80x60 分辨率的相机传感器。
"""

QQVGA: int
"""
160x120 分辨率的相机传感器。
"""

QVGA: int
"""
320x240 分辨率的相机传感器。
"""

VGA: int
"""
640x480 分辨率的相机传感器。
"""

HQQQQVGA: int
"""
30x20 分辨率的相机传感器。
"""

HQQQVGA: int
"""
60x40 分辨率的相机传感器。
"""

HQQVGA: int
"""
120x80 分辨率的相机传感器。
"""

HQVGA: int
"""
240x160 分辨率的相机传感器。
"""

HVGA: int
"""
480x320 分辨率的相机传感器。
"""

B64X32: int
"""
64x32 分辨率的相机传感器。
用于 Image.find_displacement() 和任何其他基于FFT的算法。
"""

B64X64: int
"""
64x64 分辨率的相机传感器。
用于 Image.find_displacement() 和任何其他基于FFT的算法。
"""

B128X64: int
"""
128x64 分辨率的相机传感器。
用于 Image.find_displacement() 和任何其他基于FFT的算法。
"""

B128X128: int
"""
128x128 分辨率的相机传感器。
用于 Image.find_displacement() 和任何其他基于FFT的算法。
"""

B160X160: int
"""
HM01B0相机传感器的160x160分辨率。
"""

B320X320: int
"""
HM01B0相机传感器的320x320分辨率。
"""

LCD: int
"""
相机传感器的分辨率为 128x160（与 LCD 保护罩一起使用）。
"""

QQVGA2: int
"""
相机传感器的分辨率为 128x160（与 LCD 保护罩一起使用）。
"""

WVGA: int
"""
MT9V034相机传感器的720x480分辨率。
"""

WVGA2: int
"""
MT9V034相机传感器的752x480分辨率。
"""

SVGA: int
"""
800x600 分辨率的相机传感器。
"""

XGA: int
"""
1024x768 分辨率的相机传感器。
"""

WXGA: int
"""
MT9M114相机传感器的1280x768分辨率。
"""

SXGA: int
"""
1280x1024 分辨率的相机传感器。仅适用于OV2640/OV5640相机。
"""

SXGAM: int
"""
MT9M114相机传感器的1280x960分辨率。
"""

UXGA: int
"""
1600x1200 分辨率的相机传感器。仅适用于 OV2640/OV5640相机。
"""

HD: int
"""
1280x720 分辨率的相机传感器。
"""

FHD: int
"""
1920x1080 分辨率的相机传感器。仅适用于 OV5640 相机。
"""

QHD: int
"""
2560x1440 分辨率的相机传感器。仅适用于 OV5640 相机。
"""

QXGA: int
"""
2048x1536 分辨率的相机传感器。仅适用于 OV5640 相机。
"""

WQXGA: int
"""
2560x1600 分辨率的相机传感器。仅适用于 OV5640 相机。
"""

WQXGA2: int
"""
2592x1944 分辨率的相机传感器。仅适用于 OV5640 相机。
"""

IOCTL_SET_READOUT_WINDOW: int
"""
允许您设置OV5640的读出窗口。
"""

IOCTL_GET_READOUT_WINDOW: int
"""
允许您获取OV5640的读出窗口。
"""

IOCTL_SET_TRIGGERED_MODE: int
"""
允许您设置MT9V034的触发模式。
"""

IOCTL_GET_TRIGGERED_MODE: int
"""
允许您获取MT9V034的触发模式。
"""

IOCTL_SET_FOV_WIDE: int
"""
启用 sensor.set_framesize() 以优化视场而不是FPS。
"""

IOCTL_GET_FOV_WIDE: int
"""
如果 sensor.set_framesize() 正在针对 FPS 的视野进行优化，则返回。
"""

IOCTL_TRIGGER_AUTO_FOCUS: int
"""
用于触发OV5640 FPC相机模块的自动对焦。
"""

IOCTL_PAUSE_AUTO_FOCUS: int
"""
用于暂停OV5640 FPC相机模块的自动对焦（在运行时）。
"""

IOCTL_RESET_AUTO_FOCUS: int
"""
用于将自动对焦重置为OV5640 FPC相机模块的默认设置。
"""

IOCTL_WAIT_ON_AUTO_FOCUS: int
"""
用于等待OV5640 FPC相机模块触发后自动对焦完成。
"""

IOCTL_SET_NIGHT_MODE: int
"""
用于在传感器上打开或关闭夜间模式。夜间模式会降低帧速率以动态增加曝光。
"""

IOCTL_GET_NIGHT_MODE: int
"""
获取传感器是否启用或禁用夜间模式的当前值。
"""

IOCTL_LEPTON_GET_WIDTH: int
"""
允许您获取FLIR Lepton图像分辨率的宽度（以像素为单位）。
"""

IOCTL_LEPTON_GET_HEIGHT: int
"""
允许您获取 FLIR Lepton 图像分辨率的高度（以像素为单位）。
"""

IOCTL_LEPTON_GET_RADIOMETRY: int
"""
允许您获取 FLIR Lepton 类型（辐射或非辐射）。
"""

IOCTL_LEPTON_GET_REFRESH: int
"""
允许您获取 FLIR Lepton 刷新率（以赫兹为单位）。
"""

IOCTL_LEPTON_GET_RESOLUTION: int
"""
允许您获取 FLIR Lepton ADC 分辨率（以位为单位）。
"""

IOCTL_LEPTON_RUN_COMMAND: int
"""
根据FLIR Lepton SDK执行16位命令。
"""

IOCTL_LEPTON_SET_ATTRIBUTE: int
"""
根据 FLIR Lepton SDK 设置 FLIR Lepton 属性。
"""

IOCTL_LEPTON_GET_ATTRIBUTE: int
"""
根据 FLIR Lepton SDK获取 FLIR Lepton 属性。
"""

IOCTL_LEPTON_GET_FPA_TEMPERATURE: int
"""
获取以摄氏度为单位的 FLIR Lepton FPA 温度。
"""

IOCTL_LEPTON_GET_AUX_TEMPERATURE: int
"""
获取以摄氏度为单位的 FLIR Lepton AUX 温度。
"""

IOCTL_LEPTON_SET_MEASUREMENT_MODE: int
"""
允许您将 FLIR Lepton 驱动程序设置为可以获取每个像素的有效温度值的模式。有关更多信息，请参见 sensor.ioctl()。
"""

IOCTL_LEPTON_GET_MEASUREMENT_MODE: int
"""
允许您获取FLIR Lepton 传感器是否启用了测量模式。有关更多信息，请参见 sensor.ioctl()。
"""

IOCTL_LEPTON_SET_MEASUREMENT_RANGE: int
"""
允许您在测量模式下将像素映射到的温度范围。有关更多信息，请参见 sensor.ioctl() 。
"""

IOCTL_LEPTON_GET_MEASUREMENT_RANGE: int
"""
允许您获取用于测量模式的温度范围。有关更多信息，请参见 sensor.ioctl()。
"""

IOCTL_HIMAX_MD_ENABLE: int
"""
允许您控制HM01B0的运动检测中断。有关更多信息，请参见 sensor.ioctl().
"""

IOCTL_HIMAX_MD_CLEAR: int
"""
允许您控制HM01B0的运动检测中断。有关更多信息，请参见 sensor.ioctl().
"""

IOCTL_HIMAX_MD_WINDOW: int
"""
允许您控制HM01B0的运动检测中断。有关更多信息，请参见 sensor.ioctl().
"""

IOCTL_HIMAX_MD_THRESHOLD: int
"""
允许您控制HM01B0的运动检测中断。有关更多信息，请参见 sensor.ioctl().
"""

IOCTL_HIMAX_OSC_ENABLE: int
"""
允许您控制HM01B0上的内部振荡器。有关更多信息，请参见 sensor.ioctl()。
"""

SINGLE_BUFFER: int
"""
传递给 sensor.set_framebuffers() 以设置单缓冲区模式（1缓冲区）。
"""

DOUBLE_BUFFER: int
"""
传递给 sensor.set_framebuffers() 以设置双缓冲区模式（2缓冲区）。
"""

TRIPLE_BUFFER: int
"""
传递给 sensor.set_framebuffers() 以设置三缓冲区模式（3缓冲区）。
"""

VIDEO_FIFO: int
"""
传递给 sensor.set_framebuffers() 以设置视频FIFO模式（4缓冲区）。
"""

def reset() -> None:
    """
    初始化相机传感器。
    """
    pass
    
    
def sleep(enable: bool) -> None:
    """
    如果enable是True，则让相机进入睡眠状态。否则，唤醒相机。
    """
    pass
    
    
def shutdown(enable: bool) -> None:
    """
    将相机置于比睡眠模式更低的功耗模式（但相机必须在唤醒时进行重置）。
    """
    pass
    
    
def flush() -> None:
    """
    将帧缓冲区中的内容复制到IDE中。如果不是在运行带有无循环的脚本，则应调用此方法来显示OpenMV Cam拍摄的最后一张图像。请注意，在脚本完成后，您需要添加约一秒的延迟时间，以便IDE从相机中获取图像。否则，此方法无效。
    """
    pass
    
    
def snapshot() -> image.Image:
    """
    使用相机拍照并返回一个 image 对象。
    OpenMV Cam 有两个用于图像的内存区域。用于正常 MicroPython 处理的经典堆栈/堆区可以在其堆区中存储小型图像。但是，MicroPython 堆的大小仅约为 ~100 KB，这不足以存储较大的图像。因此，您的 OpenMV Cam 具有用于存储由 sensor.snapshot() 拍摄的图像的第二个帧缓冲区内存区域。图像存储在此内存区域的底部。剩余的任何内存将可供帧缓冲区堆栈使用，您的 OpenMV Cam 固件用于保存用于图像处理算法的大型临时数据结构。
    如果您需要空间来存储多个帧，可以通过调用 sensor.alloc_extra_fb() 来“窃取”帧缓冲区空间。
    如果启用了 sensor.set_auto_rotation()，则此方法将返回一个新的已旋转的 image 对象。
    """
    pass
    
    
def skip_frames(n: int | None = None,time: int | None = None) -> None:
    """
    获取 n 个快照，以使相机图像在更改相机设置后稳定。 n 作为常规参数传递，例如 skip_frames(10) 跳过 10 帧。在更改相机设置后，应调用此函数。
    或者，您可以传递关键字参数 time 来跳过一些毫秒数的帧，例如 skip_frames(time = 2000) 跳过 2000 毫秒的帧。
    如果未指定 n 或 time，则此方法将跳过300毫秒的帧。
    如果两者都指定，则此方法将跳过 n 个帧，但在 time 毫秒后超时。
    """
    pass
    
    
def width() -> int:
    """
    返回传感器分辨率的宽度。
    """
    pass
    
    
def height() -> int:
    """
    返回传感器分辨率的高度。
    """
    pass
    
    
def get_fb() -> image.Image | None:
    """
    （获取帧缓冲区）返回先前调用 sensor.snapshot() 返回的图像对象。如果之前未调用过 sensor.snapshot()，则返回 None。
    """
    pass
    
    
def get_id() -> int:
    """
    返回相机模块ID。
    """
    pass
    
    
def alloc_extra_fb(width: int,height: int,pixformat: int) -> image.Image:
    """
    从帧缓冲区堆栈中为图像存储分配另一个帧缓冲区，并返回 width 、 height 和 pixformat 的 image 对象。
    只要有可用的内存，您可以调用此函数任意次数，以分配任意数量的额外帧缓冲区。
    如果 pixformat 是大于等于 4 的数字，则将分配 JPEG 图像。然后，您可以使用 Image.bytearray() 来获得对 JPEG 图像的字节级读写访问。
    """
    pass
    
    
def dealloc_extra_fb() -> None:
    """
    释放上一个先前分配的额外帧缓冲区。额外帧缓冲区用于存储在类似堆栈的结构中。
    """
    pass
    
    
def set_pixformat(pixformat: int) -> None:
    """
    设置相机模块的像素格式。
    如果您正在尝试使用 OV2640 或 OV5640 相机模块拍摄 JPEG 图像，并且分辨率较高，则应将 pixformat 设置为 sensor.JPEG。然后，您可以使用 sensor.set_quality() 控制图像质量。
    """
    pass
    
    
def get_pixformat() -> int:
    """
    返回相机模块的像素格式。
    """
    pass
    
    
def set_framesize(framesize: int) -> None:
    """
    设置相机模块的帧大小。
    """
    pass
    
    
def get_framesize() -> int:
    """
    返回相机模块的帧大小。
    """
    pass
    
    
def set_framerate(rate: int) -> None:
    """
    设置相机模块的帧率（以赫兹为单位）。
    """
    pass
    
    
def get_framerate() -> int:
    """
    返回相机模块的帧率（以赫兹为单位）。
    """
    pass
    
    
def set_windowing(roi: Tuple[int, int] | Tuple[int, int, int, int]) -> None:
    """
    将相机的分辨率设置为当前分辨率内的子分辨率。例如，将分辨率设置为 sensor.VGA，然后将窗口设置为（120，140，200，200）将使 sensor.snapshot() 捕获相机传感器输出的VGA分辨率的中心200×200像素。您可以使用窗口化来获取自定义分辨率。此外，在较大分辨率上使用窗口化实际上是数字变焦。
    roi 是一个矩形元组 (x, y, w, h)。但是，您也可以只传递 (w, h)，并且 roi 将在帧中居中。您还可以不使用括号传递 roi。
    此函数将自动处理将传递的roi裁剪到帧大小。
    """
    pass
    
    
def get_windowing() -> Tuple[int, int, int, int]:
    """
    返回先前使用 sensor.set_windowing() 设置的 roi 元组 (x, y, w, h)。
    """
    pass
    
    
def set_gainceiling(gainceiling: int) -> None:
    """
    设置相机图像增益上限。2、4、8、16、32、64 或 128。
    """
    pass
    
    
def set_contrast(contrast: int) -> None:
    """
    设计相机图像对比度。-3 到 +3。
    """
    pass
    
    
def set_brightness(brightness: int) -> None:
    """
    设置相机图像亮度。-3 到 +3。
    """
    pass
    
    
def set_saturation(saturation: int) -> None:
    """
    设置相机图像饱和度。-3 到 +3。
    """
    pass
    
    
def set_quality(quality: int) -> None:
    """
    设置相机图像JPEG压缩质量。0 - 100。
    """
    pass
    
    
def set_colorbar(enable: bool) -> None:
    """
    打开（True）或关闭（False）彩色条模式。默认为关闭。
    """
    pass
    
    
def set_auto_gain(enable: bool,gain_db=-1,gain_db_ceiling: int | None = None) -> None:
    """
    enable 打开（True）或关闭（False）自动增益控制。相机将启动时默认启用自动增益控制。
    如果 enable 为 False，则可以使用 gain_db 设置固定增益（以分贝为单位）。
    如果 enable 为 True，则可以使用 gain_db_ceiling 设置自动增益控制算法的最大增益上限（以分贝为单位）。
    """
    pass
    
    
def get_gain_db() -> float:
    """
    以分贝（float）为单位返回当前相机增益值。
    """
    pass
    
    
def set_auto_exposure(enable: bool,exposure_us: int | None = None) -> None:
    """
    enable 打开（True）或关闭（False）自动曝光控制。相机启动时将打开自动曝光控制。
    如果 enable 为 False，则可以使用 exposure_us 设置固定曝光时间（以微秒为单位）。
    """
    pass
    
    
def get_exposure_us() -> int:
    """
    返回以微秒（int）为单位的当前相机曝光时间。
    """
    pass
    
    
def set_auto_whitebal(enable: bool,rgb_gain_db: Tuple[float, float, float] | None = None) -> None:
    """
    enable 参数用于打开（True）或关闭（False）自动白平衡。相机将以自动白平衡状态启动。
    如果 enable 为 False，则可以使用 rgb_gain_db 分别设置红色、绿色和蓝色通道的固定增益（以分贝为单位）。
    """
    pass
    
    
def get_rgb_gain_db() -> Tuple[float, float, float]:
    """
    返回当前相机的红色、绿色、蓝色增益值的元组，以分贝为单位（(float, float, float)）。
    """
    pass
    
    
def set_auto_blc(enable: bool,regs: Any | None = None):
    """
    设置相机的自动黑色校准（blc）控制。
    enable 传入 True 或 False 以打开或关闭 BLC。通常情况下，您始终希望将其打开。
    regs 如果禁用，则可以通过先前从 get_blc_regs() 获得的值手动设置 blc 寄存器的值。
    """
    pass
    
    
def get_blc_regs() -> Any:
    """
    以不透明的整数元组形式返回传感器blc寄存器。用于 set_auto_blc。
    """
    pass
    
    
def set_hmirror(enable: bool) -> None:
    """
    打开（True）或关闭（False）水平镜像模式。默认为关闭。
    """
    pass
    
    
def get_hmirror() -> bool:
    """
    如果启用了水平镜像模式则返回。
    """
    pass
    
    
def set_vflip(enable: bool) -> None:
    """
    打开（True）或关闭（False）垂直翻转模式。默认为关闭。
    """
    pass
    
    
def get_vflip() -> bool:
    """
    如果垂直翻转模式启用则返回。
    """
    pass
    
    
def set_transpose(enable: bool) -> None:
    """
    打开（True）或关闭（False）转置模式。默认为关闭。
    """
    pass
    
    
def get_transpose() -> bool:
    """
    如果转置模式启用则返回。
    """
    pass
    
    
def set_auto_rotation(enable: bool) -> None:
    """
    打开（True）或关闭（False）自动旋转模式。默认为关闭。
    """
    pass
    
    
def get_auto_rotation() -> bool:
    """
    如果自动旋转模式启用则返回。
    """
    pass
    
    
def set_framebuffers(count: int) -> None:
    """
    设置用于接收图像数据的帧缓冲区数量。默认情况下，您的 OpenMV Cam 将尝试自动分配尽可能多的帧缓冲区，以确保在分配时不超过可用帧缓冲区 RAM 的一半，以确保获得最佳性能。每当调用 sensor.set_pixformat()、sensor.set_framesize() 和 sensor.set_windowing() 时，都会自动重新分配帧缓冲区。
    sensor.snapshot() 会在后台自动处理切换活动帧缓冲区。从你的代码角度来看，始终只有一个活动帧缓冲区，尽管系统中可能有多个帧缓冲区，并且另一个帧缓冲区在后台接收数据。
    如果计数为：
    关于上述重新分配，首先尝试三重缓冲区，然后是双重缓冲区，如果这两种都无法适应可用帧缓冲区RAM的一半，则使用单缓冲区模式。
    您可以传递大于4的值，将传感器驱动程序设置为视频FIFO模式，其中接收到的图像存储在带有 count 个缓冲区的帧缓冲区FIFO中。这对于视频记录到SD卡非常有用，当SD卡执行诸如预擦除块以写入数据时，可能会随机阻塞您的代码。
    有趣的事实是，在带有 SDRAM 的 OpenMV Cam 上可以传递大约 100 的值以获得巨大的视频 FIFO。然后，如果您以比相机帧速率慢的速度调用快照（通过添加 machine.sleep()），您将在 OpenMV IDE 中获得慢动作效果。但是，您还将看到上述策略效果，即在帧丢失时重置帧缓冲区，以确保帧不会过时。如果要记录慢动作视频，请正常将视频记录到 SD 卡，然后在桌面计算机上以比记录速度慢的速度播放视频。
    """
    pass
    
    
def get_framebuffers() -> int:
    """
    返回当前分配的帧缓冲区数量。
    """
    pass
    
    
def disable_delays(disable: bool | None = None) -> bool:
    """
    如果 disable 是 True，则禁用传感器模块中的所有延迟时间。每当您重置相机模块、更改模式等，传感器驱动程序都会延迟，以防止您在之后很快调用 snapshot 并从相机模块接收损坏的帧。通过禁用延迟，您可以在最后延迟并调用 snapshot 之前通过多个函数调用快速更新相机模块设置。
    如果此函数不带参数调用，则在禁用延迟时返回。
    """
    pass
    
    
def disable_full_flush(disable: bool | None = None) -> bool:
    """
    如果 disable 是 True，则禁用 set_framebuffers 中提到的自动帧缓冲刷新。这将移除帧缓冲 FIFO 中帧的任何时间限制。例如，如果您将帧缓冲区数设置为 30，并将帧速率设置为 30，现在您可以精确地从相机记录 1 秒的视频，而不会丢失帧。
    如果此函数不带参数调用，则返回自动刷新是否已禁用。默认情况下，启用帧丢失时的自动刷新以清除陈旧的帧。
    """
    pass
    
    
def set_lens_correction(enable: bool,radi: int,coef: int) -> None:
    """
    enable 为 True 则启用，为 False 则禁用（bool）。radi 要更正的像素半径（int）。coef 更正的幂（int）。
    """
    pass
    
    
def set_vsync_callback(cb) -> None:
    """
    注册回调函数 cb （在中断上下文中执行），每当相机模块生成新帧时（但在接收到帧之前）执行。
    cb 接受一个参数，并传递更改后的垂直同步引脚的当前状态。
    """
    pass
    
    
def set_frame_callback(cb) -> None:
    """
    注册回调函数 cb （在中断上下文中执行），每当相机模块生成新帧并准备通过 sensor.snapshot() 读取时执行。
    cb 不接受参数。
    使用此功能获取中断以稍后使用 micropython.schedule() 读取帧。
    """
    pass
    
    
def get_frame_available() -> bool:
    """
    如果通过调用 sensor.snapshot() 读取帧，则返回True。
    """
    pass
    
    
def ioctl(*args,**kwargs) -> Any:
    """
    执行传感器特定方法：
    """
    pass
    
    
def set_color_palette(palette: int) -> None:
    """
    设置用于 FLIR Lepton 灰度到 RGB565 转换的颜色调色板。
    """
    pass
    
    
def get_color_palette() -> int:
    """
    返回当前的颜色调色板设置。默认为 image.PALETTE_RAINBOW。
    """
    pass
    
    
def __write_reg(address: int,value: int) -> None:
    """
    将 value （int）写入到地址为 address （int）的相机寄存器中。
    """
    pass
    
    
def __read_reg(address: int) -> int:
    """
    读取地址为 address （int）的相机寄存器。
    """
    pass
    
    
