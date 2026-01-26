"""
Functions related to the hardware.

MicroPython module: https://docs.micropython.org/en/vab847696a/library/machine.html

``machine`` 模块包含特定于某个板上的与硬件相关的特定函数。该模块中的大多数函数允许直接和无限制地访问和控制系统上的硬件模块（如 CPU、定时器、总线等）。如果使用不当，这可能导致板的故障、死机、崩溃，甚至在极端情况下可能造成硬件损坏。
"""

# source version: vab847696a
# origin module:: repos/micropython/docs/library/machine.rst
# + module: machine.Pin.rst
# + module: machine.Signal.rst
# + module: machine.ADC.rst
# + module: machine.ADCBlock.rst
# + module: machine.CAN.rst
# + module: machine.PWM.rst
# + module: machine.UART.rst
# + module: machine.SPI.rst
# + module: machine.I2C.rst
# + module: machine.I2S.rst
# + module: machine.RTC.rst
# + module: machine.Timer.rst
# + module: machine.WDT.rst
from __future__ import annotations
from typing import Any, Callable, List, NoReturn, Optional, Tuple, Union
from _typeshed import Incomplete
mem8: Incomplete
"""读/写内存的8位。"""
mem16: Incomplete
"""读/写内存的16位。"""
mem32: int
"""\
读/写内存的32位。

使用下标符号 ``[...]`` 来使用感兴趣的地址索引这些对象。请注意，无论所访问的内存大小如何，地址都是字节地址。

使用示例（寄存器特定于stm32微控制器）：
"""
IDLE: Incomplete
"""IRQ唤醒值。"""
SLEEP: Incomplete
"""IRQ唤醒值。"""
DEEPSLEEP: Incomplete
"""IRQ唤醒值。"""
PWRON_RESET: Incomplete
"""重置原因。"""
HARD_RESET: Incomplete
"""重置原因。"""
WDT_RESET: Incomplete
"""重置原因。"""
DEEPSLEEP_RESET: Incomplete
"""重置原因。"""
SOFT_RESET: Incomplete
"""重置原因。"""
WLAN_WAKE: Incomplete
"""唤醒原因。"""
PIN_WAKE: Incomplete
"""唤醒原因。"""
RTC_WAKE: Incomplete
"""唤醒原因。"""
class Pin():
    """
       Access the pin peripheral (GPIO pin) associated with the given ``id``.  If
       additional arguments are given in the constructor then they are used to initialise
       the pin.  Any settings that are not specified will remain in their previous state.
    
       The arguments are:
    
         - ``id`` is mandatory and can be an arbitrary object.  Among possible value
           types are: int (an internal Pin identifier), str (a Pin name), and tuple
           (pair of [port, pin]).
    
         - ``mode`` specifies the pin mode, which can be one of:
    
           - ``Pin.IN`` - Pin is configured for input.  If viewed as an output the pin
             is in high-impedance state.
    
           - ``Pin.OUT`` - Pin is configured for (normal) output.
    
           - ``Pin.OPEN_DRAIN`` - Pin is configured for open-drain output. Open-drain
             output works in the following way: if the output value is set to 0 the pin
             is active at a low level; if the output value is 1 the pin is in a high-impedance
             state.  Not all ports implement this mode, or some might only on certain pins.
    
           - ``Pin.ALT`` - Pin is configured to perform an alternative function, which is
             port specific.  For a pin configured in such a way any other Pin methods
             (except :meth:`Pin.init`) are not applicable (calling them will lead to undefined,
             or a hardware-specific, result).  Not all ports implement this mode.
    
           - ``Pin.ALT_OPEN_DRAIN`` - The Same as ``Pin.ALT``, but the pin is configured as
             open-drain.  Not all ports implement this mode.
    
           - ``Pin.ANALOG`` - Pin is configured for analog input, see the :class:`ADC` class.
    
         - ``pull`` specifies if the pin has a (weak) pull resistor attached, and can be
           one of:
    
           - ``None`` - No pull up or down resistor.
           - ``Pin.PULL_UP`` - Pull up resistor enabled.
           - ``Pin.PULL_DOWN`` - Pull down resistor enabled.
    
         - ``value`` is valid only for Pin.OUT and Pin.OPEN_DRAIN modes and specifies initial
           output pin value if given, otherwise the state of the pin peripheral remains
           unchanged.
    
         - ``drive`` specifies the output power of the pin and can be one of: ``Pin.DRIVE_0``,
           ``Pin.DRIVE_1``, etc., increasing in drive strength.  The actual current driving
           capabilities are port dependent.  Not all ports implement this argument.
    
         - ``alt`` specifies an alternate function for the pin and the values it can take are
           port dependent.  This argument is valid only for ``Pin.ALT`` and ``Pin.ALT_OPEN_DRAIN``
           modes.  It may be used when a pin supports more than one alternate function.  If only
           one pin alternate function is supported the this argument is not required.  Not all
           ports implement this argument.
    
       As specified above, the Pin class allows to set an alternate function for a particular
       pin, but it does not specify any further operations on such a pin.  Pins configured in
       alternate-function mode are usually not used as GPIO but are instead driven by other
       hardware peripherals.  The only operation supported on such a pin is re-initialising,
       by calling the constructor or :meth:`Pin.init` method.  If a pin that is configured in
       alternate-function mode is re-initialised with ``Pin.IN``, ``Pin.OUT``, or
       ``Pin.OPEN_DRAIN``, the alternate function will be removed from the pin.
    """
    IN: Incomplete
    """Selects the pin mode."""
    OUT: Incomplete
    """Selects the pin mode."""
    OPEN_DRAIN: Incomplete
    """Selects the pin mode."""
    ALT: Incomplete
    """Selects the pin mode."""
    ALT_OPEN_DRAIN: Incomplete
    """Selects the pin mode."""
    ANALOG: Incomplete
    """Selects the pin mode."""
    PULL_UP: Incomplete
    """\
    Selects whether there is a pull up/down resistor.  Use the value
    ``None`` for no pull.
    """
    PULL_DOWN: Incomplete
    """\
    Selects whether there is a pull up/down resistor.  Use the value
    ``None`` for no pull.
    """
    PULL_HOLD: Incomplete
    """\
    Selects whether there is a pull up/down resistor.  Use the value
    ``None`` for no pull.
    """
    DRIVE_0: int
    """\
    Selects the pin drive strength.  A port may define additional drive
    constants with increasing number corresponding to increasing drive
    strength.
    """
    DRIVE_1: int
    """\
    Selects the pin drive strength.  A port may define additional drive
    constants with increasing number corresponding to increasing drive
    strength.
    """
    DRIVE_2: int
    """\
    Selects the pin drive strength.  A port may define additional drive
    constants with increasing number corresponding to increasing drive
    strength.
    """
    IRQ_FALLING: Incomplete
    """Selects the IRQ trigger type."""
    IRQ_RISING: Incomplete
    """Selects the IRQ trigger type."""
    IRQ_LOW_LEVEL: Incomplete
    """Selects the IRQ trigger type."""
    IRQ_HIGH_LEVEL: Incomplete
    """Selects the IRQ trigger type."""
    def __init__(self, id, mode=-1, pull=-1, *, value=None, drive=0, alt=-1) -> None:
        ...
    def init(self, mode=-1, pull=-1, *, value=None, drive=0, alt=-1) -> None:
        """
           Re-initialise the pin using the given parameters.  Only those arguments that
           are specified will be set.  The rest of the pin peripheral state will remain
           unchanged.  See the constructor documentation for details of the arguments.
        
           Returns ``None``.
        """
        ...
    def value(self, x: Optional[Any]=None) -> int:
        """
           This method allows to set and get the value of the pin, depending on whether
           the argument ``x`` is supplied or not.
        
           If the argument is omitted then this method gets the digital logic level of
           the pin, returning 0 or 1 corresponding to low and high voltage signals
           respectively.  The behaviour of this method depends on the mode of the pin:
        
             - ``Pin.IN`` - The method returns the actual input value currently present
               on the pin.
             - ``Pin.OUT`` - The behaviour and return value of the method is undefined.
             - ``Pin.OPEN_DRAIN`` - If the pin is in state '0' then the behaviour and
               return value of the method is undefined.  Otherwise, if the pin is in
               state '1', the method returns the actual input value currently present
               on the pin.
        
           If the argument is supplied then this method sets the digital logic level of
           the pin.  The argument ``x`` can be anything that converts to a boolean.
           If it converts to ``True``, the pin is set to state '1', otherwise it is set
           to state '0'.  The behaviour of this method depends on the mode of the pin:
        
             - ``Pin.IN`` - The value is stored in the output buffer for the pin.  The
               pin state does not change, it remains in the high-impedance state.  The
               stored value will become active on the pin as soon as it is changed to
               ``Pin.OUT`` or ``Pin.OPEN_DRAIN`` mode.
             - ``Pin.OUT`` - The output buffer is set to the given value immediately.
             - ``Pin.OPEN_DRAIN`` - If the value is '0' the pin is set to a low voltage
               state.  Otherwise the pin is set to high-impedance state.
        
           When setting the value this method returns ``None``.
        """
        ...
    def __call__(self, x: Optional[Any]=None) -> Incomplete:
        """
           Pin objects are callable.  The call method provides a (fast) shortcut to set
           and get the value of the pin.  It is equivalent to Pin.value([x]).
           See :meth:`Pin.value` for more details.
        """
        ...
    def on(self) -> None:
        """
           Set pin to "1" output level.
        """
        ...
    def off(self) -> None:
        """
           Set pin to "0" output level.
        """
        ...
    def irq(self, handler=None, trigger=IRQ_FALLING , *, priority=1, wake=None, hard=False) -> Callable[..., Incomplete]:
        """
           Configure an interrupt handler to be called when the trigger source of the
           pin is active.  If the pin mode is ``Pin.IN`` then the trigger source is
           the external value on the pin.  If the pin mode is ``Pin.OUT`` then the
           trigger source is the output buffer of the pin.  Otherwise, if the pin mode
           is ``Pin.OPEN_DRAIN`` then the trigger source is the output buffer for
           state '0' and the external pin value for state '1'.
        
           The arguments are:
        
             - ``handler`` is an optional function to be called when the interrupt
               triggers. The handler must take exactly one argument which is the
               ``Pin`` instance.
        
             - ``trigger`` configures the event which can generate an interrupt.
               Possible values are:
        
               - ``Pin.IRQ_FALLING`` interrupt on falling edge.
               - ``Pin.IRQ_RISING`` interrupt on rising edge.
               - ``Pin.IRQ_LOW_LEVEL`` interrupt on low level.
               - ``Pin.IRQ_HIGH_LEVEL`` interrupt on high level.
        
               These values can be OR'ed together to trigger on multiple events.
        
             - ``priority`` sets the priority level of the interrupt.  The values it
               can take are port-specific, but higher values always represent higher
               priorities.
        
             - ``wake`` selects the power mode in which this interrupt can wake up the
               system.  It can be ``machine.IDLE``, ``machine.SLEEP`` or ``machine.DEEPSLEEP``.
               These values can also be OR'ed together to make a pin generate interrupts in
               more than one power mode.
        
             - ``hard`` if true a hardware interrupt is used. This reduces the delay
               between the pin change and the handler being called. Hard interrupt
               handlers may not allocate memory; see :ref:`isr_rules`.
               Not all ports support this argument.
        
           This method returns a callback object.
        
        The following methods are not part of the core Pin API and only implemented on certain ports.
        """
        ...
    def low(self) -> None:
        """
           Set pin to "0" output level.
        
           Availability: nrf, rp2, stm32 ports.
        """
        ...
    def high(self) -> None:
        """
           Set pin to "1" output level.
        
           Availability: nrf, rp2, stm32 ports.
        """
        ...
    def mode(self, mode: Optional[Any]=None) -> Incomplete:
        """
           Get or set the pin mode.
           See the constructor documentation for details of the ``mode`` argument.
        
           Availability: cc3200, stm32 ports.
        """
        ...
    def pull(self, pull: Optional[Any]=None) -> Incomplete:
        """
           Get or set the pin pull state.
           See the constructor documentation for details of the ``pull`` argument.
        
           Availability: cc3200, stm32 ports.
        """
        ...
    def drive(self, drive: Optional[Any]=None) -> Incomplete:
        """
           Get or set the pin drive strength.
           See the constructor documentation for details of the ``drive`` argument.
        
           Availability: cc3200 port.
        """
        ...
class Signal(Pin):
    """
               Signal(pin_arguments..., *, invert=False)
    
       Create a Signal object. There're two ways to create it:
    
       * By wrapping existing Pin object - universal method which works for
         any board.
       * By passing required Pin parameters directly to Signal constructor,
         skipping the need to create intermediate Pin object. Available on
         many, but not all boards.
    
       The arguments are:
    
         - ``pin_obj`` is existing Pin object.
    
         - ``pin_arguments`` are the same arguments as can be passed to Pin constructor.
    
         - ``invert`` - if True, the signal will be inverted (active low).
    """
    def __init__(self, pin_obj, *args, invert=False) -> None:
        ...
    def value(self, x: Optional[Any]=None) -> int:
        """
           This method allows to set and get the value of the signal, depending on whether
           the argument ``x`` is supplied or not.
        
           If the argument is omitted then this method gets the signal level, 1 meaning
           signal is asserted (active) and 0 - signal inactive.
        
           If the argument is supplied then this method sets the signal level. The
           argument ``x`` can be anything that converts to a boolean. If it converts
           to ``True``, the signal is active, otherwise it is inactive.
        
           Correspondence between signal being active and actual logic level on the
           underlying pin depends on whether signal is inverted (active-low) or not.
           For non-inverted signal, active status corresponds to logical 1, inactive -
           to logical 0. For inverted/active-low signal, active status corresponds
           to logical 0, while inactive - to logical 1.
        """
        ...
    def on(self) -> None:
        """
           Activate signal.
        """
        ...
    def off(self) -> None:
        """
           Deactivate signal.
        """
        ...
class ADC():
    """
       Access the ADC associated with a source identified by *id*.  This
       *id* may be an integer (usually specifying a channel number), a
       :ref:`Pin <machine.Pin>` object, or other value supported by the
       underlying machine.
    
       If additional keyword-arguments are given then they will configure
       various aspects of the ADC.  If not given, these settings will take
       previous or default values.  The settings are:
    
         - *sample_ns* is the sampling time in nanoseconds.
    
         - *atten* specifies the input attenuation.
    """
    def __init__(self, id, *, sample_ns:Optional[int]=0, atten:Optional[int]=ATTN_0DB) -> None:
        ...
    def init(self, *, sample_ns, atten) -> Incomplete:
        """
           Apply the given settings to the ADC.  Only those arguments that are
           specified will be changed.  See the ADC constructor above for what the
           arguments are.
        """
        ...
    def block(self) -> Incomplete:
        """
           Return the :ref:`ADCBlock <machine.ADCBlock>` instance associated with
           this ADC object.
        
           This method only exists if the port supports the
           :ref:`ADCBlock <machine.ADCBlock>` class.
        """
        ...
    def read_u16(self) -> int:
        """
           Take an analog reading and return an integer in the range 0-65535.
           The return value represents the raw reading taken by the ADC, scaled
           such that the minimum value is 0 and the maximum value is 65535.
        """
        ...
    def read_uv(self) -> int:
        """
           Take an analog reading and return an integer value with units of
           microvolts.  It is up to the particular port whether or not this value
           is calibrated, and how calibration is done.
        """
        ...
class ADCBlock():
    """
       Access the ADC peripheral identified by *id*, which may be an integer
       or string.
    
       The *bits* argument, if given, sets the resolution in bits of the
       conversion process.  If not specified then the previous or default
       resolution is used.
    """
    def __init__(self, id, *, bits) -> None:
        ...
    def init(self, *, bits) -> None:
        """
           Configure the ADC peripheral.  *bits* will set the resolution of the
           conversion process.
        """
        ...
    def connect(self, channel, source, *args, **kwargs) -> Incomplete:
        """
           Connect up a channel on the ADC peripheral so it is ready for sampling,
           and return an :ref:`ADC <machine.ADC>` object that represents that connection.
        
           The *channel* argument must be an integer, and *source* must be an object
           (for example a :ref:`Pin <machine.Pin>`) which can be connected up for sampling.
        
           If only *channel* is given then it is configured for sampling.
        
           If only *source* is given then that object is connected to a default
           channel ready for sampling.
        
           If both *channel* and *source* are given then they are connected together
           and made ready for sampling.
        
           Any additional keyword arguments are used to configure the returned ADC object,
           via its :meth:`init <machine.ADC.init>` method.
        """
        ...
class CAN():
    """
       Construct a CAN object on the given bus.  *bus* can be 0.
       With no additional parameters, the CAN object is created but not
       initialised (it has the settings from the last initialisation of
       the bus, if any).  If extra arguments are given, the bus is initialised.
       See :meth:`CAN.init` for parameters of initialisation.
    
       The physical pins of the CAN buses are:
    
         - ``CAN(0)``: ``(RX, TX) = (P3, P1)``
    """
    NORMAL: Incomplete
    """The mode of the CAN bus used in :meth:`~CAN.init()`."""
    LOOPBACK: Incomplete
    """The mode of the CAN bus used in :meth:`~CAN.init()`."""
    SILENT: Incomplete
    """The mode of the CAN bus used in :meth:`~CAN.init()`."""
    SILENT_LOOPBACK: Incomplete
    """The mode of the CAN bus used in :meth:`~CAN.init()`."""
    STOPPED: Incomplete
    """Possible states of the CAN controller returned from :meth:`~CAN.state()`."""
    ERROR_ACTIVE: Incomplete
    """Possible states of the CAN controller returned from :meth:`~CAN.state()`."""
    ERROR_WARNING: Incomplete
    """Possible states of the CAN controller returned from :meth:`~CAN.state()`."""
    ERROR_PASSIVE: Incomplete
    """Possible states of the CAN controller returned from :meth:`~CAN.state()`."""
    BUS_OFF: Incomplete
    """Possible states of the CAN controller returned from :meth:`~CAN.state()`."""
    LIST32: Incomplete
    """The operation mode of a filter used in :meth:`~CAN.setfilter()` for classic CAN."""
    DUAL: Incomplete
    """The operation mode of a filter used in :meth:`~CAN.setfilter()` for classic CAN."""
    def __init__(self, bus,  mode, baudrate=328125, *, prescaler=-1, polarity=1, phase=0, bits=8, firstbit=MSB, ti=False, crc=None) -> None:
        ...
    def init(self, mode, *, auto_restart=False, baudrate=0) -> None:
        """
           Initialise the CAN bus with the given parameters:
        
             - *mode* is one of:  NORMAL, LOOPBACK, SILENT, SILENT_LOOPBACK
             - *auto_restart* sets whether the controller will automatically try and restart
               communications after entering the bus-off state; if this is disabled then
               :meth:`~CAN.restart()` can be used to leave the bus-off state
             - *baudrate* sets the baudrate used to connect to the CAN bus
        """
        ...
    def deinit(self) -> None:
        """
           Turn off the CAN bus.
        """
        ...
    def restart(self) -> Incomplete:
        """
           Force a software restart of the CAN controller without resetting its
           configuration.
        
           If the controller enters the bus-off state then it will no longer participate
           in bus activity.  If the controller is not configured to automatically restart
           (see :meth:`~CAN.init()`) then this method can be used to trigger a restart,
           and the controller will follow the CAN protocol to leave the bus-off state and
           go into the error active state.
        """
        ...
    def state(self) -> Incomplete:
        """
           Return the state of the controller.  The return value can be one of:
        
           - ``CAN.STOPPED`` -- the controller is completely off and reset;
           - ``CAN.ERROR_ACTIVE`` -- the controller is on and in the Error Active state
             (both TEC and REC are less than 96);
           - ``CAN.ERROR_WARNING`` -- the controller is on and in the Error Warning state
             (at least one of TEC or REC is 96 or greater);
           - ``CAN.ERROR_PASSIVE`` -- the controller is on and in the Error Passive state
             (at least one of TEC or REC is 128 or greater);
           - ``CAN.BUS_OFF`` -- the controller is on but not participating in bus activity
             (TEC overflowed beyond 255).
        """
        ...
    def info(self, list: Optional[Any]=None) -> Incomplete:
        """
           Get information about the controller's error states and TX and RX buffers.
           If *list* is provided then it should be a list object with at least 8 entries,
           which will be filled in with the information.  Otherwise a new list will be
           created and filled in.  In both cases the return value of the method is the
           populated list.
        
           The values in the list are:
        
           - TEC value
           - REC value
           - number of times the controller enterted the Error Warning state (wrapped
             around to 0 after 65535)
           - number of times the controller enterted the Error Passive state (wrapped
             around to 0 after 65535)
           - number of times the controller enterted the Bus Off state (wrapped
             around to 0 after 65535)
           - number of pending TX messages
           - number of pending RX messages on fifo 0
           - always 0
        """
        ...
    def setfilter(self, bank, mode, fifo, params, *, rtr=None, extframe=False) -> None:
        """
           Configure a filter bank:
        
           - *bank* is the classic CAN controller filter bank to configure.
           - *mode* is the mode the filter should operate in, see the tables below.
           - *fifo* is which fifo (0) a message should be stored in, if it is accepted by this filter.
           - *params* is an array of values the defines the filter. The contents of the array depends on the *mode* argument.
        
           +-----------+---------------------------------------------------------+
           |*mode*     |Contents of *params* array for classic CAN controller    |
           +===========+=========================================================+
           |CAN.LIST32 |Two 32 bit ids that will be accepted                     |
           +-----------+---------------------------------------------------------+
           |CAN.DUAL   |Two ids that will be accepted. For example (1, 2)        |
           +-----------+---------------------------------------------------------+
        
           - *rtr* For classic CAN controllers, this is an array of booleans that states if
             a filter should accept a remote transmission request message. If this argument
             is not given then it defaults to ``False`` for all entries. The length of the
             array depends on the *mode* argument.
        
           +-----------+----------------------+
           |*mode*     |length of *rtr* array |
           +===========+======================+
           |CAN.LIST32 |2                     |
           +-----------+----------------------+
           |CAN.DUAL   |2                     |
           +-----------+----------------------+
        
           - *extframe* If True the frame will have an extended identifier (29 bits),
             otherwise a standard identifier (11 bits) is used.
        """
        ...
    def clearfilter(self, bank, extframe=False) -> None:
        """
           Clear and disables a filter bank:
        
           - *bank* is the classic CAN controller filter bank to clear.
           - *extframe* ignored
        """
        ...
    def any(self, fifo) -> bool:
        """
           Return ``True`` if any message waiting on the FIFO, else ``False``.
        """
        ...
    def recv(self, fifo, list=None, *, timeout=5000) -> Tuple:
        """
           Receive data on the bus:
        
             - *fifo* is an integer, which is the FIFO to receive on - always 0
             - *list* is an optional list object to be used as the return value
             - *timeout* is the timeout in milliseconds to wait for the receive.
        
           Return value: A tuple containing five values.
        
             - The id of the message.
             - A boolean that indicates if the message ID is standard or extended.
             - A boolean that indicates if the message is an RTR message.
             - The FMI (Filter Match Index) value.
             - An array containing the data.
        
           If *list* is ``None`` then a new tuple will be allocated, as well as a new
           bytes object to contain the data (as the fifth element in the tuple).
        
           If *list* is not ``None`` then it should be a list object with a least five
           elements.  The fifth element should be a memoryview object which is created
           from either a bytearray or an array of type 'B' or 'b', and this array must
           have enough room for at least 8 bytes.  The list object will then be
           populated with the first four return values above, and the memoryview object
           will be resized inplace to the size of the data and filled in with that data.
           The same list and memoryview objects can be reused in subsequent calls to
           this method, providing a way of receiving data without using the heap.
           For example::
        
                buf = bytearray(8)
                lst = [0, 0, 0, 0, memoryview(buf)]
                # No heap memory is allocated in the following call
                can.recv(0, lst)
        """
        ...
    def send(self, data, id, *, timeout=0, rtr=False, extframe=False) -> None:
        """
           Send a message on the bus:
        
             - *data* is the data to send (an integer to send, or a buffer object).
             - *id* is the id of the message to be sent.
             - *timeout* is the timeout in milliseconds to wait for the send.
             - *rtr* is a boolean that specifies if the message shall be sent as
               a remote transmission request.  If *rtr* is True then only the length
               of *data* is used to fill in the DLC slot of the frame; the actual
               bytes in *data* are unused.
             - *extframe* if True the frame will have an extended identifier (29 bits),
               otherwise a standard identifier (11 bits) is used.
        
             If timeout is 0 the message is placed in a buffer and the method returns immediately.
        	 If all three buffers are in use an exception is thrown. If timeout is not 0,
        	 the method waits until the message is transmitted. If the message can't be transmitted
        	 within the specified time an exception is thrown.
        
           Return value: ``None``.
        """
        ...
    def rxcallback(self, fifo, fun) -> None:
        """
           Register a function to be called when a message is accepted into a empty fifo:
        
           - *fifo* is the receiving fifo - always 0.
           - *fun* is the function to be called when the fifo becomes non empty.
        
           The callback function takes two arguments the first is the can object it self the second is
           a integer that indicates the reason for the callback.
        
           +--------+------------------------------------------------+
           | Reason |                                                |
           +========+================================================+
           | 0      | A message has been accepted into a empty FIFO. |
           +--------+------------------------------------------------+
           | 1      | The FIFO is full                               |
           +--------+------------------------------------------------+
           | 2      | A message has been lost due to a full FIFO     |
           +--------+------------------------------------------------+
        
           Example use of rxcallback::
        
             def cb0(bus, reason):
               print('cb0')
               if reason == 0:
                   print('pending')
               if reason == 1:
                   print('full')
               if reason == 2:
                   print('overflow')
        
             can = CAN(0, CAN.LOOPBACK)
             can.rxcallback(0, cb0)
        """
        ...
class PWM():
    """
       Construct and return a new PWM object using the following parameters:
    
          - *dest* is the entity on which the PWM is output, which is usually a
            :ref:`machine.Pin <machine.Pin>` object, but a port may allow other values,
            like integers.
          - *freq* should be an integer which sets the frequency in Hz for the
            PWM cycle.
          - *duty_u16* sets the duty cycle as a ratio ``duty_u16 / 65535``.
          - *duty_ns* sets the pulse width in nanoseconds.
          - *invert*  inverts the respective output if the value is True
    
       Setting *freq* may affect other PWM objects if the objects share the same
       underlying PWM generator (this is hardware specific).
       Only one of *duty_u16* and *duty_ns* should be specified at a time.
       *invert* is not available at all ports.
    """
    def __init__(self, dest, *, freq=0,duty=0, duty_u16=0, duty_ns=0, invert=False) -> None:
        ...
    def init(self, *, freq, duty_u16, duty_ns) -> None:
        """
           Modify settings for the PWM object.  See the above constructor for details
           about the parameters.
        """
        ...
    def deinit(self) -> None:
        """
           Disable the PWM output.
        """
        ...
    def freq(self, value: Optional[Any]=None) -> Incomplete:
        """
           Get or set the current frequency of the PWM output.
        
           With no arguments the frequency in Hz is returned.
        
           With a single *value* argument the frequency is set to that value in Hz.  The
           method may raise a ``ValueError`` if the frequency is outside the valid range.
        """
        ...
    def duty_u16(self, value: Optional[Any]=None) -> int:
        """
           Get or set the current duty cycle of the PWM output, as an unsigned 16-bit
           value in the range 0 to 65535 inclusive.
        
           With no arguments the duty cycle is returned.
        
           With a single *value* argument the duty cycle is set to that value, measured
           as the ratio ``value / 65535``.
        """
        ...
    def duty_ns(self, value: Optional[Any]=None) -> int:
        """
           Get or set the current pulse width of the PWM output, as a value in nanoseconds.
        
           With no arguments the pulse width in nanoseconds is returned.
        
           With a single *value* argument the pulse width is set to that value.
        """
        ...
class UART():
    """
       Construct a UART object of the given id.
    """
    def __init__(self, id, *args, **kwargs) -> None:
        ...
    def init(self, baudrate=9600, bits=8, parity=None, stop=1, *args, **kwargs) -> None:
        """
           Initialise the UART bus with the given parameters:
        
             - *baudrate* is the clock rate.
             - *bits* is the number of bits per character, 7, 8 or 9.
             - *parity* is the parity, ``None``, 0 (even) or 1 (odd).
             - *stop* is the number of stop bits, 1 or 2.
        
           Additional keyword-only parameters that may be supported by a port are:
        
             - *tx* specifies the TX pin to use.
             - *rx* specifies the RX pin to use.
             - *rts* specifies the RTS (output) pin to use for hardware receive flow control.
             - *cts* specifies the CTS (input) pin to use for hardware transmit flow control.
             - *txbuf* specifies the length in characters of the TX buffer.
             - *rxbuf* specifies the length in characters of the RX buffer.
             - *timeout* specifies the time to wait for the first character (in ms).
             - *timeout_char* specifies the time to wait between characters (in ms).
             - *invert* specifies which lines to invert.
        
                 - ``0`` will not invert lines (idle state of both lines is logic high).
                 - ``UART.INV_TX`` will invert TX line (idle state of TX line now logic low).
                 - ``UART.INV_RX`` will invert RX line (idle state of RX line now logic low).
                 - ``UART.INV_TX | UART.INV_RX`` will invert both lines (idle state at logic low).
        
             - *flow* specifies which hardware flow control signals to use. The value
               is a bitmask.
        
                 - ``0`` will ignore hardware flow control signals.
                 - ``UART.RTS`` will enable receive flow control by using the RTS output pin to
                   signal if the receive FIFO has sufficient space to accept more data.
                 - ``UART.CTS`` will enable transmit flow control by pausing transmission when the
                   CTS input pin signals that the receiver is running low on buffer space.
                 - ``UART.RTS | UART.CTS`` will enable both, for full hardware flow control.
        
           .. note::
             It is possible to call ``init()`` multiple times on the same object in
             order to reconfigure  UART on the fly. That allows using single UART
             peripheral to serve different devices attached to different GPIO pins.
             Only one device can be served at a time in that case.
             Also do not call ``deinit()`` as it will prevent calling ``init()``
             again.
        """
        ...
    def deinit(self) -> None:
        """
           Turn off the UART bus.
        
           .. note::
             You will not be able to call ``init()`` on the object after ``deinit()``.
             A new instance needs to be created in that case.
        """
        ...
    def any(self) -> int:
        """
           Returns an integer counting the number of characters that can be read without
           blocking.  It will return 0 if there are no characters available and a positive
           number if there are characters.  The method may return 1 even if there is more
           than one character available for reading.
        
           For more sophisticated querying of available characters use select.poll::
        
            poll = select.poll()
            poll.register(uart, select.POLLIN)
            poll.poll(timeout)
        """
        ...
    def read(self, nbytes: Optional[Any]=None) -> bytes:
        """
           Read characters.  If ``nbytes`` is specified then read at most that many bytes,
           otherwise read as much data as possible.
        
           Return value: a bytes object containing the bytes read in.  Returns ``None``
           on timeout.
        """
        ...
    def readinto(self, buf, nbytes: Optional[Any]=None) -> Union[int,None]:
        """
           Read bytes into the ``buf``.  If ``nbytes`` is specified then read at most
           that many bytes.  Otherwise, read at most ``len(buf)`` bytes.
        
           Return value: number of bytes read and stored into ``buf`` or ``None`` on
           timeout.
        """
        ...
    def readline(self) -> Union[str,None]:
        """
           Read a line, ending in a newline character.
        
           Return value: the line read or ``None`` on timeout.
        """
        ...
    def write(self, buf) -> Union[int,None]:
        """
           Write the buffer of bytes to the bus.
        
           Return value: number of bytes written or ``None`` on timeout.
        """
        ...
    def sendbreak(self) -> None:
        """
           Send a break condition on the bus. This drives the bus low for a duration
           longer than required for a normal transmission of a character.
        """
        ...
    def flush(self) -> Incomplete:
        """
           Waits until all data has been sent. In case of a timeout, an exception is raised. The timeout
           duration depends on the tx buffer size and the baud rate. Unless flow control is enabled, a timeout
           should not occur.
        
           .. note::
        
               For the rp2, esp8266 and nrf ports the call returns while the last byte is sent.
               If required, a one character wait time has to be added in the calling script.
        
           Availability: rp2, esp32, esp8266, mimxrt, cc3200, stm32, nrf ports, renesas-ra
        """
        ...
    def txdone(self) -> bool:
        """
           Tells whether all data has been sent or no data transfer is happening. In this case,
           it returns ``True``. If a data transmission is ongoing it returns ``False``.
        
           .. note::
        
               For the rp2, esp8266 and nrf ports the call may return ``True`` even if the last byte
               of a transfer is still being sent. If required, a one character wait time has to be
               added in the calling script.
        
           Availability: rp2, esp32, esp8266, mimxrt, cc3200, stm32, nrf ports, renesas-ra
        """
        ...
class SPI():
    """
       Construct an SPI object on the given bus, *id*. Values of *id* depend
       on a particular port and its hardware. Values 0, 1, etc. are commonly used
       to select hardware SPI block #0, #1, etc.
    
       With no additional parameters, the SPI object is created but not
       initialised (it has the settings from the last initialisation of
       the bus, if any).  If extra arguments are given, the bus is initialised.
       See ``init`` for parameters of initialisation.
    """
    CONTROLLER: Incomplete
    """for initialising the SPI bus to controller; this is only used for the WiPy"""
    MSB: Incomplete
    """set the first bit to be the most significant bit"""
    LSB: Incomplete
    """set the first bit to be the least significant bit"""
    def __init__(self, id, *args, **kwargs) -> None:
        ...
    def init(self, baudrate=1000000, *, polarity=0, phase=0, bits=8, firstbit=MSB, sck=None, mosi=None, miso=None, pins:Optional[Tuple]) -> None:
        """
           Initialise the SPI bus with the given parameters:
        
             - ``baudrate`` is the SCK clock rate.
             - ``polarity`` can be 0 or 1, and is the level the idle clock line sits at.
             - ``phase`` can be 0 or 1 to sample data on the first or second clock edge
               respectively.
             - ``bits`` is the width in bits of each transfer. Only 8 is guaranteed to be supported by all hardware.
             - ``firstbit`` can be ``SPI.MSB`` or ``SPI.LSB``.
             - ``sck``, ``mosi``, ``miso`` are pins (machine.Pin) objects to use for bus signals. For most
               hardware SPI blocks (as selected by ``id`` parameter to the constructor), pins are fixed
               and cannot be changed. In some cases, hardware blocks allow 2-3 alternative pin sets for
               a hardware SPI block. Arbitrary pin assignments are possible only for a bitbanging SPI driver
               (``id`` = -1).
             - ``pins`` - WiPy port doesn't ``sck``, ``mosi``, ``miso`` arguments, and instead allows to
               specify them as a tuple of ``pins`` parameter.
        
           In the case of hardware SPI the actual clock frequency may be lower than the
           requested baudrate. This is dependent on the platform hardware. The actual
           rate may be determined by printing the SPI object.
        """
        ...
    def deinit(self) -> None:
        """
           Turn off the SPI bus.
        """
        ...
    def read(self, nbytes, write=0x00) -> bytes:
        """
            Read a number of bytes specified by ``nbytes`` while continuously writing
            the single byte given by ``write``.
            Returns a ``bytes`` object with the data that was read.
        """
        ...
    def readinto(self, buf, write=0x00) -> None:
        """
            Read into the buffer specified by ``buf`` while continuously writing the
            single byte given by ``write``.
            Returns ``None``.
        """
        ...
    def write(self, buf) -> None:
        """
            Write the bytes contained in ``buf``.
            Returns ``None``.
        """
        ...
    def write_readinto(self, write_buf, read_buf) -> None:
        """
            Write the bytes from ``write_buf`` while reading into ``read_buf``.  The
            buffers can be the same or different, but both buffers must have the
            same length.
            Returns ``None``.
        """
        ...
class SoftSPI(SPI):
    """
       Construct a new software SPI object.  Additional parameters must be
       given, usually at least *sck*, *mosi* and *miso*, and these are used
       to initialise the bus.  See `SPI.init` for a description of the parameters.
    """
    MSB: Incomplete
    """set the first bit to be the most significant bit"""
    LSB: Incomplete
    """set the first bit to be the least significant bit"""
    def __init__(self, baudrate=500000, *, polarity=0, phase=0, bits=8, firstbit=MSB, sck=None, mosi=None, miso=None) -> None:
        ...
class I2C():
    """
       Construct and return a new I2C object using the following parameters:
    
          - *id* identifies a particular I2C peripheral.  Allowed values for
            depend on the particular port/board
          - *scl* should be a pin object specifying the pin to use for SCL.
          - *sda* should be a pin object specifying the pin to use for SDA.
          - *freq* should be an integer which sets the maximum frequency
            for SCL.
          - *timeout* is the maximum time in microseconds to allow for I2C
            transactions.  This parameter is not allowed on some ports.
    
       Note that some ports/boards will have default values of *scl* and *sda*
       that can be changed in this constructor.  Others will have fixed values
       of *scl* and *sda* that cannot be changed.
    """
    def __init__(self, id:Union[int,str]=-1, *, scl:Optional[Union[Pin,str]]=None, sda:Optional[Union[Pin,str]]=None, freq=400_000, timeout=50000) -> None:
        ...
    def init(self, scl, sda, *, freq=400000) -> None:
        """
          Initialise the I2C bus with the given arguments:
        
             - *scl* is a pin object for the SCL line
             - *sda* is a pin object for the SDA line
             - *freq* is the SCL clock rate
        
           In the case of hardware I2C the actual clock frequency may be lower than the
           requested frequency. This is dependent on the platform hardware. The actual
           rate may be determined by printing the I2C object.
        """
        ...
    def scan(self) -> List:
        """
           Scan all I2C addresses between 0x08 and 0x77 inclusive and return a list of
           those that respond.  A device responds if it pulls the SDA line low after
           its address (including a write bit) is sent on the bus.
        """
        ...
    def start(self) -> None:
        """
           Generate a START condition on the bus (SDA transitions to low while SCL is high).
        """
        ...
    def stop(self) -> None:
        """
           Generate a STOP condition on the bus (SDA transitions to high while SCL is high).
        """
        ...
    def readinto(self, buf, nack=True, ) -> Incomplete:
        """
           Reads bytes from the bus and stores them into *buf*.  The number of bytes
           read is the length of *buf*.  An ACK will be sent on the bus after
           receiving all but the last byte.  After the last byte is received, if *nack*
           is true then a NACK will be sent, otherwise an ACK will be sent (and in this
           case the peripheral assumes more bytes are going to be read in a later call).
        """
        ...
    def write(self, buf) -> int:
        """
           Write the bytes from *buf* to the bus.  Checks that an ACK is received
           after each byte and stops transmitting the remaining bytes if a NACK is
           received.  The function returns the number of ACKs that were received.
        """
        ...
    def readfrom(self, addr, nbytes, stop=True, ) -> bytes:
        """
           Read *nbytes* from the peripheral specified by *addr*.
           If *stop* is true then a STOP condition is generated at the end of the transfer.
           Returns a `bytes` object with the data read.
        """
        ...
    def readfrom_into(self, addr, buf, stop=True, ) -> None:
        """
           Read into *buf* from the peripheral specified by *addr*.
           The number of bytes read will be the length of *buf*.
           If *stop* is true then a STOP condition is generated at the end of the transfer.
        
           The method returns ``None``.
        """
        ...
    def writeto(self, addr, buf, stop=True, ) -> int:
        """
           Write the bytes from *buf* to the peripheral specified by *addr*.  If a
           NACK is received following the write of a byte from *buf* then the
           remaining bytes are not sent.  If *stop* is true then a STOP condition is
           generated at the end of the transfer, even if a NACK is received.
           The function returns the number of ACKs that were received.
        """
        ...
    def writevto(self, addr, vector, stop=True, ) -> int:
        """
           Write the bytes contained in *vector* to the peripheral specified by *addr*.
           *vector* should be a tuple or list of objects with the buffer protocol.
           The *addr* is sent once and then the bytes from each object in *vector*
           are written out sequentially.  The objects in *vector* may be zero bytes
           in length in which case they don't contribute to the output.
        
           If a NACK is received following the write of a byte from one of the
           objects in *vector* then the remaining bytes, and any remaining objects,
           are not sent.  If *stop* is true then a STOP condition is generated at
           the end of the transfer, even if a NACK is received.  The function
           returns the number of ACKs that were received.
        """
        ...
    def readfrom_mem(self, addr, memaddr, nbytes, *, addrsize=8) -> bytes:
        """
           Read *nbytes* from the peripheral specified by *addr* starting from the memory
           address specified by *memaddr*.
           The argument *addrsize* specifies the address size in bits.
           Returns a `bytes` object with the data read.
        """
        ...
    def readfrom_mem_into(self, addr, memaddr, buf, *, addrsize=8) -> None:
        """
           Read into *buf* from the peripheral specified by *addr* starting from the
           memory address specified by *memaddr*.  The number of bytes read is the
           length of *buf*.
           The argument *addrsize* specifies the address size in bits.
        
           The method returns ``None``.
        """
        ...
    def writeto_mem(self, addr, memaddr, buf, *, addrsize=8) -> None:
        """
           Write *buf* to the peripheral specified by *addr* starting from the
           memory address specified by *memaddr*.
           The argument *addrsize* specifies the address size in bits.
        
           The method returns ``None``.
        """
        ...
class SoftI2C(I2C):
    """
       Construct a new software I2C object.  The parameters are:
    
          - *scl* should be a pin object specifying the pin to use for SCL.
          - *sda* should be a pin object specifying the pin to use for SDA.
          - *freq* should be an integer which sets the maximum frequency
            for SCL.
          - *timeout* is the maximum time in microseconds to wait for clock
            stretching (SCL held low by another device on the bus), after
            which an ``OSError(ETIMEDOUT)`` exception is raised.
    """
    def __init__(self, scl, sda, *, freq=400000, timeout=50000) -> None:
        ...
class I2S():
    """
       Construct an I2S object of the given id:
    
       - ``id`` identifies a particular I2S bus; it is board and port specific
    
       Keyword-only parameters that are supported on all ports:
    
         - ``sck`` is a pin object for the serial clock line
         - ``ws`` is a pin object for the word select line
         - ``sd`` is a pin object for the serial data line
         - ``mck`` is a pin object for the master clock line;
           master clock frequency is sampling rate * 256
         - ``mode`` specifies receive or transmit
         - ``bits`` specifies sample size (bits), 16 or 32
         - ``format`` specifies channel format, STEREO or MONO
         - ``rate`` specifies audio sampling rate (Hz);
           this is the frequency of the ``ws`` signal
         - ``ibuf`` specifies internal buffer length (bytes)
    
       For all ports, DMA runs continuously in the background and allows user applications to perform other operations while
       sample data is transferred between the internal buffer and the I2S peripheral unit.
       Increasing the size of the internal buffer has the potential to increase the time that user applications can perform non-I2S operations
       before underflow (e.g. ``write`` method) or overflow (e.g. ``readinto`` method).
    """
    RX: Incomplete
    """for initialising the I2S bus ``mode`` to receive"""
    TX: Incomplete
    """for initialising the I2S bus ``mode`` to transmit"""
    STEREO: Incomplete
    """for initialising the I2S bus ``format`` to stereo"""
    MONO: Incomplete
    """for initialising the I2S bus ``format`` to mono"""
    def __init__(self, id, *, sck, ws, sd, mck=None, mode, bits, format, rate, ibuf) -> None:
        ...
    def init(self, sck, *args, **kwargs) -> Incomplete:
        """
          see Constructor for argument descriptions
        """
        ...
    def deinit(self) -> Incomplete:
        """
          Deinitialize the I2S bus
        """
        ...
    def readinto(self, buf) -> int:
        """
          Read audio samples into the buffer specified by ``buf``.  ``buf`` must support the buffer protocol, such as bytearray or array.
          "buf" byte ordering is little-endian.  For Stereo format, left channel sample precedes right channel sample. For Mono format,
          the left channel sample data is used.
          Returns number of bytes read
        """
        ...
    def write(self, buf) -> int:
        """
          Write audio samples contained in ``buf``. ``buf`` must support the buffer protocol, such as bytearray or array.
          "buf" byte ordering is little-endian.  For Stereo format, left channel sample precedes right channel sample. For Mono format,
          the sample data is written to both the right and left channels.
          Returns number of bytes written
        """
        ...
    def irq(self, handler) -> Incomplete:
        """
          Set a callback. ``handler`` is called when ``buf`` is emptied (``write`` method) or becomes full (``readinto`` method).
          Setting a callback changes the ``write`` and ``readinto`` methods to non-blocking operation.
          ``handler`` is called in the context of the MicroPython scheduler.
        """
        ...
    @staticmethod
    def shift(*, buf, bits, shift) -> Incomplete:
        """
          bitwise shift of all samples contained in ``buf``. ``bits`` specifies sample size in bits. ``shift`` specifies the number of bits to shift each sample.
          Positive for left shift, negative for right shift.
          Typically used for volume control.  Each bit shift changes sample volume by 6dB.
        """
        ...
class RTC():
    """
       Create an RTC object. See init for parameters of initialization.
    """
    ALARM0: Incomplete
    """irq trigger source"""
    def __init__(self, id=0, *args, **kwargs) -> None:
        ...
    def datetime(self, datetimetuple: Optional[Any]=None) -> Tuple:
        """
           Get or set the date and time of the RTC.
        
           With no arguments, this method returns an 8-tuple with the current
           date and time.  With 1 argument (being an 8-tuple) it sets the date
           and time.
        
           The 8-tuple has the following format:
        
               (year, month, day, weekday, hours, minutes, seconds, subseconds)
        
           The meaning of the ``subseconds`` field is hardware dependent.
        """
        ...
    def init(self, datetime) -> None:
        """
           Initialise the RTC. Datetime is a tuple of the form:
        
              ``(year, month, day[, hour[, minute[, second[, microsecond[, tzinfo]]]]])``
        """
        ...
    def now(self) -> Tuple:
        """
           Get get the current datetime tuple.
        """
        ...
    def deinit(self) -> None:
        """
           Resets the RTC to the time of January 1, 2015 and starts running it again.
        """
        ...
    def alarm(self, id, time, *, repeat=False) -> None:
        """
           Set the RTC alarm. Time might be either a millisecond value to program the alarm to
           current time + time_in_ms in the future, or a datetimetuple. If the time passed is in
           milliseconds, repeat can be set to ``True`` to make the alarm periodic.
        """
        ...
    def alarm_left(self, alarm_id=0) -> int:
        """
           Get the number of milliseconds left before the alarm expires.
        """
        ...
    def cancel(self, alarm_id=0) -> None:
        """
           Cancel a running alarm.
        """
        ...
    def irq(self, *, trigger, handler=None, wake=IDLE) -> Incomplete:
        """
           Create an irq object triggered by a real time clock alarm.
        
              - ``trigger`` must be ``RTC.ALARM0``
              - ``handler`` is the function to be called when the callback is triggered.
              - ``wake`` specifies the sleep mode from where this interrupt can wake
                up the system.
        """
        ...
    def memory(self, data: Optional[Any]=None) -> bytes:
        """
           ``RTC.memory(data)`` will write *data* to the RTC memory, where *data* is any
           object which supports the buffer protocol (including `bytes`, `bytearray`,
           `memoryview` and `array.array`). ``RTC.memory()`` reads RTC memory and returns
           a `bytes` object.
        
           Data written to RTC user memory is persistent across restarts, including
           `machine.soft_reset()` and `machine.deepsleep()`.
        
           The maximum length of RTC user memory is 2048 bytes by default on esp32,
           and 492 bytes on esp8266.
        
           Availability: esp32, esp8266 ports.
        """
        ...
class Timer():
    """
       Construct a new timer object of the given ``id``. ``id`` of -1 constructs a
       virtual timer (if supported by a board).
       ``id`` shall not be passed as a keyword argument.
    
       See ``init`` for parameters of initialisation.
    """
    ONE_SHOT: Incomplete
    """Timer operating mode."""
    PERIODIC: Incomplete
    """Timer operating mode."""
    def __init__(self, id=-1, *args, **kwargs) -> None:
        ...
    def init(self, *, mode=PERIODIC, freq=-1, period=-1, callback=None) -> None:
        """
           Initialise the timer. Example::
        
               def mycallback(t):
                   pass
        
               # periodic at 1kHz
               tim.init(mode=Timer.PERIODIC, freq=1000, callback=mycallback)
        
               # periodic with 100ms period
               tim.init(period=100, callback=mycallback)
        
               # one shot firing after 1000ms
               tim.init(mode=Timer.ONE_SHOT, period=1000, callback=mycallback)
        
           Keyword arguments:
        
             - ``mode`` can be one of:
        
               - ``Timer.ONE_SHOT`` - The timer runs once until the configured
                 period of the channel expires.
               - ``Timer.PERIODIC`` - The timer runs periodically at the configured
                 frequency of the channel.
        
             - ``freq`` - The timer frequency, in units of Hz.  The upper bound of
               the frequency is dependent on the port.  When both the ``freq`` and
               ``period`` arguments are given, ``freq`` has a higher priority and
               ``period`` is ignored.
        
             - ``period`` - The timer period, in milliseconds.
        
             - ``callback`` - The callable to call upon expiration of the timer period.
               The callback must take one argument, which is passed the Timer object.
               The ``callback`` argument shall be specified. Otherwise an exception
               will occur upon timer expiration:
               ``TypeError: 'NoneType' object isn't callable``
        """
        ...
    def deinit(self) -> None:
        """
           Deinitialises the timer. Stops the timer, and disables the timer peripheral.
        """
        ...
class WDT():
    """
       Create a WDT object and start it. The timeout must be given in milliseconds.
       Once it is running the timeout cannot be changed and the WDT cannot be stopped either.
    
       Notes: On the esp8266 a timeout cannot be specified, it is determined by the underlying system.
       On rp2040 devices, the maximum timeout is 8388 ms.
    """
    def __init__(self, id=0, timeout=5000) -> None:
        ...
    def feed(self) -> None:
        """
           Feed the WDT to prevent it from resetting the system. The application
           should place this call in a sensible place ensuring that the WDT is
           only fed after verifying that everything is functioning correctly.
        """
        ...
def reset() -> NoReturn:
    """
       以类似于按外部RESET按钮的方式重置设备。
    """
    ...
def soft_reset() -> NoReturn:
    """
       执行解释器的软重置，删除所有 Python 对象并重置 Python 堆。它尝试保留用户连接到 MicroPython REPL 的方法（例如串行、USB、Wifi）。
    """
    ...
def reset_cause() -> int:
    """
       获取重置原因。参见 :ref:`constants <machine_constants>` 以获取可能的返回值。
    """
    ...
def bootloader(value: Optional[Any]=None) -> None:
    """
       重置设备并进入其引导加载程序。通常用于将设备置于可编程新固件状态。
    
       一些移植版本支持传入一个可选的 *value* 参数，该参数可以控制要进入的引导加载程序、要传递给它的内容或其他事项。
    """
    ...
def disable_irq() -> Incomplete:
    """
       禁用中断请求。返回先前的 IRQ 状态，应将此返回值视为不透明值。此返回值应传递给 `enable_irq()` 函数以将中断恢复到调用 `disable_irq()` 之前的原始状态。
    """
    ...
def enable_irq(state) -> Incomplete:
    """
       重新启用中断请求。*state* 参数应是从最近调用 `disable_irq()` 函数返回的值。
    """
    ...
def freq(hz: Optional[Any]=None) -> Incomplete:
    """
        返回以赫兹为单位的CPU频率。
    
        在某些移植版本上，这也可以用于通过传入 *hz* 来设置 CPU 的频率。
    """
    ...
def idle() -> Incomplete:
    """
       门控 CPU 的时钟，可在短时间或长时间内降低功耗。外围设备继续工作，并在触发任何中断时恢复执行（在许多移植版本上，包括以毫秒为单位的定期发生的系统定时器中断）。
    """
    ...
def sleep() -> Incomplete:
    """
       ``Note:`` 此函数已弃用，请改用无参数的 `lightsleep()`。
    """
    ...
def lightsleep(time_ms: Optional[Any]=None) -> Incomplete:
    """
       停止执行以尝试进入低功耗状态。
    
       如果指定了 *time_ms*，则此值将是睡眠的最长时间（以毫秒为单位）。否则，睡眠可能持续无限期。
    
       无论是否设置了超时，如果有需要处理的事件，执行都可能随时恢复。这些事件或唤醒源应在睡眠前配置，如 `Pin` 变化或 `RTC` 超时。
    
       lightsleep 和 deepsleep 的精确行为和节能能力高度依赖于底层硬件，但一般属性包括：
    
       * lightsleep 具有完整的 RAM 和状态保留。唤醒时，从请求睡眠的点继续执行，所有子系统都正常工作。
    
       * deepsleep 可能不保留系统的 RAM 或任何其他状态（例如外围设备或网络接口）。唤醒时，从主脚本继续执行，类似于硬重置或上电重置。`reset_cause()` 函数将返回 `machine.DEEPSLEEP`，这可以用于区分深睡唤醒和其他重置。
    """
    ...
def deepsleep(time_ms: Optional[Any]=None) -> NoReturn:
    """
       停止执行以尝试进入低功耗状态。
    
       如果指定了 *time_ms*，则此值将是睡眠的最长时间（以毫秒为单位）。否则，睡眠可能持续无限期。
    
       无论是否设置了超时，如果有需要处理的事件，执行都可能随时恢复。这些事件或唤醒源应在睡眠前配置，如 `Pin` 变化或 `RTC` 超时。
    
       lightsleep 和 deepsleep 的精确行为和节能能力高度依赖于底层硬件，但一般属性包括：
    
       * lightsleep 具有完整的 RAM 和状态保留。唤醒时，从请求睡眠的点继续执行，所有子系统都正常工作。
    
       * deepsleep 可能不保留系统的 RAM 或任何其他状态（例如外围设备或网络接口）。唤醒时，从主脚本继续执行，类似于硬重置或上电重置。`reset_cause()` 函数将返回 `machine.DEEPSLEEP`，这可以用于区分深睡唤醒和其他重置。
    """
    ...
def unique_id() -> bytes:
    """
       返回一个板/SoC 的唯一标识符的字节串。如果底层硬件允许，它将从一个板/SoC 实例变化到另一个实例。硬件的长度可能会有所不同（因此如果您期望一个短 ID，使用完整值的子串）。在某些 MicroPython 移植版本中，ID 对应于网络 MAC 地址。
    """
    ...
def time_pulse_us(pin, pulse_level, timeout_us=1000000, ) -> int:
    """
       计时给定 *pin* 上的脉冲，并以微秒为单位返回脉冲持续时间。*pulse_level* 参数应为 0 以计时低脉冲，或为 1 以计时高脉冲。
    
       如果引脚的当前输入值与 *pulse_level* 不同，函数首先（*）等待引脚输入变为等于 *pulse_level*，然后（**）计时引脚等于 *pulse_level* 的持续时间。如果引脚已经等于 *pulse_level*，则计时立即开始。
    
       如果在等待上述条件（*）时超时，函数将返回 -2；如果在主要测量（**）期间超时，函数将返回 -1。超时对于两种情况是相同的，由 *timeout_us* 给出（以微秒为单位）。
    """
    ...
def bitstream(pin, encoding, timing, data, ) -> Incomplete:
    """
       通过对指定的 *pin* 进行比特振荡来传输 *data*。*encoding* 参数指定了位的编码方式，*timing* 是一个特定于编码的时间规范。
    
       支持的编码有：
    
         - ``0`` 用于 "高低" 脉冲持续时间调制。这将以定时脉冲的方式传输 0 和 1 位，从最高有效位开始。*timing* 必须是一个四元组，以纳秒格式表示 ``(高时间_0, 低时间_0, 高时间_1, 低时间_1)``。例如，``(400, 850, 800, 450)`` 是用于 WS2812 RGB LED 的 800kHz 的时序规范。
    
       时间的准确性因移植版本而异。在 Cortex M0 上，时钟为 48MHz，最好的情况下为 +/- 120ns；然而，在更快的 MCU（ESP8266、ESP32、STM32、Pyboard）上，它将更接近于 +/-30ns。
    
       ``Note:`` 用于控制 WS2812 / NeoPixel 条，请参阅 :mod:`neopixel` 模块以获得更高级的 API。
    """
    ...
