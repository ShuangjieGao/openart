"""
cpufreq 模块用于获取/设置 CPU 频率以节省电力。
"""

from typing import Tuple
from typing import List
from typing import Optional
from typing import Any
import image

def set_frequency(supported_frequency: int) -> None:
    """
    将 CPU 频率设置为支持的频率（以 MHz 为单位）。不会更改外围设备频率，只影响 CPU 性能。
    """
    pass
    
    
def get_current_frequencies() -> Tuple[int, int, int, int]:
    """
    返回当前的频率 (cpu_clk_in_mhz, hclk_in_mhz, pclk1_in_mhz, pclk2_in_mhz)。
    """
    pass
    
    
def get_supported_frequencies() -> List[int]:
    """
    返回支持的 CPU 频率列表，在 OpenMV Cam M7 上为 [120, 144, 168, 192, 216] MHz，在 OpenMV Cam H7 Rev V/XY 上为 [60/50, 120/100, 240/200, 480/400] MHz。
    """
    pass
    
    
