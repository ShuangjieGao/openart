"""
Frame buffer manipulation.

MicroPython module: https://docs.micropython.org/en/vab847696a/library/framebuf.html

该模块提供一个可用于创建位图、可发送到显示器的通用帧缓冲区。
"""

# source version: vab847696a
# origin module:: repos/micropython/docs/library/framebuf.rst
from __future__ import annotations
from typing import Any, Optional
from _typeshed import Incomplete
MONO_VLSB: bytes
"""\
单色（1位）颜色格式。这定义了一个映射，其中字节中的位垂直映射，位0最靠近屏幕顶部。因此，每个字节占据8个垂直像素。后续字节出现在连续的水平位置，直到达到最右边缘。更多的字节在最左边缘的位置，低8个像素处渲染。
"""
MONO_HLSB: bytes
"""\
单色（1位）颜色格式。这定义了一个映射，其中字节中的位水平映射。每个字节占据8个水平像素，位7是最左边的。后续字节出现在连续的水平位置，直到达到最右边缘。更多的字节在下一行渲染，低一像素。
"""
MONO_HMSB: bytes
"""\
单色（1位）颜色格式。这定义了一个映射，其中字节中的位是水平映射。每个字节占据8个水平像素，位0是最左边的。后续字节出现在连续的水平位置，直到达到最右边缘。更多的字节在下一行渲染，低一像素。
"""
RGB565: Incomplete
"""红绿蓝（16位，5+6+5）颜色格式"""
GS2_HMSB: Incomplete
"""灰度（2位）颜色格式"""
GS4_HMSB: Incomplete
"""灰度（4位）颜色格式"""
GS8: Incomplete
"""灰度（8位）颜色格式"""
class FrameBuffer():
    """
        构建一个帧缓冲区对象。参数为:
    
            - *buffer* 缓冲区是一个带有缓冲区协议的对象，且其大小须足以容纳由宽度、高度和帧缓冲区定义的每个像素。
            - *width* 为以像素为单位的帧缓冲区的宽度
            - *width* 为以像素为单位的帧缓冲区的高度
            - *format* 指定在FrameBuffer中使用的像素类型；允许的值列在下面的常量下。这些设置了用于编码颜色值的位数以及这些位在 *buffer* 中的布局。在将颜色值c传递给方法的地方，c是一个小整数，其编码依赖于FrameBuffer的格式。
            - *stride* 是FrameBuffer中每个像素水平线之间的像素数。默认为 *width* ，但在另一个较大的FrameBuffer或屏幕中实现FrameBuffer时可能需要调整。 *buffer* 的大小必须适应增加的步长。
    
        必须指定有效的*buffer*、*width*、*height*、*format*和可选的*stride*。无效的*缓冲区*大小或维度可能导致意外错误。
    """
    def __init__(self, buffer, width, height, format, stride=-1, ) -> None:
        ...
    def fill(self, c) -> None:
        """
            使用指定颜色填满整个帧缓冲区。
        """
        ...
    def pixel(self, x, y, c: Optional[Any]=None) -> Incomplete:
        """
            若未给定*c*，则获取指定像素的色值。若给定*c*，将指定像素设置到给定颜色。
        """
        ...
    def hline(self, x, y, w, c) -> Incomplete:
        ...
    def vline(self, x, y, h, c) -> Incomplete:
        ...
    def line(self, x1, y1, x2, y2, c) -> None:
        """
            使用给定颜色和1像素的厚度从一组坐标中绘制一条线。`line` 方法将这条线画到另一组坐标上，而 `hline` 和 `vline` 方法分别将水平和垂直线绘制到给定的长度。
        """
        ...
    def rect(self, x, y, w, h, c, f: Optional[Any]=None) -> None:
        """
            在给定位置、按照给定大小和颜色绘制一个矩形。
        
            可选的*f*参数可以设置为 ``True`` 以填充矩形。否则，只绘制一个像素的轮廓。
        """
        ...
    def ellipse(self, x, y, xr, yr, c, f, m: Optional[Any]=None) -> None:
        """
            在给定位置绘制一个椭圆。半径*xr*和*yr*定义几何形状；相等的值会导致画出一个圆。*c*参数定义颜色。
        
            可选的*f*参数可以设置为 ``True`` 以填充椭圆。否则，只画一个像素的轮廓。
        
            可选的*m*参数允许将绘画限制在椭圆的某些象限。LS四位决定哪些象限被绘制，其中位0指定Q1，b1指定Q2，b2指定Q3，b3指定Q4。象限逆时针编号，Q1为右上。
        """
        ...
    def poly(self, x, y, coords, c, f: Optional[Any]=None) -> Incomplete:
        """
            给定一个坐标列表，在给定的x, y位置使用给定的颜色绘制一个任意的（凸或凹）闭合多边形。
        
            *coords* 必须指定为整数的 :mod:`array`，例如 ``array('h', [x0, y0, x1, y1, ... xn, yn])``。
        
            可选的*f*参数可以设置为 ``True`` 以填充多边形。否则，只画一个像素的轮廓。
        """
        ...
    def text(self, s, x, y, c: Optional[Any]=None) -> None:
        """
            使用坐标作为文本的左上角将文本写入FrameBuffer。文本的颜色可以通过可选参数定义，否则默认值为1。所有字符的尺寸为8x8像素，目前没有办法更改字体。
        """
        ...
    def scroll(self, xstep, ystep) -> Incomplete:
        """
            将FrameBuffer的内容按给定向量移动。这可能会在FrameBuffer中留下之前颜色的痕迹。
        """
        ...
    def blit(self, fbuf, x, y, key=-1, palette=None) -> None:
        """
            在当前FrameBuffer上的给定坐标处绘制另一个FrameBuffer。如果指定了*key*，则它应该是一个颜色整数，相应的颜色将被视为透明：所有具有该颜色值的像素都不会被绘制。（如果指定了*palette*，则*key*与*palette*中的值进行比较，而不是直接与*fbuf*中的值进行比较。）
        
            *palette*参数允许在具有不同格式的FrameBuffers之间进行blit。典型用途是将单色或灰度图标/图形渲染到彩色显示器上。*palette*是一个FrameBuffer实例，其格式是当前FrameBuffer的格式。*palette*的高度是一个像素，其像素宽度是源FrameBuffer中的颜色数。N位源的*palette*需要2**N个像素；单色源的*palette*将有2个像素，代表背景和前景颜色。应用程序为*palette*中的每个像素分配一个颜色。当前像素的颜色将是那个*palette*像素的颜色，其x位置是相应源像素的颜色。
        """
        ...
