"""
Mathematical functions.

MicroPython module: https://docs.micropython.org/en/vab847696a/library/math.html

CPython module: :mod:`python:math` https://docs.python.org/3/library/math.html .

``math`` 模块提供了一些基本的数学函数，用于处理浮点数。

*注意：* 在 pyboard 上，浮点数精度为 32 位。
"""

# source version: vab847696a
# origin module:: repos/micropython/docs/library/math.rst
from __future__ import annotations
from typing import Tuple
from _typeshed import Incomplete
e: float
"""自然对数的底数"""
pi: float
"""圆周长与直径之比"""
def acos(x) -> float:
    """
       返回 ``x`` 的反余弦值。
    """
    ...
def acosh(x) -> float:
    """
       返回 ``x`` 的反双曲余弦值。
    """
    ...
def asin(x) -> float:
    """
       返回 ``x`` 的反正弦值。
    """
    ...
def asinh(x) -> float:
    """
       返回 ``x`` 的反双曲正弦值。
    """
    ...
def atan(x) -> float:
    """
       返回 ``x`` 的反正切值。
    """
    ...
def atan2(y, x) -> float:
    """
       返回 ``y/x`` 的反正切主值。
    """
    ...
def atanh(x) -> float:
    """
       返回 ``x`` 的反双曲正切值。
    """
    ...
def ceil(x) -> int:
    """
       返回一个整数，将 ``x`` 四舍五入到正无穷大。
    """
    ...
def copysign(x, y) -> Incomplete:
    """
       返回带有 ``y`` 符号的 ``x``。
    """
    ...
def cos(x) -> float:
    """
       返回 ``x`` 的余弦值。
    """
    ...
def cosh(x) -> float:
    """
       返回 ``x`` 的双曲余弦值。
    """
    ...
def degrees(x) -> Incomplete:
    """
       返回弧度 ``x`` 转换为度数。
    """
    ...
def erf(x) -> Incomplete:
    """
       返回 ``x`` 的误差函数。
    """
    ...
def erfc(x) -> Incomplete:
    """
       返回 ``x`` 的互补误差函数。
    """
    ...
def exp(x) -> float:
    """
       返回 ``x`` 的指数函数。
    """
    ...
def expm1(x) -> Incomplete:
    """
       返回 ``exp(x) - 1``。
    """
    ...
def fabs(x) -> Incomplete:
    """
       返回 ``x`` 的绝对值。
    """
    ...
def floor(x) -> int:
    """
       返回一个整数，将 ``x`` 四舍五入到负无穷大。
    """
    ...
def fmod(x, y) -> Incomplete:
    """
       返回 ``x/y`` 的余数。
    """
    ...
def frexp(x) -> Incomplete:
    """
       将浮点数分解为尾数和指数。返回值是元组 ``(m, e)``，使得 ``x == m * 2**e``。如果 ``x == 0``，则函数返回 ``(0.0, 0)``，否则满足关系式 ``0.5 <= abs(m) < 1``。
    """
    ...
def gamma(x) -> Incomplete:
    """
       返回 ``x`` 的伽玛函数。
    """
    ...
def isfinite(x) -> bool:
    """
       如果 ``x`` 是有限数，则返回 ``True``。
    """
    ...
def isinf(x) -> bool:
    """
       如果 ``x`` 是无穷大数，则返回 ``True``。
    """
    ...
def isnan(x) -> bool:
    """
       如果 ``x`` 是非数字，则返回 ``True``
    """
    ...
def ldexp(x, exp) -> Incomplete:
    """
       返回 ``x * (2**exp)``。
    """
    ...
def lgamma(x) -> float:
    """
       返回 ``x`` 的伽玛函数的自然对数。
    """
    ...
def log(x) -> float:
    """
       返回 ``x`` 的自然对数。
    """
    ...
def log10(x) -> float:
    """
       返回 ``x`` 的以 10 为底的对数。
    """
    ...
def log2(x) -> float:
    """
       返回 ``x`` 的以 2 为底的对数。
    """
    ...
def modf(x) -> Tuple:
    """
       返回一个包含两个浮点数的元组，分别是 ``x`` 的小数部分和整数部分。两个返回值的符号与 ``x`` 相同。
    """
    ...
def pow(x, y) -> Incomplete:
    """
       返回 ``x`` 的 ``y`` 次幂。
    """
    ...
def radians(x) -> Incomplete:
    """
       返回度数 ``x`` 转换为弧度。
    """
    ...
def sin(x) -> float:
    """
       返回 ``x`` 的正弦值。
    """
    ...
def sinh(x) -> float:
    """
       返回 ``x`` 的双曲正弦值。
    """
    ...
def sqrt(x) -> Incomplete:
    """
       返回 ``x`` 的平方根。
    """
    ...
def tan(x) -> float:
    """
       返回 ``x`` 的正切值。
    """
    ...
def tanh(x) -> float:
    """
       返回 ``x`` 的双曲正切值。
    """
    ...
def trunc(x) -> int:
    """
       返回一个整数，将 ``x`` 四舍五入到 0。
    """
    ...
