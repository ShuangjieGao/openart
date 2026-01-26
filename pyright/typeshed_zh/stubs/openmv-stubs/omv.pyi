"""
omv 模块用于获取 OpenMV Cam 信息。
"""

from typing import Tuple
from typing import List
from typing import Optional
from typing import Any
import image

def version_major() -> int:
    """
    返回主版本号（int）。
    """
    pass
    
    
def version_minor() -> int:
    """
    返回次版本号（int）。
    """
    pass
    
    
def version_patch() -> int:
    """
    返回补丁版本号（int）。
    """
    pass
    
    
def version_string() -> str:
    """
    返回补丁字符串（例如 “2.8.0”）。
    """
    pass
    
    
def arch() -> str:
    """
    返回板子架构字符串。该字符串实际上是为OpenMV IDE设计的，但您可以使用此函数获取它。
    """
    pass
    
    
def board_type() -> str:
    """
    返回板子类型字符串。该字符串实际上是为了OpenMV IDE 设计的，但您可以使用此函数获取它。
    """
    pass
    
    
def board_id() -> str:
    """
    返回板子 ID 字符串。该字符串实际上是为了OpenMV IDE 设计的。但您可以使用此函数获取它。
    """
    pass
    
    
def disable_fb(disable: bool | None = None) -> bool:
    """
    当 disable 设置为 True 时，OpenMV Cam 将不再对图像进行 JPEG 压缩并将其流式传输到 OpenMV IDE。除非在 OpenMV IDE 中选中了 Disable FB，否则 IDE 仍可能轮询图像。在使用 OpenMV IDE 调试脚本时，您可能希望在将图像流式传输到另一个系统时禁用帧缓冲区。如果没有传递参数，则此函数将返回帧缓冲区禁用时为 True，否则为 False。
    """
    pass
    
    
