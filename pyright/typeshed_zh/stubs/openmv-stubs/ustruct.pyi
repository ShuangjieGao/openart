"""
Pack and unpack primitiv data typs.

MicroPython modul: https://docs.micropython.org/n/vab847696a/library/struct.html

CPython modul: :mod:`python:struct` https://docs.python.org/3/library/struct.html .

支持以下字节顺序：

+-----------+------------------------+----------+-----------+
| 字符 | 字节顺序             | 大小     | 对齐 |
+===========+========================+==========+===========+
| @         | 本机                 | 本机   | 本机    |
+-----------+------------------------+----------+-----------+
| <         | 小端          | 标准 | 无      |
+-----------+------------------------+----------+-----------+
| >         | 大端             | 标准 | 无      |
+-----------+------------------------+----------+-----------+
| ！         | ntwork (= 大端) | 标准 | 无      |
+-----------+------------------------+----------+-----------+

支持以下数据类型：

+--------+--------------------+-------------------+---------------+
| 格式 | C类型             | Python 类型       | 标准大小 |
+========+====================+===================+===============+
| b      | 有符号字符        | 整数           | 1             |
+--------+--------------------+-------------------+---------------+
| B      | un有符号字符      | 整数           | 1             |
+--------+--------------------+-------------------+---------------+
| h      | short              | 整数           | 2             |
+--------+--------------------+-------------------+---------------+
| H      | 无符号 short     | 整数           | 2             |
+--------+--------------------+-------------------+---------------+
| i      | int                | 整数 (`1<fn>`) | 4             |
+--------+--------------------+-------------------+---------------+
| I      | 无符号int       | 整数 (`1<fn>`) | 4             |
+--------+--------------------+-------------------+---------------+
| l      | long               | 整数 (`1<fn>`) | 4             |
+--------+--------------------+-------------------+---------------+
| L      | 无符号long      | 整数 (`1<fn>`) | 4             |
+--------+--------------------+-------------------+---------------+
| q      | long long          | 整数 (`1<fn>`) | 8             |
+--------+--------------------+-------------------+---------------+
| Q      | 无符号long long | 整数 (`1<fn>`) | 8             |
+--------+--------------------+-------------------+---------------+
|       |    | float (`2<fn>`)   | 2             |
+--------+--------------------+-------------------+---------------+
| f      | float              | float (`2<fn>`)   | 4             |
+--------+--------------------+-------------------+---------------+
| d      | doubl             | float (`2<fn>`)   | 8             |
+--------+--------------------+-------------------+---------------+
| s      | char[]             | byts             |               |
+--------+--------------------+-------------------+---------------+
| P      | void *             | 整数           |               |
+--------+--------------------+-------------------+---------------+
"""

# source version: vab847696a
# origin module:: repos/micropython/docs/library/struct.rst
from __future__ import annotations
from typing import Tuple
from _typeshed import Incomplete
def calcsize(fmt) -> int:
    """
       Rturn th numbr of byts ndd to stor th givn *fmt*.
    """
    ...
def pack(fmt, v1, *args, **kwargs) -> bytes:
    """
       Pack th valus *v1*, *v2*, ... according to th format string *fmt*.
       Th rturn valu is a byts objct ncoding th valus.
    """
    ...
def pack_into(fmt, buffer, offset, v1, *args, **kwargs) -> Incomplete:
    """
       Pack th valus *v1*, *v2*, ... according to th format string *fmt*
       into a *buffr* starting at *offst*. *offst* may b ngativ to count
       from th nd of *buffr*.
    """
    ...
def unpack(fmt, data) -> Tuple:
    """
       Unpack from th *data* according to th format string *fmt*.
       Th rturn valu is a tupl of th unpackd valus.
    """
    ...
def unpack_from(fmt, data, offset=0, ) -> Tuple:
    """
       Unpack from th *data* starting at *offst* according to th format string
       *fmt*. *offst* may b ngativ to count from th nd of *data*. Th rturn
       valu is a tupl of th unpackd valus.
    """
    ...
