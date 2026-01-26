"""
Cryptographic ciphers.

MicroPython module: https://docs.micropython.org/en/vab847696a/library/cryptolib.html
"""

# source version: vab847696a
# origin module:: repos/micropython/docs/library/cryptolib.rst
from __future__ import annotations
from typing import Any, Optional
from _typeshed import Incomplete
class aes():
    def __init__(self, key, mode, IV: Optional[Any]=None) -> None:
        """
                初始化密码对象，适用于加密/解密。注意：初始化后，密码对象只能用于加密或解密之一。在执行 encrypt() 操作后再执行 decrypt()，或者反之，是不支持的。
        
                参数为：
        
                    * *key* 是加密/解密密钥（类似于字节）。
                    * *mode* 为：
        
                        * ``1`` （或者 ``cryptolib.MODE_ECB`` ，如果存在）表示Electronic Code Book（ECB）模式。
                        * ``2`` （或者 ``cryptolib.MODE_CBC`` ，如果存在）表示Cipher Block Chaining（CBC）模式。
                        * ``6`` （或者 ``cryptolib.MODE_CTR`` ，如果存在）表示Counter mode（CTR）模式。
        
                    * *IV* 是 CBC 模式的初始化向量。
                    * 对于计数器模式，*IV* 是计数器的初始值。
        """
        ...
    def encrypt(self, in_buf, out_buf: Optional[Any]=None) -> Incomplete:
        """
                加密 *in_buf*。如果没有给出 *out_buf*，则结果将作为新分配的 `bytes` 对象返回。否则，结果将写入可变缓冲区 *out_buf*。*in_buf* 和 *out_buf* 也可以引用同一个可变缓冲区，在这种情况下，数据将被原地加密。
        """
        ...
    def decrypt(self, in_buf, out_buf: Optional[Any]=None) -> Incomplete:
        """
                类似于 `encrypt()`，但用于解密。
        """
        ...
