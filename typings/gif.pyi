"""
The gif module is used for gif recording.
"""

from typing import Tuple
from typing import List
from typing import Optional
from typing import Any
import image

class Gif:
    def __init__(self, filename: str, width: int | None = None, height: int | None = None, color: bool | None = None, loop=True):
        """
        Create a Gif object which you can add frames to. filename is the path to
        save the gif recording to.
        width is automatically set equal to the image sensor horizontal resolution
        unless explicitly overridden.
        height is automatically set equal to the image sensor vertical resolution
        unless explicitly overridden.
        color is automatically set equal to the image sensor color mode
        unless explicitly overridden:
        loop when True results in the gif automatically looping on playback.
        """
        pass
        
        
    def width(self) -> int:
        """
        Returns the width (horizontal resolution) for the gif object.
        """
        pass
        
        
    def height(self) -> int:
        """
        Returns the height (vertical resolution) for the gif object.
        """
        pass
        
        
    def format(self) -> int:
        """
        Returns sensor.RGB565 if color is True or sensor.GRAYSCALE if not.
        """
        pass
        
        
    def size(self) -> int:
        """
        Returns the file size of the gif so far. This value is updated after adding frames.
        """
        pass
        
        
    def loop(self) -> bool:
        """
        Returns if the gif object had loop set in its constructor.
        """
        pass
        
        
    def add_frame(self,image: image.Image,delay=10) -> None:
        """
        Add an image to the gif recording. The image width, height, and color mode,
        must be equal to the same width, height, and color modes used in the constructor
        for the gif.
        delay is the number of centi-seconds to wait before displaying this frame
        after the previous frame (if not the first frame).
        """
        pass
        
        
    def close(self) -> None:
        """
        Finalizes the gif recording. This method must be called once the recording
        is complete to make the file viewable.
        """
        pass
        
        
    
