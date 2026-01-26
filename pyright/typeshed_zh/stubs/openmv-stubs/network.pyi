"""
Network configuration.

MicroPython module: https://docs.micropython.org/en/vab847696a/library/network.html

本模块提供了网络驱动程序和路由配置。要使用此模块，必须安装带有网络功能的 MicroPython 变体/构建。特定硬件的网络驱动程序位于此模块中，并用于配置硬件网络接口。通过配置的接口提供的网络服务可以通过 :mod:`socket` 模块进行使用。

举例::

    # connect/ show IP config a specific network interface
    # see below for examples of specific drivers
    import network
    import time
    nic = network.Driver(...)
    if not nic.isconnected():
        nic.connect()
        print("Waiting for connection...")
        while not nic.isconnected():
            time.sleep(1)
    print(nic.ifconfig())

    # now use socket as usual
    import socket
    addr = socket.getaddrinfo('micropython.org', 80)[0][-1]
    s = socket.socket()
    s.connect(addr)
    s.send(b'GET / HTTP/1.1\r\nHost: micropython.org\r\n\r\n')
    data = s.recv(1000)
    s.close()
"""

# source version: vab847696a
# origin module:: repos/micropython/docs/library/network.rst
# + module: network.WINC.rst
# + module: network.WLAN.rst
# + module: network.LAN.rst
from __future__ import annotations
from typing import IO, Any, Callable, Coroutine, Dict, Generator, Iterator, List, NoReturn, Optional, Tuple, Union, NamedTuple, TypeVar
from _typeshed import Incomplete
OPEN: Incomplete
"""For connecting to an open wifi network."""
WPA_PSK: Incomplete
"""For connecting to a WPA/PSK based password protected network."""
802_1X: Incomplete
"""Network is secured with WPA/WPA2 Enterprise."""
MODE_STA: Incomplete
"""Start in station mode (i.e. connect to a network)."""
MODE_AP: Incomplete
"""Start in access point mode (i.e. become the network)."""
MODE_P2P: Incomplete
"""Start in wifi-direct mode."""
MODE_BSP: Incomplete
"""Init BSP."""
MODE_FIRMWARE: Incomplete
"""Setup in firmware update mode."""
class AbstractNIC():
    """
    实例化网络接口对象。参数取决于网络接口。如果有多个相同类型的接口，则第一个参数应为 `id`。
    """
    def __init__(self, id=None, *args, **kwargs) -> None:
        ...
    def active(self, is_active: Optional[Any]=None) -> None:
        """
                激活 ("up") 或停用 ("down") 网络接口，如果传递了布尔参数。否则，如果未提供参数，则查询当前状态。大多数其他方法都需要活动接口（在非活动接口上调用它们的行为是未定义的）。
        """
        ...
    def connect(self, service_id: Optional[Any]=None, key: Optional[Any]=None, *args, **kwargs) -> None:
        """
               将接口连接到网络。此方法是可选的，仅适用于不是 "始终连接" 的接口。如果没有给出参数，则连接到默认（或唯一）服务。如果给定单个参数，则它是要连接的服务的主要标识符。它可能需要与访问所述服务所需的密码。还可以有进一步的任意关键字参数，这取决于网络介质类型和/或特定设备。参数可用于：a）指定替代服务标识符类型；b）提供附加的连接参数。对于各种介质类型，有不同的预定义/推荐参数集，其中包括：
        
               * * WiFi: *bssid* 关键字以连接到特定的 BSSID（MAC 地址）
        """
        ...
    def disconnect(self) -> None:
        """
               断开网络连接。
        """
        ...
    def isconnected(self) -> bool:
        """
               如果连接到网络，则返回 ``True``，否则返回 ``False``。
        """
        ...
    def scan(self, *args, **kwargs) -> List[Tuple]:
        """
               扫描可用的网络服务/连接。返回发现的服务参数的元组列表。对于各种网络媒体，有不同的预定义/推荐元组格式变体，其中包括：
        
               * WiFi: (ssid, bssid, channel, RSSI, security, hidden)。还可能有其他字段，特定于特定设备。
        
               该函数可能接受其他关键字参数以过滤扫描结果（例如，扫描特定服务、特定信道上的服务、特定集合的服务等），并影响扫描持续时间和其他参数。在可能的情况下，参数名称应与 connect() 中的参数名称匹配。
        """
        ...
    def status(self, param: Optional[Any]=None) -> Incomplete:
        """
               查询接口的动态状态信息。当不带参数调用时，返回值描述网络链接状态。否则，*param* 应该是命名要检索的特定状态参数的字符串。
        
               返回类型和值取决于网络媒体/技术。可能支持的一些参数包括：
        
               * WiFi STA: 使用 ``'rssi'`` 检索 AP 信号的 RSSI
               * WiFi AP: 使用 ``'stations'`` 检索连接到 AP 的所有 STA 的列表。该列表包含形式为 (MAC、RSSI) 的元组。
        """
        ...
    def ifconfig(self, configtuple: Optional[Any]=None) -> Tuple:
        """
               Get/set IP-level network interface parameters: IP address, subnet mask,
               gateway and DNS server. When called with no arguments, this method returns
               a 4-tuple with the above information. To set the above values, pass a
               4-tuple with the required information.  举例::
        
                nic.ifconfig(('192.168.0.4', '255.255.255.0', '192.168.0.1', '8.8.8.8'))
        """
        ...
    def config(self, param) -> Incomplete:
        """
               获取或设置一般的网络接口参数。这些方法允许处理标准IP配置（由 `ifconfig()`处理）之外的附加参数。这些包括网络特定和硬件特定的参数。对于设置参数，应使用关键字参数语法，并且可以一次设置多个参数。对于查询，应将参数名称作为字符串引用，并且一次只能查询一个参数::
        
                # Set WiFi access point name (formally known as SSID) and WiFi channel
                ap.config(ssid='My AP', channel=11)
                # Query params one by one
                print(ap.config('ssid'))
                print(ap.config('channel'))
        """
        ...
class WINC():
    """
       Creates a winc driver object and connects to the wifi shield which uses
       I/O pins P0, P1, P2, P3, P6, P7, and P8.
    
       ``mode`` controls the mode the WINC module works in:
    
         * network.WINC.MODE_STATION
    
           The module connects to an access point as a client. This is the default mode.
    
         * network.WINC.MODE_AP
    
           The module will create an AP (Access Point) and accept connections from a client.
    
           .. note::
    
              The start_ap() method must be called after setting AP mode to configure the AP.
    
              Also, the WINC1500 has some limitations in its AP implementation:
    
                 * Only one client can connect at a time.
                 * Only OPEN or WEP security are supported.
                 * There's a bug in the WiFi Module FW, when the client disconnects any bound sockets are lost (they just stop working). As a workaround, set a timeout for the server socket to force it to raise an exception and then reopen it (See the example script).
    
         * network.WINC.MODE_FIRMWARE:
    
           This mode enables WiFi module firmware update.
    
       .. note::
    
          ``mode`` can also be ``network.STA_IF`` (station aka client, connects to upstream WiFi access
          points) and and ``network.AP_IF`` (access point, allows other WiFi clients to
          connect). Availability of the methods below depends on interface type.
          For example, only STA interface may `WLAN.connect()` to an access point.
    
       Methods
       -------
    """
    def __init__(self, mode=MODE_STATION: Optional[Any]=None) -> None:
        ...
    def active(self, is_active: Optional[Any]=None) -> None:
        """
              Activate ("up") or deactivate ("down") network interface, if boolean
              argument is passed. Otherwise, query current state if no argument is
              provided. Most other methods require active interface.
        """
        ...
    def connect(self, ssid, key=None, security=WPA_PSK, channel=1: Optional[Any]=None) -> None:
        """
              Connect to a wifi network with ssid ``ssid`` using key ``key`` with
              security ``security`` and channel ``channel``.
        
              After connecting to the network use the :mod:`usocket` module to open TCP/UDP
              ports to send and receive data.
        
              .. note::
        
                 This method takes a little while to return.
        """
        ...
    def start_ap(self, ssid, key=None, security=OPEN, channel=1: Optional[Any]=None) -> Incomplete:
        """
              When running in AP mode this method must be called after creating
              a WINC object to configure and start the AP .
        
              * ssid: The AP SSID (must be set).
              * key: The AP encryption key. A Key is required only if security is WEP.
              * security: AP security mode (only OPEN or WEP are supported).
              * channel: WiFi channel, change this if you have another AP running at the same channel.
        """
        ...
    def disconnect(self) -> None:
        """
              Disconnect from the wifi network.
        """
        ...
    def isconnected(self) -> bool:
        """
              Returns True if connected to an access point and an IP address has been
              obtained.
        """
        ...
    def connected_sta(self) -> Incomplete:
        """
              This method returns a list containing the connected client's IP address.
        """
        ...
    def wait_for_sta(self, timeout) -> Incomplete:
        """
              This method blocks and waits for a client to connect. If timeout is 0
              this will block forever. This method returns a list containing the
              connected client's IP address.
        """
        ...
    def ifconfig(self, ip_addr, subnet_addr, gateway_addr, dns_addr: Optional[Any]=None) -> Tuple:
        """
              Returns a tuple containing:
        
                 * [0]: IP Address String (XXX.XXX.XXX.XXX)
                 * [1]: Subnet Address String (XXX.XXX.XXX.XXX)
                 * [2]: Gateway String (XXX.XXX.XXX.XXX)
                 * [3]: DNS Address String (XXX.XXX.XXX.XXX)
        
              While connected to the network.
        
              You may optionally pass a tuple/list of the ip_addr, subnet_addr,
              gateway_addr, and dns_addr strings in ipv4 (XXX.XXX.XXX.XXX) format
              to set a static IP address versus an address obtained through DHCP (which happens by default).
        
              Example usage::
        
                 wlan = network.WINC()
                 wlan.ifconfig(('192.168.1.100', '255.255.255.0', '192.168.1.1', '192.168.1.1'))
                 wlan.connect(SSID, key=KEY, security=wlan.WPA_PSK)
        """
        ...
    def netinfo(self) -> Tuple:
        """
              Returns a tuple containing:
        
                 * [0]: RSSI - received signal strength indicator (int)
                 * [1]: Authorization Type (see constants)
                 * [2]: Set Service Identifier String (SSID)
                 * [3]: MAC Address String (XX:XX:XX:XX:XX:XX) (BSSID)
                 * [4]: IP Address String (XXX.XXX.XXX.XXX)
        
              While connected to the network.
        """
        ...
    def scan(self) -> Incomplete:
        """
              Returns a list containing:
        
                 * [0]: Set Service Identifier String (SSID)
                 * [1]: MAC Address String (XX:XX:XX:XX:XX:XX) (BSSID)
                 * [2]: Channel Number (int)
                 * [3]: RSSI - received signal strength indicator (int)
                 * [4]: Authorization Type (see constants)
                 * [5]: 1 (int)
        
              You don't need to be connected to call this.
        """
        ...
    def rssi(self) -> Incomplete:
        """
              Returns the received signal strength indicator (int) of the currently
              connected network.
        """
        ...
    def fw_version(self) -> Tuple:
        """
              Returns a tuple containing the wifi shield firmware version number.
        
                 * [0]: Firmware Major Version Number (int)
                 * [1]: Firmware Minor Version Number (int)
                 * [2]: Firmware Patch Version Number (int)
                 * [3]: Driver Major Version Number (int)
                 * [4]: Driver Minor Version Number (int)
                 * [5]: Driver Patch Version Number (int)
                 * [6]: Hardware Revision Number - Chip ID (int)
        """
        ...
    def fw_dump(self, path) -> Incomplete:
        """
              Dumps the wifi shield firmware to a binary file at ``path``. You must
              have put the module into firmware mode to use this.
        """
        ...
    def fw_update(self, path) -> Incomplete:
        """
              Programs the wifi shield with binary image found at ``path``. You must
              have put the module into firmware mode to use this.
        
           Constants
           ---------
        """
        ...
class WLAN():
    """
    Create a WLAN network interface object. Supported interfaces are
    ``network.STA_IF`` (station aka client, connects to upstream WiFi access
    points) and ``network.AP_IF`` (access point, allows other WiFi clients to
    connect). Availability of the methods below depends on interface type.
    For example, only STA interface may `WLAN.connect()` to an access point.
    """
    PM_PERFORMANCE: Incomplete
    """\
    WLAN.PM_POWERSAVE
    WLAN.PM_NONE
    
    Allowed values for the ``WLAN.config(pm=...)`` network interface parameter:
    
    * ``PM_PERFORMANCE``: enable WiFi power management to balance power
    savings and WiFi performance
    * ``PM_POWERSAVE``: enable WiFi power management with additional power
    savings and reduced WiFi performance
    * ``PM_NONE``: disable wifi power management
    """
    def __init__(self, interface_id) -> None:
        ...
    def active(self, is_active: Optional[Any]=None) -> None:
        """
            Activate ("up") or deactivate ("down") network interface, if boolean
            argument is passed. Otherwise, query current state if no argument is
            provided. Most other methods require active interface.
        """
        ...
    def connect(self, ssid=None, key=None, *, bssid=None) -> None:
        """
            Connect to the specified wireless network, using the specified key.
            If *bssid* is given then the connection will be restricted to the
            access-point with that MAC address (the *ssid* must also be specified
            in this case).
        """
        ...
    def disconnect(self) -> None:
        """
            Disconnect from the currently connected wireless network.
        """
        ...
    def scan(self) -> List[Tuple]:
        """
            Scan for the available wireless networks.
            Hidden networks -- where the SSID is not broadcast -- will also be scanned
            if the WLAN interface allows it.
        
            Scanning is only possible on STA interface. Returns list of tuples with
            the information about WiFi access points:
        
                (ssid, bssid, channel, RSSI, security, hidden)
        
            *bssid* is hardware address of an access point, in binary form, returned as
            bytes object. You can use `binascii.hexlify()` to convert it to ASCII form.
        
            There are five values for security:
        
                * 0 -- open
                * 1 -- WEP
                * 2 -- WPA-PSK
                * 3 -- WPA2-PSK
                * 4 -- WPA/WPA2-PSK
        
            and two for hidden:
        
                * 0 -- visible
                * 1 -- hidden
        """
        ...
    def status(self, param: Optional[Any]=None) -> Incomplete:
        """
            Return the current status of the wireless connection.
        
            When called with no argument the return value describes the network link status.
            The possible statuses are defined as constants:
        
                * ``STAT_IDLE`` -- no connection and no activity,
                * ``STAT_CONNECTING`` -- connecting in progress,
                * ``STAT_WRONG_PASSWORD`` -- failed due to incorrect password,
                * ``STAT_NO_AP_FOUND`` -- failed because no access point replied,
                * ``STAT_CONNECT_FAIL`` -- failed due to other problems,
                * ``STAT_GOT_IP`` -- connection successful.
        
            When called with one argument *param* should be a string naming the status
            parameter to retrieve.  Supported parameters in WiFI STA mode are: ``'rssi'``.
        """
        ...
    def isconnected(self) -> bool:
        """
            In case of STA mode, returns ``True`` if connected to a WiFi access
            point and has a valid IP address.  In AP mode returns ``True`` when a
            station is connected. Returns ``False`` otherwise.
        """
        ...
    def ifconfig(self, configtuple: Optional[Any]=None) -> Tuple:
        """
           Get/set IP-level network interface parameters: IP address, subnet mask,
           gateway and DNS server. When called with no arguments, this method returns
           a 4-tuple with the above information. To set the above values, pass a
           4-tuple with the required information.  举例::
        
            nic.ifconfig(('192.168.0.4', '255.255.255.0', '192.168.0.1', '8.8.8.8'))
        """
        ...
    def config(self, *args, **kwargs) -> Incomplete:
        """
           Get or set general network interface parameters. These methods allow to work
           with additional parameters beyond standard IP configuration (as dealt with by
           `WLAN.ifconfig()`). These include network-specific and hardware-specific
           parameters. For setting parameters, keyword argument syntax should be used,
           multiple parameters can be set at once. For querying, parameters name should
           be quoted as a string, and only one parameter can be queries at time::
        
            # Set WiFi access point name (formally known as SSID) and WiFi channel
            ap.config(ssid='My AP', channel=11)
            # Query params one by one
            print(ap.config('ssid'))
            print(ap.config('channel'))
        
           Following are commonly supported parameters (availability of a specific parameter
           depends on network technology type, driver, and :term:`MicroPython port`).
        
           =============  ===========
           Parameter      Description
           =============  ===========
           mac            MAC address (bytes)
           ssid           WiFi access point name (string)
           channel        WiFi channel (integer)
           hidden         Whether SSID is hidden (boolean)
           security       Security protocol supported (enumeration, see module constants)
           key            Access key (string)
           hostname       The hostname that will be sent to DHCP (STA interfaces) and mDNS (if supported, both STA and AP). (Deprecated, use :func:`network.hostname` instead)
           reconnects     Number of reconnect attempts to make (integer, 0=none, -1=unlimited)
           txpower        Maximum transmit power in dBm (integer or float)
           pm             WiFi Power Management setting (see below for allowed values)
           =============  ===========
        """
        ...
class LAN():
    """
       Create a LAN driver object, initialise the LAN module using the given
       PHY driver name, and return the LAN object.
    
       Arguments are:
    
         - *id* is the number of the Ethernet port, either 0 or 1.
         - *phy_type* is the name of the PHY driver. For most board the on-board PHY has to be used and
           is the default. Suitable values are port specific.
         - *phy_addr* specifies the address of the PHY interface. As with *phy_type*, the hardwired value has
           to be used for most boards and that value is the default.
         - *ref_clk_mode* specifies, whether the data clock is provided by the Ethernet controller or
           the PYH interface.
           The default value is the one that matches the board. If set to ``LAN.OUT`` or ``Pin.OUT``
           or ``True``, the clock is driven by the Ethernet controller, if set to ``LAN.IN``
           or ``Pin.IN`` or ``False``, the clock is driven by the PHY interface.
    
       For example, with the Seeed Arch Mix board you can  use::
    
         nic = LAN(0, phy_type=LAN.PHY_LAN8720, phy_addr=1, ref_clk_mode=Pin.IN)
    """
    def __init__(self, id, *, phy_type=0, phy_addr=0, ref_clk_mode=0) -> None:
        ...
    def active(self, state: Optional[Any]=None) -> Incomplete:
        """
           With a parameter, it sets the interface active if *state* is true, otherwise it
           sets it inactive.
           Without a parameter, it returns the state.
        """
        ...
    def isconnected(self) -> bool:
        """
           Returns ``True`` if the physical Ethernet link is connected and up.
           Returns ``False`` otherwise.
        """
        ...
    def status(self) -> Incomplete:
        """
           Returns the LAN status.
        """
        ...
    def ifconfig(self, configtuple: Optional[Any]=None) -> Tuple:
        """
           Get/set IP address, subnet mask, gateway and DNS.
        
           When called with no arguments, this method returns a 4-tuple with the above information.
        
           To set the above values, pass a 4-tuple with the required information.  举例::
        
            nic.ifconfig(('192.168.0.4', '255.255.255.0', '192.168.0.1', '8.8.8.8'))
        """
        ...
    def config(self, config_parameters) -> Incomplete:
        """
           Sets or gets parameters of the LAN interface. The only parameter that can be
           retrieved is the MAC address, using::
        
              mac = LAN.config("mac")
        
           The parameters that can be set are:
        
            - ``trace=n`` sets trace levels; suitable values are:
        
                - 2: trace TX
                - 4: trace RX
                - 8: full trace
        
            - ``low_power=bool`` sets or clears low power mode, valid values being ``False``
              or ``True``.
        """
        ...
