"""
Control of WS2812 / NeoPixel LEDs.

MicroPython module: https://docs.micropython.org/en/vab847696a/library/neopixel.html

此模块提供了对 WS2818 / NeoPixel LED 的驱动程序。

``Note:`` 此模块仅默认包含在 ESP8266、ESP32 和 RP2 移植版本中。在 STM32 / Pyboard 和其他移植版本上，您可以使用 :term:`mip` 安装 ``neopixel`` 包，或者您可以直接从 :term:`micropython-lib` 下载模块并将其复制到文件系统中。
"""

# source version: vab847696a
# origin module:: repos/micropython/docs/library/neopixel.rst
from __future__ import annotations
from typing import Tuple
from _typeshed import Incomplete
class NeoPixel():
    """
        构造一个 NeoPixel 对象。参数为：
    
            - *pin* 是一个 machine.Pin 实例。
            - *n* 是条中 LED 的数量。
            - *bpp* 是 RGB LED 为 3，RGBW LED 为 4。
            - *timing* 为 0 表示 400KHz，1 表示 800KHz 的 LED（大多数是 800KHz）。
    """
    def __init__(self, pin, n, *, bpp=3, timing=1) -> None:
        ...
    def fill(self, pixel) -> None:
        """
            将所有像素的值设置为指定的 *pixel* 值（即 RGB/RGBW 元组）。
        """
        ...
    def __len__(self) -> int:
        """
            返回条中LED的数量。
        """
        ...
    def __setitem__(self, index, val) -> None:
        """
            将 *index* 处的像素设置为值，这个值是一个 RGB/RGBW 元组。
        """
        ...
    def __getitem__(self, index) -> Tuple:
        """
            返回 *index* 处的像素作为 RGB/RGBW 元组。
        """
        ...
    def write(self) -> None:
        """
            将当前像素数据写入条中。
        """
        ...
