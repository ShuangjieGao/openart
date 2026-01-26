"""
The buzzer module is used to control the amplitude and frequency of a buzzer onboard your OpenMV Cam.
"""

from typing import Tuple
from typing import List
from typing import Optional
from typing import Any
import image

RESONANT_FREQ: int
"""
Constant definting the highest volume frequency of the buzzer (typically 4000 Hz).
"""

def freq(freq: int) -> None:
    """
    Sets the buzzer frequency independently of the volume.
    freq any frequency to drive the buzzer at.
    """
    pass
    
    
def duty(duty: int) -> None:
    """
    Sets the buzzer duty cycle independently of the frequency.
    duty any PWM duty cycle percentage (0-255 for 0-100%).
    """
    pass
    
    
