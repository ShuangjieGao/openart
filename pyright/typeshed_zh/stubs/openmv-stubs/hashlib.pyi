"""
Hashing algorithms.

MicroPython module: https://docs.micropython.org/en/vab847696a/library/hashlib.html

CPython module: :mod:`python:hashlib` https://docs.python.org/3/library/hashlib.html .

此模块实现了二进制数据的散列算法。可用算法的确切清单取决于开发板。可能实现的算法包括：

* SHA256 - 当前代的现代散列算法（SHA2系列之一）。适用于加密安全目的。包含在MicroPython核心中，任何开发板都建议提供此算法，除非它有特定的代码大小限制。

* SHA1 - 上一代算法。不推荐用于新的用途，但SHA1是许多互联网标准和现有应用程序的一部分，因此，针对网络连接和互操作性的开发板将尝试提供此算法。

* MD5 - 一个遗留算法，不被认为是加密安全的。只有选定的开发板，针对与遗留应用程序的互操作性，将提供此算法。
"""

# source version: vab847696a
# origin module:: repos/micropython/docs/library/hashlib.rst
from __future__ import annotations
from typing import Any, Optional
from _typeshed import Incomplete
class sha256():
    """
        创建一个SHA256哈希器对象，并可选地向其输入 ``data``。
    """
    def __init__(self, data: Optional[Any]=None) -> None:
        ...
class sha1():
    """
        创建一个SHA1哈希器对象，并可选地向其输入 ``data``。
    """
    def __init__(self, data: Optional[Any]=None) -> None:
        ...
class md5():
    """
        创建一个MD5哈希器对象，并可选地向其输入 ``data``。
    """
    def __init__(self, data: Optional[Any]=None) -> None:
        ...
class hash():
    """ """
    def update(self, data) -> Incomplete:
        """
           向哈希中输入更多的二进制数据。
        """
        ...
    def digest(self) -> bytes:
        """
           返回通过哈希传递的所有数据的哈希值，作为一个字节对象。在调用此方法后，不能再向哈希中输入更多数据。
        """
        ...
    def hexdigest(self) -> Incomplete:
        """
           此方法未实现。使用 ``binascii.hexlify(hash.digest())`` 可以达到类似的效果。
        """
        ...
