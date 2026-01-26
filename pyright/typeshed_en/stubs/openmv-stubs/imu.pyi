"""
The imu module is used for reading the 6-DOF LSM6DS3
IMU sensor under the camera sensor.
"""

from typing import Tuple
from typing import List
from typing import Optional
from typing import Any
import image

def acceleration_mg() -> Tuple[float, float, float]:
    """
    Returns the acceleration for (x, y, z) in a float tuple in milli-g’s.
    For when the camera board is lying on a table face up:
    X points to the right of the camera sensor
    Y points down below the camera sensor (towards the bottom on the board)
    Z points in the reverse direction of the camera sensor (into the table)
    """
    pass
    
    
def angular_rate_mdps() -> Tuple[float, float, float]:
    """
    Returns the angular rate for (x, y, z) in a float tuple in milli-degrees-per-second.
    For when the camera board is lying on a table face up:
    X points to the right of the camera sensor
    Y points down below the camera sensor (towards the bottom on the board)
    Z points in the reverse direction of the camera sensor (into the table)
    """
    pass
    
    
def temperature_c() -> float:
    """
    Returns the temperature in celsius (float).
    """
    pass
    
    
def roll() -> float:
    """
    Returns the rotation angle in degrees (float) of the camera module.
    """
    pass
    
    
def pitch() -> float:
    """
    Returns the rotation angle in degrees (float) of the camera module.
    """
    pass
    
    
def sleep(enable: bool) -> None:
    """
    Pass True to put the IMU sensor to sleep. False to wake it back up (the default).
    """
    pass
    
    
def __write_reg(addr: int,val: int) -> None:
    """
    Set 8-bit LSM6DS3 register addr to 8-bit val.
    """
    pass
    
    
def __read_reg(addr: int) -> int:
    """
    Get 8-bit LSM6DS3 register addr.
    """
    pass
    
    
