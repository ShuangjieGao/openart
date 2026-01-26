"""
Provides standard Asymmetric Multiprocessing (AMP) support.

MicroPython module: https://docs.micropython.org/en/vab847696a/library/openamp.html

``openamp`` 模块为 MicroPython 提供了标准的进程间通信基础设施。该模块处理 OpenAMP 的所有细节，如设置共享资源表、初始化虚拟环 (vrings) 等。它通过 `Endpoint` 类提供了使用 RPMsg 总线基础设施的 API，并通过 `RemoteProc` 类提供了处理器生命周期管理（LCM）支持，如加载固件、启动和停止远程核心等。

示例用法::

    import openamp

    def ept_recv_callback(src, data):
        print("Received message on endpoint", data)

    # Create a new RPMsg endpoint to communicate with the remote core.
    ept = openamp.Endpoint("vuart-channel", callback=ept_recv_callback)

    # Create a RemoteProc object, load its firmware and start it.
    rproc = openamp.RemoteProc("virtual_uart.elf") # Or entry point address (ex 0x081E0000)
    rproc.start()

    while True:
        if ept.is_ready():
            ept.send("data")
"""

# source version: vab847696a
# origin module:: repos/micropython/docs/library/openamp.rst
from __future__ import annotations
from _typeshed import Incomplete
class Endpoint():
    """
       构建一个新的RPMsg端点。端点是两个核心之间的双向通信通道。
    
       参数是：
    
            - *name* 是端点的名称。
            - *callback* 是当端点接收到数据时调用的函数，数据包含远程点的源地址，以及作为引用传递的字节数据。
            - *src* 是端点的源地址。如果没有提供，库将为端点分配一个地址。
            - *dest* 是端点的目标地址。如果端点是通过 new_service_callback 创建的，则必须提供此地址，并且它必须与远程端点的源地址匹配。如果端点在本地注册，且在公告之前，目标地址将在端点绑定时由库分配。
    """
    def __init__(self, name, callback, src=ENDPOINT_ADDR_ANY, dest=ENDPOINT_ADDR_ANY) -> None:
        ...
    def deinit(self) -> Incomplete:
        """
           销毁端点并释放其所有资源。
        """
        ...
    def is_ready(self) -> bool:
        """
           如果端点准备好发送（即，具有源地址和目标地址），则返回True
        """
        ...
    def send(self, src=-1, dest=-1, timeout=-1) -> None:
        """
           通过此端点向远程处理器发送消息。
        
           参数是：
        
                - *src* 是消息的源端点地址。如果没有提供，将使用端点绑定的源地址。
                - *dest* 是消息的目标端点地址。如果没有提供，将使用端点绑定的目标地址。
                - *timeout* 指定等待空闲缓冲区的时间（以毫秒为单位）。默认情况下，函数是阻塞的。
        """
        ...
class RemoteProc():
    """
       RemoteProc 对象提供处理器生命周期管理（LCM）支持，例如加载固件、启动和停止远程核心。
    
       *entry* 参数可以是固件镜像的路径，在这种情况下，固件将从文件加载到目标内存；或者是入口点地址，在这种情况下，固件必须已经加载到给定的地址。
    """
    def __init__(self, entry) -> None:
        ...
    def start(self) -> Incomplete:
        """
           启动远程处理器。
        """
        ...
    def stop(self) -> None:
        """
           停止远程处理器。具体行为取决于平台。例如，在STM32H7上，无法停止然后重新启动Cortex-M4核心，因此调用此函数时会执行完整的系统重置。
        """
        ...
    def shutdown(self) -> Incomplete:
        """
           Shutdown 停止远程处理器并释放其所有资源。具体行为取决于平台，但通常会禁用远程核心的电源和时钟。此函数还作为最终处理函数（即在 ``RemoteProc`` 对象被回收时调用）。请注意，在STM32H7上，无法停止然后重新启动Cortex-M4核心，因此调用此函数时会执行完整的系统重置。
        """
        ...
def new_service_callback(ns_callback) -> None:
    """
        设置新的服务回调。
    
        `*ns_callback*` 参数是一个函数，当远程处理器宣布新服务时，该函数将被调用。此时，主机处理器可以选择创建已宣布的端点（如果该服务受支持），或者忽略它（如果不受支持）。如果未设置此函数，主机处理器应首先在本地注册端点，并且在远程宣布服务时，它将自动绑定。
    """
    ...
