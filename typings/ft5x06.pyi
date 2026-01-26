"""
Touch Screen Driver for the OpenMV Pure Thermal.
"""

from typing import Tuple
from typing import List
from typing import Optional
from typing import Any
import image

LCD_GESTURE_MOVE_UP: int
"""
Touch screen move up gesture.
"""

LCD_GESTURE_MOVE_LEFT: int
"""
Touch screen move left gesture.
"""

LCD_GESTURE_MOVE_DOWN: int
"""
Touch screen move down gesture.
"""

LCD_GESTURE_MOVE_RIGHT: int
"""
Touch screen move right gesture.
"""

LCD_GESTURE_ZOOM_IN: int
"""
Touch screen zoom in gesture.
"""

LCD_GESTURE_ZOOM_OUT: int
"""
Touch screen zoom out gesture.
"""

LCD_GESTURE_NONE: int
"""
Touch screen no gesture.
"""

LCD_FLAG_PRESSED: int
"""
Touch point is pressed.
"""

LCD_FLAG_RELEASED: int
"""
Touch point is released.
"""

LCD_FLAG_MOVED: int
"""
Touch point is moved.
"""

class FT5X06:
    def __init__(self, i2c_addr=0x38):
        """
        Creates a touch screen controller object
        """
        pass
        
        
    
