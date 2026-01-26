"""
The rpc module on the OpenMV Cam allows you to connect your OpenMV Cam to another microcontroller
or computer and execute remote python (or procedure) calls on your OpenMV Cam. The rpc module also
allows for the reverse too if you want your OpenMV Cam to be able to execute remote procedure
(or python) calls on another microcontroller or computer.
"""

from typing import Tuple
from typing import List
from typing import Optional
from typing import Any
import image

class rpc:
    def __init__(self):
        """
        Creates an rpc object. This constructor is not meant to be used directly.
        """
        pass
        
        
    def get_bytes(self,buff,timeout_ms: int):
        """
        This method is meant to be reimplemented by specific interface classes of rpc_master and rpc_slave.
        It should fill the buff argument which is either a bytearray or memoryview object of bytes from the
        interface equal to the length of the buff object in timeout_ms milliseconds. On timeout this method
        should return None. Note that for master and slave synchronization this method should try to always
        complete in at least timeout_ms milliseconds and not faster as the rpc_master and rpc_slave objects
        will automatically increase the timeout_ms to synchronize.
        """
        pass
        
        
    def put_bytes(self,data,timeout_ms: int):
        """
        This method is meant to be reimplemented by specific interface classes of rpc_master and rpc_slave.
        It should send data bytes on the interface within timeout_ms milliseconds. If it completes faster
        than the timeout that is okay. No return value is expected.
        """
        pass
        
        
    def stream_reader(self,call_back,queue_depth=1,read_timeout_ms=5000):
        """
        This method is meant to be called directly. After synchronization of the master and slave on return
        of a callback stream_reader may be called to receive data as fast as possible from the master or
        slave device. call_back will be called repeatedly with a bytes_or_memory_view argument that was
        sent by the stream_writer. call_back is not expected to return anything. queue_depth defines how
        many frames of data the stream_writer may generate before slowing down and waiting on the
        stream_reader. Higher queue_depth values lead to higher performance (up to a point) but require the
        stream_reader to be able to handle outstanding packets in its interface layer. If you make the
        queue_depth larger than 1 then call_back should return very quickly and not block. Finally,
        read_timeout_ms defines how many milliseconds to wait to receive the bytes_or_memory_view payload per call_back.
        On any errors stream_reader will return. The master and slave devices can try to setup the stream
        again afterwards to continue.
        If you need to cancel the stream_reader just raise an exception in the call_back and catch it. The
        remote side will automatically timeout.
        """
        pass
        
        
    def stream_writer(self,call_back,write_timeout_ms=5000):
        """
        This method is meant to be called directly. After synchronization of the master and slave on return
        of a callback stream_writer may be called to send data as fast as possible from the master or slave
        device. call_back will be called repeatedly and should return a bytes_or_memory_view object that
        will be sent to the stream_reader. call_back should not take any arguments. Finally,
        write_timeout_ms defines how many milliseconds to wait to send the bytes_or_memory_view object
        returned by call_back.
        On any errors stream_writer will return. The master and slave devices can try to setup the stream
        again afterwards to continue.
        If you need to cancel the stream_writer just raise an exception in the call_back and catch it. The
        remote side will automatically timeout.
        """
        pass
        
        
    
class rpc_master:
    def __init__(self):
        """
        Creates an rpc_master object. This constructor is not meant to be used directly.
        """
        pass
        
        
    def call(self,name,data=bytes(),send_timeout=1000,recv_timeout=1000):
        """
        Executes a remote call on the slave device. name is a string name of the remote function or method
        to execute. data is the bytes like object that will be sent as the argument of the remote function
        or method to execute. send_timeout defines how many milliseconds to wait while trying to connect to
        the slave and get it to execute the remote function or method. Once the master starts sending the
        argument to the slave device send_timeout does not apply. The library will allow the argument to
        take up to 5 seconds to be sent. recv_timeout defines how many milliseconds to wait after the slave
        started executing the remote method to receive the response. Note that once the master starts
        receiving the response recv_timeout does not apply. The library will allow the response to take up
        to 5 seconds to be received.
        Note that a new packet that includes a copy of data will be created internally inside the rpc
        library. You may encounter memory issues on the OpenMV Cam if you try to pass very large data
        arguments.
        """
        pass
        
        
    
class rpc_slave:
    def __init__(self):
        """
        Creates an rpc_slave object. This constructor is not meant to be used directly.
        """
        pass
        
        
    def register_callback(self,cb):
        """
        Registers a call back that can be executed by the master device. The call back should take one
        argument which will be a memoryview object and it should return a bytes() like object as the
        result. The call back should return in less than 1 second if possible.
        """
        pass
        
        
    def schedule_callback(self,cb):
        """
        After you execute rpc_slave.loop() it is not possible to execute long running operations outside of the rpc
        library. schedule_callback allows you to break out of the rpc library temporarily after completion
        of an call back. You should execute schedule_callback during the execution of an rpc call back
        method to register a new non-rpc call back that will be executed immediately after the successful
        completion of that call back you executed schedule_callback in. The function or method should not
        take any arguments. After the the call back that was registered returns it must be registered again
        in the next parent call back. On any error of the parent call back the registered call back will
        not be called and must be registered again. Here’s how to use this:
        schedule_callback in particular allows you to use the get_bytes and put_bytes methods for
        cut-through data transfer between one device and another without the cost of packetization which
        limits the size of the data moved inside the rpc library without running out of memory on the
        OpenMV Cam.
        """
        pass
        
        
    def setup_loop_callback(self,cb):
        """
        The loop call back is called every loop iteration of rpc_slave.loop(). Unlike the rpc.schedule_callback() call
        back this call back stays registered after being registered once. You can use the loop call back to
        blink an activity LED or something like that. You should not use the loop call back to execute any
        blocking code as this will get in the way of polling for communication from the master.
        Additionally, the loop call back will be called at a variable rate depending on when and what call
        backs the master is trying to execute. Given this, the loop call back is not suitable for any
        method that needs to be executed at a fixed frequency.
        On the OpenMV Cam, if you need to execute something at a fixed frequency, you should setup a timer
        before executing rpc_slave.loop() and use a timer interrupt based callback to execute some function or method
        at a fixed frequency. Please see how to Write Interrupt Handlers for more information. Note: The
        Mutex library is installed on your OpenMV Cam along with the rpc library.
        """
        pass
        
        
    def loop(self,recv_timeout=1000,send_timeout=1000):
        """
        Starts execution of the rpc library on the slave to receive data. This method does not return
        (except via an exception from a call back). You should register all call backs first before
        executing this method. However, it is possible to register new call backs inside of a call back
        previously being registered that is executing.
        recv_timeout defines how long to wait to receive a command from the master device before trying
        again. send_timeout defines how long the slave will wait for the master to receive the call back
        response before going back to trying to receive. The loop call back will be executed before trying
        to receive again.
        """
        pass
        
        
    
class rpc_can_master:
    def __init__(self, message_if=0x7FF, bit_rate=250000, sample_point=75, can_bus=2):
        """
        Creates a CAN rpc master. This interface can move up to 1 Mb/s.
        NOTE: Master and slave message ids and can bit rates must match. Connect master can high to slave
        can high and master can low to slave can lo. The can bus must be terminated with 120 ohms.
        """
        pass
        
        
    
class rpc_can_slave:
    def __init__(self, message_id=0x7FF, bit_rate=250000, sample_point=75, can_bus=2):
        """
        Creates a CAN rpc slave. This interface can move up to 1 Mb/s.
        NOTE: Master and slave message ids and can bit rates must match. Connect master can high to slave
        can high and master can low to slave can lo. The can bus must be terminated with 120 ohms.
        """
        pass
        
        
    
class rpc_i2c_master:
    def __init__(self, slave_addr=0x12, rate=100000, i2c_bus=2):
        """
        Creates a I2C rpc master. This interface can move up to 1 Mb/s.
        NOTE: Master and slave addresses must match. Connect master scl to slave scl and master sda
        to slave sda. You must use external pull ups. Finally, both devices must share a ground.
        """
        pass
        
        
    
class rpc_i2c_slave:
    def __init__(self, slave_addr=0x12, i2c_bus=2):
        """
        Creates a I2C rpc slave. This interface can move up to 1 Mb/s.
        NOTE: Master and slave addresses must match. Connect master scl to slave scl and master sda
        to slave sda. You must use external pull ups. Finally, both devices must share a ground.
        """
        pass
        
        
    
class rpc_spi_master:
    def __init__(self, cs_pin='P3', freq=10000000, clk_polarity=1, clk_phase=0, spi_bus=2):
        """
        Creates a SPI rpc master. This interface can move up to 80 Mb/s.
        NOTE: Master and slave settings much match. Connect CS, SCLK, MOSI, MISO to CS, SCLK, MOSI, MISO.
        Finally, both devices must share a common ground.
        """
        pass
        
        
    
class rpc_spi_slave:
    def __init__(self, cs_pin='P3', clk_polarity=1, clk_phase=0, spi_bus=2):
        """
        Creates a SPI rpc slave. This interface can move up to 80 Mb/s.
        NOTE: Master and slave settings much match. Connect CS, SCLK, MOSI, MISO to CS, SCLK, MOSI, MISO.
        Finally, both devices must share a common ground.
        """
        pass
        
        
    
class rpc_uart_master:
    def __init__(self, baudrate=115200, uart_port=3):
        """
        Creates a UART rpc master. This interface can move up to 7.5 Mb/s.
        NOTE: Master and slave baud rates must match. Connect master tx to slave rx and master rx to
        slave tx. Finally, both devices must share a common ground.
        """
        pass
        
        
    
class rpc_uart_slave:
    def __init__(self, baudrate=115200, uart_port=3):
        """
        Creates a UART rpc slave. This interface can move up to 7.5 Mb/s.
        NOTE: Master and slave baud rates must match. Connect master tx to slave rx and master rx to
        slave tx. Finally, both devices must share a common ground.
        """
        pass
        
        
    
class rpc_usb_vcp_master:
    def __init__(self):
        """
        Creates a USB VCP rpc master. This interface can move data at the USB speed.
        """
        pass
        
        
    
class rpc_usb_vcp_slave:
    def __init__(self):
        """
        Creates a USB VCP rpc slave. This interface can move data at the USB speed.
        """
        pass
        
        
    
