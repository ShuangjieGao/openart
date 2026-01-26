"""
System specific functions.

MicroPython module: https://docs.micropython.org/en/vab847696a/library/sys.html

CPython module: :mod:`python:sys` https://docs.python.org/3/library/sys.html .
"""

# source version: vab847696a
# origin module:: repos/micropython/docs/library/sys.rst
from __future__ import annotations
from typing import Dict, List, Tuple
from _typeshed import Incomplete
argv: List
"""当前程序启动时使用的可变参数列表。"""
byteorder: Incomplete
"""系统的字节顺序（``"little"`` 或 ``"big"``）。"""
implementation: Incomplete
"""\
包含有关当前Python实现的信息的对象。对于MicroPython，它具有以下属性：

* *name* - 字符串 "micropython"
* *version* - 元组 (major, minor, micro, releaselevel)，例如 (1, 22, 0, '')
* *_machine* - 描述底层机器的字符串
* *_mpy* - 支持的 mpy 文件格式版本（可选属性）

此对象是推荐的区分 MicroPython 和其他 Python 实现的方式（请注意，它仍然可能不存在于非常小的移植版本中）。

从版本 1.22.0-preview 开始，*implementation.version* 中的第四个节点 *releaselevel* 要么是空字符串，要么是 ``"preview"``。

与CPython的不同之处

CPython 对此对象规定了更多的属性，但实际有用的最低限度是在 MicroPython中实现的。
"""
maxsize: int
"""\
当前平台的整机整数类型可以容纳的最大值，或者如果MicroPython整数类型的最大值小于平台最大值（这是没有长整型支持的MicroPython移植版本的情况）。

这个属性对于检测平台的 "位数"（32位还是64位等）非常有用。建议不直接将此属性与某个值进行比较，而是计算其中的位数::

bits = 0
v = sys.maxsize
while v:
bits += 1
v >>= 1
if bits > 32:
# 64-bit (or more) platform
"""
modules: Dict
"""\
已加载模块的字典。在某些移植版本上，可能不包括内置模块。
"""
path: List
"""\
用于搜索导入模块的可变目录列表。

与CPython的不同之处

在 MicroPython 中，一个带有值为 ``".frozen"`` 的条目表示导入应在搜索中的该点搜索 :term:`冻结模块 <frozen module>`。如果找不到冻结模块，则搜索不会继续寻找名为 ``.frozen`` 的目录，而是会继续下一个条目中 ``sys.path``。
"""
platform: Incomplete
"""\
MicroPython 运行的平台。对于 OS/RTOS 移植版本，这通常是操作系统的标识符，例如 ``"linux"``。对于裸机移植版本，它是一个板的标识符，例如原始的 MicroPython 参考板的 ``"pyboard"``。因此，它可用于区分一个板与另一个板。如果您需要检查您的程序是否在 MicroPython 上运行（与其他 Python 实现相比），请改用 `sys.implementation`。
"""
ps1: Incomplete
"""\
包含字符串的可变属性，用于REPL提示符。默认值为标准Python提示符 ``>>>`` 和 ``...``。
"""
ps2: Incomplete
"""\
包含字符串的可变属性，用于REPL提示符。默认值为标准Python提示符 ``>>>`` 和 ``...``。
"""
stderr: Incomplete
"""标准错误 :std:term:`stream`。"""
stdin: Incomplete
"""标准输入 :std:term:`stream`。"""
stdout: Incomplete
"""标准输出 :std:term:`stream`。"""
tracebacklimit: int
"""\
这是一个可变属性，包含一个整数值，是异常中存储的最大回溯条目数。设置为0以禁用添加回溯。默认为1000。

注意：这些功能并非在所有移植版本上都可用。
"""
version: str
"""该实现符合的 Python 语言版本，以字符串形式表示。"""
version_info: Tuple
"""\
该实现符合的 Python 语言版本，以整数元组的形式表示。

与CPython的不同之处

仅支持前三个版本号（主版本、次版本、微版本），并且只能通过索引引用，而不能通过名称引用。
"""
def exit(retval=0, ) -> Incomplete:
    """
       以给定的退出码终止当前程序。底层上，此函数会引发 `SystemExit` 异常。如果给定了参数，则将其作为 `SystemExit` 的参数传递。
    """
    ...
def atexit(func) -> Incomplete:
    """
       注册 *fun*在终止时调用。*fun*必须是一个不带参数的可调对象，或 ``None`` 以禁用调用。``atexit`` 函数将返回此函数设置的先前值，最初为 ``None``。
    
       与CPython的不同之处
    
          此函数是 MicroPython 的扩展，旨在提供类似于 CPython 中的 :mod:`atexit` 模块。
    """
    ...
def print_exception(exc, file=stdout, ) -> None:
    """
       将异常及其回溯打印到文件样对象 *file*（默认为 `sys.stdout`）。
    
       与CPython的不同之处
    
          这是简化版本的函数，类似于 CPython 中的 ``traceback`` 模块中的函数。与 ``traceback.print_exception()`` 不同，此函数仅接受异常值，而不是异常类型、异常值和回溯对象； *file* 参数应为位置参数；不支持更多的参数。与 CPython 兼容的 ``traceback`` 模块可以在 `micropython-lib` 中找到。
    """
    ...
def settrace(tracefunc) -> None:
    """
       Enable tracing of bytecode execution.  For details see the `CPython
       documentation `<https://docs.python.org/3/library/sys.html#sys.settrace>.
    
       此函数需要自定义的 MicroPython 构建，因为它通常不包含在预构建的固件中（因为它会影响性能）。相关的配置选项是 *MICROPY_PY_SYS_SETTRACE*。
    """
    ...
