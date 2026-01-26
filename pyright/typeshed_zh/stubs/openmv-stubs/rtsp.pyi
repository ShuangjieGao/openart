"""
OpenMV Cam上的 rtsp 模块允许您将视频从OpenMV Cam流式传输到任何兼容的RTSP客户端（如 VLC）。
"""

from typing import Tuple
from typing import List
from typing import Optional
from typing import Any
import image

class rtsp_server:
    def __init__(self, network_if, port=554):
        """
        创建一个WiFi rtsp 服务器。
        network_if 是从 network.LAN()、network.WLAN() 等创建的网络模块接口。
        port 是要使用的端口号。默认的RTSP端口是554。
        """
        pass
        
        
    def register_setup_cb(self,cb):
        """
        将回调函数（cb）绑定到当客户端与 rtsp_server 建立RTSP连接时执行。
        注册回调函数不是 rtsp_server 工作的必需条件。
        回调函数应该接受两个参数：
        pathname 是客户端想要的流资源的名称。如果不需要，可以忽略这一点。否则，您可以使用它来确定要返回的图像对象。默认情况下，pathname 将为”/”。
        session 是一个随机数，在建立新连接时会更改。您可以将 session 与字典一起使用，以区分对同一 pathname 的不同访问。
        """
        pass
        
        
    def register_play_cb(self,cb):
        """
        将回调函数（cb）绑定到当前客户端想要开始流式传输时执行。
        注册回调函数不是 rtsp_server 工作的必需条件。
        回调函数应该接受两个参数：
        pathname 是客户端想要的流资源的名称。如果不需要，可以忽略这一点。否则，您可以使用它来确定要返回的图像对象。默认情况下，pathname 将为”/”。
        session 是一个随机数，在建立新连接时会更改。您可以将 session 与字典一起使用，以区分对同一 pathname 的不同访问。
        """
        pass
        
        
    def register_pause_cb(self,cb):
        """
        将回调函数（cb）绑定到当客户端想要暂停流式传输时执行。
        注册回调函数不是 rtsp_server 工作的必需条件。
        注意：在 VLC 上单击暂停按钮不会告诉服务器暂停。
        回调函数应该接受两个参数：
        pathname 是客户端想要的流资源的名称。如果不需要，可以忽略这一点。否则，您可以使用它来确定要返回的图像对象。默认情况下，pathname 将为”/”。
        session 是一个随机数，在建立新连接时会更改。您可以将 session 与字典一起使用，以区分对同一 pathname 的不同访问。
        """
        pass
        
        
    def register_teardown_cb(self,cb):
        """
        将回调函数（cb）绑定到当前客户端想要拆除与 rtsp_server 的RTSP连接时执行。
        注册回调函数不是 rtsp_server 工作的必需条件。
        回调函数应该接受两个参数：
        pathname 是客户端想要的流资源的名称。如果不需要，可以忽略这一点。否则，您可以使用它来确定要返回的图像对象。默认情况下，pathname 将为”/”。
        session 是一个随机数，在建立新连接时会更改。您可以将 session 与字典一起使用，以区分对同一 pathname 的不同访问。
        """
        pass
        
        
    def stream(self,cb,quality=90):
        """
        启动 rtsp_server 逻辑并且不返回。在调用此方法之前，请确保首先设置好一切。一旦调用，rtsp_server 将开始接受连接并流式传输视频数据。
        cb 应该是一个回调函数，返回一个 Image 对象，RTSP库将对其进行jpeg压缩并流式传输到远程客户端。您可以在返回图像对象之前自由修改 sensor.snapshot() 图像。
        quality 是在流式传输时使用的JPEG压缩质量。
        回调函数应该接受两个参数：
        pathname 是客户端想要的流资源的名称。如果不需要，可以忽略这一点。否则，您可以使用它来确定要返回的图像对象。默认情况下，pathname 将为”/”。
        session 是一个随机数，在建立新连接时会更改。您可以将 session 与字典一起使用，以区分对同一 pathname 的不同访问。
        """
        pass
        
        
    
