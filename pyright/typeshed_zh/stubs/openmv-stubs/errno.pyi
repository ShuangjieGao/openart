"""
System error codes.

MicroPython module: https://docs.micropython.org/en/vab847696a/library/errno.html

CPython module: :mod:`python:errno` https://docs.python.org/3/library/errno.html .

该模块提供了对 `OSError` 异常的符号化错误代码的访问。特定错误代码的清单取决于 :term:`MicroPython port` 。
"""

# source version: vab847696a
# origin module:: repos/micropython/docs/library/errno.rst
from __future__ import annotations
from typing import Dict
from _typeshed import Incomplete
EEXIST: Incomplete
"""\
错误代码，基于 ANSI C/POSIX 标准。所有错误代码以 "E" 开头。如上所述，错误代码的清单取决于 :term:`MicroPython port`。错误通常可以通过 ``exc.errno`` 访问，其中 ``exc`` 是 `OSError` 的一个实例。使用示例::

try:
os.mkdir("my_dir")
except OSError as exc:
if exc.errno == errno.EEXIST:
print("Directory already exists")
"""
EAGAIN: Incomplete
"""\
错误代码，基于 ANSI C/POSIX 标准。所有错误代码以 "E" 开头。如上所述，错误代码的清单取决于 :term:`MicroPython port`。错误通常可以通过 ``exc.errno`` 访问，其中 ``exc`` 是 `OSError` 的一个实例。使用示例::

try:
os.mkdir("my_dir")
except OSError as exc:
if exc.errno == errno.EEXIST:
print("Directory already exists")
"""
errorcode: Dict
"""\
将数值错误代码映射到带有符号错误代码的字符串的字典（参见上文）::

>>> print(errno.errorcode[errno.EEXIST])
EEXIST
"""
