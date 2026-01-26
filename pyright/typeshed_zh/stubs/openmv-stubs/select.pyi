"""
Wait for events on a set of streams.

MicroPython module: https://docs.micropython.org/en/vab847696a/library/select.html

CPython module: :mod:`python:select` https://docs.python.org/3/library/select.html .

该模块提供了一组函数，用于有效地等待多个 :std:term:`streams <stream>` （已准备好进行操作的选择流）上的事件。
"""

# source version: vab847696a
# origin module:: repos/micropython/docs/library/select.rst
from __future__ import annotations
from typing import Any, Iterator, List, Optional, Tuple
from _typeshed import Incomplete
class poll():
    """
       创建一个Poll类的实例。
    """
    def __init__(self) -> None:
        ...
    def register(self, obj, eventmask: Optional[Any]=None) -> None:
        """
           将 :std:term:`streams <stream>` *obj* 注册到轮询中。*eventmask* 是以下值的逻辑或：
        
           * ``select.POLLIN`` - 可读数据
           * ``select.POLLOUT`` - 可写入更多数据
        
           请注意，像 ``select.POLLHUP`` 和 ``select.POLLERR`` 这样的标志作为输入事件掩码不是有效的（这些是不被请求的事件，无论是否请求，都将从 `poll()` 返回）。这一语义符合POSIX标准。
        
           *eventmask* 默认为 ``select.POLLIN | select.POLLOUT``。
        
           可以多次调用此函数以对同一 *obj* 进行注册。连续调用将更新 *obj* 的事件掩码为 *eventmask* 的值（即将表现为 `modify()`）。
        """
        ...
    def unregister(self, obj) -> Incomplete:
        """
           将 *obj* 从轮询中注销。
        """
        ...
    def modify(self, obj, eventmask) -> None:
        """
           修改 *obj* 的 *eventmask*。如果 *obj* 未注册，则引发 `OSError` 并显示 ENOENT 错误。
        """
        ...
    def poll(self, timeout=-1, ) -> List:
        """
           等待至少一个已注册对象变为就绪或出现异常情况，可选择指定毫秒级超时（如果未指定 *timeout* 参数或为-1，则没有超时）。
        
           返回 (``obj``, ``event``, ...) 元组列表。元组中可能还有其他元素，这取决于平台和版本，因此不要假设其大小为2。 ``event`` 元素指定流发生了哪些事件，并且是上述 `select.POLL*` 常量的组合。请注意，标志 ``select.POLLHUP`` 和 ``select.POLLERR`` 可以随时返回（即使没有被请求），必须相应地进行处理（从轮询中注销相应的流并可能关闭），因为否则所有后续对 `poll()` 的调用可能会立即返回，并再次设置这些流的标志。
        
           在超时情况下，返回一个空列表。
        
           与CPython的不同之处
        
              如上所述，返回的元组可能包含2个以上元素。
        """
        ...
    def ipoll(self, timeout=-1, flags=0, ) -> Iterator[Tuple]:
        """
           类似于 :meth:`poll.poll`，但返回一个迭代器，该迭代器生成 `callee-owned tuple`。此函数提供了一种有效的，无分配的方式来轮询流。
        
           如果 *flags* 为1，则采用一次性行为以处理事件：发生事件的流将自动重置其事件掩码（相当于 ``poll.modify(obj, 0)``），因此对于这样的流，新事件将不会被处理，直到使用 `poll.modify()` 设置了新的掩码。这种行为对于异步I/O调度器非常有用。
        
           与CPython的不同之处
        
              此函数是MicroPython 的扩展。
        """
        ...
def select(rlist, wlist, xlist, timeout: Optional[Any]=None) -> None:
    """
       等待一组对象上的活动。
    
       此函数由某些MicroPython移植版本提供以确保兼容性，但效率不高。建议使用 :class:`Poll`。
    """
    ...
