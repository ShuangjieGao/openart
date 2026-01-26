"""
Zlib compression & decompression.

MicroPython module: https://docs.micropython.org/en/vab847696a/library/zlib.html

CPython module: :mod:`python:zlib` https://docs.python.org/3/library/zlib.html .

该模块允许使用 `DEFLATE 算法 <https://en.wikipedia.org/wiki/DEFLATE>`_ （通常用于 zlib 库和 gzip 压缩器）对二进制数据进行压缩和解压缩。

``Note:`` 优先使用 :class:`deflate.DeflateIO`，而不是本模块中的函数，因为它提供了对压缩和解压缩的流接口，当处理读取或写入压缩数据到文件、套接字或流时更方便且更节省内存。

**可用性：**

* 从 MicroPython v1.21 起，该模块可能不会默认出现在所有 MicroPython 固件中，因为它重复了 :mod:`deflate <deflate>` 模块中可用的功能。

* 该模块的副本可以从 :term:`micropython-lib`（`源代码 <https://github.com/micropython/micropython-lib/blob/master/python-stdlib/zlib/zlib.py>`_）安装（或冻结）。有关更多信息，请参阅 :ref:`packages`。本文档描述了该模块。

* 需要内置的 :mod:`deflate <deflate>` 模块（自 MicroPython v1.21 起可用）

* 只有在内置的 :mod:`deflate <deflate>` 模块中启用了压缩支持时，才能使用压缩支持。
"""

# source version: vab847696a
# origin module:: repos/micropython/docs/library/zlib.rst
from __future__ import annotations
from _typeshed import Incomplete
def decompress(data, wbits=15, ) -> Incomplete:
    """
       将 *data* 解压缩为一个字节对象。
    
       *wbits* 参数的工作方式与 :meth:`zlib.compress` 相同，但还支持以下额外的有效值：
    
       * ``0``: 从 zlib 头自动确定窗口大小（*data* 必须采用 zlib 格式）。
       * ``35`` 到 ``47``: 自动检测 zlib 或 gzip 格式。
    
       有关 *wbits* 参数的更多信息，请参阅 :meth:`zlib.compress` 的 :mod:`CPython 文档 <python:zlib>`。与 :meth:`zlib.compress` 类似，MicroPython 也支持比 CPython 更小的窗口大小。在 :mod:`deflate <deflate>` 模块文档中查看更多 :ref:`MicroPython 特定的详细信息 <deflate_wbits>`。
    
       如果要解压缩的数据需要更大的窗口大小，则在解压期间会失败。
    """
    ...
def compress(data, wbits=15, ) -> Incomplete:
    """
       将 *data* 压缩为一个字节对象。
    
       *wbits* 允许您配置 DEFLATE 字典窗口大小和输出格式。窗口大小允许您在内存使用和压缩级别之间进行权衡。较大的窗口大小将允许压缩器引用输入中更远处的片段。输出格式包括 "raw" DEFLATE（无头/尾），zlib 和 gzip，其中后两者包括头和校验和。
    
       *wbits* 的绝对值的低四位设置 DEFLATE 字典窗口大小的以2为基数的对数。因此，例如， ``wbits=10``、``wbits=-10`` 和 ``wbits=26`` 都将窗口大小设置为 1024 字节。有效的窗口大小为 ``5`` 到 ``15`` （对应于 32 到 32k 字节）。
    
       *wbits* 的负值介于 ``-5`` 和 ``-15`` 之间对应于 "raw" 输出模式，介于 ``5`` 和 ``15`` 之间的正值对应于 zlib 输出模式，介于 ``21`` 和 ``31`` 之间的正值对应于 gzip 输出模式。
    
       有关 *wbits* 参数的更多信息，请参阅 :mod:`CPython 文档 <python:zlib>`。注意，MicroPython 允许更小的窗口大小，这在内存受限的情况下非常有用，同时仍然可以实现合理的压缩水平。这也加速了压缩器。在 :mod:`deflate <deflate>` 模块文档中查看更多 :ref:`MicroPython 特定的详细信息 <deflate_wbits>`。
    """
    ...
