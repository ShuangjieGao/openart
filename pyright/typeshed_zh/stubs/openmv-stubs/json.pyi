"""
JSON encoding and decoding.

MicroPython module: https://docs.micropython.org/en/vab847696a/library/json.html

CPython module: :mod:`python:json` https://docs.python.org/3/library/json.html .

此模块允许在 Python 对象和 JSON 数据格式之间转换。
"""

# source version: vab847696a
# origin module:: repos/micropython/docs/library/json.rst
from __future__ import annotations
from _typeshed import Incomplete
def dump(obj, stream, separators=None) -> Incomplete:
    """
       将 *obj* 序列化为 JSON 字符串，将其写入给定的 *stream*。
    
       如果指定，separators 应该是一个 ``(item_separator, key_separator)`` 元组。默认值是 ``(', ', ': ')``。为了获得最紧凑的 JSON 表示，你应该指定 ``(',', ':')`` 来消除空白。
    """
    ...
def dumps(obj, separators=None) -> str:
    """
       返回表示为 JSON 字符串的 *obj*。
    
       参数的含义与 `dump` 中相同。
    """
    ...
def load(stream) -> Incomplete:
    """
       解析给定的 *stream*，将其解释为 JSON 字符串，并将数据反序列化为 Python 对象。返回结果对象。
    
       解析持续到遇到文件结尾。如果 *stream* 中的数据格式不正确，将引发:exc:`ValueError` 异常。
    """
    ...
def loads(str) -> Incomplete:
    """
       解析 JSON *str* 并返回一个对象。如果字符串格式不正确，将引发 :exc:`ValueError` 异常。
    """
    ...
