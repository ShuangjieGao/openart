"""
Socket module.

MicroPython module: https://docs.micropython.org/en/vab847696a/library/socket.html

CPython module: :mod:`python:socket` https://docs.python.org/3/library/socket.html .

该模块提供了对BSD套接字接口的访问。

与CPython的不同之处

   为了效率和一致性，在MicroPython中，套接字对象直接实现了 :std:term:`stream`（类似文件）接口。在CPython中，您需要使用 `makefile()` 方法将套接字转换为类似文件的对象。此方法仍受MicroPython支持（但不执行任何操作），因此在与CPython兼容性有关的情况下，请确保使用它。

套接字地址格式
------------------------

``socket`` 模块的原生套接字地址格式是由 `getaddrinfo` 函数返回的不透明数据类型，必须使用它来解析文本地址（包括数值地址）::

    sockaddr = socket.getaddrinfo('www.micropython.org', 80)[0][-1]
    # You must use getaddrinfo() even for numeric addresses
    sockaddr = socket.getaddrinfo('127.0.0.1', 80)[0][-1]
    # Now you can use that address
    sock.connect(sockaddr)

使用 `getaddrinfo` 是处理地址的最有效（无论是在内存还是处理能力方面）和可移植的方法。

但是，``socket`` 模块（请注意，这与本文描述的原生MicroPython ``socket`` 模块有所不同）提供了一种与CPython兼容的方式来使用元组指定地址，如下所述。请注意，根据 :term:`MicroPython port`，``socket`` 模块可以是内置的，也可以需要从 `micropython-lib` （如：MicroPython Unix移植版本）安装，并且一些移植版本仍然仅接受元组格式的数值地址，并且需要使用 `getaddrinfo` 函数来解析域名。

总结：

* 编写可移植应用程序时，请始终使用 `getaddrinfo`。
* 如果您的移植版本支持它们，则可以将下面描述的元组地址用作快速处理和交互使用的快捷方式。

``socket`` 模块的元组地址格式：

* IPv4：*(ipv4_address, port)*，其中*ipv4_address*是具有点符号数值IPv4地址的字符串，例如 ``"8.8.8.8"``，而*port*是1-65535范围内的整数端口号。请注意，域名不被接受为*ipv4_address*，它们应首先使用 `socket.getaddrinfo()` 解析。
* IPv6：*(ipv6_address, port, flowinfo, scopeid)*，其中*ipv6_address*是具有冒号表示法数值IPv6地址的字符串，例如 ``"2001:db8::1"``，而*port*是1-65535范围内的整数端口号。*flowinfo*必须为0。*scopeid*是链路本地地址的接口范围标识符。请注意，域名不被接受为*ipv6_address*，它们应首先使用 `socket.getaddrinfo()` 解析。IPv6支持的可用性取决于 :term:`MicroPython port`。
"""

# source version: vab847696a
# origin module:: repos/micropython/docs/library/socket.rst
from __future__ import annotations
from typing import IO, Any, Optional, Tuple
from _typeshed import Incomplete
from stdlib.socket import *  # type: ignore
AF_INET: Incomplete
"""地址族类型。可用性取决于特定的 :term:`MicroPython移植版本`。"""
AF_INET6: Incomplete
"""地址族类型。可用性取决于特定的 :term:`MicroPython移植版本`。"""
SOCK_STREAM: Incomplete
"""套接字类型。"""
SOCK_DGRAM: Incomplete
"""套接字类型。"""
IPPROTO_UDP: Incomplete
"""\
IP协议号。可用性取决于特定的 :term:`MicroPython移植版本`。请注意，您不需要在调用 `socket.socket()` 时指定这些值，因为 `SOCK_STREAM` 套接字类型会自动选择 `IPPROTO_TCP`，和 `SOCK_DGRAM` - `IPPROTO_UDP`。因此，这些常量的唯一真正用途是作为 `setsockopt()` 的参数。
"""
IPPROTO_TCP: Incomplete
"""\
IP协议号。可用性取决于特定的 :term:`MicroPython移植版本`。请注意，您不需要在调用 `socket.socket()` 时指定这些值，因为 `SOCK_STREAM` 套接字类型会自动选择 `IPPROTO_TCP`，和 `SOCK_DGRAM` - `IPPROTO_UDP`。因此，这些常量的唯一真正用途是作为 `setsockopt()` 的参数。
"""
# SOL_*: Incomplete
"""\
套接字选项级别（用于 `setsockopt()` 的参数）。确切的清单取决于 :term:`MicroPython移植版本`。
"""
# SO_*: Incomplete
"""\
套接字选项（用于 `setsockopt()` 的参数）。确切的清单取决于 :term:`MicroPython移植版本`。
"""
IPPROTO_SEC: Incomplete
"""创建与SSL兼容的套接字的特殊协议值。"""
class socket():
    """
       使用给定的地址族、套接字类型和协议号创建一个新的套接字。请注意，在大多数情况下，指定*proto*是不需要的（也不建议的，因为一些MicroPython移植版本可能会省略 ``IPPROTO_*`` 常量）。相反，*type*参数将自动选择所需的协议::
    
            # Create STREAM TCP socket
            socket(AF_INET, SOCK_STREAM)
            # Create DGRAM UDP socket
            socket(AF_INET, SOCK_DGRAM)
    """
    def __init__(self, af=AF_INET, type=SOCK_STREAM, proto=IPPROTO_TCP, ) -> None:
        ...
    def close(self) -> Incomplete:
        """
           标记套接字关闭并释放所有资源。一旦发生这种情况，套接字对象上的所有未来操作都将失败。如果协议支持，远程端将接收EOF指示。
        
           当套接字被垃圾收集时，它们会自动关闭，但建议在完成对它们的操作后明确地 `close()` 它们。
        """
        ...
    def bind(self, address) -> Incomplete:
        """
           将套接字绑定到*sddress*。套接字必须尚未绑定。
        """
        ...
    def listen(self, backlog: Optional[Any]=None) -> None:
        """
           启用服务器接受连接。如果指定了*backlog*，它必须至少为0（如果低于此值，则将设置为0）；并指定系统在拒绝新连接之前允许的未接受连接的数量。如果未指定，则选择一个默认合理的值。
        """
        ...
    def accept(self) -> Tuple:
        """
           接受连接。套接字必须绑定到地址并侦听连接。返回值是一对（conn，address），其中conn是一个新的套接字对象，可用于在连接上发送和接收数据，而address是与连接的另一端绑定到的套接字的地址。
        """
        ...
    def connect(self, address) -> None:
        """
           连接到*address*处的远程套接字。
        """
        ...
    def send(self, bytes) -> int:
        """
           将数据发送到套接字。套接字必须连接到远程套接字。返回发送的字节数，这可能小于数据的长度（“短写”）。
        """
        ...
    def sendall(self, bytes) -> int:
        """
           将所有数据发送到套接字。套接字必须连接到远程套接字。与 `send()` 不同，此方法将尝试发送所有数据，通过连续逐块发送数据。
        
           非阻塞套接字上此方法的行为未定义。因此，在MicroPython上，建议使用 `write()` 方法，该方法对于阻塞套接字具有相同的“无短写”策略，并且在非阻塞套接字上返回发送的字节数。
        """
        ...
    def recv(self, bufsize) -> bytes:
        """
           从套接字接收数据。返回一个表示接收到的数据的字节对象。一次要接收的最大数据量由bufsize指定。
        """
        ...
    def sendto(self, bytes, address) -> None:
        """
           将数据发送到套接字。套接字不应该连接到远程套接字，因为目标套接字由*address*指定。
        """
        ...
    def recvfrom(self, bufsize) -> Tuple:
        """
          从套接字接收数据。返回一个*(bytes, address)*对，其中*bytes*是表示接收到的数据的字节对象，而*address*是发送数据的套接字的地址。
        """
        ...
    def setsockopt(self, level, optname, value) -> None:
        """
           设置给定套接字选项的值。所需的符号常量在套接字模块中定义（SO_*等）。*value*可以是一个整数或表示缓冲区的类似字节的对象。
        """
        ...
    def settimeout(self, value) -> Incomplete:
        """
           **注意**：并非每个移植版本都支持此方法，请参见下文。
        
           对阻塞套接字操作设置超时。值参数可以是表示秒数的非负浮点数，也可以为None。如果给出了非零值，则在操作完成之前，如果超时周期值已过去，则后续的套接字操作将引发 `OSError` 异常。如果给出了零，则套接字将置于非阻塞模式。如果给出了None，则套接字将置于阻塞模式。
        
           并非每个 :term:`MicroPython移植版本` 都支持此方法。更便携和通用的解决方案是使用 `select.poll` 对象。这允许在多个对象上同时等待（不仅仅是套接字，还有支持轮询的通 用 :std:term:`stream` 对象）。示例::
        
                # Instead of:
                s.settimeout(1.0)  # time in seconds
                s.read(10)  # may timeout
        
                # Use:
                poller = select.poll()
                poller.register(s, select.POLLIN)
                res = poller.poll(1000)  # time in milliseconds
                if not res:
                    # s is still not ready for input, i.e. operation timed out
        
           与CPython的不同之处
        
              在超时的情况下，CPython会引发一个 ``socket.timeout`` 异常，它是 `OSError` 的子类。MicroPython直接引发OSError。如果您使用 ``except OSError:`` 捕获异常，则您的代码将在MicroPython和CPython中均可工作。
        """
        ...
    def setblocking(self, flag) -> Incomplete:
        """
           设置套接字的阻塞或非阻塞模式：如果flag为false，则将套接字设置为非阻塞模式，否则设置为阻塞模式。
        
           该方法是某些 `settimeout()` 调用的简写：
        
           * ``sock.setblocking(True)`` 等同于 ``sock.settimeout(None)``
           * ``sock.setblocking(False)`` 等同于 ``sock.settimeout(0)``
        """
        ...
    def makefile(self, mode='rb', buffering=0, ) -> IO:
        """
           返回与套接字关联的文件对象。返回的确切类型取决于传递给makefile()的参数。支持的仅限于二进制模式（'rb'、'wb'和'rwb'）。不支持CPython的参数：*encoding*、*errors*和*newline*。
        
           与CPython的不同之处
        
              由于MicroPython不支持缓冲流，因此*buffering*参数的值将被忽略，并视为0（无缓冲）。
        
           与CPython的不同之处
        
              关闭由makefile()返回的文件对象将同时关闭原始套接字。
        """
        ...
    def read(self, size: Optional[Any]=None) -> bytes:
        """
           从套接字读取最多size字节。返回一个字节对象。如果未给出*size*，则从套接字中读取所有可用的数据直到EOF；因此该方法在套接字关闭之前不会返回。此函数尝试读取所请求的所有数据（没有“短读取”）。这对于非阻塞套接字可能不可能，然后将返回的数据量较少。
        """
        ...
    def readinto(self, buf, nbytes: Optional[Any]=None) -> int:
        """
           将字节读入*buf*中。如果指定了*nbytes*，则最多读取*nbytes*字节。否则，最多读取*len(buf)*字节。就像 `read()` 一样，此方法遵循“无短读取”策略。
        
           返回值：读取并存储到*buf*中的字节数。
        """
        ...
    def readline(self) -> Incomplete:
        """
           读取一行，以换行字符结束。
        
           返回值：读取的行。
        """
        ...
    def write(self, buf) -> int:
        """
           将字节缓冲区写入套接字。此函数将尝试将所有数据写入套接字（没有“短写”）。这对于非阻塞套接字可能不可能，然后返回的值将小于*buf*的长度。
        
           返回值：写入的字节数。
        """
        ...
class error(Exception) : ...
def getaddrinfo(host, port, af=0, type=0, proto=0, flags=0, ) -> Incomplete:
    """
       将主机/端口参数转换为一个包含所有必要参数的5元组序列，以便创建连接到该服务的套接字。参数*af*、*type*和*proto*（与 `socket()` 函数的含义相同）可用于过滤返回的地址类型。如果未指定或设置为零，则可以返回所有地址组合（在用户端需要进行过滤）。
    
       结果列表的5元组具有以下结构::
    
          (family, type, proto, canonname, sockaddr)
    
       以下示例显示了如何连接到给定的url::
    
          s = socket.socket()
          # This assumes that if "type" is not specified, an address for
          # SOCK_STREAM will be returned, which may be not true
          s.connect(socket.getaddrinfo('www.micropython.org', 80)[0][-1])
    
       推荐使用过滤参数::
    
          s = socket.socket()
          # Guaranteed to return an address which can be connect'ed to for
          # stream operation.
          s.connect(socket.getaddrinfo('www.micropython.org', 80, 0, SOCK_STREAM)[0][-1])
    
       与CPython的不同之处
    
          在此函数出错时，CPython会引发一个 ``socket.gaierror`` 异常（`OSError` 子类）。MicroPython没有 ``socket.gaierror``，而是直接引发OSError。请注意，`getaddrinfo()` 的错误编号形成了一个独立的命名空间，可能与 :mod:`errno` 模块中的错误编号不匹配。为了区分 `getaddrinfo()` 错误，它们用负数表示，而标准系统错误使用正数表示（可以使用异常对象的 ``e.args[0]`` 属性访问错误编号）。负值的使用是一个临时的细节，将来可能会改变。
    """
    ...
def inet_ntop(af, bin_addr) -> Incomplete:
    """
       将给定地址族*af*的二进制网络地址*bin_addr*转换为文本表示::
    
            >>> socket.inet_ntop(socket.AF_INET, b"\x7f\0\0\1")
            '127.0.0.1'
    """
    ...
def inet_pton(af, txt_addr) -> Incomplete:
    """
       将给定地址族*af*的文本网络地址*txt_addr*转换为二进制表示::
    
            >>> socket.inet_pton(socket.AF_INET, "1.2.3.4")
            b'\x01\x02\x03\x04'
    """
    ...
