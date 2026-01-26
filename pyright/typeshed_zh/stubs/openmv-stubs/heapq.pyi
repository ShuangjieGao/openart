"""
Heap queue algorithm.

MicroPython module: https://docs.micropython.org/en/vab847696a/library/heapq.html

CPython module: :mod:`python:heapq` https://docs.python.org/3/library/heapq.html .

此模块实现了 `最小堆队列算法 <https://en.wikipedia.org/wiki/Heap_%28data_structure%29>`_。

堆队列本质上是一个列表，其元素以这样的方式存储：列表的第一个项目始终是最小的。
"""

# source version: vab847696a
# origin module:: repos/micropython/docs/library/heapq.rst
from __future__ import annotations
from _typeshed import Incomplete
def heappush(heap, item) -> Incomplete:
    """
       将 ``item`` 推入 ``heap`` 中。
    """
    ...
def heappop(heap) -> Incomplete:
    """
       从 ``heap`` 中弹出第一个项目，并返回它。如果 ``heap`` 为空，则引发 ``IndexError`` 。
    
       返回的项目将是 ``heap`` 中最小的项目。
    """
    ...
def heapify(x) -> Incomplete:
    """
       将列表 ``x`` 转换为堆。这是一个就地操作。
    """
    ...
