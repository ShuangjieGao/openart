"""
OpenMV Pure Thermal 的触摸屏驱动。
"""

from typing import Tuple
from typing import List
from typing import Optional
from typing import Any
import image

LCD_GESTURE_MOVE_UP: int
"""
触摸屏上滑手势。
"""

LCD_GESTURE_MOVE_LEFT: int
"""
触摸屏左滑手势。
"""

LCD_GESTURE_MOVE_DOWN: int
"""
触摸屏下滑手势。
"""

LCD_GESTURE_MOVE_RIGHT: int
"""
触摸屏右滑手势。
"""

LCD_GESTURE_ZOOM_IN: int
"""
触摸屏放大手势。
"""

LCD_GESTURE_ZOOM_OUT: int
"""
触摸屏缩小手势。
"""

LCD_GESTURE_NONE: int
"""
触摸屏无手势。
"""

LCD_FLAG_PRESSED: int
"""
触摸点被按下。
"""

LCD_FLAG_RELEASED: int
"""
触摸点被释放。
"""

LCD_FLAG_MOVED: int
"""
触摸点被移动。
"""

class FT5X06:
    def __init__(self, i2c_addr=0x38):
        """
        创建一个触摸屏控制器对象
        """
        pass
        
        
    
