"""
Deflate compression & decompression.

MicroPython module: https://docs.micropython.org/en/vab847696a/library/deflate.html

该模块允许使用 `DEFLATE 算法 <https://en.wikipedia.org/wiki/DEFLATE>`_ （通常用于 zlib 库和 gzip 压缩器）对二进制数据进行压缩和解压缩。

**可用性：**

* 在 MicroPython v1.21 中添加。

* 解压缩: 通过 ``MICROPY_PY_DEFLATE`` 构建选项启用，默认情况下在具有 "extra features " 级别或更高级别的移植版本上启用（大多数开发板）。

* 压缩: 通过 ``MICROPY_PY_DEFLATE_COMPRESS`` 构建选项启用，默认情况下在具有 "full features" 级别或更高级别的移植版本上启用（通常这意味着您需要构建自己的固件以启用此功能）。
"""

# source version: vab847696a
# origin module:: repos/micropython/docs/library/deflate.rst
from __future__ import annotations
from _typeshed import Incomplete
AUTO: Incomplete
"""*format* 参数支持的值。"""
RAW: Incomplete
"""*format* 参数支持的值。"""
ZLIB: Incomplete
"""*format* 参数支持的值。"""
GZIP: Incomplete
"""*format* 参数支持的值。"""
class DeflateIO():
    """
       这个类可以用来包装一个 *stream*，它是任何 :term:`stream-like <stream>` 对象，比如文件、套接字或流（包括 :class:`io.BytesIO`）。它本身是一个流，并实现了标准的read/readinto/write/close 方法。
    
       *stream* 必须是一个阻塞流。非阻塞流目前不受支持。
    
       *format* 可以设置为下面定义的任何常量，默认为 ``AUTO``，对于解压缩，它将自动检测 gzip 或 zlib 流，对于压缩，它将生成一个原始流。
    
       *wbits* 参数设置了 DEFLATE 字典窗口大小的以 2 为底的对数。例如，将 *wbits*设置为 ``10`` ，将窗口大小设置为 1024 字节。有效值为 ``5`` 到 ``15`` （包括）（对应窗口大小为 32 到 32k 字节）。
    
       如果 *wbits* 设置为 ``0`` （默认值），则对于压缩，将使用 256 字节的窗口大小（就好像 *wbits* 设置为 8）。对于解压缩，它取决于格式:
    
       * ``RAW`` 将使用 256 字节（对应 *wbits* 设置为 8）。
       * ``ZLIB`` （或检测到 zlib 的 ``AUTO``）将使用 zlib 标头中的值。
       * ``GZIP`` （或检测到 gzip 的 ``AUTO``）将使用 32 千字节（对应 *wbits* 设置为 15）。
    
       查看下面关于窗口大小、zlib 和 gzip 流的 :ref:`window size <deflate_wbits>` 注意事项，获取更多信息。
    
       如果 *close* 设置为 ``True``，那么在关闭 :class:`deflate.DeflateIO` 流时将自动关闭底层流。如果您希望返回一个包装另一个流的 :class:`deflate.DeflateIO` 流，并且不希望调用者知道如何管理底层流，这是有用的。
    
       如果启用了压缩，给定的 :class:`deflate.DeflateIO` 实例支持读和写。例如，可以包装一个双向流（如套接字），这样就可以在两个方向上进行压缩/解压缩。
    """
    def __init__(self, stream, format=AUTO, wbits=0, close=False, ) -> None:
        ...
