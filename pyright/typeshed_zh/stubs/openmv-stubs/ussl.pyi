"""
TLS/SSL wrapper for socket objects.

MicroPython module: https://docs.micropython.org/en/vab847696a/library/ssl.html

CPython module: :mod:`python:ssl` https://docs.python.org/3/library/ssl.html .

该模块提供了对传输层安全性（以前和广泛称为“安全套接字层”）加密和对等身份验证功能的访问，用于网络套接字，包括客户端和服务器端。
"""

# source version: vab847696a
# origin module:: repos/micropython/docs/library/ssl.rst
from __future__ import annotations
from typing import IO, List
from _typeshed import Incomplete
from stdlib.ssl import *  # type: ignore
SSLError: Incomplete
"""不存在此异常。相反，使用其基类，OSError。"""
PROTOCOL_TLS_CLIENT: Incomplete
"""*protocol* 参数支持的值。"""
PROTOCOL_TLS_SERVER: Incomplete
"""*protocol* 参数支持的值。"""
CERT_NONE: Incomplete
"""\
*cert_reqs* 参数支持的值，以及 :attr:`SSLContext.verify_mode` 属性。
"""
CERT_OPTIONAL: Incomplete
"""\
*cert_reqs* 参数支持的值，以及 :attr:`SSLContext.verify_mode` 属性。
"""
CERT_REQUIRED: Incomplete
"""\
*cert_reqs* 参数支持的值，以及 :attr:`SSLContext.verify_mode` 属性。
"""
class SSLContext():
    """
        创建一个新的 SSLContext 实例。 *protocol* 参数必须是 ``PROTOCOL_*`` 常量之一。
    """
    def __init__(self, protocol, ) -> None:
        ...
    def load_cert_chain(self, certfile, keyfile) -> None:
        """
           加载私钥和相应的证书。 *certfile* 是包含证书文件路径的字符串。 *keyfile* 是包含私钥文件路径的字符串。
        
           与CPython的不同之处
        
              MicroPython扩展：*certfile* 和 *keyfile* 可以是字节对象，而不是字符串，这种情况下，它们被解释为实际的证书/密钥数据。
        """
        ...
    def load_verify_locations(self, cafile=None, cadata=None) -> None:
        """
           加载将验证对等体证书的CA证书链。 *cafile* 是 CA 证书的文件路径。 *cadata* 是一个包含 CA 证书的字节对象。应该只提供这些参数中的一个。
        """
        ...
    def get_ciphers(self) -> List[str]:
        """
           获取启用的密码列表，作为字符串列表返回。
        """
        ...
    def set_ciphers(self, ciphers) -> None:
        """
           为使用此上下文创建的套接字设置可用密码。 *ciphers* 应该是 `IANA密码套件格式 <https://wiki.mozilla.org/Security/Cipher_Suites>`_ 中的字符串列表。
        """
        ...
    def wrap_socket(self, sock, *, server_side=False, do_handshake_on_connect=True, server_hostname=None) -> Incomplete:
        """
           接受一个 :std:term:`stream` *sock*（通常是 ``SOCK_STREAM`` 类型的 socket.socket 实例），并返回一个 ssl.SSLSocket 的实例，用于包装底层流。返回的对象具有像 ``read()``、``write()`` 等的常规 :std:term:`stream` 接口方法。
        
           - *server_side* 选择包装套接字是服务器端还是客户端。服务器端的SSL套接字应该从非SSL监听服务器套接字的 :meth:`~socket.socket.accept()` 返回的普通套接字创建。
        
           - *do_handshake_on_connect* 确定是否在 ``wrap_socket`` 的一部分进行握手，或者是否推迟到作为初始读取或写入的一部分进行。对于立即执行握手的阻塞套接字是标准的。对于非阻塞套接字（即传递给 ``wrap_socket`` 的 *sock* 处于非阻塞模式时），握手通常应该推迟，因为否则 ``wrap_socket`` 将阻塞，直到完成。请注意，在AXTLS中，握手可以推迟到第一次读取或写入，但然后它会阻塞直到完成。
        
           - *server_hostname* 用于作为客户端使用，并设置要与收到的服务器证书进行验证的主机名。它还设置了Server Name Indication（SNI）的名称，允许服务器呈现适当的证书。
        """
        ...
def wrap_socket(sock, server_side=False, key=None, cert=None, cert_reqs=None, cadata=None, server_hostname=None, do_handshake=True) -> IO:
    """
        包装给定的 *sock* 并返回一个新的包装套接字对象。此函数的实现是首先创建一个 `SSLContext` ，然后在该上下文对象上调用 `SSLContext.wrap_socket` 方法。参数 *sock* 、 *server_side* 和 *server_hostname* 未经修改地传递给方法调用。参数 *do_handshake* 传递为 *do_handshake_on_connect* 。其余参数具有以下行为：
    
       - *cert_reqs* 决定对等端（服务器或客户端）是否必须提供有效证书。请注意，对于基于 mbedtls 的移植版本，``ssl.CERT_NONE`` 和 ``ssl.CERT_OPTIONAL`` 将不会验证任何证书，只有 ``ssl.CERT_REQUIRED`` 会。
    
       - *cadata* 是一个包含 CA 证书链（DER 格式）的字节对象，该链将验证对等体的证书。当前仅支持单个 DER 编码的证书。
    
       根据特定 :term:`MicroPython移植版本` 中的底层模块实现，上述一些或全部关键字参数可能不受支持。
    """
    ...
