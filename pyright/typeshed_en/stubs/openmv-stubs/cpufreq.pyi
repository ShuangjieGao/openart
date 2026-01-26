"""
The cpufreq module is used to get/set the CPU frequency to save power.
"""

from typing import Tuple
from typing import List
from typing import Optional
from typing import Any
import image

def set_frequency(supported_frequency: int) -> None:
    """
    Sets the CPU frequency to a supported frequency in MHz. Peripherals
    frequencies are not changed. Only the CPU performance.
    """
    pass
    
    
def get_current_frequencies() -> Tuple[int, int, int, int]:
    """
    Returns (cpu_clk_in_mhz, hclk_in_mhz, pclk1_in_mhz, pclk2_in_mhz).
    """
    pass
    
    
def get_supported_frequencies() -> List[int]:
    """
    Returns the supported CPU frequencies [120, 144, 168, 192, 216] on the
    OpenMV Cam M7 and [60/50, 120/100, 240/200, 480/400] on the OpenMV Cam H7 Rev V/XY silicon in MHz.
    """
    pass
    
    
