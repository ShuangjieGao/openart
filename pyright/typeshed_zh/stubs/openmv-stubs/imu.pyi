"""
imu 模块用于读取摄像头传感器下的 6 自由度 LSM6DS3 IMU 传感器。
"""

from typing import Tuple
from typing import List
from typing import Optional
from typing import Any
import image

def acceleration_mg() -> Tuple[float, float, float]:
    """
    返回浮点元组中（x，y，z）的加速度，单位为毫克（mg）。
    当摄像头板面朝上放在桌子上时：
    X 指向相机传感器的右侧 Y 指向相机传感器下方（朝向板子的底部） Z 指向相机传感器的相反方向（进入桌子）
    """
    pass
    
    
def angular_rate_mdps() -> Tuple[float, float, float]:
    """
    返回以毫度每秒（mdps）为单位的角速率 (x, y, z) 的浮点元组。
    当摄像头板面朝上放在桌子上时：
    X 指向相机传感器的右侧 Y 指向相机传感器下方（朝向板子的底部） Z 指向相机传感器的相反方向（进入桌子）
    """
    pass
    
    
def temperature_c() -> float:
    """
    返回摄氏温度（浮点数）。
    """
    pass
    
    
def roll() -> float:
    """
    返回相机模块以度为单位（浮点数）的旋转角度。
    """
    pass
    
    
def pitch() -> float:
    """
    返回相机模块以度为单位（浮点数）的旋转角度。
    """
    pass
    
    
def sleep(enable: bool) -> None:
    """
    传入 True 将 IMU 传感器置于睡眠状态。传入 False 将其唤醒（默认情况下）。
    """
    pass
    
    
def __write_reg(addr: int,val: int) -> None:
    """
    将 8 位 LSM6DS3 寄存器 addr 设置为 8 位 val。
    """
    pass
    
    
def __read_reg(addr: int) -> int:
    """
    获取 8 位 LSM6DS3 寄存器 addr。
    """
    pass
    
    
