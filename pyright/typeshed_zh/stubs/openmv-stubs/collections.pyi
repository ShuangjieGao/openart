"""
Collection and container types.

MicroPython module: https://docs.micropython.org/en/vab847696a/library/collections.html

CPython module: :mod:`python:collections` https://docs.python.org/3/library/collections.html .

该模块实现了高级的集合和容器类型，用于保存/累积各种对象。
"""

# source version: vab847696a
# origin module:: repos/micropython/docs/library/collections.rst
from __future__ import annotations
from typing import Any, Optional
from _typeshed import Incomplete
from stdlib.collections import OrderedDict as stdlib_OrderedDict, deque as stdlib_deque, namedtuple as stdlib_namedtuple
class deque(stdlib_deque):
    """
        Deques（双端队列）是一种类似于列表的容器，支持从deque的任一端进行 O(1)的附加和弹出操作。可以使用以下参数创建新的deque：
    
            - *iterable* 是在创建时用于填充 deque 的可迭代对象。它可以是一个空元组或列表，用于创建一个初始为空的 deque。
    
            - 必须指定 *maxlen*，deque将被限制为最大长度。一旦deque已满，添加的任何新项都将从另一端丢弃项。
    
            - 可选的 *flags* 可以为 1，以检查添加项时是否溢出。
    
        Deque 对象支持 `bool`、`len`、迭代以及下标加载和存储。它们还具有以下方法：
    """
    def __init__(self, iterable, maxlen, flags: Optional[Any]=None) -> None:
        ...
    def append(self, x) -> Incomplete:
        """
                将 *x* 添加到 deque 的右侧。如果启用了溢出检查且队列没有更多空间，将引发 ``IndexError``。
        """
        ...
    def appendleft(self, x) -> Incomplete:
        """
                将 *x* 添加到 deque 的左侧。如果启用了溢出检查且队列没有更多空间，将引发 ``IndexError``。
        """
        ...
    def pop(self) -> Incomplete:
        """
                从 deque 的右侧移除并返回一个项。如果队列为空，将引发 ``IndexError``。
        """
        ...
    def popleft(self) -> Incomplete:
        """
                从 deque 的左侧移除并返回一个项。如果队列为空，将引发 ``IndexError``。
        """
        ...
    def extend(self, iterable) -> Incomplete:
        """
                通过将 *iterable* 中的所有项追加到 deque 的右侧来扩展 deque。如果启用了溢出检查且 deque 没有更多空间，将引发 ``IndexError``。
        """
        ...
class OrderedDict(stdlib_OrderedDict):
    """
        ``dict`` 类型的子类，它记住并保留添加的键的顺序。当有序字典进行迭代时，键/项将以它们添加的顺序返回::
    
            from collections import OrderedDict
    
            # To make benefit of ordered keys, OrderedDict should be initialized
            # from sequence of (key, value) pairs.
            d = OrderedDict([("z", 1), ("a", 2)])
            # More items can be added as usual
            d["w"] = 5
            d["b"] = 3
            for k, v in d.items():
                print(k, v)
    
        输出::
    
            z 1
            a 2
            w 5
            b 3
    """
    def __init__(self, *args, **kwargs) -> None:
        ...
def namedtuple(name, fields) -> stdlib_namedtuple:
    """
        这是一个工厂函数，用于创建具有特定名称和字段集的新命名元组类型。命名元组是tuple 的子类，它允许不仅通过数字索引，而且还可以使用带有符号字段名称的属性访问语法来访问其字段。字段是指定字段名称的字符串序列。为了与 CPython 兼容，它也可以是一个带有空格分隔的字段名称的字符串（但这样效率较低）。使用示例::
    
            from collections import namedtuple
    
            MyTuple = namedtuple("MyTuple", ("id", "name"))
            t1 = MyTuple(1, "foo")
            t2 = MyTuple(2, "bar")
            print(t1.name)
            assert t2.name == t2[1]
    """
    ...
