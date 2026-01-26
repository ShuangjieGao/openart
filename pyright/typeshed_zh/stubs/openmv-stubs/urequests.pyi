"""
HTTP 客户端的相关功能函数，提供各种 HTTP 请求方法.

MicroPython module: https://docs.micropython.org/en/vab847696a/library/urequests.html

HTTP 客户端的相关功能函数，提供各种 HTTP 请求方法

响应类
--------------
"""

# source version: vab847696a
# origin module:: repos/micropython/docs/library/urequests.rst
from __future__ import annotations
from typing import Dict
from _typeshed import Incomplete
class Response():
    """
       The 响应类 object contains the server's response to the HTTP request.
    
       方法
       ~~~~~~~
    """
    def __init__(self, s) -> None:
        ...
    def json(self) -> Dict:
        """
              返回响应json编码的内容并转换为字典类型。
        """
        ...
def request(function, url, data=None, json=None, files=None, headers={}, auth=None) -> None:
    """
    向服务器发送 HTTP 请求。
    
        - ``function`` - 要使用的 HTTP 方法
        - ``url`` - 要发送的 URL
        - ``data`` - 要附加到请求主体的数据。如果提供了字典或元组列表，则将对其进行编码。
        - ``json`` - 用于附加到请求主体的 json 数据。
        - ``files`` - 用于文件上传，类型为 2 元组，定义了文件名、文件路径和内容类型。如下，{'name'，（文件路径，内容类型）}
        - ``headers`` - 要发送的标头字典。
        - ``auth`` - 启用 Basic/Digest/自定义 HTTP Auth 的 Auth 元组。
    """
    ...
def head(url, **kw) -> Response:
    """
        发送 HEAD 请求并返回 Response 对象。
    
            - ``url`` - 请求对象的 URL
            - ``**kw`` - 请求函数的参数。
    """
    ...
def get(url, **kw) -> Response:
    """
        发送 GET 请求并返回 Response 对象。
    
            - ``url`` - 请求对象的 URL
            - ``**kw`` - 请求函数的参数。
    """
    ...
def post(url, **kw) -> Response:
    """
        发送 POST 请求并返回 Response 对象。
    
            - ``url`` - 请求对象的 URL
            - ``**kw`` - 请求函数的参数。
    """
    ...
def put(url, **kw) -> Response:
    """
        发送 PUT 请求并返回 Response 对象。
    
            - ``url`` - 请求对象的 URL
            - ``**kw`` - 请求函数的参数。
    """
    ...
def patch(url, **kw) -> Response:
    """
        发送 PATCH 请求并返回 Response 对象。
    
            - ``url`` - 请求对象的 URL
            - ``**kw`` - 请求函数的参数。
    """
    ...
def delete(url, **kw) -> Request:
    """
        发送 DELETE 请求并返回 Response 对象。
    
            - ``url`` - 请求对象的 URL
            - ``**kw`` - 请求函数的参数。
    """
    ...
