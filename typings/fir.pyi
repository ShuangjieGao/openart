"""
The fir module is used for controlling the thermal sensors.
Example usage:
"""

from typing import Tuple
from typing import List
from typing import Optional
from typing import Any
import image

FIR_NONE: int
"""
No FIR sensor type.
"""

FIR_SHIELD: int
"""
The OpenMV Cam Thermopile Shield Type (MLX90621).
"""

FIR_MLX90621: int
"""
FIR_MLX90621 FIR sensor.
"""

FIR_MLX90640: int
"""
FIR_MLX90640 FIR sensor.
"""

FIR_MLX90641: int
"""
FIR_MLX90640 FIR sensor.
"""

FIR_AMG8833: int
"""
FIR_AMG8833 FIR sensor.
"""

FIR_LEPTON: int
"""
FIR_LEPTON FIR sensor.
"""

def init(type=-1,refresh: int | None = None,resolution: int | None = None) -> None:
    """
    Initializes an attached thermopile shield using I/O pins P4 and P5 (and P0, P1, P2, P3 for fir.FIR_LEPTON)
    type indicates the type of thermopile shield:
    By default type is -1 which will cause fir.init() to automatically scan and initialize an
    attached thermal sensor based on the I2C address. Note that fir.FIR_MLX90640 and
    fir.FIR_MLX90641 have the same I2C address so you must pass fir.FIR_MLX90641 to type
    to initialize it specifically.
    fir.FIR_LEPTON on the OpenMV Cam Pure Thermal this uses internal I/O pins and does not use P0-P5.
    refresh is the thermopile sensor power-of-2 refresh rate in Hz:
    resolution is the thermopile sensor measurement resolution:
    For the fir.FIR_SHIELD and fir.FIR_MLX90621:
    For the fir.FIR_MLX90640 and fir.FIR_MLX90641:
    For the fir.FIR_AMG8833:
    For the fir.FIR_LEPTON:
    """
    pass
    
    
def deinit() -> None:
    """
    Deinitializes the thermal sensor freeing up resources.
    """
    pass
    
    
def width() -> int:
    """
    Returns the width (horizontal resolution) of the thermal sensor in-use:
    """
    pass
    
    
def height() -> int:
    """
    Returns the height (vertical resolution) of the thermal sensor in-use:
    """
    pass
    
    
def type() -> int:
    """
    Returns the type of the thermal sensor in-use:
    """
    pass
    
    
def refresh() -> int:
    """
    Returns the current refresh rate set during fir.init() call.
    """
    pass
    
    
def resolution() -> int:
    """
    Returns the current resolution set during the fir.init() call.
    """
    pass
    
    
def radiometric() -> bool:
    """
    Returns if the thermal sensor reports accurate temperature readings (True or False). If False
    this means that the thermal sensor reports relative temperature readings based on its ambient
    temperature which may not be very accurate.
    """
    pass
    
    
def register_vsync_cb(cb) -> None:
    """
    For the fir.FIR_LEPTON mode only on the OpenMV Cam Pure Thermal.
    Registers callback cb to be executed (in interrupt context) whenever the FLIR Lepton
    generates a new frame (but, before the frame is received).
    This nomially triggers at 9 Hz.
    cb takes no arguments.
    """
    pass
    
    
def register_frame_cb(cb) -> None:
    """
    For the fir.FIR_LEPTON mode only on the OpenMV Cam Pure Thermal.
    Registers callback cb to be executed (in interrupt context) whenever the FLIR Lepton
    generates a new frame and the frame is ready to be read via fir.read_ir() or fir.snapshot().
    This nomially triggers at 9 Hz.
    cb takes no arguments.
    Use this to get an interrupt to schedule reading a frame later with micropython.schedule().
    """
    pass
    
    
def get_frame_available() -> bool:
    """
    Returns True if a frame is available to read by calling fir.read_ir() or fir.snapshot().
    """
    pass
    
    
def trigger_ffc(timeout=-1) -> None:
    """
    For the fir.FIR_LEPTON mode only.
    Triggers the Flat-Field-Correction process on your FLIR Lepton which calibrates the thermal
    image. This process happens automatically with the sensor. However, you may call this function
    to force the process to happen.
    timeout if not -1 then how many milliseconds to wait for FFC to complete.
    """
    pass
    
    
def read_ta() -> float:
    """
    Returns the ambient temperature (i.e. sensor temperature).
    Example:
    The value returned is a float that represents the temperature in celsius.
    """
    pass
    
    
def read_ir(hmirror=False,vflip=False,transpose=False,timeout=-1):
    """
    Returns a tuple containing the ambient temperature (i.e. sensor temperature),
    the temperature list (width * height), the minimum temperature seen, and
    the maximum temperature seen.
    hmirror if set to True horizontally mirrors the ir array.
    vflip if set to True vertically flips the ir array.
    transpose if set to True transposes the ir array.
    timeout if not -1 then how many milliseconds to wait for the new frame.
    If you want to rotate an image by multiples of 90 degrees pass the following:
    Example:
    The values returned are floats that represent the temperature in celsius.
    """
    pass
    
    
def draw_ir(image: image.Image,ir,x: int | None = None,y: int | None = None,x_scale=1.0,y_scale=1.0,roi: Tuple[int, int, int, int] | None = None,rgb_channel=-1,alpha=128,color_palette=image.PALETTE_RAINBOW,alpha_palette=-1,hint=0,scale=Optional[Tuple[float, float]]) -> None:
    """
    Draws an ir array on image whose top-left corner starts at location x, y. This method
    automatically handles rendering the image passed into the correct pixel format for the destination
    image while also handling clipping seamlessly.
    x_scale controls how much the displayed image is scaled by in the x direction (float). If this
    value is negative the image will be flipped horizontally. Note that if y_scale is not specified
    then it will match x_scale to maintain the aspect ratio.
    y_scale controls how much the displayed image is scaled by in the y direction (float). If this
    value is negative the image will be flipped vertically. Note that if x_scale is not specified
    then it will match x_scale to maintain the aspect ratio.
    roi is the region-of-interest rectangle tuple (x, y, w, h) of the source image to draw. This
    allows you to extract just the pixels in the ROI to scale and draw on the destination image.
    rgb_channel is the RGB channel (0=R, G=1, B=2) to extract from an RGB565 image (if passed)
    and to render onto the destination image. For example, if you pass rgb_channel=1 this will
    extract the green channel of the source RGB565 image and draw that in grayscale on the
    destination image.
    alpha controls how much of the source image to blend into the destination image. A value of
    256 draws an opaque source image while a value lower than 256 produces a blend between the source
    and destination image. 0 results in no modification to the destination image.
    color_palette if not -1 can be image.PALETTE_RAINBOW, image.PALETTE_IRONBOW, or
    a 256 pixel in total RGB565 image to use as a color lookup table on the grayscale value of
    whatever the source image is. This is applied after rgb_channel extraction if used.
    alpha_palette if not -1 can be a 256 pixel in total GRAYSCALE image to use as a alpha
    palette which modulates the alpha value of the source image being drawn at a pixel pixel
    level allowing you to precisely control the alpha value of pixels based on their grayscale value.
    A pixel value of 255 in the alpha lookup table is opaque which anything less than 255 becomes
    more transparent until 0. This is applied after rgb_channel extraction if used.
    hint can be a logical OR of the flags:
    scale is a two value tuple which controls the min and max temperature (in celsius) to scale
    the ir image. By default it’s equal to the image ir min and ir max.
    If x/y are not specified the image will be centered in the field of view. If x_scale/y_scale or
    x_size/y_size are not specified the ir array will be scaled to fit on the image.
    """
    pass
    
    
def snapshot(hmirror=False,vflip=False,transpose=False,x_scale=1.0,y_scale=1.0,roi: Tuple[int, int, int, int] | None = None,rgb_channel=-1,alpha=128,color_palette=image.PALETTE_RAINBOW,alpha_palette=None,hint=0,scale: Tuple[float, float] | None = None,pixformat=image.RGB565,copy_to_fb=False,timeout=-1) -> image.Image:
    """
    Works like sensor.snapshot() and returns an image object that is either
    image.GRAYSCALE (grayscale) or image.RGB565 (color). If copy_to_fb is False then
    the new image is allocated on the MicroPython heap. However, the MicroPython heap is limited
    and may not have space to store the new image if exhausted. Instead, set copy_to_fb to
    True to set the frame buffer to the new image making this function work just like sensor.snapshot().
    hmirror if set to True horizontally mirrors the new image.
    vflip if set to True vertically flips the new image.
    transpose if set to True transposes the new image.
    If you want to rotate an image by multiples of 90 degrees pass the following:
    x_scale controls how much the displayed image is scaled by in the x direction (float). If this
    value is negative the image will be flipped horizontally. Note that if y_scale is not specified
    then it will match x_scale to maintain the aspect ratio.
    y_scale controls how much the displayed image is scaled by in the y direction (float). If this
    value is negative the image will be flipped vertically. Note that if x_scale is not specified
    then it will match x_scale to maintain the aspect ratio.
    roi is the region-of-interest rectangle tuple (x, y, w, h) of the source image to draw. This
    allows you to extract just the pixels in the ROI to scale and draw on the destination image.
    rgb_channel is the RGB channel (0=R, G=1, B=2) to extract from an RGB565 image (if passed)
    and to render onto the destination image. For example, if you pass rgb_channel=1 this will
    extract the green channel of the source RGB565 image and draw that in grayscale on the
    destination image.
    alpha controls how much of the source image to blend into the destination image. A value of
    256 draws an opaque source image while a value lower than 256 produces a blend between the source
    and destination image. 0 results in no modification to the destination image.
    color_palette if not -1 can be image.PALETTE_RAINBOW, image.PALETTE_IRONBOW, or
    a 256 pixel in total RGB565 image to use as a color lookup table on the grayscale value of
    whatever the source image is. This is applied after rgb_channel extraction if used.
    alpha_palette if not -1 can be a 256 pixel in total GRAYSCALE image to use as a alpha
    palette which modulates the alpha value of the source image being drawn at a pixel pixel
    level allowing you to precisely control the alpha value of pixels based on their grayscale value.
    A pixel value of 255 in the alpha lookup table is opaque which anything less than 255 becomes
    more transparent until 0. This is applied after rgb_channel extraction if used.
    hint can be a logical OR of the flags:
    scale is a two value tuple which controls the min and max temperature (in celsius) to scale
    the ir image. By default it’s equal to the image ir min and ir max.
    pixformat if specified controls the final image pixel format.
    timeout if not -1 then how many milliseconds to wait for the new frame.
    Returns an image object.
    """
    pass
    
    
