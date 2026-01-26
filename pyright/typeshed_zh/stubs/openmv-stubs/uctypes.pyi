"""
Access binary data in a structured way.

MicroPython module: https://docs.micropython.org/en/vab847696a/library/uctypes.html

该模块为MicroPython实现了“外部数据接口”。其背后的思想类似于CPython的 ``ctypes`` 模块，但实际API有所不同，经过简化和优化以适应小型尺寸。该模块的基本思想是使用与C语言允许的大致相同的功能来定义数据结构布局，然后使用熟悉的点语法来访问子字段。
"""

# source version: vab847696a
# origin module:: repos/micropython/docs/library/uctypes.rst
from __future__ import annotations
from _typeshed import Incomplete
LITTLE_ENDIAN: bytes
"""\
小端紧凑结构的布局类型。 （紧凑意味着每个字段占用的字节数与描述符中定义的一样多，即对齐为1）。
"""
BIG_ENDIAN: Incomplete
"""大端紧凑结构的布局类型。"""
NATIVE: Incomplete
"""\
本地结构的布局类型 - 数据字节序和对齐符合MicroPython运行所在系统的ABI。
"""
UINT8: int
"""\
结构描述符的整数类型。提供了8、16、32和64位类型的常量，有符号和无符号。
"""
INT8: int
"""\
结构描述符的整数类型。提供了8、16、32和64位类型的常量，有符号和无符号。
"""
UINT16: int
"""\
结构描述符的整数类型。提供了8、16、32和64位类型的常量，有符号和无符号。
"""
INT16: int
"""\
结构描述符的整数类型。提供了8、16、32和64位类型的常量，有符号和无符号。
"""
UINT32: int
"""\
结构描述符的整数类型。提供了8、16、32和64位类型的常量，有符号和无符号。
"""
INT32: int
"""\
结构描述符的整数类型。提供了8、16、32和64位类型的常量，有符号和无符号。
"""
UINT64: int
"""\
结构描述符的整数类型。提供了8、16、32和64位类型的常量，有符号和无符号。
"""
INT64: int
"""\
结构描述符的整数类型。提供了8、16、32和64位类型的常量，有符号和无符号。
"""
FLOAT32: Incomplete
"""结构描述符的浮点类型。"""
FLOAT64: Incomplete
"""结构描述符的浮点类型。"""
VOID: Incomplete
"""\
``VOID`` 是 ``UINT8`` 的别名，提供了方便地定义C的void指针的方法： ``(uctypes.PTR, uctypes.VOID)``。
"""
PTR: Incomplete
"""\
指针和数组的类型常量。请注意，没有显式的结构常量，它是隐式的：没有 ``PTR`` 或 ``ARRAY`` 标志的聚合类型是一个结构。
"""
ARRAY: Incomplete
"""\
指针和数组的类型常量。请注意，没有显式的结构常量，它是隐式的：没有 ``PTR`` 或 ``ARRAY`` 标志的聚合类型是一个结构。
"""
class struct():
    """
       基于内存中的结构地址、描述符（编码为字典）和布局类型（见下文）实例化一个“外部数据结构”对象。
    """
    def __init__(self, addr, descriptor, layout_type=NATIVE, ) -> None:
        ...
def sizeof(struct, layout_type=NATIVE, ) -> int:
    """
       返回数据结构的字节数。 *struct* 参数可以是结构类或特定实例化的结构对象（或其聚合字段）。
    """
    ...
def addressof(obj) -> int:
    """
       返回对象的地址。参数应为bytes、bytearray或支持缓冲区协议的其他对象（实际返回的是该缓冲区的地址）。
    """
    ...
def bytes_at(addr, size) -> bytes:
    """
       将给定地址和大小的内存捕获为字节对象。由于字节对象是不可变的，因此实际上会复制并复制内存到字节对象，因此如果稍后更改了内存内容，则创建的对象保留原始值。
    """
    ...
def bytearray_at(addr, size) -> bytearray:
    """
       将给定地址和大小的内存捕获为bytearray对象。不同于上面的bytes_at()函数，内存是通过引用捕获的，因此可以同时写入，并且您将访问给定内存地址的当前值。
    """
    ...
