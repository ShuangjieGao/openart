"""
mjpeg 模块用于mjpeg录音。
"""

from typing import Tuple
from typing import List
from typing import Optional
from typing import Any
import image

class Mjpeg:
    def __init__(self, filename: str, width: int | None = None, height: int | None = None):
        """
        创建一个可以添加帧的Mjpeg对象。filename 是保存mjpeg录制的路径。
        width 被自动设置为图像传感器的水平分辨率，除非明确覆盖。
        height 被自动设置为图像传感器的垂直分辨率，除非明确覆盖。
        """
        pass
        
        
    def is_closed(self) -> bool:
        """
        如果文件关闭则返回True。您不能向已关闭的文件写入更多数据。
        """
        pass
        
        
    def width(self) -> int:
        """
        返回mjpeg文件的宽度（水平分辨率）。
        """
        pass
        
        
    def height(self) -> int:
        """
        返回mjpeg的高度（垂直分辨率）。
        """
        pass
        
        
    def count(self) -> int:
        """
        返回mjpeg文件的帧数。
        """
        pass
        
        
    def size(self) -> int:
        """
        返回目前为止mjpeg的文件大小（以字节为单位）。添加帧后会更新此值。
        """
        pass
        
        
    def add_frame(self,image: image.Image,roi: Tuple[int, int, int, int] | None = None,rgb_channel=-1,alpha=256,color_palette=None,alpha_palette=None,hint=0,quality=90):
        """
        向mjpeg录制添加图像。添加的图像会自动放大/缩小，同时保持与创建mjpeg文件时指定的分辨率相同的宽高比。
        image 可以是任何图像格式。甚至是分辨率错误的PNG图像或JPEG图像。此方法将自动为文件解压、缩放/转换和重新压缩图像。
        roi 是图像的感兴趣区域矩形元组(x, y, w, h)。这允许您仅提取ROI中的像素。默认情况下，这是整个图像。
        rgb_channel 是RGB通道（0=R, G=1, B=2）从RGB565图像（如果传递）中提取并渲染到目的地。例如，如果您传递 rgb_channel=1，这将提取源RGB565图像的绿色通道，并在目标上以灰度绘制。
        alpha 控制源图像与目标图像混合的程度。值256绘制不透明的源图像，而值低于256则生成源图像和目标之间的混合图像（在本例中为黑色背景）。0的结果是黑的图像。
        color_palette 如果不是 -1 ，可以是 image.PALETTE_RAINBOW 、 image.PALETTE_IRONBOW ，或者总像素 256 的 RGB565 图像，用作对源图像的灰度值进行颜色查找表。如果使用，此操作将在 rgb_channel 提取之后应用。
        alpha_palette 如果不是 -1，可以是总像素256 的 GRAYSCALE 图像，用作调制被绘制到像素级别的源图像的 alpha 值的 alpha 调色板，从而允许您根据它们的灰度值精确控制像素的 alpha 值。在 alpha 查找表中的像素值为 255 时是不透明的，小于 255 的任何值都会变得更透明，直到 0。如果使用，此操作将在 rgb_channel 提取之后应用。
        hint 可以是标志的逻辑 OR：
        quality 是用于非jpeg图像的压缩质量（0-100）（int）。
        返回对象。
        """
        pass
        
        
    def write(self,image: image.Image,quality=90,roi: Tuple[int, int, int, int] | None = None,rgb_channel=-1,alpha=256,color_palette=None,alpha_palette=None,hint=0):
        """
        Mjpeg.add_frame() 的别称。
        """
        pass
        
        
    def sync(self):
        """
        将mjpeg文件刷新到磁盘，但保持文件打开以写入更多数据。您应该定期调用flush以确保文件保存到磁盘。
        返回对象。
        """
        pass
        
        
    def close(self):
        """
        完成mjpeg录制。录制完成后必须调用此方法才能查看文件。
        返回对象。
        """
        pass
        
        
    
