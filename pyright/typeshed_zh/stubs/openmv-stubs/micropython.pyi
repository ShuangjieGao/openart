"""
Access and control MicroPython internals.

MicroPython module: https://docs.micropython.org/en/vab847696a/library/micropython.html
"""

# source version: vab847696a
# origin module:: repos/micropython/docs/library/micropython.rst
from __future__ import annotations
from typing import Any, Optional, Tuple, TypeVar
from _typeshed import Incomplete
Const_T = TypeVar('Const_T',int, float, str, bytes, Tuple) # constant
def const(expr:Const_T) -> Const_T:
    """
       用于声明表达式是一个常量，以便编译器可以优化它。应使用此函数如下::
    
        from micropython import const
    
        CONST_X = const(123)
        CONST_Y = const(2 * CONST_X + 1)
    
       以这种方式声明的常量仍然可以从它们声明所在的模块外部作为全局变量访问。另一方面，如果常量以下划线开头，则它是隐藏的，它不作为全局变量可用，并且在执行期间不占用任何内存。
    
       此 `const` 函数被 MicroPython 解析器直接识别，并作为 :mod:`micropython` 模块的一部分提供，主要是为了可以编写同时在 CPython 和 MicroPython 下运行的脚本，遵循上述模式。
    """
    ...
def opt_level(level: Optional[Any]=None) -> Incomplete:
    """
       如果给出了 *level*，则此函数设置后续脚本编译的优化级别，并返回 ``None``。否则，它返回当前的优化级别。
    
       优化级别控制以下编译特性：
    
       - 断言：在级别 0，断言语句被启用并编译到字节码中；在级别 1 及更高级别，断言不会被编译。
       - 内置的 ``__debug__`` 变量：在级别 0，此变量扩展为 ``True``；在级别 1 及更高级别，它扩展为 ``False``。
       - 源代码行号：在级别 0、1 和 2，源代码行号将与字节码一起存储，以便异常可以报告它们发生的行号；在级别 3 及更高级别，不会存储行号。
    
       默认优化级别通常是级别 0。
    """
    ...
def alloc_emergency_exception_buf(size) -> Incomplete:
    """
       为紧急情况异常缓冲区分配 *size* 字节的 RAM（一个很好的大小大约是 100 字节）。该缓冲区用于在正常 RAM 分配失败时创建异常（例如在中断处理程序中），因此在这些情况下给出有用的回溯信息。
    
       使用此函数的好方法是将它放在主脚本的开头（例如 ``boot.py`` 或 ``main.py``），然后紧急异常缓冲区将为其后的所有代码激活。
    """
    ...
def mem_info(verbose: Optional[Any]=None) -> None:
    """
       打印有关当前使用的内存的信息。如果给出了 *verbose* 参数，则会打印额外的信息。
    
       打印的信息是实现相关的，但目前包括使用的堆栈和堆的数量。在详细模式下，它会打印出整个堆，指示哪些块正在使用，哪些是空闲的。
    """
    ...
def qstr_info(verbose: Optional[Any]=None) -> None:
    """
       打印当前内存化字符串的信息。如果提供了 *verbose* 参数，则会打印额外的信息。
    
       打印的信息依赖于具体实现，但目前包括内存化字符串的数量及其占用的 RAM 大小。在详细模式下，它还会打印出所有 RAM 内存化字符串的名称。
    """
    ...
def stack_use() -> int:
    """
       返回一个整数，表示当前正在使用的堆栈量。此绝对值并不特别有用，而是应该用于计算不同点的堆栈使用量之间的差异。
    """
    ...
def heap_lock() -> int:
    ...
def heap_unlock() -> int:
    ...
def heap_locked() -> bool:
    """
       锁定或解锁堆。当锁定时，无法进行内存分配，如果尝试进行任何堆分配，则会引发 `MemoryError`。如果堆被锁定，则 `heap_locked()` 返回一个真值。
    
       这些函数可以嵌套，即可以连续多次调用 `heap_lock()`，锁深度将增加，然后必须调用相同数量的 `heap_unlock()` 来重新使堆可用。
    
       `heap_unlock()` 和 `heap_locked()` 都以非负整数返回当前锁定深度（前者解锁后），0 表示堆未锁定。
    
       如果 REPL 在堆被锁定的情况下变为活动状态，则它将被强制解锁。
    
       注意：`heap_locked()` 在大多数移植版本上默认未启用，需要 ``MICROPY_PY_MICROPYTHON_HEAP_LOCKED``。
    """
    ...
def kbd_intr(chr) -> None:
    """
       设置将引发 `KeyboardInterrupt` 异常的字符。在脚本执行期间，默认情况下将此设置为 3，对应于 Ctrl-C。将 -1 传递给此函数将禁用捕获 Ctrl-C，将 3 传递给此函数将恢复它。
    
       此函数可用于防止捕获通常用于 REPL 的字符流上的 Ctrl-C，以防该流用于其他目的。
    """
    ...
def schedule(func, arg) -> Incomplete:
    """
       调度函数 *func* "立即" 执行。该函数将值 *arg* 作为其单个参数。 "立即" 的意思是 MicroPython 运行时将尽其所能在最早可能的时间执行该函数，前提是它还试图高效地执行，并且以下条件成立：
    
       - 已调度的函数永远不会抢占另一个已调度的函数。
       - 调度的函数始终在 "操作码之间" 执行，这意味着所有基本的 Python 操作（例如向列表附加）都是原子的。
       - A given port may define "critical regions" within which scheduled
         functions will never be executed.  函数 may be scheduled within
         a critical region but they will not be executed until that region
         is exited.  An example of a critical region is a preempting interrupt
         handler (an IRQ).
    
       此函数的一个用途是从抢占 IRQ 调度回调。这种 IRQ 对 IRQ 中运行的代码施加了限制（例如，堆可能被锁定），而调度一个稍后调用的函数将解除这些限制。
    
       注意：如果从抢占 IRQ 中调用 `schedule()`，则不允许内存分配，并且要传递给 `schedule()` 的回调是绑定方法，则直接传递这个会失败。这是因为创建对绑定方法的引用会导致内存分配。解决方案是在类构造函数中创建对该方法的引用，并将该引用传递给 `schedule()`。这在此处详细讨论 :ref:`参考文档 <isr_rules>` 中的 "创建 Python 对象" 下。
    
       有限队列用于保存调度的函数，如果队列已满，则 `schedule()` 将引发 `RuntimeError`。
    """
    ...
