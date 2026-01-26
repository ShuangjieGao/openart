"""
Control the garbage collector.

MicroPython module: https://docs.micropython.org/en/vab847696a/library/gc.html

CPython module: :mod:`python:gc` https://docs.python.org/3/library/gc.html .
"""

# source version: vab847696a
# origin module:: repos/micropython/docs/library/gc.rst
from __future__ import annotations
from typing import Any, Optional
from _typeshed import Incomplete
def enable() -> None:
    """
       启用自动垃圾收集。
    """
    ...
def disable() -> None:
    """
       禁用自动垃圾收集。堆内存仍然可以被分配，垃圾收集仍然可以通过使用 :meth:`gc.collect` 手动启动。
    """
    ...
def collect() -> None:
    """
       运行一次垃圾收集。
    """
    ...
def mem_alloc() -> int:
    """
       返回由Python代码分配的堆RAM的字节数。
    
       与CPython的不同之处
    
          此函数是MicroPython扩展。
    """
    ...
def mem_free() -> int:
    """
       返回可供Python代码分配的堆RAM的字节数，如果此数量未知，则返回-1。
    
       与CPython的不同之处
    
          此函数是MicroPython扩展。
    """
    ...
def threshold(amount: Optional[Any]=None) -> Incomplete:
    """
       设置或查询额外的GC分配阈值。通常情况下，只有在新的分配无法满足时才会触发收集，即在内存不足（OOM）条件下。如果调用此函数，除了OOM条件外，每次分配 *amount* 字节（总的来说，因为上次已经分配了这么多字节）后都会触发一次收集。*amount* 通常指定为小于整个堆大小，意图是在堆耗尽之前触发收集，并希望提前收集将防止过度的内存碎片化。这是一种启发式措施，其效果将因应用程序而异，以及 *amount* 参数的最佳值也会有所不同。
    
       不带参数调用此函数将返回阈值的当前值。-1的值意味着禁用了分配阈值。
    
       与CPython的不同之处
    
          此函数是MicroPython扩展。CPython有一个类似的函数 - ``set_threshold()``，但由于GC实现不同，其签名和语义有所不同。
    """
    ...
