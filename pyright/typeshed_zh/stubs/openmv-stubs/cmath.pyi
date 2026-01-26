"""
Mathematical functions for complex numbers.

MicroPython module: https://docs.micropython.org/en/vab847696a/library/cmath.html

CPython module: :mod:`python:cmath` https://docs.python.org/3/library/cmath.html .

``cmath`` 模块提供一些对复数有效的基本数学函数。
"""

# source version: vab847696a
# origin module:: repos/micropython/docs/library/cmath.rst
from __future__ import annotations
from typing import Tuple
from _typeshed import Incomplete
e: float
"""自然对数的底数"""
pi: float
"""圆周长与直径之比"""
def cos(z) -> float:
    """
       返回 ``z`` 的余弦。
    """
    ...
def exp(z) -> float:
    """
       返回 ``z`` 的指数。
    """
    ...
def log(z) -> float:
    """
       返回 ``z`` 的自然对数。分支切割线沿着负实轴。
    """
    ...
def log10(z) -> float:
    """
       返回以 ``z`` 以10为底的对数。分支切割线沿着负实轴。
    """
    ...
def phase(z) -> float:
    """
       返回数字 ``z`` 的相位，范围为(-pi, +pi]。
    """
    ...
def polar(z) -> Tuple:
    """
       以元组返回 ``z`` 的极坐标形式。
    """
    ...
def rect(r, phi) -> float:
    """
       使用模块 ``r`` 和相位 ``phi`` 来返回复数。
    """
    ...
def sin(z) -> float:
    """
       返回 ``z`` 的正弦。
    """
    ...
def sqrt(z) -> Incomplete:
    """
       返回 ``z`` 的平方根。
    """
    ...
