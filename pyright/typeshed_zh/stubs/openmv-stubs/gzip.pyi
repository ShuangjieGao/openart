"""
Gzip compression & decompression.

MicroPython module: https://docs.micropython.org/en/vab847696a/library/gzip.html

CPython module: :mod:`python:gzip` https://docs.python.org/3/library/gzip.html .

此模块允许使用 gzip 文件格式采用的 `DEFLATE算法 <https://en.wikipedia.org/wiki/DEFLATE>`_ 对二进制数据进行压缩和解压缩。

``Note:`` 优先使用 :class:`deflate.DeflateIO`，而不是本模块中的函数，因为它提供了对压缩和解压缩的流接口，当处理读取或写入压缩数据到文件、套接字或流时更方便且更节省内存。

**可用性：**

* 此模块 **默认不包含** 在官方 MicroPython 固件发布中，因为它复制了 :mod:`deflate <deflate>` 模块中可用的功能。

* 此模块的副本可以从 :term:`micropython-lib` （ `source <https://github.com/micropython/micropython-lib/blob/master/python-stdlib/gzip/gzip.py>`_ ）安装（或冻结）。有关更多信息，请参阅 :ref:`packages`。本文档描述了该模块。

* 只有在内置的 :mod:`deflate <deflate>` 模块中启用了压缩支持时，才能使用压缩支持。
"""

# source version: vab847696a
# origin module:: repos/micropython/docs/library/gzip.rst
from __future__ import annotations
from _typeshed import Incomplete
class GzipFile():
    """
       此类可用于包装一个 *fileobj* ，它是任何 :term:`stream-like <stream>` 对象，例如文件、套接字或流（包括 :class:`io.BytesIO`）。它本身就是一个流，并实现了标准的 read/readinto/write/close 方法。
    
       当 *mode* 参数为 ``"rb"`` 时，从 GzipFile 实例读取将会解压缩底层流中的数据并返回解压缩后的数据。
    
       如果启用了压缩支持，则 *mode* 参数可以设置为 ``"wb"``，并且对 GzipFile 实例的写入将被压缩并写入底层流。
    
       默认情况下，GzipFile 类将使用 gzip 文件格式读取和写入数据，包括带有校验和的页眉和页脚以及 512 字节的窗口大小。
    
       **file**、**compresslevel** 和 **mtime** 参数不受支持。必须始终指定 **fileobj** 和 **mode** 作为关键字参数。
    """
    def __init__(self, *, fileobj, mode) -> None:
        ...
def open(filename, mode, ) -> Incomplete:
    """
       对内置 :func:`open` 函数的封装，返回一个 GzipFile 实例。
    """
    ...
def decompress(data, ) -> Incomplete:
    """
       将 *data* 解压缩为一个字节对象。
    """
    ...
def compress(data, ) -> Incomplete:
    """
       将 *data* 压缩为一个字节对象。
    """
    ...
