"""
audio 模块用于从 Arduino Portenta 或 Arduino Nicla 上的麦克风录制音频样本。
"""

from typing import Tuple
from typing import List
from typing import Optional
from typing import Any
import image

def init(channels: int = 2,frequency: int = 16000,gain_db: float = 24,highpass: float = 0.9883,samples: int = -1) -> None:
    """
    初始化音频模块。必须在使用音频模块前先调用。
    channels 指定音频通道的数量。可以是 1 或 2。当使用两个音频通道时，音频样本会交错排列。使用多个通道仅在具有多个麦克风的板上才可实现。
    frequency 是运行的采样频率。以更高的采样频率运行会导致更高的噪声底噪，这意味着每个样本的有效位数会减少。
    gain_db 是要应用的麦克风增益。
    highpass 是根据目标采样频率设置的高通滤波器截止频率。此参数仅适用于 Arduino Portenta H7。
    samples 是每次回调时要积累的样本数。通常根据抽取因子（decimation factor）和通道数量计算。如果设置为 -1，样本数将根据抽取因子和通道数量自动计算。
    """
    pass
    
    
def start_streaming(callback) -> None:
    """
    当根据 audio 模块的设置累积足够的 PCM 样本时，自动永远调用带有一个参数 pcmbuf 的 callback。您可以将 pcmbuf 转换为 ndarray 以使用 numpy 处理音频样本，然后将该 ndarray 传递给 ml.Model 对象进行推理。
    pcmbuf 是一个有符号 16 位音频样本数组，其大小基于抽取因子（decimation factor）和通道数量，或者是 audio.init() 函数中指定的样本数。
    在单通道模式下，音频样本将是 16 位，每个样本填充 16 位数组。
    在双通道模式下，音频样本将是 16 位的每对样本，成对填充 16 位数组。
    """
    pass
    
    
def stop_streaming() -> None:
    """
    停止音频流和回调被调用。
    """
    pass
    
    
