"""
Asynchronous I/O scheduler for writing concurrent code.

MicroPython module: https://docs.micropython.org/en/vab847696a/library/asyncio.html

CPython module:
`asyncio `<https://docs.python.org/3.8/library/asyncio.html>

例子::

    import asyncio

    async def blink(led, period_ms):
        while True:
            led.on()
            await asyncio.sleep_ms(5)
            led.off()
            await asyncio.sleep_ms(period_ms)

    async def main(led1, led2):
        asyncio.create_task(blink(led1, 700))
        asyncio.create_task(blink(led2, 400))
        await asyncio.sleep_ms(10_000)

    # Running on a pyboard
    from pyb import LED
    asyncio.run(main(LED(1), LED(2)))

    # Running on a generic board
    from machine import Pin
    asyncio.run(main(Pin(1), Pin(2)))

核心函数
--------------
"""

# source version: vab847696a
# origin module:: repos/micropython/docs/library/asyncio.rst
from __future__ import annotations
from typing import Any, Coroutine, List, Tuple
from _typeshed import Incomplete
class Task():
    """
        此对象将协程封装到运行中的任务中。任务可以使用 ``await task`` 等待，等待任务完成并返回任务的返回值。
    
        任务不应直接创建，而应使用 `create_task` 创建它们。
    """
    def __init__(self) -> None:
        ...
    def cancel(self) -> None:
        """
            通过注入 ``asyncio.CancelledError`` 来取消任务。任务可以忽略此异常。可以通过捕获它或通过 ``try ... finally`` 运行清理代码。
        """
        ...
class Event():
    """
        创建一个新的事件，可用于同步任务。事件从清除状态开始。
    """
    def __init__(self) -> None:
        ...
    def is_set(self) -> bool:
        """
            如果事件已设置，则返回 ``True``，否则返回 ``False``。
        """
        ...
    def set(self) -> None:
        """
            设置事件。任何等待事件的任务都将被安排运行。
        
            注意：这必须在任务内部调用。从 IRQ、调度程序回调或其他线程调用此函数是不安全的。参见 `ThreadSafeFlag`。
        """
        ...
    def clear(self) -> None:
        """
            清除事件。
        """
        ...
    def wait(self) -> Coroutine[Incomplete, Any, Any]:
        """
            等待事件设置。如果事件已设置，则立即返回。
        
            这是一个协程。
        """
        ...
class ThreadSafeFlag():
    """
        创建一个新的标志，可以用来将任务与在 asyncio 循环外运行的代码同步，例如其他线程、中断请求（IRQs）或调度器回调。标志默认处于清除状态。
    """
    def __init__(self) -> None:
        ...
    def set(self) -> None:
        """
            设置标志。如果有等待标志的任务，则将其安排运行。
        """
        ...
    def clear(self) -> None:
        """
            清除标志。这可用于确保在等待标志之前清除可能先前设置的标志。
        """
        ...
    def wait(self) -> Coroutine[Incomplete, Any, Any]:
        """
            等待标志设置。如果标志已设置，则立即返回。标志在从 ``wait`` 返回时会自动重置。
        
            一次只能由一个任务等待标志。
        
            这是一个协程。
        """
        ...
class Lock():
    """
        创建一个新的锁，可用于协调任务。锁从未锁定状态开始。
    
        除了下面列出的方法之外，还可以在 ``async with`` 语句中使用锁。
    """
    def __init__(self) -> None:
        ...
    def locked(self) -> bool:
        """
            如果锁已锁定，则返回 ``True``，否则返回 ``False``。
        """
        ...
    def acquire(self) -> Coroutine[None, Any, Any]:
        """
            等待锁处于未锁定状态，然后以原子方式锁定它。一次只能有一个任务获取锁。
        
            这是一个协程。
        """
        ...
    def release(self) -> Incomplete:
        """
            释放锁。如果有任务在等待锁，则排队中的下一个任务将被安排运行，并且锁仍然保持锁定状态。否则，没有任务等待锁，锁变为未锁定状态。
        """
        ...
class Stream():
    """
        这表示 TCP 流连接。为了尽量减少代码，此类实现了读取器和写入器，而 ``StreamReader`` 和 ``StreamWriter`` 别名为此类。
    """
    def __init__(self) -> None:
        ...
    def get_extra_info(self, v) -> Incomplete:
        """
            获取有关流的额外信息，由 *v* 给出。*v* 的有效值为：``peername``。
        """
        ...
    def close(self) -> None:
        """
            关闭流。
        """
        ...
    def wait_closed(self) -> Coroutine[None, Any, Any]:
        """
            等待流关闭。
        
            这是一个协程。
        """
        ...
    def read(self, n=-1) -> Coroutine[Incomplete, Any, Any]:
        """
            读取最多 *n* 字节并返回它们。如果未提供 *n* 或为 -1，则读取直到 EOF 的所有字节。如果在读取任何字节之前遇到 EOF，则返回一个空字节对象。
        
            这是一个协程。
        """
        ...
    def readinto(self, buf) -> Coroutine[int, Any, Any]:
        """
            将最多 n 字节读入到 *buf* 中，其中 n 等于 *buf* 的长度。
        
            返回读入 *buf* 的字节数。
        
            这是一个协程，并且是 MicroPython 的扩展。
        """
        ...
    def readexactly(self, n) -> Coroutine[bytes, Any, Any]:
        """
            读取确切的 *n* 字节并返回它们作为字节对象。
        
            如果在读取 *n* 字节之前流结束，则引发 ``EOFError`` 异常。
        
            这是一个协程。
        """
        ...
    def readline(self) -> Coroutine[Incomplete, Any, Any]:
        """
            读取一行并返回它。
        
            这是一个协程。
        """
        ...
    def write(self, buf) -> Incomplete:
        """
            将 *buf* 累积到输出缓冲区中。只有在调用 `Stream.drain` 后才会刷新数据。建议在调用此函数后立即调用 `Stream.drain`。
        """
        ...
    def drain(self) -> Coroutine[Incomplete, Any, Any]:
        """
            将所有缓冲的输出数据刷新到流中。
        
            这是一个协程。
        """
        ...
class Server():
    """
        这表示从 `start_server` 返回的服务器类。可以在 ``async with`` 语句中使用它以在退出时关闭服务器。
    """
    def __init__(self) -> None:
        ...
    def close(self) -> None:
        """
            关闭服务器。
        """
        ...
    def wait_closed(self) -> Coroutine[None, Any, Any]:
        """
            等待服务器关闭。
        
            这是一个协程。
        """
        ...
class Loop():
    """
        这表示调度和运行任务的对象。不能创建它，请改用 `get_event_loop`。
    """
    def __init__(self) -> None:
        ...
    def create_task(self, coro) -> Task:
        """
            从给定的 *coro* 创建一个任务，并返回新的 `Task` 对象。
        """
        ...
    def run_forever(self) -> Incomplete:
        """
            运行时间循环直到 `stop()` 被调用。
        """
        ...
    def run_until_complete(self, awaitable) -> Incomplete:
        """
            运行给定的 *awaitable* 直到完成。如果 *awaitable* 不是任务，则将其升级为任务。
        """
        ...
    def stop(self) -> None:
        """
            停止事件循环。
        """
        ...
    def close(self) -> None:
        """
            关闭事件循环。
        """
        ...
    def set_exception_handler(self, handler) -> None:
        """
            设置当任务引发未捕获的异常时调用的异常处理程序。*handler* 应接受两个参数： ``(loop, context)``。
        """
        ...
    def get_exception_handler(self) -> None:
        """
            获取当前的异常处理程序。如果未设置自定义处理程序，则返回处理程序，否则返回 ``None``。
        """
        ...
    def default_exception_handler(self, context) -> Incomplete:
        """
            调用默认的异常处理程序。
        """
        ...
    def call_exception_handler(self, context) -> Incomplete:
        """
            调用当前的异常处理程序。参数 *context* 通过，是一个包含键的字典：``'message'``、``'exception'``、``'future'``。
        """
        ...
def create_task(coro) -> Task:
    """
        从给定的协程创建一个新任务并安排其运行。
    
        返回相应的 `Task` 对象。
    """
    ...
def current_task() -> Task:
    """
        返回当前正在运行的任务关联的 `Task` 对象。
    """
    ...
def run(coro) -> Incomplete:
    """
        从给定的协程创建一个新任务并运行它，直到完成。
    
        返回 *coro* 返回的值。
    """
    ...
def sleep(t) -> Coroutine[Incomplete, Any, Any]:
    """
        休眠 *t* 秒（可以是浮点数）。
    
        这是一个协程。
    """
    ...
def sleep_ms(t) -> Coroutine[Incomplete, Any, Any]:
    """
        休眠 *t* 毫秒。
    
        这是一个协程，并且是 MicroPython 的扩展。
    """
    ...
def wait_for(awaitable, timeout) -> Coroutine[Incomplete, Any, Any]:
    """
        等待 *awaitable* 完成，但如果超过 *timeout* 秒，则取消它。如果 *awaitable* 不是一个任务，则将从中创建一个任务。
    
        如果超时发生，它会取消任务并引发 ``asyncio.TimeoutError``：这应该由调用者捕获。任务接收 ``asyncio.CancelledError``，可以忽略或使用 ``try...except`` 或 ``try...finally`` 捕获以运行清理代码。
    
        返回 *awaitable* 的返回值。
    
        这是一个协程。
    """
    ...
def wait_for_ms(awaitable, timeout) -> Coroutine[Incomplete, Any, Any]:
    """
        类似于 `wait_for`，但 *timeout* 是以毫秒为单位的整数。
    
        这是一个协程，并且是 MicroPython 的扩展。
    """
    ...
def gather(*awaitables, return_exceptions=False) -> Coroutine[List, Any, Any]:
    """
        同时运行所有 *awaitables*。任何不是任务的 *awaitables* 都会提升为任务。
    
        返回所有 *awaitables* 的返回值列表。
    
        这是一个协程。
    """
    ...
def open_connection(host, port, ssl=None) -> Coroutine[Tuple, Any, Any]:
    """
        打开到给定 *host* 和 *port* 的 TCP 连接。将使用 `socket.getaddrinfo` 解析 *host* 地址，这是一个当前阻塞的调用。如果 *ssl* 是一个 `ssl.SSLContext` 对象，则使用此上下文创建传输；如果 *ssl* 是 ``True``，则使用默认上下文。
    
        返回一对流：读取器流和写入器流。如果无法解析主机或无法建立连接，则会引发特定于套接字的 ``OSError``。
    
        这是一个协程。
    """
    ...
def start_server(callback, host, port, backlog=5, ssl=None) -> Coroutine[Server, Any, Any]:
    """
        在给定的 *host* 和 *port* 上启动 TCP 服务器。将使用 *callback* 处理传入的、已接受的连接，并传递两个参数：连接的读取器和写入器流。
    
        如果 *ssl* 是一个 `ssl.SSLContext` 对象，则使用此上下文创建传输。
    
        返回一个 `Server` 对象。
    
        这是一个协程。
    """
    ...
def get_event_loop() -> Incomplete:
    """
        返回用于调度和运行任务的事件循环。参见 `Loop`。
    """
    ...
def new_event_loop() -> Incomplete:
    """
        重置事件循环并返回它。
    
        注意：由于 MicroPython 只有一个事件循环，此函数只是重置循环的状态，而不会创建新的循环。
    """
    ...
