"""
Mutex module.

MicroPython module: https://docs.micropython.org/en/vab847696a/library/mutex.html

``mutex`` 模块用于创建互斥锁。
"""

# source version: vab847696a
# origin module:: repos/micropython/docs/library/mutex.rst
from __future__ import annotations
from _typeshed import Incomplete
class Mutex():
    """
       创建一个未锁定的互斥锁对象。
    
       方法
       ~~~~~~~
    """
    def __init__(self) -> None:
        ...
    def release(self) -> Incomplete:
        """
           解锁互斥锁。
        """
        ...
    def test(self) -> bool:
        """
           尝试以非阻塞方式获取互斥锁。成功返回 ``True``，失败返回 ``False``。
        
           您也可以使用 ``with`` 以阻塞方式获取互斥锁。
        """
        ...
