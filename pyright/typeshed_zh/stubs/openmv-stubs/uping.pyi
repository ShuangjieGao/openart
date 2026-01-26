"""
Ping another computer.

MicroPython module: https://docs.micropython.org/en/vab847696a/library/uping.html
"""

# source version: vab847696a
# origin module:: repos/micropython/docs/library/uping.rst
from __future__ import annotations
from _typeshed import Incomplete
def ping(host, count=4, timeout=5000, interval=10, quiet=False, size=64) -> int:
    """
        使用每个具有 ``timeout`` 的 ``count`` 个数据包对 ``host`` 进行 ping，每个数据包之间的速率为 ``interval``。如果 ``quiet`` 为 ``True``，则不打印返回时的统计信息。每个数据包的大小为 ``size`` 字节。
    
        返回一个包含发送的数据包数和接收的数据包数的元组。
    """
    ...
