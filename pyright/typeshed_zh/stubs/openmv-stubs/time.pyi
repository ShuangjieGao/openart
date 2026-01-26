"""
Time related functions.

MicroPython module: https://docs.micropython.org/en/vab847696a/library/time.html

CPython module: :mod:`python:time` https://docs.python.org/3/library/time.html .

``time`` 模块提供了获取当前时间和日期、测量时间间隔以及延迟的函数。

**时间基准**：Unix 移植版本使用 POSIX 系统纪元标准，即 1970-01-01 00:00:00 UTC。然而，一些嵌入式移植版本使用 2000-01-01 00:00:00 UTC 的纪元。可以使用 ``gmtime(0)[0]`` 确定纪元年份。

**维护实际日历日期/时间**：这需要一个实时时钟（RTC）。在具有底层操作系统的系统上（包括一些实时操作系统），RTC 可能是隐式的。设置和维护实际日历时间是操作系统/实时操作系统的责任，并且是在 MicroPython 之外完成的，它只是使用操作系统 API 查询日期/时间。然而，在裸机移植版本上，系统时间取决于 ``machine.RTC()`` 对象。可以使用 ``machine.RTC().datetime(tuple)`` 函数设置当前日历时间，并通过以下方式进行维护：

* 通过备用电池（对于特定板卡可能是一个额外的、可选的组件）。
* 使用网络时间协议（需要由移植版本/用户进行设置）。
* 每次上电由用户手动设置（许多板卡会在硬件重置时维护RTC时间，但有些可能在这种情况下需要重新设置）。

如果没有使用系统/MicroPython RTC 维护实际的日历时间，则下面需要参考当前绝对时间的函数可能不会按预期方式工作。
"""

# source version: vab847696a
# origin module:: repos/micropython/docs/library/time.rst
from __future__ import annotations
from typing import Any, Optional, Tuple
from _typeshed import Incomplete
class clock():
    """
       返回一个时钟对象。
    
       方法
       -------
    """
    def __init__(self) -> None:
        ...
    def tick(self) -> Incomplete:
        """
              开始跟踪运行时间。
        """
        ...
    def fps(self) -> Incomplete:
        """
              停止跟踪经过的时间并返回当前FPA（帧/秒）。
        
              总是在调用此函数之前先调用 ``tick``。
        """
        ...
    def avg(self) -> Incomplete:
        """
              停止跟踪运行时间并返回以微秒为单位的当前平均运行时间。
        
              总是在调用此函数之前先调用 ``tick``。
        """
        ...
    def reset(self) -> None:
        """
              重置时钟对象。
        """
        ...
def gmtime(secs: Optional[Any]=None) -> Tuple:
    """
       将自Epoch（见上文）以来以秒为单位表示的时间 *secs* 转换为包含 8 元组的格式，其中包含：``(year, month, mday, hour, minute, second, weekday, yearday)``。如果未提供 *secs* 或为 None，则使用来自 RTC 的当前时间。
    
       `gmtime()` 函数返回 UTC 中的日期时间元组，`localtime()` 返「回本地时间中的日期时间元组。
    
       8元组中条目的格式为：
    
       * year包含世纪（例如2014）。
       * month 为1-12
       * mday 为 1-31
       * hour 为 0-23
       * minute 为 0-59
       * second 为 0-59
       * weekday 为 0-6，代表周一至周日
       * yearday 为 1-366
    """
    ...
def localtime(secs: Optional[Any]=None) -> Tuple:
    """
       将自Epoch（见上文）以来以秒为单位表示的时间 *secs* 转换为包含 8 元组的格式，其中包含：``(year, month, mday, hour, minute, second, weekday, yearday)``。如果未提供 *secs* 或为 None，则使用来自 RTC 的当前时间。
    
       `gmtime()` 函数返回 UTC 中的日期时间元组，`localtime()` 返「回本地时间中的日期时间元组。
    
       8元组中条目的格式为：
    
       * year包含世纪（例如2014）。
       * month 为1-12
       * mday 为 1-31
       * hour 为 0-23
       * minute 为 0-59
       * second 为 0-59
       * weekday 为 0-6，代表周一至周日
       * yearday 为 1-366
    """
    ...
def mktime() -> int:
    """
       这是localtime的逆函数。它的参数是一个完整的8元组，表示localtime的时间。它返回一个整数，即自2000年1月1日以来的秒数。
    """
    ...
def sleep(seconds) -> Incomplete:
    """
       休眠指定的秒数。某些板卡可以接受 *seconds* 作为浮点数以休眠一定数量的秒数。注意，其他板卡可能不接受浮点参数，为了与它们兼容，请使用 `sleep_ms()` 和 `sleep_us()` 函数。
    """
    ...
def sleep_ms(ms) -> None:
    """
       延迟给定的毫秒数，应为正数或0.
    
       该函数将至少延迟给定的毫秒数，但如果必须进行其他处理，例如中断处理程序或其他线程，则可能需要更长的时间。将*ms*设置为0将允许进行其他处理。对于更精确的延迟，请使用 `sleep_us()`。
    """
    ...
def sleep_us(us) -> None:
    """
       延迟给定的微秒数，应为正数或0.
    
       该函数尝试提供至少*us*微秒的准确延迟，但如果系统有其他更高优先级的处理要执行，则可能需要更长的时间。
    """
    ...
def ticks_ms() -> int:
    """
        返回一个带有任意参考点的递增毫秒计数器，在某个值之后会环绕。
    
        环绕值没有显式暴露，但我们将其称为 *TICKS_MAX*，以简化讨论。值的周期是*TICKS_PERIOD = TICKS_MAX + 1*。*TICKS_PERIOD* 被保证是 2 的幂，但除此之外可能因移植版本而异。对于所有的 `ticks_ms()`、`ticks_us()`、`ticks_cpu()` 函数都使用相同的周期值（为了简单起见）。因此，这些函数将返回范围为 [*0* ..*TICKS_MAX*] 的值，包括 *TICKS_PERIOD* 个值。请注意，仅使用非负值。在大多数情况下，您应该将这些函数返回的值视为不透明的。它们的唯一可用操作是下面描述的 `ticks_diff()` 和 `ticks_add()` 函数。
    
        注意：对这些值执行标准数学操作（+、-）或关系运算符（<、<=、>、>=）会导致无效结果。对数学操作执行，然后将其结果作为参数传递给 `ticks_diff()` 或 `ticks_add()` 也会导致从后者函数返回的结果无效。
    """
    ...
def ticks_us() -> Incomplete:
    """
       类似于上面的 `ticks_ms()`，但以微秒为单位。
    """
    ...
def ticks_cpu() -> Incomplete:
    """
       类似于 `ticks_ms()` 和 `ticks_us()`，但在系统中具有最高的可能分辨率。通常是 CPU 时钟，这就是该函数被命名的原因。但它不一定是 CPU 时钟，系统中可用的其他时序源（例如高分辨率定时器）也可以使用。该函数的确切时间单位（分辨率）未在 ``time`` 模块级别指定，但特定移植版本的文档可能提供更具体的信息。该函数用于非常精细的基准测试或非常紧密的实时循环。避免在可移植代码中使用它。
    
       可用性：并非每个移植版本都实现了此功能。
    """
    ...
def ticks_add(ticks, delta) -> Incomplete:
    """
       将 ticks 值偏移给定的数字，可以是正数也可以是负数。给定一个 *ticks* 值，此函数允许计算在其之前或之后的 *delta* ticks 值，遵循了 tick 值的模运算定义（参见上面的 `ticks_ms()`）。*ticks* 参数必须是对 `ticks_ms()`、`ticks_us()` 或 `ticks_cpu()` 函数的直接调用的结果（或从以前对 `ticks_add()` 的调用）。但 *delta* 可以是任意整数或数值表达式。`ticks_add()` 对于计算事件/任务的截止时间很有用。（注意：您必须使用 `ticks_diff()` 函数来处理截止日期。）
    
       示例::
    
            # Find out what ticks value there was 100ms ago
            print(ticks_add(time.ticks_ms(), -100))
    
            # Calculate deadline for operation and test for it
            deadline = ticks_add(time.ticks_ms(), 200)
            while ticks_diff(deadline, time.ticks_ms()) > 0:
                do_a_little_of_something()
    
            # Find out TICKS_MAX used by this port
            print(ticks_add(0, -1))
    """
    ...
def ticks_diff(ticks1, ticks2) -> int:
    """
       测量从 `ticks_ms()`、`ticks_us()` 或 `ticks_cpu()` 函数返回的值之间的 ticks 差异，作为可能会环绕的有符号值。
    
       参数顺序与减法运算符相同，``ticks_diff(ticks1, ticks2)`` 具有与 ``ticks1 - ticks2`` 相同的含义。但是，`ticks_ms()` 等函数返回的值可能会环绕，因此直接在其上执行减法将产生不正确的结果。这就是需要 `ticks_diff()` 的原因，它实现了模（或更具体地说，环）算术，以便即使对于环绕值（只要它们之间的距离不太大，参见下文）也能产生正确的结果。该函数返回范围为 [*-TICKS_PERIOD/2* .. *TICKS_PERIOD/2-1*] 的**有符号**值（这是二进制补码有符号整数的典型范围定义）。如果结果为负，则表示 *ticks1* 在时间上早于 *ticks2*。否则，表示 *ticks1* 在 *ticks2* 之后发生。这仅在 *ticks1* 和 *ticks2* 之间的时间相隔不超过 *TICKS_PERIOD/2-1* ticks 时才有效。如果不满足此条件，将返回不正确的结果。具体来说，如果两个 tick 值相隔 *TICKS_PERIOD/2-1* ticks，那么该值将由函数返回。然而，如果 *TICKS_PERIOD/2* 的实时 ticks 之间已经过去了，那么该函数将返回 *-TICKS_PERIOD/2*，即结果值将环绕到可能的值范围的负值区域。
    
       上述约束的非正式解释：假设您被锁在一个没有其他监视时间流逝手段的房间里，只有一个标准的 12 格钟。如果您现在看一眼表盘，并且再过 13 小时才再次看一眼（例如，如果您长时间睡觉），那么一旦您最终再次看时，您可能会觉得仅经过了 1 小时。为了避免这种错误，只需定期查看时钟。您的应用程序应该做同样的事情。"太长时间的睡眠"隐喻也直接映射到应用程序行为：不要让应用程序运行任何单个任务太长时间。在步骤中运行任务，并在其间进行时间记录。
    
       `ticks_diff()` 设计用于适应各种使用模式，其中包括：
    
       * 带有超时的轮询。在这种情况下，事件顺序已知，并且您将仅处理 `ticks_diff()` 的正结果::
    
            # Wait for GPIO pin to be asserted, but at most 500us
            start = time.ticks_us()
            while pin.value() == 0:
                if time.ticks_diff(time.ticks_us(), start) > 500:
                    raise TimeoutError
    
       * 安排事件。在这种情况下，如果事件已过期，`ticks_diff()` 可能为负值::
    
            # This code snippet is not optimized
            now = time.ticks_ms()
            scheduled_time = task.scheduled_time()
            if ticks_diff(scheduled_time, now) > 0:
                print("Too early, let's nap")
                sleep_ms(ticks_diff(scheduled_time, now))
                task.run()
            elif ticks_diff(scheduled_time, now) == 0:
                print("Right at time!")
                task.run()
            elif ticks_diff(scheduled_time, now) < 0:
                print("Oops, running late, tell task to run faster!")
                task.run(run_faster=true)
    
       注意：不要将 `time()` 值传递给 `ticks_diff()`，您应该对它们进行正常的数学运算。但请注意，`time()` 可能（而且将）溢出。这就是所谓的https://en.wikipedia.org/wiki/Year_2038_problem 。
    """
    ...
def time() -> int:
    """
       返回自纪元以来的秒数，作为整数，假设底层 RTC 被设置和维护如上所述。如果未设置 RTC，则该函数返回自特定于移植版本的参考时间点以来的秒数（对于没有备电 RTC 的嵌入式板，通常是自上电或复位以来）。如果您希望开发可移植的 MicroPython 应用程序，则不应依赖此函数提供高于秒精度的精度。如果需要更高的精度、绝对时间戳，请使用 `time_ns()`。如果相对时间可接受，则使用 `ticks_ms()` 和 `ticks_us()` 函数。如果需要日历时间，则使用没有参数的 `gmtime()` 或 `localtime()` 更好。
    
       与CPython的不同之处
    
          在 CPython 中，此函数返回自 Unix 纪元以来的秒数，即 1970-01-01 00:00 UTC，作为浮点数，通常具有微秒精度。使用 MicroPython 时，只有 Unix 移植版本使用相同的纪元，如果浮点精度允许，返回子秒精度。嵌入式硬件通常没有浮点精度来表示长时间范围和子秒精度，因此它们使用具有秒精度的整数值。一些嵌入式硬件也缺少电池供电的 RTC，因此返回自上次上电或相对于其他相对、硬件特定点（例如复位）的秒数。
    """
    ...
def time_ns() -> int:
    """
        类似于 `time()`，但返回自纪元以来的纳秒数，作为整数（通常是大整数，因此将在堆上分配）。
    """
    ...
