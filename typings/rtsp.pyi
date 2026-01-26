"""
The rtsp module on the OpenMV Cam allows you to stream video from your OpenMV Cam to any
compatible RTSP client (like VLC).
"""

from typing import Tuple
from typing import List
from typing import Optional
from typing import Any
import image

class rtsp_server:
    def __init__(self, network_if, port=554):
        """
        Creates a WiFi rtsp server.
        network_if is the network module interface created from network.LAN(), network.WLAN(), or etc.
        port is the port number to use. The default RTSP port is 554.
        """
        pass
        
        
    def register_setup_cb(self,cb):
        """
        Bind a call back (cb) to be executed when a client sets up a RTSP connection with the rtsp_server.
        Registering a call back is not required for the rtsp_server to work.
        The call back should accept two arguments:
        pathname is the name of the stream resource the client wants. You can ignore this if it’s not
        needed. Otherwise, you can use it to determine what image object to return. By default the
        pathname will be “/”.
        session is random number that will change when a new connection is established. You can use
        session with a dictionary to differentiate different accesses to the same pathname.
        """
        pass
        
        
    def register_play_cb(self,cb):
        """
        Bind a call back (cb) to be executed when a client wants to start streaming.
        Registering a call back is not required for the rtsp_server to work.
        The call back should accept two arguments:
        pathname is the name of the stream resource the client wants. You can ignore this if it’s not
        needed. Otherwise, you can use it to determine what image object to return. By default the
        pathname will be “/”.
        session is random number that will change when a new connection is established. You can use
        session with a dictionary to differentiate different accesses to the same pathname.
        """
        pass
        
        
    def register_pause_cb(self,cb):
        """
        Bind a call back (cb) to be executed when a client wants to pause streaming.
        Registering a call back is not required for the rtsp_server to work.
        NOTE: When you click the pause button on VLC in does not tell the server to pause.
        The call back should accept two arguments:
        pathname is the name of the stream resource the client wants. You can ignore this if it’s not
        needed. Otherwise, you can use it to determine what image object to return. By default the
        pathname will be “/”.
        session is random number that will change when a new connection is established. You can use
        session with a dictionary to differentiate different accesses to the same pathname.
        """
        pass
        
        
    def register_teardown_cb(self,cb):
        """
        Bind a call back (cb) to be executed when a client wants tear down a RTSP connection with the rtsp_server.
        Registering a call back is not required for the rtsp_server to work.
        The call back should accept two arguments:
        pathname is the name of the stream resource the client wants. You can ignore this if it’s not
        needed. Otherwise, you can use it to determine what image object to return. By default the
        pathname will be “/”.
        session is random number that will change when a new connection is established. You can use
        session with a dictionary to differentiate different accesses to the same pathname.
        """
        pass
        
        
    def stream(self,cb,quality=90):
        """
        Starts running the rtsp_server logic and does not return. Make sure to setup everything you
        want to first before calling this method. Once called the rtsp_server will start accepting
        connections and streaming video data.
        cb should be a call back that returns an Image object which the RTSP library will jpeg
        compress and stream to the remote client. You are free to modify a sensor.snapshot() image
        as much as you like before returning the image object to be sent.
        quality is the JPEG compression quality to use while streaming.
        The call back should accept two arguments:
        pathname is the name of the stream resource the client wants. You can ignore this if it’s not
        needed. Otherwise, you can use it to determine what image object to return. By default the
        pathname will be “/”.
        session is random number that will change when a new connection is established. You can use
        session with a dictionary to differentiate different accesses to the same pathname.
        """
        pass
        
        
    
