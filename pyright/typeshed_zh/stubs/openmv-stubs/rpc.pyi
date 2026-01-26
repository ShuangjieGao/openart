"""
OpenMV Cam上的 rpc 模块允许您将您的OpenMV Cam连接到另一个微控制器或计算机，并在您的OpenMV Cam上执行远程Python（或过程）调用。rpc 模块还允许反向操作，如果您希望您的OpenMV Cam能够在另一个微控制器或计算机上执行远程过程（或Python）调用。
"""

from typing import Tuple
from typing import List
from typing import Optional
from typing import Any
import image

class rpc:
    def __init__(self):
        """
        创建一个rpc对象。这个构造函数不应该直接使用。
        """
        pass
        
        
    def get_bytes(self,buff,timeout_ms: int):
        """
        这个方法应该由`rpc_master`和`rpc_slave`的特定接口类重新实现。它应该将来自接口的字节填充到 buff 参数中，buff 是一个与 timeout_ms 毫秒长的接口字节对象或内存视图对象相等的 bytearray 或 memoryview 对象。在超时时，此方法应返回 None。注意，为了主从同步，该方法应尝试始终在至少 timeout_ms 毫秒内完成，并且不要太快，因为 rpc_master 和 rpc_slave 对象会自动增加 timeout_ms 以进行同步。
        """
        pass
        
        
    def put_bytes(self,data,timeout_ms: int):
        """
        这个方法应该由 rpc_master 和 rpc_slave 的特定接口类重新实现。它应该在 timeout_ms 毫秒内在接口上发生 data 字节。如果完成速度比超时快，那没问题。不需要返回值。
        """
        pass
        
        
    def stream_reader(self,call_back,queue_depth=1,read_timeout_ms=5000):
        """
        这个方法应该直接调用。在主和从设备同步后，可以调用 stream_reader 以尽可能快地从主或从设备接收数据。call_back 将重复调用，其参数是由 stream_writer 发送的 bytes_or_memory_view 参数。call_back 不应返回任何内容。queue_depth 定义了 stream_writer 在减速并等待 stream_writer 之前可能生成多少帧数据。更高的 queue_depth 值会导致更高的性能（在一定程度上），但是需要 stream_reader 能够处理接口层中的未完成数据包。如果使 queue_depth 大于1，则 call_back 应该非常快速且不阻塞。最后，read_timeout_ms 定义了每次调用要等待多少毫秒才能接收到 bytes_or_memory_view 负载。
        在任何错误上，stream_reader 将返回。主和从设备可以尝试在之后重新设置流以继续。
        如果需要取消 stream_reader ，只需在 call_back 中引发异常并捕捉它。远程端将自动超时。
        """
        pass
        
        
    def stream_writer(self,call_back,write_timeout_ms=5000):
        """
        这个方法应该直接调用。在主和从设备同步后，在返回 callback 的回调时，可以调用 stream_writer 以尽可能快地从主或从设备发送数据。call_back 将重复调用，并且应该返回一个由 stream_reader 发送到 bytes_or_memory_view 对象的对象。 call_back 不应该接受任何参数。最后，write_timeout_ms 定义了等待多少毫秒来发送 call_back 返回的 bytes_or_memory_view 对象。
        在任何错误上，stream_writer 将返回。主和从设备可以尝试在之后重新设置流以继续。
        如果需要取消 stream_writer，只需要在 call_back 中引发异常并捕获它。远程端将自动超时。
        """
        pass
        
        
    
class rpc_master:
    def __init__(self):
        """
        创建一个rpc_master对象。这个构造函数不应该直接使用。
        """
        pass
        
        
    def call(self,name,data=bytes(),send_timeout=1000,recv_timeout=1000):
        """
        在从属设备上执行远程调用。name 是要执行的远程函数或方法的字符串名称。data 是将作为远程函数或方法参数发送的类似 bytes 的对象。send_timeout 定义了在尝试连接到从属设备并让其执行远程函数或方法时等待的毫秒数。一旦主设备开始将参数发送到从属设备，send_timeout 就不再适用。库将允许参数的发送最多花费 5 秒钟。recv_timeout 定义了在从属设备开始执行远程方法后，等待接收响应的毫秒数。请注意，一旦主设备开始接收响应，recv_timeout 就不再适用。库将允许响应的接收最多花费 5 秒钟。
        请注意，内部将创建包含 data 副本的新数据包，该数据包将在 rpc 库内部创建。如果尝试传递非常大的数据参数，则可能会在 OpenMV Cam 上遇到内存问题。
        """
        pass
        
        
    
class rpc_slave:
    def __init__(self):
        """
        创建一个rpc_slave对象。这个构造函数不应该直接使用。
        """
        pass
        
        
    def register_callback(self,cb):
        """
        注册可以由主设备执行的回调。回调应该接受一个参数，该参数将是一个 memoryview 对象，它应该返回一个 bytes() 类似的对象作为结果。回调应该在可能的情况下在1秒内返回。
        """
        pass
        
        
    def schedule_callback(self,cb):
        """
        在执行完 rpc_slave.loop() 后，不可能在 rpc 库外执行长时间运行的操作。 schedule_callback 允许您在完成调用回调后暂时退出 rpc 库。您应该在执行 rpc 回调方法时执行 schedule_callback ，以注册一个新的非rpc回调，该回调将在成功完成您在其中执行 schedule_callback 的回调后立即执行。该函数或方法不应该接受任何参数。在注册的回调返回后，必须在下一个父回调中重新注册。如果父回调发生任何错误，则注册的回调将不会被调用，并且必须再次注册。下面是如何使用它的示例:
        特别是 schedule_callback 允许您使用 get_bytes 和 put_bytes 方法进行直通式数据传输，该方法可在设备之间进行数据传输而不需要包装成数据包，这会限制在 rpc 库内部移动的数据大小而不会耗尽OpenMV Cam的内存。
        """
        pass
        
        
    def setup_loop_callback(self,cb):
        """
        循环回调在 rpc_slave.loop() 的每个循环迭代中调用。与 rpc.schedule_callback() 回调不同，一旦注册，此回调将保持注册状态。您可以使用循环回调来闪烁活动LED等。您不应该使用循环回调来执行任何阻塞代码，因为这会妨碍从主服务器轮询通信。此外，循环回调将根据主服务器尝试执行的回调的时间和内容以可变速率调用。鉴于此，循环回调不适用于任何需要以固定频率执行的方法。
        在OpenMV Cam上，如果需要以固定频率执行某些操作，应在执行 rpc_slave.loop() 之前设置一个定时器，并使用基于定时器中断的回调以固定频率执行某些函数或方法。有关更多信息，请参阅如何编写中断处理程序。注意：Mutex 库与 rpc 库一起安装在您的OpenMV Cam上。
        """
        pass
        
        
    def loop(self,recv_timeout=1000,send_timeout=1000):
        """
        开始在从设备上执行 rpc 库以接收数据。此方法不返回（除非来自回调的异常）。在执行此方法之前，应首先注册所有回调。但是，在正在注册的回调内部执行此方法是可能的。
        recv_timeout 定义了在再次尝试从主设备接收命令之前要等待多长时间。 send_timeout 定义了从设备在等待主设备接收回调响应之前要等待多长时间。在再次尝试接收之前，循环回调将被执行。
        """
        pass
        
        
    
class rpc_can_master:
    def __init__(self, message_if=0x7FF, bit_rate=250000, sample_point=75, can_bus=2):
        """
        创建一个CAN rpc 主设备。该接口可移动达1 Mb/s。
        注意：主和从消息id和can比特率必须匹配。将主can高连接到从can高，将主can低连接到从can低。CAN总线必须使用120欧姆终端电阻终止。
        """
        pass
        
        
    
class rpc_can_slave:
    def __init__(self, message_id=0x7FF, bit_rate=250000, sample_point=75, can_bus=2):
        """
        创建一个CAN rpc 从设备。该接口可移动达 1 Mb/s。
        注意：主和从消息id和can比特率必须匹配。将主can高连接到从can高，将主can低连接到从can低。CAN总线必须使用120欧姆终端电阻终止。
        """
        pass
        
        
    
class rpc_i2c_master:
    def __init__(self, slave_addr=0x12, rate=100000, i2c_bus=2):
        """
        创建一个 I2C rpc 主设备。该接口可移动达 1 Mb/s。
        注意：主和从地址必须匹配。将主scl连接到从scl，将主sda连接到从sda。您必须使用外部上拉电阻。最后，两个设备必须共享地线。
        """
        pass
        
        
    
class rpc_i2c_slave:
    def __init__(self, slave_addr=0x12, i2c_bus=2):
        """
        创建一个I2C rpc 从设备。该接口可移动达1 Mb/s。
        注意：主和从地址必须匹配。将主scl连接到从scl，将主sda连接到从sda。您必须使用外部上拉电阻。最后，两个设备必须共享地线。
        """
        pass
        
        
    
class rpc_spi_master:
    def __init__(self, cs_pin='P3', freq=10000000, clk_polarity=1, clk_phase=0, spi_bus=2):
        """
        创建一个SPI rpc 主设备。该接口可以动达 80 Mb/s。
        注意：主和从设备必须匹配。将CS、SCLK、MOSI、MISO连接到CS、SCLK、MOSI、MISO。最后，两个设备必须共享一个公共地线。
        """
        pass
        
        
    
class rpc_spi_slave:
    def __init__(self, cs_pin='P3', clk_polarity=1, clk_phase=0, spi_bus=2):
        """
        创建一个 SPI rpc 从设备。该接口可移动达 80 Mb/s。
        注意：主和从设备必须匹配。将CS、SCLK、MOSI、MISO连接到CS、SCLK、MOSI、MISO。最后，两个设备必须共享一个公共地线。
        """
        pass
        
        
    
class rpc_uart_master:
    def __init__(self, baudrate=115200, uart_port=3):
        """
        创建一个UART rpc 主设备。该接口可移动达 7.5 Mb/s。
        注意：主和从波特率必须匹配。将主tx连接到从rx，将主rx连接到从tx。最后，两个设备必须共享一个公共地线。
        """
        pass
        
        
    
class rpc_uart_slave:
    def __init__(self, baudrate=115200, uart_port=3):
        """
        创建一个UART rpc 从设备。该接口可移动达7.5 Mb/s.
        注意：主和从波特率必须匹配。将主tx连接到从rx，将主rx连接到从tx。最后，两个设备必须共享一个公共地线。
        """
        pass
        
        
    
class rpc_usb_vcp_master:
    def __init__(self):
        """
        创建一个USB VCP rpc 主控。该接口可以以USB速度传输数据。
        """
        pass
        
        
    
class rpc_usb_vcp_slave:
    def __init__(self):
        """
        创建一个USB VCP rpc 从机。该接口可以以USB速度传输数据。
        """
        pass
        
        
    
