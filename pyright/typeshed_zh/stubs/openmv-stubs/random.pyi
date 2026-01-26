"""
Random numbers.

MicroPython module: https://docs.micropython.org/en/vab847696a/library/random.html

该模块实现了一个伪随机数生成器（PRNG）。

CPython module: :mod:`python:random` https://docs.python.org/3/library/random.html . .

.. note::

   以下符号用于表示区间：

   - () 表示开区间，不包括端点。例如，(0, 1) 表示大于 0 且小于 1。在集合表示中：(0, 1) = {x | 0 < x < 1}。

   - [] 表示闭区间，包括所有的极限点。例如，[0, 1] 表示大于等于 0 且小于等于 1。在集合表示中：[0, 1] = {x | 0 <= x <= 1}。

.. note::

   只有在启用 ``MICROPY_PY_RANDOM_EXTRA_FUNCS`` 配置选项时，才能使用 :func:`randrange`、:func:`randint` 和 :func:`choice` 函数。
"""

# source version: vab847696a
# origin module:: repos/micropython/docs/library/random.rst
from __future__ import annotations
from typing import Any, Optional
from _typeshed import Incomplete
def getrandbits(n) -> int:
    """
        返回一个具有 *n* 个随机位的整数（0 <= n <= 32）。
    """
    ...
def randint(a, b) -> int:
    """
        返回范围在 [*a*, *b*] 内的随机整数。
    """
    ...
def randrange(start, stop, step: Optional[Any]=None) -> int:
    """
        第一种形式从范围 [0, *stop*) 中返回一个随机整数。第二种形式从范围 [*start*, *stop*) 中返回一个随机整数。第三种形式从范围 [*start*, *stop*) 中以 *step* 为步长返回一个随机整数。例如，调用 ``randrange(1, 10, 2)`` 将返回介于 1 和 9（包括）之间的奇数。
    """
    ...
def random() -> int:
    """
        返回范围在 [0.0, 1.0) 内的一个随机浮点数。
    """
    ...
def uniform(a, b) -> int:
    """
        返回一个随机浮点数 N，使得对于 *a* <= *b*，*a* <= N <= *b*，对于 *b* < *a*，*b* <= N <= *a*。
    """
    ...
def seed(n=None, ) -> None:
    """
        使用种子 *n*（应为整数）初始化随机数生成器模块。当不传入参数（或传入 ``None``）时，如果支持的话，它将使用真随机数（通常是硬件生成的随机数）初始化 PRNG。
    
        如果由移植版本启用了 ``MICROPY_PY_RANDOM_SEED_INIT_FUNC``，则 ``None`` 情况才能工作，否则会引发 ``ValueError``。
    """
    ...
def choice(sequence) -> Incomplete:
    """
        从 *sequence*（元组、列表或支持下标操作的任何对象）中随机选择并返回一个项目。
    """
    ...
