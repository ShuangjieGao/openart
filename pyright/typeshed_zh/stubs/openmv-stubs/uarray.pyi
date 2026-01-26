"""
Efficient arrays of numeric data.

MicroPython module: https://docs.micropython.org/en/vab847696a/library/array.html

CPython module: :mod:`python:array` https://docs.python.org/3/library/array.html .

支持格式编码： ``b``, ``B``, ``h``, ``H``, ``i``, ``I``, ``l``, ``L``, ``q``, ``Q``, ``f``, ``d`` （后两种依赖于浮点支持）。
"""

# source version: vab847696a
# origin module:: repos/micropython/docs/library/array.rst
from __future__ import annotations
from typing import Any, List, Optional
from _typeshed import Incomplete
class array(List):
    """
        使用给定类型的元素创建数组。数组的初始内容由 *iterable* 给定。若未给定内容，则创建一个空数组。
    """
    def __init__(self, typecode, iterable: Optional[Any]=None) -> None:
        ...
    def append(self, val) -> Incomplete:
        """
                将 *val* 添加到数组末尾，并扩展数组。
        """
        ...
    def extend(self, iterable) -> Incomplete:
        """
                将包含在 *iterable* 中的新元素添加到数组末尾，并扩展数组。
        """
        ...
    def __getitem__(self, index) -> List[int]:
        """
                通过索引读取数组，使用 ``a[index]`` 的形式调用（其中 ``a`` 是一个 ``array``）。如果 *index* 是一个 ``int``，则返回一个值；如果 *index* 是一个切片，则返回一个 ``array``。如果索引为负数，则从末尾计数，如果索引超出范围，则引发 ``IndexError``。
        
                **注意：** 不能直接调用 ``__getitem__`` （``a.__getitem__(index)`` 会失败），也不在 ``__dict__`` 中，但是 ``a[index]`` 可以正常工作。
        """
        ...
    def __setitem__(self, index, value) -> Incomplete:
        """
                通过索引写入数组，使用 ``a[index] = value`` 的形式调用（其中 ``a`` 是一个 ``array``）。如果 *index* 是一个 ``int``，则 *value* 是一个值；如果 *index* 是一个切片，则 *value* 是一个 ``array``。如果索引为负数，则从末尾计数，如果索引超出范围，则引发 ``IndexError``。
        
                **注意：** 不能直接调用 ``__setitem__`` （``a.__setitem__(index, value)`` 会失败），也不在 ``__dict__`` 中，但是 ``a[index] = value`` 可以正常工作。
        """
        ...
    def __len__(self) -> int:
        """
                返回数组中的项数，使用 ``len(a)`` 的形式调用（其中 ``a`` 是一个 ``array``）。
        
                **注意：** 不能直接调用 ``__len__`` （``a.__len__()`` 会失败），方法也不在 ``__dict__`` 中，但是 ``len(a)`` 可以正常工作。
        """
        ...
    def __add__(self, other) -> Incomplete:
        """
                返回一个新的 ``array``，它是数组与 *other* 的连接，使用 ``a + other`` 的形式调用（其中 ``a`` 和 *other* 都是 ``arrays``）。
        
                **注意：** 不能直接调用 ``__add__`` （ ``a.__add__(other)`` 会失败），方法也不在 ``__dict__`` 中，但是 ``a + other`` 可以正常工作。
        """
        ...
    def __iadd__(self, other) -> Incomplete:
        """
                在原地将数组与 *other* 连接，使用 ``a += other`` 的形式调用（其中 ``a`` 和 *other* 都是 ``arrays``）。等效于 ``extend(other)``。
        
                **注意：** 不能直接调用 ``__iadd__`` （ ``a.__iadd__(other)`` 会失败），方法也不在 ``__dict__`` 中，但是 ``a += other`` 可以正常工作。
        """
        ...
    def __repr__(self) -> str:
        """
                返回数组的字符串表示形式，使用 ``str(a)`` 或 ``repr(a)`` 的形式调用（其中 ``a`` 是一个 ``array`` ）。返回字符串 ``"array(<type>, [<elements>])"``，其中 ``<type>`` 是数组的类型代码字母，``<elements>`` 是数组的元素的逗号分隔列表。
        
                **注意：** 不能直接调用 ``__repr__`` （ ``a.__repr__()`` 会失败），也不在 ``__dict__`` 中，但是 ``str(a)`` 和 ``repr(a)`` 都可以正常工作。
        """
        ...
