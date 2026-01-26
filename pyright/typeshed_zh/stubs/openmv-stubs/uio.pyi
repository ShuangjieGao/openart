"""
Input/output streams.

MicroPython module: https://docs.micropython.org/en/vab847696a/library/io.html

CPython module: :mod:`python:io` https://docs.python.org/3/library/io.html .

此模块包含额外类型的 `std::term`（类似文件）对象和辅助函数。

概念层次结构
--------------------

与CPython的不同之处

   概念层次结构 of stream base classes is simplified in MicroPython,
   as described in this section.

（抽象）基础流类作为所有具体类行为的基础，在 CPython 中遵循一些二分法（成对分类）。在 MicroPython 中，这些类被简化并隐式化，以提高效率并节省资源。

在 CPython 中的一个重要二分法是非缓冲流与缓冲流。在 MicroPython 中，所有流当前都是非缓冲的。这是因为所有现代操作系统，甚至许多实时操作系统和文件系统驱动程序已经在它们一侧进行了缓冲。添加另一层缓冲是适得其反的（一个称为“缓冲膨胀”的问题）并且占用宝贵的内存。注意，仍然有一些情况下缓冲可能是有用的，所以我们可能会在以后引入可选的缓冲支持。

但在 CPython 中，另一个重要的二分法与“缓冲性”相关 - 它是关于流是否可能发生短读/写的。短读是指用户从流中请求例如 10 个字节，但得到的少于此数量，对于写入也是类似的。在 CPython 中，非缓冲流自动容易受到短操作的影响，而缓冲流则保证免受它们的影响。无短读/写是一个重要的特性，因为它允许开发更简洁高效的程序 - 这对于 MicroPython 来说是非常可取的。因此，虽然 MicroPython 不支持缓冲流，但它仍然提供了无短操作流。是否会有短操作取决于每个特定类的需求，但出于上述原因，强烈建议开发者倾向于无短操作行为。例如，MicroPython 套接字保证避免短读/写。实际上，目前在核心中没有短操作流类的例子，一个会是特定移植版本的类，其中这种需求由硬件特性决定。

在非阻塞流的情况下，无短操作行为变得棘手，阻塞与非阻塞行为是 CPython 的另一个二分法，MicroPython 完全支持。非阻塞流永远不会等待数据到达或被写入 - 它们读/写任何可能的数据，或信号数据缺失（或无法写入数据的能力）。显然，这与“无短操作”政策相冲突，确实，非阻塞缓冲（以及这种无短操作）流在 CPython 中的情况是复杂的 - 在某些地方，这种组合是禁止的，在某些地方它是未定义的或只是没有文档，在某些情况下它会引发详细的异常。在 MicroPython 中，情况要简单得多：非阻塞流对于高效的异步操作很重要，所以这个属性优先于“无短操作”属性。因此，虽然阻塞流会尽可能避免短读/写（唯一得到短读的情况是如果到达文件末尾，或在错误情况下（但错误不返回短数据，而是引发异常）），非阻塞流可能产生短数据以避免阻塞操作。

最后的二分法是二进制流与文本流。MicroPython 当然支持这些，但虽然在 CPython 中文本流本质上是缓冲的，它们在 MicroPython 中则不是。（实际上，这是我们可能引入缓冲支持的情况之一。）

注意，为了效率，MicroPython 不提供对应于上述层次结构的抽象基类，而且不可能在纯 Python 中实现或子类化流类。
"""

# source version: vab847696a
# origin module:: repos/micropython/docs/library/io.rst
from __future__ import annotations
from typing import IO, Any, Optional
from _typeshed import Incomplete
from stdlib.io import *  # type: ignore
class StringIO(IO):
    def __init__(self, string: Optional[Any]=None) -> None:
        ...
class BytesIO(IO):
    """
        内存中的类文件对象，用于输入/输出。`StringIO` 用于文本模式 I/O（类似于以 "t" 修饰符打开的普通文件）。`BytesIO` 用于二进制模式 I/O（类似于以 "b" 修饰符打开的普通文件）。类文件对象的初始内容可以用 *string* 参数指定（对于 `StringIO` 应该是普通字符串，对于 `BytesIO` 应该是字节对象）。所有常见的文件方法，如 ``read()``, ``write()``, ``seek()``, ``flush()``, ``close()`` 在这些对象上都可用，并且还有以下方法：
    """
    def __init__(self, string: Optional[Any]=None) -> None:
        ...
    def getvalue(self) -> Incomplete:
        """
                获取保存数据的底层缓冲区的当前内容。
        """
        ...
def open(name, mode='r', **kwargs) -> Incomplete:
    """
        打开一个文件。内置的 ``open()`` 函数被别名为此函数。所有的移植版本（提供对文件系统的访问）都需要支持 *mode* 参数，但对其他参数的支持因移植版本而异。
    """
    ...
