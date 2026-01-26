"""
The tv module is used for controlling the tv shield.
Example usage:
"""

from typing import Tuple
from typing import List
from typing import Optional
from typing import Any
import image

TV_NONE: int
"""
Returned by tv.type() when the this module is not initialized.
"""

TV_SHIELD: int
"""
Used to initialize the TV module.
"""

def init(type=TV_SHIELD,triple_buffer=False) -> None:
    """
    Initializes an attached tv output module.
    type indicates how the lcd module should be initialized:
    """
    pass
    
    
def deinit() -> None:
    """
    Deinitializes the tv module, internal/external hardware, and I/O pins.
    """
    pass
    
    
def width() -> int:
    """
    Returns 352 pixels. This is the sensor.SIF resolution.
    """
    pass
    
    
def height() -> int:
    """
    Returns 240 pixels. This is the sensor.SIF resolution.
    """
    pass
    
    
def type() -> int:
    """
    Returns the type of the screen that was set during tv.init().
    """
    pass
    
    
def triple_buffer() -> bool:
    """
    Returns if triple buffering is enabled that was set during tv.init().
    """
    pass
    
    
def refresh() -> None:
    """
    Returns 60 Hz.
    """
    pass
    
    
def channel(channel: int | None = None) -> int:
    """
    For the wireless TV shield this sets the broadcast channel between 1-8. If passed without a channel
    argument then this method returns the previously set channel (1-8). Default is channel 8.
    """
    pass
    
    
def display(image: image.Image,x=0,y=0,x_scale=1.0,y_scale=1.0,roi: Tuple[int, int, int, int] | None = None,rgb_channel=-1,alpha=256,color_palette=None,alpha_palette=None,hint=0):
    """
    Displays an image whose top-left corner starts at location x, y.
    x_scale controls how much the displayed image is scaled by in the x direction (float). If this
    value is negative the image will be flipped horizontally. Note that if y_scale is not specified
    then it will match x_scale to maintain the aspect ratio.
    y_scale controls how much the displayed image is scaled by in the y direction (float). If this
    value is negative the image will be flipped vertically. Note that if x_scale is not specified
    then it will match x_scale to maintain the aspect ratio.
    roi is the region-of-interest rectangle tuple (x, y, w, h) of the image to display. This
    allows you to extract just the pixels in the ROI to scale.
    rgb_channel is the RGB channel (0=R, G=1, B=2) to extract from an RGB565 image (if passed)
    and to render on the display. For example, if you pass rgb_channel=1 this will
    extract the green channel of the RGB565 image and display that in grayscale.
    alpha controls how opaque the image is. A value of 256 displays an opaque image while a
    value lower than 256 produces a black transparent image. 0 results in a perfectly black image.
    color_palette if not -1 can be image.PALETTE_RAINBOW, image.PALETTE_IRONBOW, or
    a 256 pixel in total RGB565 image to use as a color lookup table on the grayscale value of
    whatever the input image is. This is applied after rgb_channel extraction if used.
    alpha_palette if not -1 can be a 256 pixel in total GRAYSCALE image to use as a alpha
    palette which modulates the alpha value of the input image being displayed at a pixel pixel
    level allowing you to precisely control the alpha value of pixels based on their grayscale value.
    A pixel value of 255 in the alpha lookup table is opaque which anything less than 255 becomes
    more transparent until 0. This is applied after rgb_channel extraction if used.
    hint can be a logical OR of the flags:
    """
    pass
    
    
