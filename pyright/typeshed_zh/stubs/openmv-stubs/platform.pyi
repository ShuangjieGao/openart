"""
Access to underlying platform’s identifying data.

MicroPython module: https://docs.micropython.org/en/vab847696a/library/platform.html

CPython module: :mod:`python:platform` https://docs.python.org/3/library/platform.html .

该模块尝试尽可能多地检索平台识别数据。它通过函数API提供此信息。
"""

# source version: vab847696a
# origin module:: repos/micropython/docs/library/platform.rst
from __future__ import annotations
from typing import Tuple
from _typeshed import Incomplete
def platform() -> str:
    """
       返回一个字符串，标识底层平台。此字符串由几个子字符串组成，按照以下顺序用破折号（``-``）分隔：
    
       - 平台系统的名称（例如 Unix、Windows 或 MicroPython）
       - MicroPython 版本
       - 平台的架构
       - 底层平台的版本
       - MicroPython 链接到的 libc 的名称和其相应版本的连接字符串。
    
       例如，可能是 ``"MicroPython-1.20.0-xtensa-IDFv4.2.4-with-newlib3.0.0"``。
    """
    ...
def python_compiler() -> str:
    """
       返回一个字符串，标识用于编译 MicroPython 的编译器。
    """
    ...
def libc_ver() -> Tuple:
    """
       返回一个字符串元组 *(lib, version)*，其中 *lib* 是 MicroPython 链接到的 libc 的名称，*version* 是该 libc 的相应版本。
    """
    ...
