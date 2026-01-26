"""
Functionality specific to STM32 MCUs.

MicroPython module: https://docs.micropython.org/en/vab847696a/library/stm.html

该模块提供了特定于STM32微控制器的功能，包括直接访问外设寄存器。
"""

# + module: stm.rst
# source version: vab847696a
# origin module:: repos/micropython/docs/library/stm.rst
from __future__ import annotations
from typing import Tuple
from _typeshed import Incomplete
mem8: bytearray
"""读/写内存的8位。"""
mem16: bytearray
"""读/写内存的16位。"""
mem32: bytearray
"""\
读/写内存的32位。

使用下标符号 ``[...]`` 用感兴趣的地址来索引这些对象。

这些内存对象可以与外设寄存器的常量结合使用，以读取和写入MCU硬件外设的寄存器，以及地址空间的所有其他区域。
"""
GPIOA: int
"""GPIOA 外设的基址。"""
GPIOB: int
"""GPIOB外设的基址。"""
GPIO_BSRR: Incomplete
"""GPIO位设置/重置寄存器的偏移量。"""
GPIO_IDR: Incomplete
"""GPIO输入数据寄存器的偏移量。"""
GPIO_ODR: int
"""\
GPIO输出数据寄存器的偏移量。

以外设命名的常量，如 ``GPIOA`` ，是该外设的绝对地址。以外设名称为前缀的常量，如 ``GPIO_BSRR`` ，是寄存器的相对偏移量。访问外设寄存器需要添加外设的绝对基址和相对寄存器偏移量。例如 ``GPIOA + GPIO_BSRR`` 是 ``GPIOA->BSRR`` 寄存器的完整、绝对地址。

示例用法：
"""
def rfcore_status() -> int:
    """
        返回第二个CPU的状态，以整数形式（设备信息的第一个字）。
    """
    ...
def rfcore_fw_version(id) -> Tuple:
    """
        获取运行在第二个CPU上的固件版本。对于*id*，传入0获取FUS版本，传入1获取WS版本。
    
        返回完整版本号的5元组。
    """
    ...
def rfcore_sys_hci(ogf, ocf, data, timeout_ms=0) -> bytes:
    """
        在SYS通道上执行一个HCI命令。执行是同步的。
    
        返回一个包含SYS命令结果的字节对象。
    """
    ...
def subghz_cs(level) -> None:
    """
       设置连接到无线电外设的内部 SPI CS 引脚。 ``level`` 参数是低电平有效的：真值表示 "CS 引脚高" 并取消信号，假值表示 "CS 引脚低" 并使信号有效。
    
       使用 :ref:`machine.SPI()<machine.SPI>` 中 ``id`` 值为 ``"SUBGHZ"`` 来实例化与此 CS 信号对应的内部 SPI 总线。
    """
    ...
def subghz_irq(handler) -> None:
    """
       将内部 SUBGHZ 无线电中断处理程序设置为提供的函数。处理程序函数作为 "硬" 中断在无线电外设中断时调用。有关 MicroPython 中断处理程序的更多信息，请参阅 :ref:`isr_rules` 。
    
       将此函数与设置为None的处理程序参数调用以禁用IRQ。
    
       由于硬件限制，每次此IRQ触发时，MicroPython在调用处理程序之前将其禁用。为了接收另一个中断，Python代码应调用 ``subghz_irq()`` 来重新设置处理程序。这具有重新启用IRQ的副作用。
    """
    ...
def subghz_is_busy() -> bool:
    """
       返回与无线电外设中的内部 "RFBUSYS" 信号对用的 ``bool`` 值。在将新命令通过SPI发送到无线电之前，应该轮询此函数直到它返回 ``False``，以确认忙碌信号已经取消激活。
    """
    ...
