"""
Low-level Bluetooth radio functionality.

MicroPython module: https://docs.micropython.org/en/vab847696a/library/bluetooth.html

该模块提供了与板载蓝牙控制器的接口。目前，此模块支持蓝牙低功耗（BLE）中的中央、外围、广播器和观察者角色，以及GATT服务器和客户端以及L2CAP连接定向通道。一个设备可以同时处于多种角色。在某些移植版本上支持配对（和绑定）。

此 API 旨在匹配底层蓝牙协议，并提供构建高级抽象的构建模块，例如特定设备类型。

``Note:`` 对于大多数应用程序，我们建议使用更高级别的 `aioble library <https://github.com/micropython/micropython-lib/tree/master/micropython/bluetooth/aioble>`_。

``Note:`` 此模块仍在开发中，其类、函数、方法和常量可能会发生变化。
"""

# source version: vab847696a
# origin module:: repos/micropython/docs/library/bluetooth.rst
from __future__ import annotations
from typing import Any, Optional, Tuple
from _typeshed import Incomplete
class BLE():
    """
        返回 BLE 单例对象。
    """
    def __init__(self) -> None:
        ...
    def active(self, active: Optional[Any]=None, ) -> Incomplete:
        """
            可选地更改 BLE 无线电的活动状态，并返回当前状态。
        
            在使用此类的其他方法之前，无线电必须处于活动状态。
        """
        ...
    def config(self, param, ) -> Tuple:
        """
            获取或设置 BLE 接口的配置值。要获取值，参数名称应作为字符串引用，一次仅查询一个参数。要设置值，请使用关键字语法，并且可以一次设置一个或多个参数。
        
            目前支持的值有：
        
            - ``'mac'``：使用中的当前地址，取决于当前地址模式。这返回一个 ``(addr_type, addr)`` 元组。
        
              有关地址类型的详细信息，请参阅 :meth:`gatts_write <BLE.gatts_write>`。
        
              只有在接口当前处于活动状态时才能查询此项。
        
            - ``'addr_mode'``：设置地址模式。值可以是：
        
                * 0x00 - 公共 - 使用控制器的公共地址。
                * 0x01 - RANDOM - 使用生成的静态地址。
                * 0x02 - RPA - 使用可解析的私有地址。
                * 0x03 - NRPA - 使用不可解析的私有地址。
        
              默认情况下，如果可用，接口模式将使用 PUBLIC 地址，否则将使用 RANDOM 地址。
        
            - ``'gap_name'``：获取/设置由服务 0x1800 使用的 GAP 设备名称，特性 0x2a00。可以随时设置并多次更改。
        
            - ``'rxbuf'``：获取/设置用于存储传入事件的内部缓冲区的大小（以字节为单位）。此缓冲区对整个 BLE 驱动程序全局可见，因此处理所有事件的传入数据，包括所有特性。增加此值可以更好地处理突发传入数据（例如扫描结果）并能够接收更大的特性值。
        
            - ``'mtu'``：获取/设置在 ATT MTU 交换期间将使用的 MTU。结果 MTU 将是此值与远程设备的MTU 的最小值。ATT MTU 交换不会自动发生（除非远程设备启动它），必须使用:meth:`gattc_exchange_mtu<BLE.gattc_exchange_mtu>` 手动启动。使用 ``_IRQ_MTU_EXCHANGED`` 事件发现给定连接的 MTU。
        
            - ``'bond'``：设置在配对过程中是否启用绑定。启用时，配对请求将设置“bond”标志，并且密钥将由两个设备存储。
        
            - ``'mitm'``：设置配对是否需要 MITM 保护。
        
            - ``'io'``：设置此设备的 I/O 能力。
        
              可用选项有::
        
                _IO_CAPABILITY_DISPLAY_ONLY = const(0)
                _IO_CAPABILITY_DISPLAY_YESNO = const(1)
                _IO_CAPABILITY_KEYBOARD_ONLY = const(2)
                _IO_CAPABILITY_NO_INPUT_OUTPUT = const(3)
                _IO_CAPABILITY_KEYBOARD_DISPLAY = const(4)
        
            - ``'le_secure'``：设置是否需要“LE Secure”配对。默认值为 false（即允许“Legacy Pairing”）。
        """
        ...
    def irq(self, handler, ) -> int:
        """
            为 BLE 栈的事件注册回调。*handler* 接受两个参数， ``event`` （将是下面代码之一）和 ``data`` （它是特定于事件的值元组）。
        
            **注意：** 为了防止不必要的分配以优化性能，元组中的 ``addr``、``adv_data``、``char_data``、``notify_data`` 和 ``uuid`` 条目是指向 :mod:`bluetooth` 内部环形缓冲区的只读内存视图实例，并且仅在 IRQ 处理程序函数的调用期间有效。如果您的程序需要保存其中一个值以在 IRQ 处理程序返回后访问（例如，通过将其保存在类实例或全局变量中），则需要复制数据，方法是使用 ``bytes()`` 或 ``bluetooth.UUID()``，就像这样::
        
                connected_addr = bytes(addr)  # equivalently: adv_data, char_data, or notify_data
                matched_uuid = bluetooth.UUID(uuid)
        
            例如，对于扫描结果的 IRQ 处理程序可能会检查 ``adv_data`` 以确定是否为正确的设备，然后仅在此后复制地址数据以在程序的其他地方使用。要在 IRQ 处理程序内打印数据，将需要 ``print(bytes(addr))``。
        
            显示所有可能事件的事件处理程序::
        
                def bt_irq(event, data):
                    if event == _IRQ_CENTRAL_CONNECT:
                        # A central has connected to this peripheral.
                        conn_handle, addr_type, addr = data
                    elif event == _IRQ_CENTRAL_DISCONNECT:
                        # A central has disconnected from this peripheral.
                        conn_handle, addr_type, addr = data
                    elif event == _IRQ_GATTS_WRITE:
                        # A client has written to this characteristic or descriptor.
                        conn_handle, attr_handle = data
                    elif event == _IRQ_GATTS_READ_REQUEST:
                        # A client has issued a read. Note: this is only supported on STM32.
                        # Return a non-zero integer to deny the read (see below), or zero (or None)
                        # to accept the read.
                        conn_handle, attr_handle = data
                    elif event == _IRQ_SCAN_RESULT:
                        # A single scan result.
                        addr_type, addr, adv_type, rssi, adv_data = data
                    elif event == _IRQ_SCAN_DONE:
                        # Scan duration finished or manually stopped.
                        pass
                    elif event == _IRQ_PERIPHERAL_CONNECT:
                        # A successful gap_connect().
                        conn_handle, addr_type, addr = data
                    elif event == _IRQ_PERIPHERAL_DISCONNECT:
                        # Connected peripheral has disconnected.
                        conn_handle, addr_type, addr = data
                    elif event == _IRQ_GATTC_SERVICE_RESULT:
                        # Called for each service found by gattc_discover_services().
                        conn_handle, start_handle, end_handle, uuid = data
                    elif event == _IRQ_GATTC_SERVICE_DONE:
                        # Called once service discovery is complete.
                        # Note: Status will be zero on success, implementation-specific value otherwise.
                        conn_handle, status = data
                    elif event == _IRQ_GATTC_CHARACTERISTIC_RESULT:
                        # Called for each characteristic found by gattc_discover_services().
                        conn_handle, end_handle, value_handle, properties, uuid = data
                    elif event == _IRQ_GATTC_CHARACTERISTIC_DONE:
                        # Called once service discovery is complete.
                        # Note: Status will be zero on success, implementation-specific value otherwise.
                        conn_handle, status = data
                    elif event == _IRQ_GATTC_DESCRIPTOR_RESULT:
                        # Called for each descriptor found by gattc_discover_descriptors().
                        conn_handle, dsc_handle, uuid = data
                    elif event == _IRQ_GATTC_DESCRIPTOR_DONE:
                        # Called once service discovery is complete.
                        # Note: Status will be zero on success, implementation-specific value otherwise.
                        conn_handle, status = data
                    elif event == _IRQ_GATTC_READ_RESULT:
                        # A gattc_read() has completed.
                        conn_handle, value_handle, char_data = data
                    elif event == _IRQ_GATTC_READ_DONE:
                        # A gattc_read() has completed.
                        # Note: Status will be zero on success, implementation-specific value otherwise.
                        conn_handle, value_handle, status = data
                    elif event == _IRQ_GATTC_WRITE_DONE:
                        # A gattc_write() has completed.
                        # Note: Status will be zero on success, implementation-specific value otherwise.
                        conn_handle, value_handle, status = data
                    elif event == _IRQ_GATTC_NOTIFY:
                        # A server has sent a notify request.
                        conn_handle, value_handle, notify_data = data
                    elif event == _IRQ_GATTC_INDICATE:
                        # A server has sent an indicate request.
                        conn_handle, value_handle, notify_data = data
                    elif event == _IRQ_GATTS_INDICATE_DONE:
                        # A client has acknowledged the indication.
                        # Note: Status will be zero on successful acknowledgment, implementation-specific value otherwise.
                        conn_handle, value_handle, status = data
                    elif event == _IRQ_MTU_EXCHANGED:
                        # ATT MTU exchange complete (either initiated by us or the remote device).
                        conn_handle, mtu = data
                    elif event == _IRQ_L2CAP_ACCEPT:
                        # A new channel has been accepted.
                        # Return a non-zero integer to reject the connection, or zero (or None) to accept.
                        conn_handle, cid, psm, our_mtu, peer_mtu = data
                    elif event == _IRQ_L2CAP_CONNECT:
                        # A new channel is now connected (either as a result of connecting or accepting).
                        conn_handle, cid, psm, our_mtu, peer_mtu = data
                    elif event == _IRQ_L2CAP_DISCONNECT:
                        # Existing channel has disconnected (status is zero), or a connection attempt failed (non-zero status).
                        conn_handle, cid, psm, status = data
                    elif event == _IRQ_L2CAP_RECV:
                        # New data is available on the channel. Use l2cap_recvinto to read.
                        conn_handle, cid = data
                    elif event == _IRQ_L2CAP_SEND_READY:
                        # A previous l2cap_send that returned False has now completed and the channel is ready to send again.
                        # If status is non-zero, then the transmit buffer overflowed and the application should re-send the data.
                        conn_handle, cid, status = data
                    elif event == _IRQ_CONNECTION_UPDATE:
                        # The remote device has updated connection parameters.
                        conn_handle, conn_interval, conn_latency, supervision_timeout, status = data
                    elif event == _IRQ_ENCRYPTION_UPDATE:
                        # The encryption state has changed (likely as a result of pairing or bonding).
                        conn_handle, encrypted, authenticated, bonded, key_size = data
                    elif event == _IRQ_GET_SECRET:
                        # Return a stored secret.
                        # If key is None, return the index'th value of this sec_type.
                        # Otherwise return the corresponding value for this sec_type and key.
                        sec_type, index, key = data
                        return value
                    elif event == _IRQ_SET_SECRET:
                        # Save a secret to the store for this sec_type and key.
                        sec_type, key, value = data
                        return True
                    elif event == _IRQ_PASSKEY_ACTION:
                        # Respond to a passkey request during pairing.
                        # See gap_passkey() for details.
                        # action will be an action that is compatible with the configured "io" config.
                        # passkey will be non-zero if action is "numeric comparison".
                        conn_handle, action, passkey = data
        
        
        事件代码为::
        
            from micropython import const
            _IRQ_CENTRAL_CONNECT = const(1)
            _IRQ_CENTRAL_DISCONNECT = const(2)
            _IRQ_GATTS_WRITE = const(3)
            _IRQ_GATTS_READ_REQUEST = const(4)
            _IRQ_SCAN_RESULT = const(5)
            _IRQ_SCAN_DONE = const(6)
            _IRQ_PERIPHERAL_CONNECT = const(7)
            _IRQ_PERIPHERAL_DISCONNECT = const(8)
            _IRQ_GATTC_SERVICE_RESULT = const(9)
            _IRQ_GATTC_SERVICE_DONE = const(10)
            _IRQ_GATTC_CHARACTERISTIC_RESULT = const(11)
            _IRQ_GATTC_CHARACTERISTIC_DONE = const(12)
            _IRQ_GATTC_DESCRIPTOR_RESULT = const(13)
            _IRQ_GATTC_DESCRIPTOR_DONE = const(14)
            _IRQ_GATTC_READ_RESULT = const(15)
            _IRQ_GATTC_READ_DONE = const(16)
            _IRQ_GATTC_WRITE_DONE = const(17)
            _IRQ_GATTC_NOTIFY = const(18)
            _IRQ_GATTC_INDICATE = const(19)
            _IRQ_GATTS_INDICATE_DONE = const(20)
            _IRQ_MTU_EXCHANGED = const(21)
            _IRQ_L2CAP_ACCEPT = const(22)
            _IRQ_L2CAP_CONNECT = const(23)
            _IRQ_L2CAP_DISCONNECT = const(24)
            _IRQ_L2CAP_RECV = const(25)
            _IRQ_L2CAP_SEND_READY = const(26)
            _IRQ_CONNECTION_UPDATE = const(27)
            _IRQ_ENCRYPTION_UPDATE = const(28)
            _IRQ_GET_SECRET = const(29)
            _IRQ_SET_SECRET = const(30)
        
        ``_IRQ_GATTS_READ_REQUEST`` 事件的可用返回代码如下::
        
            _GATTS_NO_ERROR = const(0x00)
            _GATTS_ERROR_READ_NOT_PERMITTED = const(0x02)
            _GATTS_ERROR_WRITE_NOT_PERMITTED = const(0x03)
            _GATTS_ERROR_INSUFFICIENT_AUTHENTICATION = const(0x05)
            _GATTS_ERROR_INSUFFICIENT_AUTHORIZATION = const(0x08)
            _GATTS_ERROR_INSUFFICIENT_ENCRYPTION = const(0x0f)
        
        ``_IRQ_PASSKEY_ACTION`` 事件的可用的操作如下::
        
            _PASSKEY_ACTION_NONE = const(0)
            _PASSKEY_ACTION_INPUT = const(2)
            _PASSKEY_ACTION_DISPLAY = const(3)
            _PASSKEY_ACTION_NUMERIC_COMPARISON = const(4)
        
        为了在固件中节省空间，这些常量未包含在 :mod:`bluetooth` 模块中。从上述列表中添加您需要的常量到您的程序中。
        """
        ...
    def gap_advertise(self, interval_us, adv_data=None, *, resp_data=None, connectable=True) -> Incomplete:
        """
            Starts advertising at the specified interval (in **micro** seconds). This
            interval will be rounded down to the nearest 625us. To stop advertising, set
            *interval_us* to ``None``.
        
            *adv_data* 和 *resp_data* 可以是实现缓冲区协议的任何类型（例如 ``bytes``、``bytearray``、``str``）。*adv_data* 包含在所有广播中，*resp_data* 在对主动扫描的回复中发送。
        
            **注意：** 如果 *adv_data*（或 *resp_data*）为 ``None``，则将重用上一次调用 ``gap_advertise`` 时传递的数据。这允许广播者仅通过 ``gap_advertise(interval_us)`` 恢复广告。如果要清除广告有效载荷，请传递一个空的 ``bytes``，即 ``b''``。
        """
        ...
    def gap_scan(self, duration_ms, interval_us=1280000, window_us=11250, active=False, ) -> Incomplete:
        """
            Run a scan operation lasting for the specified duration (in **milli** seconds).
        
            若要无限期扫描，请将 *duration_ms* 设置为 ``0``。
        
            要停止扫描，请将 *duration_ms* 设置为 ``None``。
        
            Use *interval_us* and *window_us* to optionally configure the duty cycle.
            The scanner will run for *window_us* **micro** seconds every *interval_us*
            **micro** seconds for a total of *duration_ms* **milli** seconds. The default
            interval and window are 1.28 seconds and 11.25 milliseconds respectively
            (background scanning).
        
            对于每个扫描结果，将触发 ``_IRQ_SCAN_RESULT`` 事件，其事件数据为 ``(addr_type, addr, adv_type, rssi, adv_data)``。
        
            ``addr_type`` 值表示公共地址或随机地址：
                * 0x00 - 公共
                * 0x01 - RANDOM（静态、RPA 或 NRPA 中的任意一种，类型已编码在地址本身中）
        
            ``adv_type`` 值对应于蓝牙规范：
        
                * 0x00 - ADV_IND - 可连接和可扫描的非定向广播
                * 0x01 - ADV_DIRECT_IND - 可连接定向广播
                * 0x02 - ADV_SCAN_IND - 可扫描非定向广播
                * 0x03 - ADV_NONCONN_IND - 不可连接的非定向广播
                * 0x04 - SCAN_RSP - 扫描响应
        
            如果希望在结果中接收扫描响应，则可以将 ``active`` 设置为 ``True``。
        
            当扫描停止（无论是由于持续时间结束还是显式停止时），将触发 ``_IRQ_SCAN_DONE`` 事件。
        """
        ...
    def gap_connect(self, addr_type, addr, scan_duration_ms=2000, min_conn_interval_us=None, max_conn_interval_us=None, ) -> None:
        """
            连接到外围设备。
        
            有关地址类型的详细信息，请参阅 :meth:`gap_scan <BLE.gap_scan>`。
        
            要取消未完成的连接尝试，请调用 ``gap_connect(None)``。
        
            成功时，将触发 ``_IRQ_PERIPHERAL_CONNECT`` 事件。如果取消连接尝试，则将触发 ``_IRQ_PERIPHERAL_DISCONNECT`` 事件。
        
            设备将等待最多 *scan_duration_ms* 从设备接收广播有效载荷。
        
            The connection interval can be configured in **micro** seconds using either
            or both of *min_conn_interval_us* and *max_conn_interval_us*. Otherwise a
            default interval will be chosen, typically between 30000 and 50000
            microseconds. A shorter interval will increase throughput, at the expense
            of power usage.
        """
        ...
    def gap_disconnect(self, conn_handle, ) -> bool:
        """
            断开指定的连接句柄。这可以是已连接到该设备的中心（如果充当外围设备），也可以是此设备先前连接到的外围设备（如果充当中心）。
        
            成功时，将触发 ``_IRQ_PERIPHERAL_DISCONNECT`` 或 ``_IRQ_CENTRAL_DISCONNECT`` 事件。
        
            如果连接句柄未连接，则返回 ``False``，否则返回 ``True``。
        """
        ...
    def gatts_register_services(self, services_definition, ) -> Incomplete:
        """
            使用指定的服务配置服务器，替换任何现有服务。
        
            *services_definition* 是一个 **service** 列表，其中每个 **service**是一个包含 UUID 和 **characteristic** 列表的两个元素元组。
        
            每个 **characteristic** 是一个包含 UUID、**flags** 值和可选的 *descriptors* 列表的两个或三个元素元组。
        
            每个 **descriptor** 是一个包含 UUID 和 **flags** 值的两个元素元组。
        
            **flags**是以下标志的按位或组合。这些设置特征（或描述符）的行为以及安全性和隐私要求。
        
            返回值是一个元组列表（每个服务一个元素），其中每个元组（每个特征和描述符句柄都平铺在其中）以定义的顺序排列。
        
            以下是注册两个服务（心率和 Nordic UART）的示例：
        
                HR_UUID = bluetooth.UUID(0x180D)
                HR_CHAR = (bluetooth.UUID(0x2A37), bluetooth.FLAG_READ | bluetooth.FLAG_NOTIFY,)
                HR_SERVICE = (HR_UUID, (HR_CHAR,),)
                UART_UUID = bluetooth.UUID('6E400001-B5A3-F393-E0A9-E50E24DCCA9E')
                UART_TX = (bluetooth.UUID('6E400003-B5A3-F393-E0A9-E50E24DCCA9E'), bluetooth.FLAG_READ | bluetooth.FLAG_NOTIFY,)
                UART_RX = (bluetooth.UUID('6E400002-B5A3-F393-E0A9-E50E24DCCA9E'), bluetooth.FLAG_WRITE,)
                UART_SERVICE = (UART_UUID, (UART_TX, UART_RX,),)
                SERVICES = (HR_SERVICE, UART_SERVICE,)
                ( (hr,), (tx, rx,), ) = bt.gatts_register_services(SERVICES)
        
            三个值句柄（ ``hr`` 、 ``tx`` 、 ``rx`` ）可用于 :meth:`gatts_read <BLE.gatts_read>`, :meth:`gatts_write <BLE.gatts_write>`, :meth:`gatts_notify <BLE.gatts_notify>`, 和 :meth:`gatts_indicate <BLE.gatts_indicate>`。
        
            **注意：** 在注册服务之前必须停止广播。
        
            特征和描述符的可用标志为：
        
                from micropython import const
                _FLAG_BROADCAST = const(0x0001)
                _FLAG_READ = const(0x0002)
                _FLAG_WRITE_NO_RESPONSE = const(0x0004)
                _FLAG_WRITE = const(0x0008)
                _FLAG_NOTIFY = const(0x0010)
                _FLAG_INDICATE = const(0x0020)
                _FLAG_AUTHENTICATED_SIGNED_WRITE = const(0x0040)
        
                _FLAG_AUX_WRITE = const(0x0100)
                _FLAG_READ_ENCRYPTED = const(0x0200)
                _FLAG_READ_AUTHENTICATED = const(0x0400)
                _FLAG_READ_AUTHORIZED = const(0x0800)
                _FLAG_WRITE_ENCRYPTED = const(0x1000)
                _FLAG_WRITE_AUTHENTICATED = const(0x2000)
                _FLAG_WRITE_AUTHORIZED = const(0x4000)
        
            与上述 IRQ 一样，任何所需的常量都应添加到您的 Python 代码中。
        """
        ...
    def gatts_read(self, value_handle, ) -> Incomplete:
        """
            读取此句柄的本地值（由 :meth:`gatts_write <BLE.gatts_write>` 或远程客户端写入）。
        """
        ...
    def gatts_write(self, value_handle, data, send_update=False, ) -> None:
        """
            写入此句柄的本地值，客户端可以读取。
        
            如果 *send_update* 设置为 ``True``，则任何已订阅的客户端将收到通知（或指示，取决于客户端订阅的内容和特征支持的操作）。
        """
        ...
    def gatts_notify(self, conn_handle, value_handle, data=None, ) -> None:
        """
            向已连接的客户端发送通知请求。
        
            如果 *data* 为 ``None`` （默认值），则将发送当前本地值（由 :meth:`gatts_write <BLE.gatts_write>` 设置）。
        
            否则，如果 *data* 不为 ``None``，则该值将作为通知的一部分发送给客户端。本地值不会被修改。
        
            **注意：** 不管客户端对该特征的订阅状态如何，通知都将被发送。
        """
        ...
    def gatts_indicate(self, conn_handle, value_handle, data=None, ) -> None:
        """
            向已连接的客户端发送指示请求。
        
            如果 *data* 为 ``None`` （默认值），则将发送当前本地值（由 :meth:`gatts_write <BLE.gatts_write>` 设置）。
        
            否则，如果 *data* 不为 ``None``，则该值将作为指示的一部分发送给客户端。本地值不会被修改。
        
            在确认（或失败，例如超时）时，将触发 ``_IRQ_GATTS_INDICATE_DONE`` 事件。
        
            **注意：** 不管客户端对该特征的订阅状态如何，指示都将被发送。
        """
        ...
    def gatts_set_buffer(self, value_handle, len, append=False, ) -> None:
        """
            设置字节中值的内部缓冲区大小。这将限制可能接收的最大写入量。默认值为 20。
        
            将 *append* 设置为 ``True`` 将使所有远程写入附加到当前值，而不是替换当前值。以这种方式最多可以缓冲 *len* 字节。当您使用 :meth:`gatts_read <BLE.gatts_read>` 时，值将在读取后清除。当实现类似 Nordic UART 服务的功能时，此功能很有用。
        """
        ...
    def gattc_discover_services(self, conn_handle, uuid=None, ) -> Incomplete:
        """
            查询已连接服务器的服务。
        
            可选择指定要仅查询该服务的服务 *uuid*。
        
            对于每个发现的服务，将触发 ``_IRQ_GATTC_SERVICE_RESULT`` 事件，随后将触发 ``_IRQ_GATTC_SERVICE_DONE`` 事件。
        """
        ...
    def gattc_discover_characteristics(self, conn_handle, start_handle, end_handle, uuid=None, ) -> Incomplete:
        """
            查询指定范围内的已连接服务器的特征。
        
            可选择指定要仅查询该特征的特征 *uuid*。
        
            您可以使用 ``start_handle=1``、``end_handle=0xffff`` 来搜索任何服务中的特征。
        
            对于每个发现的特征，将触发 ``_IRQ_GATTC_CHARACTERISTIC_RESULT`` 事件，随后将触发 ``_IRQ_GATTC_CHARACTERISTIC_DONE`` 事件。
        """
        ...
    def gattc_discover_descriptors(self, conn_handle, start_handle, end_handle, ) -> Incomplete:
        """
            查询指定范围内已连接服务器的描述符。
        
            对于每个发现的描述符，将触发 ``_IRQ_GATTC_DESCRIPTOR_RESULT`` 事件，随后将触发 ``_IRQ_GATTC_DESCRIPTOR_DONE`` 事件。
        """
        ...
    def gattc_read(self, conn_handle, value_handle, ) -> None:
        """
            为指定的特征或描述符句柄向已连接的服务器发出远程读取请求。
        
            当有值可用时，将触发 ``_IRQ_GATTC_READ_RESULT`` 事件。此外，将触发 ``_IRQ_GATTC_READ_DONE`` 事件。
        """
        ...
    def gattc_write(self, conn_handle, value_handle, data, mode=0, ) -> None:
        """
            为指定的特征或描述符句柄向已连接的服务器发出远程写入请求。
        
            参数 *mode* 指定写入行为，当前支持的值为：
        
                * ``mode=0`` （默认）是写入但不回复：写入将发送到远程服务器，但不会返回确认，并且不会触发任何事件。
                * ``mode=1`` 是带回复的写入：请求远程服务器发送响应/确认，表示它已接收数据。
        
            如果从远程服务器接收到响应，则将触发 ``_IRQ_GATTC_WRITE_DONE`` 事件。
        """
        ...
    def gattc_exchange_mtu(self, conn_handle, ) -> Incomplete:
        """
            使用首选 MTU 进行与已连接服务器的 MTU 交换，设置为 ``BLE.config(mtu=value)``。
        
            完成 MTU 交换时，将触发 ``_IRQ_MTU_EXCHANGED`` 事件。
        
            **注意：** MTU 交换通常由中心发起。使用 BlueKitchen 堆栈处于中心角色时，它不支持远程外围设备发起 MTU 交换。NimBLE 对两种角色都起作用。
        """
        ...
    def l2cap_listen(self, psm, mtu, ) -> Incomplete:
        """
            以本地 MTU 设置为 *mtu*，开始侦听指定 *psm* 上的传入 L2CAP 通道请求。
        
            当远程设备启动连接时，将触发 ``_IRQ_L2CAP_ACCEPT`` 事件，这使得侦听服务器有机会拒绝传入的连接（通过返回非零整数）。
        
            一旦接受连接，将触发 ``_IRQ_L2CAP_CONNECT`` 事件，允许服务器获取通道 ID（CID）和本地和远程 MTU。
        
            **注意：** 目前无法停止侦听。
        """
        ...
    def l2cap_connect(self, conn_handle, psm, mtu, ) -> None:
        """
            使用本地 MTU 设置为 *mtu*，连接到指定 *psm* 上的侦听对等端。
        
            成功连接时，将触发 ``_IRQ_L2CAP_CONNECT`` 事件，允许客户端获取 CID 和本地和远程（对等） MTU。
        
            连接失败将触发带有非零状态的 ``_IRQ_L2CAP_DISCONNECT`` 事件。
        """
        ...
    def l2cap_disconnect(self, conn_handle, cid, ) -> None:
        """
            断开指定 *conn_handle* 和 *cid* 的活动 L2CAP 通道。
        """
        ...
    def l2cap_send(self, conn_handle, cid, buf, ) -> bool:
        """
            在由 *conn_handle* 和 *cid* 标识的 L2CAP 通道上发送指定的 *buf* （必须支持缓冲区协议）。
        
            指定的缓冲区大小不能大于远程（对等） MTU，并且不能超过本地 MTU 的两倍。
        
            如果通道现在处于“停滞”状态，则将返回 ``False`` ，这意味着在接收到 ``_IRQ_L2CAP_SEND_READY`` 事件之前不能再次调用 :meth:`l2cap_send <BLE.l2cap_send>` （这将在远程设备授予更多信用后发生， 通常在它接收并处理数据之后）。
        """
        ...
    def l2cap_recvinto(self, conn_handle, cid, buf, ) -> int:
        """
            从指定的 *conn_handle* 和 *cid* 处接收数据到提供的 *buf* 中（必须支持缓冲区协议，例如 bytearray 或 memoryview）。
        
            返回从通道中读取的字节数。
        
            如果 *buf* 为 None，则返回可用的字节数。
        
            **注意：** 在接收到 ``_IRQ_L2CAP_RECV`` 事件之后，应用程序应继续调用 :meth:`l2cap_recvinto <BLE.l2cap_recvinto>`，直到接收缓冲区中没有更多的字节可用 （通常最多等于远程（对等） MTU 的大小）。
        
            在接收缓冲区为空之前，远程设备将不会被授予更多的通道信用，也不会发送更多数据。
        """
        ...
    def gap_pair(self, conn_handle, ) -> Incomplete:
        """
            启动与远程设备的配对。
        
            在调用此方法之前，请确保通过 :meth:`config<BLE.config>` 设置了 ``io``、, ``mitm`` 、 ``le_secure`` 和 ``bond`` 配置选项。
        
            配对成功后，将触发 ``_IRQ_ENCRYPTION_UPDATE`` 事件。
        """
        ...
    def gap_passkey(self, conn_handle, action, passkey, ) -> Incomplete:
        """
            响应指定 *conn_handle* 和 *action* 的 ``_IRQ_PASSKEY_ACTION`` 事件。
        
            The *passkey* is a numeric value and will depend on on the*action* (which will depend on what I/O capability has been set):*passkey* 是一个数字值，将取决于 *action*（这取决于已设置的 I/O 能力）：
        
                * 当 *action* 为 ``_PASSKEY_ACTION_INPUT`` 时，应用程序应提示用户输入在远程设备上显示的密码。
                * 当 *action* 为 ``_PASSKEY_ACTION_DISPLAY`` 时，应用程序应生成一个随机的 6 位数密码并显示给用户。
                * 当 *action* 为 ``_PASSKEY_ACTION_NUMERIC_COMPARISON`` 时，应用程序应显示在 ``_IRQ_PASSKEY_ACTION`` 事件中提供的密码，然后响应为 ``0`` （取消配对）或 ``1`` （接受配对）。
        """
        ...
class UUID():
    """
        使用指定的 **value** 创建 UUID 实例。
    
        **value** 可以是：
    
        - 16 位整数。例如，``0x2908``。
        - 128 位 UUID 字符串。例如， ``'6E400001-B5A3-F393-E0A9-E50E24DCCA9E'``。
    """
    def __init__(self, value, ) -> None:
        ...
