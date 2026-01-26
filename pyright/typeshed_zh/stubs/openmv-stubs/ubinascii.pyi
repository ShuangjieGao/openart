"""
Binary/ASCII conversions.

MicroPython module: https://docs.micropython.org/en/vab847696a/library/binascii.html

CPython module: :mod:`python:binascii` https://docs.python.org/3/library/binascii.html .

该模块实现了二进制数据与其各种 ASCII 表示形式之间的转换（双向）。
"""

# source version: vab847696a
# origin module:: repos/micropython/docs/library/binascii.rst
from __future__ import annotations
from typing import Any, Optional
from _typeshed import Incomplete
def hexlify(data, sep: Optional[Any]=None) -> bytes:
    """
       将 *data* 对象中的字节转换为十六进制表示形式。返回一个字节对象。
    
       如果提供了额外参数 *sep*，则用作十六进制值之间的分隔符。
    """
    ...
def unhexlify(data) -> bytes:
    """
       将十六进制数据转换为二进制表示形式。返回字节字符串。（即 hexlify 的反向）
    """
    ...
def a2b_base64(data) -> bytes:
    """
       解码 base64 编码的数据，忽略输入中的无效字符。符合 `RFC 2045 s.6.8 <https://tools.ietf.org/html/rfc2045#section-6.8>`_。返回一个字节对象。
    """
    ...
def b2a_base64(data, *, newline=True) -> bytes:
    """
       将二进制数据编码为 base64 格式，如 `RFC 3548 <https://tools.ietf.org/html/rfc3548.html>`_ 中所述。返回编码后的数据，如果 newline 为 true，则跟随一个换行符，作为一个字节对象。
    """
    ...
