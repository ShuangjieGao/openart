"""
The sensor module is used for taking pictures.
Example usage:
"""

from typing import Tuple
from typing import List
from typing import Optional
from typing import Any
import image

BINARY: int
"""
BINARY (bitmap) pixel format. Each pixel is 1-bit.
This format is usful for mask storage. Can be used with Image() and
sensor.alloc_extra_fb().
"""

GRAYSCALE: int
"""
GRAYSCALE pixel format (Y from YUV422). Each pixel is 8-bits, 1-byte.
All of our computer vision algorithms run faster on grayscale images than
RGB565 images.
"""

RGB565: int
"""
RGB565 pixel format. Each pixel is 16-bits, 2-bytes. 5-bits are used for red,
6-bits are used for green, and 5-bits are used for blue.
All of our computer vision algorithms run slower on RGB565 images than
grayscale images.
"""

BAYER: int
"""
RAW BAYER image pixel format. If you try to make the frame size too big
to fit in the frame buffer your OpenMV Cam will set the pixel format
to BAYER so that you can capture images but only some image processing methods
will be operational.
"""

YUV422: int
"""
A pixel format that is very easy to jpeg compress. Each pixel is stored as a grayscale
8-bit Y value followed by alternating 8-bit U/V color values that are shared between two
Y values (8-bits Y1, 8-bits U, 8-bits Y2, 8-bits V, etc.). Only some image processing
methods work with YUV422.
"""

JPEG: int
"""
JPEG mode. The camera module outputs compressed jpeg images.
Use sensor.set_quality() to control the jpeg quality.
Only works for the OV2640/OV5640 cameras.
"""

OV2640: int
"""
sensor.get_id() returns this for the OV2640 camera.
"""

OV5640: int
"""
sensor.get_id() returns this for the OV5640 camera.
"""

OV7690: int
"""
sensor.get_id() returns this for the OV7690 camera.
"""

OV7725: int
"""
sensor.get_id() returns this for the OV7725 camera.
"""

OV9650: int
"""
sensor.get_id() returns this for the OV9650 camera.
"""

MT9V022: int
"""
sensor.get_id() returns this for the MT9V022 camera.
"""

MT9V024: int
"""
sensor.get_id() returns this for the MT9V024 camera.
"""

MT9V032: int
"""
sensor.get_id() returns this for the MT9V032 camera.
"""

MT9V034: int
"""
sensor.get_id() returns this for the MT9V034 camera.
"""

MT9M114: int
"""
sensor.get_id() returns this for the MT9M114 camera.
"""

LEPTON: int
"""
sensor.get_id() returns this for the LEPTON1/2/3 cameras.
"""

HM01B0: int
"""
sensor.get_id() returns this for the HM01B0 camera.
"""

HM0360: int
"""
sensor.get_id() returns this for the HM01B0 camera.
"""

GC2145: int
"""
sensor.get_id() returns this for the GC2145 camera.
"""

PAG7920: int
"""
sensor.get_id() returns this for the PAG7920 camera.
"""

PAJ6100: int
"""
sensor.get_id() returns this for the PAJ6100 camera.
"""

FROGEYE2020: int
"""
sensor.get_id() returns this for the FROGEYE2020 camera.
"""

QQCIF: int
"""
88x72 resolution for the camera sensor.
"""

QCIF: int
"""
176x144 resolution for the camera sensor.
"""

CIF: int
"""
352x288 resolution for the camera sensor.
"""

QQSIF: int
"""
88x60 resolution for the camera sensor.
"""

QSIF: int
"""
176x120 resolution for the camera sensor.
"""

SIF: int
"""
352x240 resolution for the camera sensor.
"""

QQQQVGA: int
"""
40x30 resolution for the camera sensor.
"""

QQQVGA: int
"""
80x60 resolution for the camera sensor.
"""

QQVGA: int
"""
160x120 resolution for the camera sensor.
"""

QVGA: int
"""
320x240 resolution for the camera sensor.
"""

VGA: int
"""
640x480 resolution for the camera sensor.
"""

HQQQQVGA: int
"""
30x20 resolution for the camera sensor.
"""

HQQQVGA: int
"""
60x40 resolution for the camera sensor.
"""

HQQVGA: int
"""
120x80 resolution for the camera sensor.
"""

HQVGA: int
"""
240x160 resolution for the camera sensor.
"""

HVGA: int
"""
480x320 resolution for the camera sensor.
"""

B64X32: int
"""
64x32 resolution for the camera sensor.
For use with Image.find_displacement() and any other FFT based algorithm.
"""

B64X64: int
"""
64x64 resolution for the camera sensor.
For use with Image.find_displacement() and any other FFT based algorithm.
"""

B128X64: int
"""
128x64 resolution for the camera sensor.
For use with Image.find_displacement() and any other FFT based algorithm.
"""

B128X128: int
"""
128x128 resolution for the camera sensor.
For use with Image.find_displacement() and any other FFT based algorithm.
"""

B160X160: int
"""
160x160 resolution for the HM01B0 camera sensor.
"""

B320X320: int
"""
320x320 resolution for the HM01B0 camera sensor.
"""

LCD: int
"""
128x160 resolution for the camera sensor (for use with the lcd shield).
"""

QQVGA2: int
"""
128x160 resolution for the camera sensor (for use with the lcd shield).
"""

WVGA: int
"""
720x480 resolution for the MT9V034 camera sensor.
"""

WVGA2: int
"""
752x480 resolution for the MT9V034 camera sensor.
"""

SVGA: int
"""
800x600 resolution for the camera sensor.
"""

XGA: int
"""
1024x768 resolution for the camera sensor.
"""

WXGA: int
"""
1280x768 resolution for the MT9M114 camera sensor.
"""

SXGA: int
"""
1280x1024 resolution for the camera sensor. Only works for the OV2640/OV5640 cameras.
"""

SXGAM: int
"""
1280x960 resolution for the MT9M114 camera sensor.
"""

UXGA: int
"""
1600x1200 resolution for the camera sensor. Only works for the OV2640/OV5640 cameras.
"""

HD: int
"""
1280x720 resolution for the camera sensor.
"""

FHD: int
"""
1920x1080 resolution for the camera sensor. Only works for the OV5640 camera.
"""

QHD: int
"""
2560x1440 resolution for the camera sensor. Only works for the OV5640 camera.
"""

QXGA: int
"""
2048x1536 resolution for the camera sensor. Only works for the OV5640 camera.
"""

WQXGA: int
"""
2560x1600 resolution for the camera sensor. Only works for the OV5640 camera.
"""

WQXGA2: int
"""
2592x1944 resolution for the camera sensor. Only works for the OV5640 camera.
"""

IOCTL_SET_READOUT_WINDOW: int
"""
Lets you set the readout window for the OV5640.
"""

IOCTL_GET_READOUT_WINDOW: int
"""
Lets you get the readout window for the OV5640.
"""

IOCTL_SET_TRIGGERED_MODE: int
"""
Lets you set the triggered mode for the MT9V034.
"""

IOCTL_GET_TRIGGERED_MODE: int
"""
Lets you get the triggered mode for the MT9V034.
"""

IOCTL_SET_FOV_WIDE: int
"""
Enable sensor.set_framesize() to optimize for the field-of-view over FPS.
"""

IOCTL_GET_FOV_WIDE: int
"""
Return if sensor.set_framesize() is optimizing for field-of-view over FPS.
"""

IOCTL_TRIGGER_AUTO_FOCUS: int
"""
Used to trigger auto focus for the OV5640 FPC camera module.
"""

IOCTL_PAUSE_AUTO_FOCUS: int
"""
Used to pause auto focus (while running) for the OV5640 FPC camera module.
"""

IOCTL_RESET_AUTO_FOCUS: int
"""
Used to reset auto focus back to the default for the OV5640 FPC camera module.
"""

IOCTL_WAIT_ON_AUTO_FOCUS: int
"""
Used to wait on auto focus to finish after being triggered for the OV5640 FPC camera module.
"""

IOCTL_SET_NIGHT_MODE: int
"""
Used to turn night mode on or off on a sensor. Nightmode reduces the frame rate to increase exposure dynamically.
"""

IOCTL_GET_NIGHT_MODE: int
"""
Gets the current value of if night mode is enabled or disabled for your sensor.
"""

IOCTL_LEPTON_GET_WIDTH: int
"""
Lets you get the FLIR Lepton image resolution width in pixels.
"""

IOCTL_LEPTON_GET_HEIGHT: int
"""
Lets you get the FLIR Lepton image resolution height in pixels.
"""

IOCTL_LEPTON_GET_RADIOMETRY: int
"""
Lets you get the FLIR Lepton type (radiometric or not).
"""

IOCTL_LEPTON_GET_REFRESH: int
"""
Lets you get the FLIR Lepton refresh rate in hertz.
"""

IOCTL_LEPTON_GET_RESOLUTION: int
"""
Lets you get the FLIR Lepton ADC resolution in bits.
"""

IOCTL_LEPTON_RUN_COMMAND: int
"""
Executes a 16-bit command given the FLIR Lepton SDK.
"""

IOCTL_LEPTON_SET_ATTRIBUTE: int
"""
Sets a FLIR Lepton Attribute given the FLIR Lepton SDK.
"""

IOCTL_LEPTON_GET_ATTRIBUTE: int
"""
Gets a FLIR Lepton Attribute given the FLIR Lepton SDK.
"""

IOCTL_LEPTON_GET_FPA_TEMPERATURE: int
"""
Gets the FLIR Lepton FPA temp in celsius.
"""

IOCTL_LEPTON_GET_AUX_TEMPERATURE: int
"""
Gets the FLIR Lepton AUX temp in celsius.
"""

IOCTL_LEPTON_SET_MEASUREMENT_MODE: int
"""
Lets you set the FLIR Lepton driver into a mode where you can get a valid temperature value per pixel. See sensor.ioctl() for more information.
"""

IOCTL_LEPTON_GET_MEASUREMENT_MODE: int
"""
Lets you get if measurement mode is enabled or not for the FLIR Lepton sensor. See sensor.ioctl() for more information.
"""

IOCTL_LEPTON_SET_MEASUREMENT_RANGE: int
"""
Lets you set the temperature range you want to map pixels in the image to when in measurement mode. See sensor.ioctl() for more information.
"""

IOCTL_LEPTON_GET_MEASUREMENT_RANGE: int
"""
Lets you get the temperature range used for measurement mode. See sensor.ioctl() for more information.
"""

IOCTL_HIMAX_MD_ENABLE: int
"""
Lets you control the motion detection interrupt on the HM01B0. See sensor.ioctl() for more information.
"""

IOCTL_HIMAX_MD_CLEAR: int
"""
Lets you control the motion detection interrupt on the HM01B0. See sensor.ioctl() for more information.
"""

IOCTL_HIMAX_MD_WINDOW: int
"""
Lets you control the motion detection interrupt on the HM01B0. See sensor.ioctl() for more information.
"""

IOCTL_HIMAX_MD_THRESHOLD: int
"""
Lets you control the motion detection interrupt on the HM01B0. See sensor.ioctl() for more information.
"""

IOCTL_HIMAX_OSC_ENABLE: int
"""
Lets you control the internal oscillator on the HM01B0. See sensor.ioctl() for more information.
"""

SINGLE_BUFFER: int
"""
Pass to sensor.set_framebuffers() to set single buffer mode (1 buffer).
"""

DOUBLE_BUFFER: int
"""
Pass to sensor.set_framebuffers() to set double buffer mode (2 buffers).
"""

TRIPLE_BUFFER: int
"""
Pass to sensor.set_framebuffers() to set triple buffer mode (3 buffers).
"""

VIDEO_FIFO: int
"""
Pass to sensor.set_framebuffers() to set video FIFO mode (4 buffers).
"""

def reset() -> None:
    """
    Initializes the camera sensor.
    """
    pass
    
    
def sleep(enable: bool) -> None:
    """
    Puts the camera to sleep if enable is True. Otherwise, wakes it back up.
    """
    pass
    
    
def shutdown(enable: bool) -> None:
    """
    Puts the camera into a lower power mode than sleep (but the camera must be reset on being woken up).
    """
    pass
    
    
def flush() -> None:
    """
    Copies whatever was in the frame buffer to the IDE. You should call this
    method to display the last image your OpenMV Cam takes if it’s not running
    a script with an infinite loop. Note that you’ll need to add a delay time
    of about a second after your script finishes for the IDE to grab the image
    from your camera. Otherwise, this method will have no effect.
    """
    pass
    
    
def snapshot() -> image.Image:
    """
    Takes a picture using the camera and returns an image object.
    The OpenMV Cam has two memory areas for images. The classical stack/heap
    area used for normal MicroPython processing can store small images within
    it’s heap. However, the MicroPython heap is only about ~100 KB which is not
    enough to store larger images. So, your OpenMV Cam has a secondary frame
    buffer memory area that stores images taken by sensor.snapshot(). Images
    are stored on the bottom of this memory area. Any memory that’s left
    over is then available for use by the frame buffer stack which your OpenMV
    Cam’s firmware uses to hold large temporary data structures for image
    processing algorithms.
    If you need room to hold multiple frames you may “steal” frame buffer space
    by calling sensor.alloc_extra_fb().
    If sensor.set_auto_rotation() is enabled this method will return a new
    already rotated image object.
    """
    pass
    
    
def skip_frames(n: int | None = None,time: int | None = None) -> None:
    """
    Takes n number of snapshots to let the camera image stabilize after
    changing camera settings. n is passed as normal argument, e.g.
    skip_frames(10) to skip 10 frames. You should call this function after
    changing camera settings.
    Alternatively, you can pass the keyword argument time to skip frames
    for some number of milliseconds, e.g. skip_frames(time = 2000) to skip
    frames for 2000 milliseconds.
    If neither n nor time is specified this method skips frames for
    300 milliseconds.
    If both are specified this method skips n number of frames but will
    timeout after time milliseconds.
    """
    pass
    
    
def width() -> int:
    """
    Returns the sensor resolution width.
    """
    pass
    
    
def height() -> int:
    """
    Returns the sensor resolution height.
    """
    pass
    
    
def get_fb() -> image.Image | None:
    """
    (Get Frame Buffer) Returns the image object returned by a previous call of
    sensor.snapshot(). If sensor.snapshot() had not been called before
    then None is returned.
    """
    pass
    
    
def get_id() -> int:
    """
    Returns the camera module ID.
    """
    pass
    
    
def alloc_extra_fb(width: int,height: int,pixformat: int) -> image.Image:
    """
    Allocates another frame buffer for image storage from the frame buffer stack
    and returns an image object of width, height, and pixformat.
    You may call this function as many times as you like as long as there’s
    memory available to allocate any number of extra frame buffers.
    If pixformat is a number >= 4 then this will allocate a JPEG image. You
    can then do Image.bytearray() to get byte level read/write access to the JPEG image.
    """
    pass
    
    
def dealloc_extra_fb() -> None:
    """
    Deallocates the last previously allocated extra frame buffer. Extra frame
    buffers are stored in a stack like structure.
    """
    pass
    
    
def set_pixformat(pixformat: int) -> None:
    """
    Sets the pixel format for the camera module.
    If you are trying to take JPEG images with the OV2640 or OV5640 camera modules at high
    resolutions you should set the pixformat to sensor.JPEG. You can control the image
    quality then with sensor.set_quality().
    """
    pass
    
    
def get_pixformat() -> int:
    """
    Returns the pixformat for the camera module.
    """
    pass
    
    
def set_framesize(framesize: int) -> None:
    """
    Sets the frame size for the camera module.
    """
    pass
    
    
def get_framesize() -> int:
    """
    Returns the frame size for the camera module.
    """
    pass
    
    
def set_framerate(rate: int) -> None:
    """
    Sets the frame rate in hz for the camera module.
    """
    pass
    
    
def get_framerate() -> int:
    """
    Returns the frame rate in hz for the camera module.
    """
    pass
    
    
def set_windowing(roi: Tuple[int, int] | Tuple[int, int, int, int]) -> None:
    """
    Sets the resolution of the camera to a sub resolution inside of the current
    resolution. For example, setting the resolution to sensor.VGA and then
    the windowing to (120, 140, 200, 200) sets sensor.snapshot() to capture
    the 200x200 center pixels of the VGA resolution outputted by the camera
    sensor. You can use windowing to get custom resolutions. Also, when using
    windowing on a larger resolution you effectively are digital zooming.
    roi is a rect tuple (x, y, w, h). However, you may just pass (w, h) and
    the roi will be centered on the frame. You may also pass roi not in parens.
    This function will automatically handle cropping the passed roi to the framesize.
    """
    pass
    
    
def get_windowing() -> Tuple[int, int, int, int]:
    """
    Returns the roi tuple (x, y, w, h) previously set with sensor.set_windowing().
    """
    pass
    
    
def set_gainceiling(gainceiling: int) -> None:
    """
    Set the camera image gainceiling. 2, 4, 8, 16, 32, 64, or 128.
    """
    pass
    
    
def set_contrast(contrast: int) -> None:
    """
    Set the camera image contrast. -3 to +3.
    """
    pass
    
    
def set_brightness(brightness: int) -> None:
    """
    Set the camera image brightness. -3 to +3.
    """
    pass
    
    
def set_saturation(saturation: int) -> None:
    """
    Set the camera image saturation. -3 to +3.
    """
    pass
    
    
def set_quality(quality: int) -> None:
    """
    Set the camera image JPEG compression quality. 0 - 100.
    """
    pass
    
    
def set_colorbar(enable: bool) -> None:
    """
    Turns color bar mode on (True) or off (False). Defaults to off.
    """
    pass
    
    
def set_auto_gain(enable: bool,gain_db=-1,gain_db_ceiling: int | None = None) -> None:
    """
    enable turns auto gain control on (True) or off (False).
    The camera will startup with auto gain control on.
    If enable is False you may set a fixed gain in decibels with gain_db.
    If enable is True you may set the maximum gain ceiling in decibels with
    gain_db_ceiling for the automatic gain control algorithm.
    """
    pass
    
    
def get_gain_db() -> float:
    """
    Returns the current camera gain value in decibels (float).
    """
    pass
    
    
def set_auto_exposure(enable: bool,exposure_us: int | None = None) -> None:
    """
    enable turns auto exposure control on (True) or off (False).
    The camera will startup with auto exposure control on.
    If enable is False you may set a fixed exposure time in microseconds
    with exposure_us.
    """
    pass
    
    
def get_exposure_us() -> int:
    """
    Returns the current camera exposure value in microseconds (int).
    """
    pass
    
    
def set_auto_whitebal(enable: bool,rgb_gain_db: Tuple[float, float, float] | None = None) -> None:
    """
    enable turns auto white balance on (True) or off (False).
    The camera will startup with auto white balance on.
    If enable is False you may set a fixed gain in decibels for the red, green,
    and blue channels respectively with rgb_gain_db.
    """
    pass
    
    
def get_rgb_gain_db() -> Tuple[float, float, float]:
    """
    Returns a tuple with the current camera red, green, and blue gain values in
    decibels ((float, float, float)).
    """
    pass
    
    
def set_auto_blc(enable: bool,regs: Any | None = None):
    """
    Sets the auto black line calibration (blc) control on the camera.
    enable pass True or False to turn BLC on or off. You typically always want this on.
    regs if disabled then you can manually set the blc register values via the values you
    got previously from get_blc_regs().
    """
    pass
    
    
def get_blc_regs() -> Any:
    """
    Returns the sensor blc registers as an opaque tuple of integers. For use with set_auto_blc.
    """
    pass
    
    
def set_hmirror(enable: bool) -> None:
    """
    Turns horizontal mirror mode on (True) or off (False). Defaults to off.
    """
    pass
    
    
def get_hmirror() -> bool:
    """
    Returns if horizontal mirror mode is enabled.
    """
    pass
    
    
def set_vflip(enable: bool) -> None:
    """
    Turns vertical flip mode on (True) or off (False). Defaults to off.
    """
    pass
    
    
def get_vflip() -> bool:
    """
    Returns if vertical flip mode is enabled.
    """
    pass
    
    
def set_transpose(enable: bool) -> None:
    """
    Turns transpose mode on (True) or off (False). Defaults to off.
    """
    pass
    
    
def get_transpose() -> bool:
    """
    Returns if transpose mode is enabled.
    """
    pass
    
    
def set_auto_rotation(enable: bool) -> None:
    """
    Turns auto rotation mode on (True) or off (False). Defaults to off.
    """
    pass
    
    
def get_auto_rotation() -> bool:
    """
    Returns if auto rotation mode is enabled.
    """
    pass
    
    
def set_framebuffers(count: int) -> None:
    """
    Sets the number of frame buffers used to receive image data. By default your OpenMV Cam will
    automatically try to allocate the maximum number of frame buffers it can possibly allocate
    without using more than 1/2 of the available frame buffer RAM at the time of allocation to
    ensure the best performance. Automatic reallocation of frame buffers occurs whenever you
    call sensor.set_pixformat(), sensor.set_framesize(), and sensor.set_windowing().
    sensor.snapshot() will automatically handle switching active frame buffers in the background.
    From your code’s perspective there is only ever 1 active frame buffer even though there might
    be more than 1 frame buffer on the system and another frame buffer receiving data in the background.
    If count is:
    Regarding the reallocation above, triple buffering is tried first, then double buffering, and if
    these both fail to fit in 1/2 of the available frame buffer RAM then single buffer mode is used.
    You may pass a value of 4 or greater to put the sensor driver into video FIFO mode where received
    images are stored in a frame buffer FIFO with count buffers. This is useful for video recording
    to an SD card which may randomly block your code from writing data when the SD card is performing
    house-keeping tasks like pre-erasing blocks to write data to.
    Fun fact, you can pass a value of 100 or so on OpenMV Cam’s with SDRAM for a huge video fifo. If
    you then call snapshot slower than the camera frame rate (by adding machine.sleep()) you’ll get
    slow-mo effects in OpenMV IDE. However, you will also see the above policy effect of resetting
    the frame buffer on a frame drop to ensure that frames do not get too old. If you want to record
    slow-mo video just record video normally to the SD card and then play the video back on a desktop
    machine slower than it was recorded.
    """
    pass
    
    
def get_framebuffers() -> int:
    """
    Returns the current number of frame buffers allocated.
    """
    pass
    
    
def disable_delays(disable: bool | None = None) -> bool:
    """
    If disable is True then disable all settling time delays in the sensor module.
    Whenever you reset the camera module, change modes, etc. the sensor driver delays to prevent
    you can from calling snapshot to quickly afterwards and receiving corrupt frames from the
    camera module. By disabling delays you can quickly update the camera module settings in bulk
    via multiple function calls before delaying at the end and calling snapshot.
    If this function is called with no arguments it returns if delays are disabled.
    """
    pass
    
    
def disable_full_flush(disable: bool | None = None) -> bool:
    """
    If disable is True then automatic framebuffer flushing mentioned in set_framebuffers
    is disabled. This removes any time limit on frames in the frame buffer fifo. For example, if
    you set the number of frame buffers to 30 and set the frame rate to 30 you can now precisely
    record 1 second of video from the camera without risk of frame loss.
    If this function is called with no arguments it returns if automatic flushing is disabled. By
    default automatic flushing on frame drop is enabled to clear out stale frames.
    """
    pass
    
    
def set_lens_correction(enable: bool,radi: int,coef: int) -> None:
    """
    enable True to enable and False to disable (bool).
    radi integer radius of pixels to correct (int).
    coef power of correction (int).
    """
    pass
    
    
def set_vsync_callback(cb) -> None:
    """
    Registers callback cb to be executed (in interrupt context) whenever the camera module
    generates a new frame (but, before the frame is received).
    cb takes one argument and is passed the current state of the vsync pin after changing.
    """
    pass
    
    
def set_frame_callback(cb) -> None:
    """
    Registers callback cb to be executed (in interrupt context) whenever the camera module
    generates a new frame and the frame is ready to be read via sensor.snapshot().
    cb takes no arguments.
    Use this to get an interrupt to schedule reading a frame later with micropython.schedule().
    """
    pass
    
    
def get_frame_available() -> bool:
    """
    Returns True if a frame is available to read by calling sensor.snapshot().
    """
    pass
    
    
def ioctl(*args,**kwargs) -> Any:
    """
    Executes a sensor specific method:
    """
    pass
    
    
def set_color_palette(palette: int) -> None:
    """
    Sets the color palette to use for FLIR Lepton grayscale to RGB565 conversion.
    """
    pass
    
    
def get_color_palette() -> int:
    """
    Returns the current color palette setting. Defaults to image.PALETTE_RAINBOW.
    """
    pass
    
    
def __write_reg(address: int,value: int) -> None:
    """
    Write value (int) to camera register at address (int).
    """
    pass
    
    
def __read_reg(address: int) -> int:
    """
    Read camera register at address (int).
    """
    pass
    
    
