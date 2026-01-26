"""
The mjpeg module is used for mjpeg recording.
"""

from typing import Tuple
from typing import List
from typing import Optional
from typing import Any
import image

class Mjpeg:
    def __init__(self, filename: str, width: int | None = None, height: int | None = None):
        """
        Create a Mjpeg object which you can add frames to. filename is the path to
        save the mjpeg recording to.
        width is automatically set equal to the image sensor horizontal resolution
        unless explicitly overridden.
        height is automatically set equal to the image sensor vertical resolution
        unless explicitly overridden.
        """
        pass
        
        
    def is_closed(self) -> bool:
        """
        Return True if the file was closed. You cannot write more data to a closed file.
        """
        pass
        
        
    def width(self) -> int:
        """
        Returns the width (horizontal resolution) for the mjpeg file.
        """
        pass
        
        
    def height(self) -> int:
        """
        Returns the height (vertical resolution) for the mjpeg file.
        """
        pass
        
        
    def count(self) -> int:
        """
        Returns the number of frames in the mjpeg file.
        """
        pass
        
        
    def size(self) -> int:
        """
        Returns the file size in bytes of the mjpeg so far. This value is updated after adding frames.
        """
        pass
        
        
    def add_frame(self,image: image.Image,roi: Tuple[int, int, int, int] | None = None,rgb_channel=-1,alpha=256,color_palette=None,alpha_palette=None,hint=0,quality=90):
        """
        Add an image to the mjpeg recording. The added image is automatically scaled up/down while
        preserving the aspect-ratio to the resolution specified when the mjpeg file was created.
        image can be any image format. Even PNG images or JPEG images at the wrong resolution.
        This method will automatically decompress, scale/convert, and re-compress images for the file.
        roi is the region-of-interest rectangle tuple (x, y, w, h) of the image. This
        allows you to extract just the pixels in the ROI. By default this is the whole image.
        rgb_channel is the RGB channel (0=R, G=1, B=2) to extract from an RGB565 image (if passed)
        and to render onto the destination. For example, if you pass rgb_channel=1 this will
        extract the green channel of the source RGB565 image and draw that in grayscale on the
        destination.
        alpha controls how much of the source image to blend into the destination. A value of
        256 draws an opaque source image while a value lower than 256 produces a blend between the source
        and destination (which is a black background in this case). 0 results in a black image.
        color_palette if not -1 can be image.PALETTE_RAINBOW, image.PALETTE_IRONBOW, or
        a 256 pixel in total RGB565 image to use as a color lookup table on the grayscale value of
        whatever the source image is. This is applied after rgb_channel extraction if used.
        alpha_palette if not -1 can be a 256 pixel in total GRAYSCALE image to use as a alpha
        palette which modulates the alpha value of the source image being drawn at a pixel pixel
        level allowing you to precisely control the alpha value of pixels based on their grayscale value.
        A pixel value of 255 in the alpha lookup table is opaque which anything less than 255 becomes
        more transparent until 0. This is applied after rgb_channel extraction if used.
        hint can be a logical OR of the flags:
        quality is the compression quality (0-100) (int) to be used for non-JPEG images.
        Returns the object.
        """
        pass
        
        
    def write(self,image: image.Image,quality=90,roi: Tuple[int, int, int, int] | None = None,rgb_channel=-1,alpha=256,color_palette=None,alpha_palette=None,hint=0):
        """
        Alias for Mjpeg.add_frame().
        """
        pass
        
        
    def sync(self):
        """
        Flushes the mjpeg file to disk but keeps the file open for writing more data. You should call
        flush periodically ensure that the file is saved to disk.
        Returns the object.
        """
        pass
        
        
    def close(self):
        """
        Finalizes the mjpeg recording. This method must be called once the recording
        is complete to make the file viewable.
        Returns the object.
        """
        pass
        
        
    
