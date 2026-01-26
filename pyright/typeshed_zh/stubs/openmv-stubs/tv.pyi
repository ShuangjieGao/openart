"""
tv 模块用于控制图传扩展板。
示例用法:
"""

from typing import Tuple
from typing import List
from typing import Optional
from typing import Any
import image

TV_NONE: int
"""
当此模块未初始化时由 tv.type() 返回。
"""

TV_SHIELD: int
"""
用于初始化TV模型。
"""

def init(type=TV_SHIELD,triple_buffer=False) -> None:
    """
    初始化连接的图传输出模型。
    type 表示应如何初始化 lcd 模块：
    """
    pass
    
    
def deinit() -> None:
    """
    取消初始化tv模块、内部/外部硬件和I/O引脚。
    """
    pass
    
    
def width() -> int:
    """
    返回352像素。这是 sensor.SIF 分辨率。
    """
    pass
    
    
def height() -> int:
    """
    返回240像素。这是 sensor.SIF 分辨率。
    """
    pass
    
    
def type() -> int:
    """
    返回在 tv.init() 期间设置的屏幕类型。
    """
    pass
    
    
def triple_buffer() -> bool:
    """
    如果在 tv.init() 期间设置的三重缓冲区已启用则返回。
    """
    pass
    
    
def refresh() -> None:
    """
    返回60Hz。
    """
    pass
    
    
def channel(channel: int | None = None) -> int:
    """
    对于无线图传扩展板，这将设置1-8之间的广播信道。如果没有传递频道参数，则此方法返回先前设置的频道（1-8）。默认频道为8。
    """
    pass
    
    
def display(image: image.Image,x=0,y=0,x_scale=1.0,y_scale=1.0,roi: Tuple[int, int, int, int] | None = None,rgb_channel=-1,alpha=256,color_palette=None,alpha_palette=None,hint=0):
    """
    显示一个左上角从位置x，y开始的 image。
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
    
    
