"""
gif 模块用于GIF录制。
"""

from typing import Tuple
from typing import List
from typing import Optional
from typing import Any
import image

class Gif:
    def __init__(self, filename: str, width: int | None = None, height: int | None = None, color: bool | None = None, loop=True):
        """
        创建一个可以向其中添加帧的 Gif 对象。filename 是保存 gif 录制的路径。
        width 被自动设置为图像传感器的水平分辨率，除非明确覆盖。
        height 被自动设置为图像传感器的垂直分辨率，除非明确覆盖。
        color 被自动设置为图像传感器的颜色模式，除非明确覆盖：
        loop 为 True 时，导致 gif 在播放时自动循环。
        """
        pass
        
        
    def width(self) -> int:
        """
        返回 gif 对象的宽度（水平分辨率）。
        """
        pass
        
        
    def height(self) -> int:
        """
        返回 gif 对象的高度（垂直分辨率）。
        """
        pass
        
        
    def format(self) -> int:
        """
        如果颜色为 True，则返回 sensor.RGB565，否则返回 sensor.GRAYSCALE。
        """
        pass
        
        
    def size(self) -> int:
        """
        返回到目前为止gif的文件大小。此值在添加帧后更新。
        """
        pass
        
        
    def loop(self) -> bool:
        """
        如果gif对象在其构造函数中设置了循环则返回。
        """
        pass
        
        
    def add_frame(self,image: image.Image,delay=10) -> None:
        """
        将图像添加到gif录制中。图像的宽度、高度和颜色模式必须与构造gif时使用的宽度、高度和颜色模式相同。
        delay 是在上一帧（如果不是第一帧）后显示此帧之前等待的以厘秒为单位的时间。
        """
        pass
        
        
    def close(self) -> None:
        """
        完成gif录制。完成录制后必须调用此方法才能查看文件。
        """
        pass
        
        
    
