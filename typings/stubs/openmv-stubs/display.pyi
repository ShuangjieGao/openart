"""
The display module is used for driving SPI LCDs, 24-bit parallel LCDs, MIPI DSI LCDs, HDMI output, and Display Port output.
"""

from typing import Tuple
from typing import List
from typing import Optional
from typing import Any
import image

QVGA: int
"""
320x240 resolution for framesize.
"""

TQVGA: int
"""
240x320 resolution for framesize.
"""

FHVGA: int
"""
480x272 resolution for framesize.
"""

FHVGA2: int
"""
480x128 resolution for framesize.
"""

VGA: int
"""
640x480 resolution for framesize.
"""

THVGA: int
"""
320x480 resolution for framesize.
"""

FWVGA: int
"""
800x480 resolution for framesize.
"""

FWVGA2: int
"""
800x320 resolution for framesize.
"""

TFWVGA: int
"""
480x800 resolution for framesize.
"""

TFWVGA2: int
"""
480x480 resolution for framesize.
"""

SVGA: int
"""
800x600 resolution for framesize.
"""

WSVGA: int
"""
1024x600 resolution for framesize.
"""

XGA: int
"""
1024x768 resolution for framesize.
"""

SXGA: int
"""
1280x1024 resolution for framesize.
"""

SXGA2: int
"""
1280x400 resolution for framesize.
"""

UXGA: int
"""
1600x1200 resolution for framesize.
"""

HD: int
"""
1280x720 resolution for framesize.
"""

FHD: int
"""
1920x1080 resolution for framesize.
"""

class DACBacklight:
    def __init__(self):
        """
        """
        pass
        
        
    def deinit(self) -> None:
        """
        Deinitializes the backlight controller.
        """
        pass
        
        
    def backlight(self,value: int | None = None) -> int:
        """
        Sets the backlight strength from 0-100. Note that a linear voltage on the backlight output
        will not necessary result in a linear brightness change on the screen. Typically there’s
        a small region where the screen brightness will change drastically.
        """
        pass
        
        
    
class PWMBacklight:
    def __init__(self):
        """
        """
        pass
        
        
    def deinit(self) -> None:
        """
        Deinitializes the backlight controller.
        """
        pass
        
        
    def backlight(self,value: int | None = None) -> int:
        """
        Sets the backlight strength from 0-100. Note that a linear pwm duty cycle on the backlight output
        will not necessary result in a linear brightness change on the screen. Typically there’s
        a small region where the screen brightness will change drastically.
        """
        pass
        
        
    
class ST7701:
    def __init__(self):
        """
        """
        pass
        
        
    def init(self,display_controller) -> None:
        """
        Initializes the display using the display controller which must provide display.DSIDisplay.bus_write() and
        display.DSIDisplay.bus_read() methods.
        """
        pass
        
        
    def read_id(self) -> int:
        """
        Returns the display id.
        """
        pass
        
        
    
class DisplayData:
    def __init__(self):
        """
        """
        pass
        
        
    def display_id(self) -> int:
        """
        Returns the external display EDID data as a bytes()
        object. Verifying the EDID headers, checksums, and concatenating all sections into one bytes()
        object is done for you. You may then parse this information by following this guide.
        """
        pass
        
        
    def send_frame(self,dst_addr,src_addr,bytes):
        """
        Sends a packet on the HDMI-CEC bus to dst_addr with source src_addr and data bytes.
        """
        pass
        
        
    def receive_frame(self,dst_addr,timeout=1000):
        """
        Waits timeout milliseconds to receive an HDMI-CEC
        frame for address dst_addr. Returns True if the received frame was for dst_addr and False
        if not. On timeout throws an OSError Exception.
        """
        pass
        
        
    def frame_callback(self,callback,dst_addr):
        """
        Registers a callback which will be called on reception of an
        HDMI-CEC frame. The callback will receive two arguments of the frame src_addr as an int and
        payload as a bytes() object.
        dst_addr sets the filter address to listen to on the CEC bus.
        If you use this method do not call DisplayData.receive_frame() anymore until the callback is
        disabled by passing None as the callback for this method.
        """
        pass
        
        
    
class DSIDisplay:
    def __init__(self):
        """
        """
        pass
        
        
    def deinit(self) -> None:
        """
        Releases the I/O pins and RAM used by the class. This is called automatically on destruction.
        """
        pass
        
        
    def width(self) -> int:
        """
        Returns the width of the screen.
        """
        pass
        
        
    def height(self) -> int:
        """
        Returns the height of the screen.
        """
        pass
        
        
    def refresh(self) -> int:
        """
        Returns the refresh rate.
        """
        pass
        
        
    def write(self,image,x=0,y=0,x_scale=1.0,y_scale=1.0,roi=None,rgb_channel=-1,alpha=256,color_palette=None,alpha_palette=None) -> None:
        """
        Displays an image whose top-left corner starts at location x, y.
        You may also pass a path instead of an image object for this method to automatically load the image
        from disk and draw it in one step. E.g. write("test.jpg").
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
        
        
    def clear(self,display_off=False) -> None:
        """
        Clears the lcd screen to black.
        display_off if True instead turns off the display logic versus clearing the frame LCD
        frame buffer to black. You should also turn off the backlight too after this to ensure the
        screen goes to black as many displays are white when only the backlight is on.
        """
        pass
        
        
    def backlight(self,value: int | None = None) -> int:
        """
        Sets the lcd backlight dimming value. 0 (off) to 100 (on).
        Note that unless you pass DACBacklight or PWMBacklight the backlight will be controlled
        as a GPIO pin and will only go from 0 (off) to !0 (on).
        Pass no arguments to get the state of the backlight value.
        """
        pass
        
        
    def bus_write(self,cmd: int,args=None,dcs=False) -> None:
        """
        Send the DSI Display cmd with args.
        """
        pass
        
        
    def bus_read(self,cmd: int,len: int,args=None,dcs=False) -> bytes:
        """
        Read len using cmd with args from the DSI Display.
        """
        pass
        
        
    
class RGBDisplay:
    def __init__(self):
        """
        """
        pass
        
        
    def deinit(self) -> None:
        """
        Releases the I/O pins and RAM used by the class. This is called automatically on destruction.
        """
        pass
        
        
    def width(self) -> int:
        """
        Returns the width of the screen.
        """
        pass
        
        
    def height(self) -> int:
        """
        Returns the height of the screen.
        """
        pass
        
        
    def refresh(self) -> int:
        """
        Returns the refresh rate.
        """
        pass
        
        
    def write(self,image: image.Image,x=0,y=0,x_scale=1.0,y_scale=1.0,roi=None,rgb_channel=-1,alpha=256,color_palette=None,alpha_palette=None,hint=0) -> None:
        """
        Displays an image whose top-left corner starts at location x, y.
        You may also pass a path instead of an image object for this method to automatically load the image
        from disk and draw it in one step. E.g. write("test.jpg").
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
        
        
    def clear(self,display_off=False) -> None:
        """
        Clears the lcd screen to black.
        display_off if True instead turns off the display logic versus clearing the frame LCD
        frame buffer to black. You should also turn off the backlight too after this to ensure the
        screen goes to black as many displays are white when only the backlight is on.
        """
        pass
        
        
    def backlight(self,value: int | None = None) -> int:
        """
        Sets the lcd backlight dimming value. 0 (off) to 100 (on).
        Note that unless you pass DACBacklight or PWMBacklight the backlight will be controlled
        as a GPIO pin and will only go from 0 (off) to !0 (on).
        Pass no arguments to get the state of the backlight value.
        """
        pass
        
        
    
class SPIDisplay:
    def __init__(self):
        """
        """
        pass
        
        
    def deinit(self) -> None:
        """
        Releases the I/O pins and RAM used by the class. This is called automatically on destruction.
        """
        pass
        
        
    def width(self) -> int:
        """
        Returns the width of the screen.
        """
        pass
        
        
    def height(self) -> int:
        """
        Returns the height of the screen.
        """
        pass
        
        
    def refresh(self) -> int:
        """
        Returns the refresh rate.
        """
        pass
        
        
    def bgr(self) -> bool:
        """
        Returns if the red and blue channels are swapped.
        """
        pass
        
        
    def byte_swap(self) -> bool:
        """
        Returns if the RGB565 pixels are displayed byte reversed.
        """
        pass
        
        
    def triple_buffer(self) -> bool:
        """
        Returns if triple buffering is enabled.
        """
        pass
        
        
    def write(self,image: image.Image,x=0,y=0,x_scale=1.0,y_scale=1.0,roi: Tuple[int, int, int, int] | None = None,rgb_channel=-1,alpha=256,color_palette=None,alpha_palette=None,hint=0):
        """
        Displays an image whose top-left corner starts at location x, y.
        You may also pass a path instead of an image object for this method to automatically load the image
        from disk and draw it in one step. E.g. write("test.jpg").
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
        
        
    def clear(self,display_off=False) -> None:
        """
        Clears the lcd screen to black.
        display_off if True instead turns off the display logic versus clearing the frame LCD
        frame buffer to black. You should also turn off the backlight too after this to ensure the
        screen goes to black as many displays are white when only the backlight is on.
        """
        pass
        
        
    def backlight(self,value: int | None = None) -> int:
        """
        Sets the lcd backlight dimming value. 0 (off) to 100 (on).
        Note that unless you pass DACBacklight or PWMBacklight the backlight will be controlled
        as a GPIO pin and will only go from 0 (off) to !0 (on).
        Pass no arguments to get the state of the backlight value.
        """
        pass
        
        
    def bus_write(self,cmd: int,args=None) -> None:
        """
        Send the SPI Display cmd with args.
        """
        pass
        
        
    
