"""
display 模块用于驱动SPI LCD、24位并行LCD、MIPI DSI LCD、HDIM输出和显示端口输出。
"""

from typing import Tuple
from typing import List
from typing import Optional
from typing import Any
import image

QVGA: int
"""
帧大小为320×240分辨率。
"""

TQVGA: int
"""
帧大小为240×320分辨率。
"""

FHVGA: int
"""
帧大小为480×272分辨率。
"""

FHVGA2: int
"""
帧大小为480×128分辨率。
"""

VGA: int
"""
帧大小为640×480分辨率。
"""

THVGA: int
"""
帧大小为320×480分辨率。
"""

FWVGA: int
"""
帧大小为800×480分辨率。
"""

FWVGA2: int
"""
帧大小为800×320分辨率。
"""

TFWVGA: int
"""
帧大小为480×800分辨率。
"""

TFWVGA2: int
"""
帧大小为480×480分辨率。
"""

SVGA: int
"""
帧大小为800×600分辨率。
"""

WSVGA: int
"""
帧大小为1024×600分辨率。
"""

XGA: int
"""
帧大小为1024×768分辨率。
"""

SXGA: int
"""
帧大小为1280×1024分辨率。
"""

SXGA2: int
"""
帧大小为1280×400分辨率。
"""

UXGA: int
"""
帧大小为1600×1200分辨率。
"""

HD: int
"""
帧大小为1280×720分辨率。
"""

FHD: int
"""
帧大小为1920×1080分辨率。
"""

class DACBacklight:
    def __init__(self):
        """
        """
        pass
        
        
    def deinit(self) -> None:
        """
        反初始化背光控制器。
        """
        pass
        
        
    def backlight(self,value: int | None = None) -> int:
        """
        将背光强度设置为 0-100。请注意，背光输出上的线性电压不一定会导致屏幕亮度的线性变化。通常存在一个小区域，屏幕亮度将会发生显著变化。
        """
        pass
        
        
    
class PWMBacklight:
    def __init__(self):
        """
        """
        pass
        
        
    def deinit(self) -> None:
        """
        反初始化背光控制器。
        """
        pass
        
        
    def backlight(self,value: int | None = None) -> int:
        """
        将背光强度设置为 0-100。请注意，在背光输出的线性pwm占空比并不一定会导致屏幕亮度的线性变化。通常存在一个小区域，屏幕亮度将会发生显著变化。
        """
        pass
        
        
    
class ST7701:
    def __init__(self):
        """
        """
        pass
        
        
    def init(self,display_controller) -> None:
        """
        使用显示控制器初始化显示器，该控制器必须提供 display.DSIDisplay.bus_write() 和 display.DSIDisplay.bus_read() 方法。
        """
        pass
        
        
    def read_id(self) -> int:
        """
        返回显示器ID。
        """
        pass
        
        
    
class DisplayData:
    def __init__(self):
        """
        """
        pass
        
        
    def display_id(self) -> int:
        """
        返回外部显示器的 EDID 数据作为 bytes()对象。已为您验证了 EDID 标头、校验和将所有部分连接成一个 bytes()对象。然后，您可以通过 此指南 进行解析。
        """
        pass
        
        
    def send_frame(self,dst_addr,src_addr,bytes):
        """
        在 HDMI-CEC 总线上向 dst_addr 发送一个帧，源地址为 src_addr，数据为 bytes。
        """
        pass
        
        
    def receive_frame(self,dst_addr,timeout=1000):
        """
        等待 timeout 毫秒以接收地址为 dst_addr 的 HDMI-CEC帧。如果接收到的帧是为 dst_addr 的，则返回 True，否则返回 False。在超时时抛出 OSError 异常。
        """
        pass
        
        
    def frame_callback(self,callback,dst_addr):
        """
        注册一个 callback，在接收到 HDMI-CEC 帧时将调用它。回调将接收两个参数，帧的 src_addr（int 类型）和 payload（bytes() 对象）。
        dst_addr 设置要在 CEC 总线上侦听的过滤地址。
        如果使用此方法，请不要调用 DisplayData.receive_frame() ，直到通过此方法的回调禁用了 None 作为回调。
        """
        pass
        
        
    
class DSIDisplay:
    def __init__(self):
        """
        """
        pass
        
        
    def deinit(self) -> None:
        """
        释放类使用的 I/O 引脚和 RAM。在销毁时自动调用此方法。
        """
        pass
        
        
    def width(self) -> int:
        """
        返回屏幕的宽度。
        """
        pass
        
        
    def height(self) -> int:
        """
        返回屏幕的高度。
        """
        pass
        
        
    def refresh(self) -> int:
        """
        返回刷新率。
        """
        pass
        
        
    def write(self,image,x=0,y=0,x_scale=1.0,y_scale=1.0,roi=None,rgb_channel=-1,alpha=256,color_palette=None,alpha_palette=None) -> None:
        """
        显示一个左上角从位置x，y开始的 image。
        您也可以传递路径而不是图像对象给此方法，一边从磁盘加载图像并在一步中绘制它。例如 write("test.jpg")。
        x_scale 控制图像在 x 方向的显示比例（float）。如果此值为负，则图像将水平翻转。注意，如果未指定 y_scale，则它将与 x_scale 匹配，以保持纵横比。
        y_scale 控制图像在 y 方向的显示比例（float）。如果此值为负，则图像将垂直翻转。注意，如果未指定 x_scale，则它将与 x_scale 匹配，以保持纵横比。
        roi 是要显示的图像的感兴趣区域矩形元组（x、y、w、h）。这允许您仅提取感兴趣区域的像素以进行缩放。
        rgb_channel 是从RGB565图像（如果传递）中提取和在显示屏上渲染的RGB通道（0=R, G=1, B=2）。例如，如果传递 rgb_channel=1 ，则会提取RGB565图像的绿色通道并以灰度显示。
        alpha 控制图像的不透明度。职位256显示不透明图像，而低于256的值会产生黑色透明图像。0会产生完全黑色图像。
        color_palette 如果不是 -1 ，可以是 image.PALETTE_RAINBOW、image.PALETTE_IRONBOW 或总共256像素的RGB565图像，用作输入图像的灰度值的颜色查找表。如果使用了 rgb_channel，则会在缩放之后应用此选项。
        alpha_palette 如果不是 -1，可以是总共 256 像素的 GRAYSCALE 图像，用作 alpha 调色板，以像素级别调制正在显示的输入图像的 alpha 值，从而精确控制根据其灰度值的像素的 alpha 值。 alpha 查找表中值为 255 的像素是不透明的，小于 255 的值会更加透明直到 0。如果使用了 rgb_channel，则会在缩放之后应用此选项。
        hint 可以是标志的逻辑 OR：
        """
        pass
        
        
    def clear(self,display_off=False) -> None:
        """
        将LCD屏幕清除为黑色。
        display_off 如果为 True则关闭显示逻辑，而不是将 LCD 帧缓冲区清除为黑色。之后，还应关闭背光，以确保屏幕变为黑色，因为许多显示器仅在打开背光时为白色。
        """
        pass
        
        
    def backlight(self,value: int | None = None) -> int:
        """
        设置LCD背光调光值。0（关闭）至100（开启）。
        请注意，除非传递 DACBacklight 或 PWMBacklight ，否则背光将作为GPIO引脚进行控制，并且只能从0（关闭）到非0（开启）。
        不传递参数以获取背光值的状态。
        """
        pass
        
        
    def bus_write(self,cmd: int,args=None,dcs=False) -> None:
        """
        发送带有 args 的 DSI 显示器 cmd。
        """
        pass
        
        
    def bus_read(self,cmd: int,len: int,args=None,dcs=False) -> bytes:
        """
        使用 args 和 cmd 从 DSI 显示器读取 len。
        """
        pass
        
        
    
class RGBDisplay:
    def __init__(self):
        """
        """
        pass
        
        
    def deinit(self) -> None:
        """
        释放类使用的 I/O 引脚和 RAM。在销毁时自动调用此方法。
        """
        pass
        
        
    def width(self) -> int:
        """
        返回屏幕的宽度。
        """
        pass
        
        
    def height(self) -> int:
        """
        返回屏幕的高度。
        """
        pass
        
        
    def refresh(self) -> int:
        """
        返回刷新率。
        """
        pass
        
        
    def write(self,image: image.Image,x=0,y=0,x_scale=1.0,y_scale=1.0,roi=None,rgb_channel=-1,alpha=256,color_palette=None,alpha_palette=None,hint=0) -> None:
        """
        显示一个左上角从位置x，y开始的 image。
        您也可以传递路径而不是图像对象给此方法，一边从磁盘加载图像并在一步中绘制它。例如 write("test.jpg")。
        x_scale 控制图像在 x 方向的显示比例（float）。如果此值为负，则图像将水平翻转。注意，如果未指定 y_scale，则它将与 x_scale 匹配，以保持纵横比。
        y_scale 控制图像在 y 方向的显示比例（float）。如果此值为负，则图像将垂直翻转。注意，如果未指定 x_scale，则它将与 x_scale 匹配，以保持纵横比。
        roi 是要显示的图像的感兴趣区域矩形元组（x、y、w、h）。这允许您仅提取感兴趣区域的像素以进行缩放。
        rgb_channel 是从RGB565图像（如果传递）中提取和在显示屏上渲染的RGB通道（0=R, G=1, B=2）。例如，如果传递 rgb_channel=1 ，则会提取RGB565图像的绿色通道并以灰度显示。
        alpha 控制图像的不透明度。职位256显示不透明图像，而低于256的值会产生黑色透明图像。0会产生完全黑色图像。
        color_palette 如果不是 -1 ，可以是 image.PALETTE_RAINBOW、image.PALETTE_IRONBOW 或总共256像素的RGB565图像，用作输入图像的灰度值的颜色查找表。如果使用了 rgb_channel，则会在缩放之后应用此选项。
        alpha_palette 如果不是 -1，可以是总共 256 像素的 GRAYSCALE 图像，用作 alpha 调色板，以像素级别调制正在显示的输入图像的 alpha 值，从而精确控制根据其灰度值的像素的 alpha 值。 alpha 查找表中值为 255 的像素是不透明的，小于 255 的值会更加透明直到 0。如果使用了 rgb_channel，则会在缩放之后应用此选项。
        hint 可以是标志的逻辑 OR：
        """
        pass
        
        
    def clear(self,display_off=False) -> None:
        """
        将LCD屏幕清除为黑色。
        display_off 如果为 True则关闭显示逻辑，而不是将 LCD 帧缓冲区清除为黑色。之后，还应关闭背光，以确保屏幕变为黑色，因为许多显示器仅在打开背光时为白色。
        """
        pass
        
        
    def backlight(self,value: int | None = None) -> int:
        """
        设置LCD背光调光值。0（关闭）至100（开启）。
        请注意，除非传递 DACBacklight 或 PWMBacklight ，否则背光将作为GPIO引脚进行控制，并且只能从0（关闭）到非0（开启）。
        不传递参数以获取背光值的状态。
        """
        pass
        
        
    
class SPIDisplay:
    def __init__(self):
        """
        """
        pass
        
        
    def deinit(self) -> None:
        """
        释放类使用的 I/O 引脚和 RAM。在销毁时自动调用此方法。
        """
        pass
        
        
    def width(self) -> int:
        """
        返回屏幕的宽度。
        """
        pass
        
        
    def height(self) -> int:
        """
        返回屏幕的高度。
        """
        pass
        
        
    def refresh(self) -> int:
        """
        返回刷新率。
        """
        pass
        
        
    def bgr(self) -> bool:
        """
        如果红色和蓝色通道交换则返回。
        """
        pass
        
        
    def byte_swap(self) -> bool:
        """
        返回 RGB565 像素是否以字节反转显示。
        """
        pass
        
        
    def triple_buffer(self) -> bool:
        """
        如果启用了三重缓冲则返回。
        """
        pass
        
        
    def write(self,image: image.Image,x=0,y=0,x_scale=1.0,y_scale=1.0,roi: Tuple[int, int, int, int] | None = None,rgb_channel=-1,alpha=256,color_palette=None,alpha_palette=None,hint=0):
        """
        显示一个左上角从位置x，y开始的 image。
        您也可以传递路径而不是图像对象给此方法，一边从磁盘加载图像并在一步中绘制它。例如 write("test.jpg")。
        x_scale 控制图像在 x 方向的显示比例（float）。如果此值为负，则图像将水平翻转。注意，如果未指定 y_scale，则它将与 x_scale 匹配，以保持纵横比。
        y_scale 控制图像在 y 方向的显示比例（float）。如果此值为负，则图像将垂直翻转。注意，如果未指定 x_scale，则它将与 x_scale 匹配，以保持纵横比。
        roi 是要显示的图像的感兴趣区域矩形元组（x、y、w、h）。这允许您仅提取感兴趣区域的像素以进行缩放。
        rgb_channel 是从RGB565图像（如果传递）中提取和在显示屏上渲染的RGB通道（0=R, G=1, B=2）。例如，如果传递 rgb_channel=1 ，则会提取RGB565图像的绿色通道并以灰度显示。
        alpha 控制图像的不透明度。职位256显示不透明图像，而低于256的值会产生黑色透明图像。0会产生完全黑色图像。
        color_palette 如果不是 -1 ，可以是 image.PALETTE_RAINBOW、image.PALETTE_IRONBOW 或总共256像素的RGB565图像，用作输入图像的灰度值的颜色查找表。如果使用了 rgb_channel，则会在缩放之后应用此选项。
        alpha_palette 如果不是 -1，可以是总共 256 像素的 GRAYSCALE 图像，用作 alpha 调色板，以像素级别调制正在显示的输入图像的 alpha 值，从而精确控制根据其灰度值的像素的 alpha 值。 alpha 查找表中值为 255 的像素是不透明的，小于 255 的值会更加透明直到 0。如果使用了 rgb_channel，则会在缩放之后应用此选项。
        hint 可以是标志的逻辑 OR：
        """
        pass
        
        
    def clear(self,display_off=False) -> None:
        """
        将LCD屏幕清除为黑色。
        display_off 如果为 True则关闭显示逻辑，而不是将 LCD 帧缓冲区清除为黑色。之后，还应关闭背光，以确保屏幕变为黑色，因为许多显示器仅在打开背光时为白色。
        """
        pass
        
        
    def backlight(self,value: int | None = None) -> int:
        """
        设置LCD背光调光值。0（关闭）至100（开启）。
        请注意，除非传递 DACBacklight 或 PWMBacklight ，否则背光将作为GPIO引脚进行控制，并且只能从0（关闭）到非0（开启）。
        不传递参数以获取背光值的状态。
        """
        pass
        
        
    def bus_write(self,cmd: int,args=None) -> None:
        """
        向 SPI 显示屏发送 cmd 和 args。
        """
        pass
        
        
    
