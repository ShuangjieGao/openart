"""
buzzer 模块用于控制 OpenMV Cam 上的蜂鸣器的幅度和频率。
"""

from typing import Tuple
from typing import List
from typing import Optional
from typing import Any
import image

RESONANT_FREQ: int
"""
定义蜂鸣器的最高音量频率的常量（通常为 4000 Hz）。
"""

def freq(freq: int) -> None:
    """
    独立于音量设置蜂鸣器频率。
    freq 要驱动蜂鸣器的任何频率。
    """
    pass
    
    
def duty(duty: int) -> None:
    """
    独立于频率设置蜂鸣器占空比。
    duty 任何 PWM 占空比百分比（0-255 对应 0-100%）。
    """
    pass
    
    
