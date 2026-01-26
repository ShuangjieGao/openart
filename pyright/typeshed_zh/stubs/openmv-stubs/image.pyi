"""
image 模块用于机器视觉。
"""

from typing import Tuple
from typing import List
from typing import Optional
from typing import Any

BINARY: int
"""
二进制（位图）像素格式。每个像素为1位。
"""

GRAYSCALE: int
"""
灰度像素格式。每个像素为8位，即1字节。
"""

RGB565: int
"""
RGB565像素格式。每个像素为16位，即2字节。5位用于红色，6位用于绿色，5位用于蓝色。
"""

BAYER: int
"""
原始BAYER图像像素格式。如果尝试将帧大小设置得太大而无法适应帧缓冲区，则OpenMV Cam将像素格式设置为BAYER，以便您可以捕获图像，但不会进行任何图像处理方法。
"""

YUV422: int
"""
非常容易进行JPEG压缩的像素格式。每个像素都存储为一个灰度8位Y值，后跟交替的8位U/V颜色值，这些值在两个Y值之间共享（8位Y1，8位U，8位Y2，8位V，等等）。只有一些图像处理方法适用于YUV422。
"""

JPEG: int
"""
JPEG图像。
"""

PNG: int
"""
PNG图像。
"""

PALETTE_RAINBOW: int
"""
OpenMV Cam的默认热像仪颜色调色板，使用平滑的颜色轮。
"""

PALETTE_IRONBOW: int
"""
使用非常非线性的颜色调色板使图像看起来像FLIR Lepton热成像。
"""

AREA: int
"""
在缩小图像时使用区域缩放（放大时使用最近邻方法）。
当缩小图像以获得最高的视觉质量时，应使用区域缩放。
"""

BILINEAR: int
"""
在放大图像时使用双线性缩放。这会产生良好质量的缩放图像输出，并且速度较快。
当缩小图像时，此方法会对输入图像进行子采样以生成缩小后的图像。如果速度不是问题，可使用 image.AREA 方法以获得最高质量的缩小效果。
"""

BICUBIC: int
"""
在放大图像时使用双三次插值。这会产生高质量的缩放图像输出，但速度较慢。
当缩小图像时，此方法会对输入图像进行子采样以生成缩小后的图像。如果速度不是问题，可使用 image.AREA 方法以获得最高质量的缩小效果。
"""

VFLIP: int
"""
垂直翻转由 draw_image 绘制的图像。
"""

HMIRROR: int
"""
水平镜像由 draw_image 绘制的图像。
"""

TRANSPOSE: int
"""
转置（交换x/y）由 draw_image 绘制的图像。
"""

CENTER: int
"""
将要绘制的图像居中绘制到其绘制的图像/画布中。传递的任何x/y偏移量将通过该偏移量将要绘制的图像从中心移动。
"""

EXTRACT_RGB_CHANNEL_FIRST: int
"""
使用 draw_image 从RGB图像中提取RGB通道，首先提取通道，然后进行缩放，以避免任何伪影。
"""

APPLY_COLOR_PALETTE_FIRST: int
"""
使用 draw_image 将颜色查找表应用于图像时，首先应用颜色查找表，然后进行缩放，以避免任何伪影。
"""

SCALE_ASPECT_KEEP: int
"""
将绘制的图像缩放以适应绘制的图像/画布，同时保持纵横比。除非图像的纵横比匹配，否则绘制的图像将无法完全覆盖目标图像/画布。传递的任何 x_scale/y_scale 值将进一步缩放已缩放的图像。
"""

SCALE_ASPECT_EXPAND: int
"""
将要绘制的图像缩放以填充绘制的图像/画布，同时保持纵横比。除非图像的纵横比匹配，否则将裁剪绘制的图像。传递的任何x_scale/y_scale值还将缩放缩放后的图像。
"""

SCALE_ASPECT_IGNORE: int
"""
将要绘制的图像缩放以填充绘制的图像/画布。这不会保持绘制的图像的纵横比。传递的任何x_scale/y_scale值还将缩放缩放后的图像。
"""

BLACK_BACKGROUND: int
"""
在黑色目标图像上绘制图像时加快 draw_image 的速度，当使用需要读取源像素和目标像素的alpha效果时，跳过读取目标像素。
"""

ROTATE_90: int
"""
将图像旋转90度（这只是 image.VFLIP 与 image.TRANSPOSE 进行“或”运算）。
"""

ROTATE_180: int
"""
将图像旋转180度（这只是 image.HMIRROR 与 image.VFLIP 进行“或”运算）。
"""

ROTATE_270: int
"""
将图像旋转270度（这只是 image.HMIRROR 与 image.TRANSPOSE 进行“或”运算）。
"""

JPEG_SUBSAMPLING_AUTO: int
"""
根据图像质量参数自动选择最佳的 JPEG 子采样方式。
"""

JPEG_SUBSAMPLING_444: int
"""
使用 4:4:4 JPEG 子采样。
"""

JPEG_SUBSAMPLING_422: int
"""
使用 4:2:2 JPEG 子采样。注意，如果您通过 MJPEG 流式传输视频，为了与第三方视频播放器的最佳兼容性，应该强制将 JPEG 子采样设置为 4:2:2。
"""

JPEG_SUBSAMPLING_420: int
"""
使用 4:2:0 JPEG 子采样。
"""

SEARCH_EX: int
"""
详尽的模板匹配搜索。
"""

SEARCH_DS: int
"""
更快的模板匹配搜索。
"""

EDGE_CANNY: int
"""
使用Canny边缘检测算法进行图像边缘检测。
"""

EDGE_SIMPLE: int
"""
使用简单的阈值高通滤波算法进行图像边缘检测。
"""

CORNER_FAST: int
"""
针对 ORB 关键点的更快、精度更低的角点检测算法。
"""

CORNER_AGAST: int
"""
针对ORB关键点的较慢且准确度较高的角点检测算法。
"""

TAG16H5: int
"""
TAG1H5标签族位掩码枚举。用于AprilTags。
"""

TAG25H7: int
"""
TAG25H7标签族位掩码枚举。用于AprilTags。
"""

TAG25H9: int
"""
TAG25H9标签族位掩码枚举。用于AprilTags。
"""

TAG36H10: int
"""
TAG36H10标签族位掩码枚举。用于AprilTags。
"""

TAG36H11: int
"""
TAG36H11标签族位掩码枚举。用于AprilTags。
"""

ARTOOLKIT: int
"""
ARTOOLKIT标签族位掩码枚举。用于AprilTags。
"""

EAN2: int
"""
EAN2条形码类型枚举。
"""

EAN5: int
"""
EAN5条形码类型枚举。
"""

EAN8: int
"""
EAN8条形码类型枚举。
"""

UPCE: int
"""
UPCE条形码类型枚举。
"""

ISBN10: int
"""
ISBN10条形码类型枚举。
"""

UPCA: int
"""
UPCA条形码类型枚举。
"""

EAN13: int
"""
EAN13条形码类型枚举。
"""

ISBN13: int
"""
ISBN13条形码类型枚举。
"""

I25: int
"""
I25条形码类型枚举。
"""

DATABAR: int
"""
DATABAR条形码类型枚举。
"""

DATABAR_EXP: int
"""
DATABAR_EXP条形码类型枚举。
"""

CODABAR: int
"""
CODABAR条形码类型枚举。
"""

CODE39: int
"""
CODE39条形码类型枚举。
"""

PDF417: int
"""
PDF417条形码类型枚举 - 未来（例如，目前无法正常工作）。
"""

CODE93: int
"""
CODE93条形码类型枚举。
"""

CODE128: int
"""
CODE128条形码类型枚举。
"""

def binary_to_grayscale(binary_image_value: 0 | 1) -> int:
    """
    返回二进制值(0-1)对应的灰度值(0-255)。
    """
    pass
    
    
def binary_to_rgb(binary_image_value: 0 | 1) -> Tuple[int, int, int]:
    """
    返回二进制值(0-1)对应的RGB888格式的元组(r, g, b)。
    """
    pass
    
    
def binary_to_lab(binary_image_value: 0 | 1) -> Tuple[int, int, int]:
    """
    返回二进制值(0-1)对应的LAB格式的元组(l, a, b)。
    L的范围为0到100, A和B的范围为-128到128。
    """
    pass
    
    
def binary_to_yuv(binary_image_value: 0 | 1) -> Tuple[int, int, int]:
    """
    返回二进制值(0-1)对应的YUV格式的元组(y, u, v)。
    Y的范围为0到255, U和V范围为-128到128。
    """
    pass
    
    
def grayscale_to_binary(grayscale_value: int) -> 0 | 1:
    """
    返回灰度值(0-255)对应的二进制值(0-1)。
    """
    pass
    
    
def grayscale_to_rgb(grayscale_value: int) -> Tuple[int, int, int]:
    """
    返回灰度值(0-255)对应的RGB888格式的元组(r, g, b)。
    """
    pass
    
    
def grayscale_to_lab(grayscale_value: int) -> Tuple[int, int, int]:
    """
    返回灰度值(0-255)对应的LAB格式的元组(l, a, b)。
    L的范围为0到100, A和B的范围为-128到128。
    """
    pass
    
    
def grayscale_to_yuv(grayscale_value: int) -> Tuple[int, int, int]:
    """
    返回灰度值(0-255)对应的YUV格式的元组(y, u, v)。
    Y的范围为0到255, U和V范围为-128到128。
    """
    pass
    
    
def rgb_to_binary(rgb_tuple: Tuple[int, int, int]) -> 0 | 1:
    """
    返回RGB888格式的元组(r, g, b)对应的中心范围阈值二进制值(0-1)。
    """
    pass
    
    
def rgb_to_grayscale(rgb_tuple: Tuple[int, int, int]) -> int:
    """
    返回RGB888格式的元组(r, g, b)对应的灰度值(0-255)。
    """
    pass
    
    
def rgb_to_lab(rgb_tuple: Tuple[int, int, int]) -> Tuple[int, int, int]:
    """
    返回RGB888格式的元组(r, g, b)对应的LAB格式的元组(l, a, b)。
    L的范围为0到100, A和B的范围为-128到128。
    """
    pass
    
    
def rgb_to_yuv(rgb_tuple: Tuple[int, int, int]) -> Tuple[int, int, int]:
    """
    返回RGB888格式的元组(r, g, b)对应的YUV格式的元组(y, u, v)。
    Y的范围为0到255, U和V范围为-128到128。
    """
    pass
    
    
def lab_to_binary(lab_tuple: Tuple[int, int, int]) -> 0 | 1:
    """
    返回LAB格式的元组(l, a, b)对应的中心范围阈值二进制值(0-1)。
    """
    pass
    
    
def lab_to_grayscale(lab_tuple: Tuple[int, int, int]) -> int:
    """
    返回LAB格式的元组(l, a, b)对应的灰度值(0-255)。
    """
    pass
    
    
def lab_to_rgb(lab_tuple: Tuple[int, int, int]) -> Tuple[int, int, int]:
    """
    返回LAB格式的元组(l, a, b)对应的RGB888格式的元组(r, g, b)。
    """
    pass
    
    
def lab_to_yuv(lab_tuple: Tuple[int, int, int]) -> Tuple[int, int, int]:
    """
    返回LAB格式的元组(l, a, b)对应的YUV格式的元组(y, u, v)。
    Y的范围为0到255, U和V范围为-128到128。
    """
    pass
    
    
def yuv_to_binary(yuv_tuple: Tuple[int, int, int]) -> 0 | 1:
    """
    返回YUV格式的元组(y, u, v)对应的中心范围阈值二进制值(0-1)。
    """
    pass
    
    
def yuv_to_grayscale(yuv_tuple: Tuple[int, int, int]) -> int:
    """
    返回YUV格式的元组(y, u, v)对应的灰度值(0-255)。
    """
    pass
    
    
def yuv_to_rgb(lab_tuple: Tuple[int, int, int]) -> Tuple[int, int, int]:
    """
    返回YUV格式的元组(y, u, v)对应的RGB888格式的元组(r, g, b)。
    """
    pass
    
    
def yuv_to_lab(yuv_tuple: Tuple[int, int, int]) -> Tuple[int, int, int]:
    """
    返回YUV格式的元组(y, u, v)对应的LAB格式的元组(l, a, b)。
    L的范围为0到100, A和B的范围为-128到128。
    """
    pass
    
    
def load_decriptor(path: str):
    """
    从磁盘上加载一个descriptor对象。
    path 是加载的descriptor的文件路径。
    """
    pass
    
    
def save_descriptor(path: str,descriptor):
    """
    保存描述符对象 descriptor 到磁盘。
    path 是descriptor文件保存的路径。
    """
    pass
    
    
def match_descriptor(descritor0,descriptor1,threshold=70,filter_outliers=False):
    """
    对于LBP描述符来说，这个函数返回的是一个体现两个描述符之间区别的整数。你可以接下来计算阈值或者比较这个距离。这个距离是对相似度的一个度量。这个测度值越接近0，LBPF特征点就越匹配。
    对于ORB描述符来说，这个函数返回的是 kptmatch 对象。以下。
    threshold 是用来为ORB键点过滤不准确的匹配。一个较低的 threshold 值将减少关键点匹配的结果。threshold 值可以为0-100 (int)。默认值为70。
    filter_outliers 用于 ORB 关键点，以过滤异常点关键点，允许您提高 threshold。默认为 False。
    """
    pass
    
    
class HaarCascade:
    def __init__(self, path: str, stages: int | None = None):
        """
        从一个Haar Cascade二进制文件导入到OpenMV的内存中。如果您传递“frontalface”字符串而不是路径，这个构造函数将会把一个内置的正脸的Haar Cascade载入内存。此外，您也可以通过“eye”来把Haar Cascade导入内存。最后，这个方法会返回载入的Haar Cascade对象，用来使用 image.find_features() 。
        stages 默认值为Haar Cascade中的阶段数。然而，您可以指定一个较低的数值来加速运行特征检测器，当然这会带来较高的误报率。
        问：Haar Cascade 是什么？
        A: Haar Cascade 是一系列用于确定图像中是否存在对象的对比检查。对比检查分为几个阶段，其中一个阶段只在前面的阶段已经通过的情况下运行。对比检查是一些简单的东西，比如检查图像的中垂直中心是否比边缘亮。在较早的阶段首先执行大面积检查，然后在后续阶段执行更多的和更小的面积检查。
        Q: 如何制作 Haar Cascade？
        A: 通过针对正负标记图像训练生成器算法来制作 Haar Cascade。例如，您可以针对数百张带有猫的图片进行训练，这些图片被标记为带有猫的图片，并且针对数百张带有不像猫的东西的图片进行标记。然后，生成器算法将生成一个可以检测猫的 Haar Cascade。
        """
        pass
        
        
    
class Similarity:
    def __init__(self):
        """
        请调用 Image. get_similarity() 来创建此对象。
        """
        pass
        
        
    def mean(self) -> float:
        """
        返回在整个图像上计算得出的相似度值的平均值（float）。
        您也可以对该对象执行 [0] 来获取此值。
        """
        pass
        
        
    def stdev(self) -> float:
        """
        返回在整个图像上计算得出的相似度值的标准差（float）。
        您也可以对该对象执行 [1] 来获取此值。
        """
        pass
        
        
    def min(self) -> float:
        """
        返回在整个图像上计算得出的相似度值的最小值（float）。
        通常，对于结构相似性指数（SSIM），你需要对最小值进行阈值处理，以确定两幅图像是否不同。
        您也可以对该对象执行 [2] 来获取此值。
        """
        pass
        
        
    def max(self) -> float:
        """
        返回在整个图像上计算得出的相似度值的最大值（float）。
        通常，对于结构差异性指数（DSIM），你需要对最大值进行阈值处理，以确定两幅图像是否不同。
        您也可以对该对象执行 [3] 来获取此值。
        """
        pass
        
        
    
class histogram:
    def __init__(self):
        """
        请调用 Image.get_histogram() 来创建此对象。
        """
        pass
        
        
    def bins(self) -> List[float]:
        """
        返回灰度直方图的浮点数列表。
        您也可以对该对象执行 [0] 来获取此值。
        """
        pass
        
        
    def l_bins(self) -> List[float]:
        """
        返回 RGB565 直方图的浮点数列表 LAB L 通道。
        您也可以对该对象执行 [0] 来获取此值。
        """
        pass
        
        
    def a_bins(self) -> List[float]:
        """
        返回 RGB565 直方图的浮点数列表 LAB A 通道。
        您也可以对该对象执行 [1] 来获取此值。
        """
        pass
        
        
    def b_bins(self) -> List[float]:
        """
        返回 RGB565 直方图的浮点数列表 LAB B 通道。
        您也可以对该对象执行 [2] 来获取此值。
        """
        pass
        
        
    def get_percentile(self,percentile) -> percentile:
        """
        计算直方图通道的累积分布函数（CDF），并返回一个带有直方图在传入的 percentile （0.0-1.0）（float）处值的 image.percentile 对象。因此，如果您传入 0.1，该方法将告诉您（从直方图的左到右）哪个柱子在加到累加器中时使累加器越过 0.1。这对于确定颜色分布的最小值（使用 0.1）和最大值（使用 0.9）而不会因异常值效果而破坏自适应颜色跟踪结果非常有用。
        """
        pass
        
        
    def get_threshold(self) -> threshold:
        """
        使用 Otsu 方法计算将直方图分成两半的每个通道的最佳阈值值。此方法返回一个 image.threshold 对象。此方法特别适用于确定最佳的 Image.binary() 阈值。
        """
        pass
        
        
    def get_statistics(self) -> statistics:
        """
        计算直方图中每个颜色通道的均值、中位数、模式、标准差、最小值、最大值、下四分位数和上四分位数，并返回一个 statistics 对象。
        您也可以将 histogram.statistics() 和 histogram.get_stats() 用作此方法的别名。
        """
        pass
        
        
    
class percentile:
    def __init__(self):
        """
        请调用 histogram.get_percentile() 来创建此对象。
        """
        pass
        
        
    def value(self) -> int:
        """
        返回灰度百分位数值（介于 0 到 255 之间）。
        您也可以对该对象执行 [0] 来获取此值。
        """
        pass
        
        
    def l_value(self) -> int:
        """
        返回 RGB565 LAB L 通道百分位数值（介于 0 到 100 之间）。
        您也可以对该对象执行 [0] 来获取此值。
        """
        pass
        
        
    def a_value(self) -> int:
        """
        返回 RGB565 LAB A 通道百分位数值（介于 -128 到 127 之间）。
        您也可以对该对象执行 [1] 来获取此值。
        """
        pass
        
        
    def b_value(self) -> int:
        """
        返回 RGB565 LAB B 通道百分位数值（介于 -128 到 127 之间）。
        您也可以对该对象执行 [2] 来获取此值。
        """
        pass
        
        
    
class threshold:
    def __init__(self):
        """
        请调用 histogram.get_threshold() 来创建此对象。
        """
        pass
        
        
    def value(self) -> int:
        """
        返回灰度阈值值（介于 0 到 255 之间）。
        您也可以对该对象执行 [0] 来获取此值。
        """
        pass
        
        
    def l_value(self) -> int:
        """
        返回 RGB565 LAB L 通道阈值值（介于 0 到 100 之间）。
        您也可以对该对象执行 [0] 来获取此值。
        """
        pass
        
        
    def a_value(self) -> int:
        """
        返回 RGB565 LAB A 通道阈值值（介于 -128 到 127 之间）。
        您也可以对该对象执行 [1] 来获取此值。
        """
        pass
        
        
    def b_value(self) -> int:
        """
        返回 RGB565 LAB B 通道阈值值（介于 -128 到 127 之间）。
        您也可以对该对象执行 [2] 来获取此值。
        """
        pass
        
        
    
class statistics:
    def __init__(self):
        """
        请调用 histogram.get_statistics() 或 Image.get_statistics() 来创建此对象。
        """
        pass
        
        
    def mean(self) -> int:
        """
        返回灰度均值(0-255) (int)。
        您也可以对该对象执行 [0] 来获取此值。
        """
        pass
        
        
    def median(self) -> int:
        """
        返回灰度中位数(0-255) (int)。
        您也可以对该对象执行 [1] 来获取此值。
        """
        pass
        
        
    def mode(self) -> int:
        """
        返回灰度模式(0-255) (int)。
        您也可以对该对象执行 [2] 来获取此值。
        """
        pass
        
        
    def stdev(self) -> int:
        """
        返回灰度标准差(0-255) (int)。
        您也可以对该对象执行 [3] 来获取此值。
        """
        pass
        
        
    def min(self) -> int:
        """
        返回灰度最小值(0-255) (int)。
        您也可以对该对象执行 [4] 来获取此值。
        """
        pass
        
        
    def max(self) -> int:
        """
        返回灰度最大值(0-255) (int)。
        您也可以对该对象执行 [5] 来获取此值。
        """
        pass
        
        
    def lq(self) -> int:
        """
        返回灰度下四分位数(0-255) (int)。
        您也可以对该对象执行 [6] 来获取此值。
        """
        pass
        
        
    def uq(self) -> int:
        """
        返回灰度上四分位数(0-255) (int)。
        您也可以对该对象执行 [7] 来获取此值。
        """
        pass
        
        
    def l_mean(self) -> int:
        """
        返回 RGB565 LAB L 均值（0-255）（int）。
        您也可以对该对象执行 [0] 来获取此值。
        """
        pass
        
        
    def l_median(self) -> int:
        """
        返回 RGB565 LAB L 中位数（0-255）（int）。
        您也可以对该对象执行 [1] 来获取此值。
        """
        pass
        
        
    def l_mode(self) -> int:
        """
        返回 RGB565 LAB L 模式（0-255）（int）。
        您也可以对该对象执行 [2] 来获取此值。
        """
        pass
        
        
    def l_stdev(self) -> int:
        """
        返回 RGB565 LAB L 标准差（0-255）（int）。
        您也可以对该对象执行 [3] 来获取此值。
        """
        pass
        
        
    def l_min(self) -> int:
        """
        返回 RGB565 LAB L 最小值（0-255）（int）。
        您也可以对该对象执行 [4] 来获取此值。
        """
        pass
        
        
    def l_max(self) -> int:
        """
        返回 RGB565 LAB L 最大值（0-255）（int）。
        您也可以对该对象执行 [5] 来获取此值。
        """
        pass
        
        
    def l_lq(self) -> int:
        """
        返回 RGB565 LAB L 下四分位数（0-255）（int）。
        您也可以对该对象执行 [6] 来获取此值。
        """
        pass
        
        
    def l_uq(self) -> int:
        """
        返回 RGB565 LAB L 上四分位数（0-255）（int）。
        您也可以对该对象执行 [7] 来获取此值。
        """
        pass
        
        
    def a_mean(self) -> int:
        """
        返回 RGB565 LAB A 均值（0-255）（int）。
        您也可以对该对象执行 [8] 来获取此值。
        """
        pass
        
        
    def a_median(self) -> int:
        """
        返回 RGB565 LAB A 中位数（0-255）（int）。
        您也可以对该对象执行 [9] 来获取此值。
        """
        pass
        
        
    def a_mode(self) -> int:
        """
        返回 RGB565 LAB A 模式（0-255）（int）。
        您也可以对该对象执行 [10] 来获取此值。
        """
        pass
        
        
    def a_stdev(self) -> int:
        """
        返回 RGB565 LAB A 标准差（0-255）（int）。
        您也可以对该对象执行 [11] 来获取此值。
        """
        pass
        
        
    def a_min(self) -> int:
        """
        返回 RGB565 LAB A 最小值（0-255）（int）。
        您也可以对该对象执行 [12] 来获取此值。
        """
        pass
        
        
    def a_max(self) -> int:
        """
        返回 RGB565 LAB A 最大值（0-255）（int）。
        您也可以对该对象执行 [13] 来获取此值。
        """
        pass
        
        
    def a_lq(self) -> int:
        """
        返回 RGB565 LAB A 下四分位数（0-255）（int）。
        您也可以对该对象执行 [14] 来获取此值。
        """
        pass
        
        
    def a_uq(self) -> int:
        """
        返回 RGB565 LAB A 上四分位数（0-255）（int）。
        您也可以对该对象执行 [15] 来获取此值。
        """
        pass
        
        
    def b_mean(self) -> int:
        """
        返回 RGB565 LAB B 均值（0-255）（int）。
        您也可以对该对象执行 [16] 来获取此值。
        """
        pass
        
        
    def b_median(self) -> int:
        """
        返回 RGB565 LAB B 中位数（0-255）（int）。
        您也可以对该对象执行 [17] 来获取此值。
        """
        pass
        
        
    def b_mode(self) -> int:
        """
        返回 RGB565 LAB B 模式（0-255）（int）。
        您也可以对该对象执行 [18] 来获取此值。
        """
        pass
        
        
    def b_stdev(self) -> int:
        """
        返回 RGB565 LAB B 标准差（0-255）（int）。
        您也可以对该对象执行 [19] 来获取此值。
        """
        pass
        
        
    def b_min(self) -> int:
        """
        返回 RGB565 LAB B 最小值（0-255）（int）。
        您也可以对该对象执行 [20] 来获取此值。
        """
        pass
        
        
    def b_max(self) -> int:
        """
        返回 RGB565 LAB B 最大值（0-255）（int）。
        您也可以对该对象执行 [21] 来获取此值。
        """
        pass
        
        
    def b_lq(self) -> int:
        """
        返回 RGB565 LAB B 下四分位数（0-255）（int）。
        您也可以对该对象执行 [22] 来获取此值。
        """
        pass
        
        
    def b_uq(self) -> int:
        """
        返回 RGB565 LAB B 上四分位数（0-255）（int）。
        您也可以对该对象执行 [23] 来获取此值。
        """
        pass
        
        
    
class blob:
    def __init__(self):
        """
        请调用 Image.find_blobs() 来创建此对象。
        """
        pass
        
        
    def corners(self) -> List[Tuple[int, int]]:
        """
        返回对象的 4 个角的 4 个 (x,y) 元组的列表。角始终按顺时针顺序返回，从左上角开始。
        """
        pass
        
        
    def min_corners(self) -> List[Tuple[int, int]]:
        """
        返回对象的最小区域矩形的 4 个角的 4 个 (x,y) 元组的列表。与 blob.corners() 不同，最小区域矩形的角不一定在 blob 上。
        """
        pass
        
        
    def rect(self) -> Tuple[int, int, int, int]:
        """
        返回一个矩形元组 (x, y, w, h)，可用于其他 image 方法，如 Image.draw_rectangle()，表示 blob 的边界框。
        """
        pass
        
        
    def x(self) -> int:
        """
        返回 blob 的边界框 x 坐标（int）。
        您也可以对该对象执行 [0] 来获取此值。
        """
        pass
        
        
    def y(self) -> int:
        """
        返回 blob 的边界框 y 坐标（int）。
        您也可以对该对象执行 [1] 来获取此值。
        """
        pass
        
        
    def w(self) -> int:
        """
        返回 blob 的边界框 w 坐标（int）。
        您也可以对该对象执行 [2] 来获取此值。
        """
        pass
        
        
    def h(self) -> int:
        """
        返回 blob 的边界框 h 坐标（int）。
        您也可以对该对象执行 [3] 来获取此值。
        """
        pass
        
        
    def pixels(self) -> int:
        """
        返回属于此 blob 的像素数（int）。
        您也可以对该对象执行 [4] 来获取此值。
        """
        pass
        
        
    def cx(self) -> int:
        """
        返回 blob 的质心 x 位置（int）。
        您也可以对该对象执行 [5] 来获取此值。
        """
        pass
        
        
    def cxf(self) -> int:
        """
        返回 blob 的质心 x 位置（float）。
        """
        pass
        
        
    def cy(self) -> int:
        """
        返回 blob 的质心 y 位置（int）。
        您也可以对该对象执行 [6] 来获取此值。
        """
        pass
        
        
    def cyf(self) -> int:
        """
        返回 blob 的质心 y 位置（float）。
        """
        pass
        
        
    def rotation(self) -> float:
        """
        返回 blob 的旋转弧度（float）。如果 blob 像铅笔或笔，这个值将在 0-180 度之间独一无二。如果 blob 是圆形，这个值是没有用的。
        您也可以对该对象执行 [7] 来获取此值。
        """
        pass
        
        
    def rotation_deg(self) -> float:
        """
        返回 blob 的旋转角度（度）。
        """
        pass
        
        
    def rotation_rad(self) -> float:
        """
        返回 blob 的旋转角度（弧度）。此方法比 blob.rotation() 更具描述性。
        """
        pass
        
        
    def code(self) -> int:
        """
        返回一个具有每个颜色阈值的位设置的 32 位二进制数字，该颜色阈值是此 blob 的一部分。例如，如果您传递了 Image.find_blobs() 来查找三个颜色阈值，那么可能会为该 blob 设置位 0/1/2。请注意，除非 Image.find_blobs() 以 merge=True 调用，否则每个 blob 只会设置一个位。然后，可能会将具有不同颜色阈值的多个 blob 合并在一起。您可以将此方法与多个阈值一起使用，以实现颜色编码跟踪。
        您也可以对该对象执行 [8] 来获取此值。
        """
        pass
        
        
    def count(self) -> int:
        """
        返回合并到此 blob 中的 blob 数量。除非您以 merge=True 调用了 Image.find_blobs()，否则为 1。
        您也可以对该对象执行 [9] 来获取此值。
        """
        pass
        
        
    def perimeter(self) -> int:
        """
        返回此 blob 周长上的像素数。
        """
        pass
        
        
    def roundness(self) -> float:
        """
        返回介于 0 和 1 之间的值，表示对象的圆度。圆将是 1。
        """
        pass
        
        
    def elongation(self) -> float:
        """
        返回介于 0 和 1 之间的值，表示对象的长度（非圆）。线将是 1。
        """
        pass
        
        
    def area(self) -> int:
        """
        返回 blob 周围边界框的面积（w * h）。
        """
        pass
        
        
    def density(self) -> float:
        """
        返回 blob 的密度比率。这是 blob 中的像素数除以其边界框区域。低密度比率通常意味着对象的锁定不太好。结果在 0 到 1 之间。
        """
        pass
        
        
    def extent(self) -> float:
        """
        blob.density() 的别名。
        """
        pass
        
        
    def compactness(self) -> float:
        """
        类似于 blob.density()，但是使用 blob 的周长来测量对象的密度，因此更准确。结果在 0 到 1 之间。
        """
        pass
        
        
    def solidity(self) -> float:
        """
        类似于 blob.density()，但是使用最小区域旋转矩形与边界矩形来测量密度。结果在 0 到 1 之间。
        """
        pass
        
        
    def convexity(self) -> float:
        """
        返回介于 0 和 1 之间的值，表示对象的凸度。正方形将是 1。
        """
        pass
        
        
    def x_hist_bins(self) -> List[float]:
        """
        返回 blob 所有列的 x 轴直方图。bin 值在 0 到 1 之间缩放。
        """
        pass
        
        
    def y_hist_bins(self) -> List[float]:
        """
        返回 blob 所有行的 y 轴直方图。bin 值在 0 到 1 之间缩放。
        """
        pass
        
        
    def major_axis_line(self) -> Tuple[int, int, int, int]:
        """
        返回可以用 Image.draw_line() 绘制的主轴线元组 (x1, y1, x2, y2)（通过最小区域矩形的最长边）。
        """
        pass
        
        
    def minor_axis_line(self) -> Tuple[int, int, int, int]:
        """
        返回可以用 Image.draw_line() 绘制的次轴线元组 (x1, y1, x2, y2)（通过最小区域矩形的最短边）。
        """
        pass
        
        
    def enclosing_circle(self) -> Tuple[int, int, int]:
        """
        返回可以用 Image.draw_circle() 绘制的圆元组 (x, y, r)（包围 blob 的最小区域矩形的圆）。
        """
        pass
        
        
    def enclosed_ellipse(self) -> Tuple[int, int, int, int, float]:
        """
        返回可以用 Image.draw_ellipse() 绘制的椭圆元组 (x, y, rx, ry, rotation)（适合于 blob 的最小区域矩形内部的椭圆）。
        """
        pass
        
        
    
class line:
    def __init__(self):
        """
        请调用 Image.find_lines()、Image.find_line_segments() 或 Image.get_regression() 来创建此对象。
        """
        pass
        
        
    def line(self) -> Tuple[int, int, int, int]:
        """
        返回一个线元组 (x1, y1, x2, y2)，可用于其他 image 方法，如 Image.draw_line()。
        """
        pass
        
        
    def x1(self) -> int:
        """
        返回线的 p1 x 分量。
        您也可以对该对象执行 [0] 来获取此值。
        """
        pass
        
        
    def y1(self) -> int:
        """
        返回线的 p1 y 分量。
        您也可以对该对象执行 [1] 来获取此值。
        """
        pass
        
        
    def x2(self) -> int:
        """
        返回线的 p2 x 分量。
        您也可以对该对象执行 [2] 来获取此值。
        """
        pass
        
        
    def y2(self) -> int:
        """
        返回线的 p2 y 分量。
        您也可以对该对象执行 [3] 来获取此值。
        """
        pass
        
        
    def length(self) -> int:
        """
        返回线的长度：sqrt(((x2-x1)^2) + ((y2-y1)^2)。
        您也可以对该对象执行 [4] 来获取此值。
        """
        pass
        
        
    def magnitude(self) -> int:
        """
        通过霍夫变换返回直线的幅度。
        您也可以对该对象执行 [5] 来获取此值。
        """
        pass
        
        
    def theta(self) -> int:
        """
        通过霍夫变换返回线的角度 - (0 - 179) 度。
        您也可以对该对象执行 [7] 来获取此值。
        """
        pass
        
        
    def rho(self) -> int:
        """
        返回线的霍夫变换中的 rho 值。
        您也可以对该对象执行 [8] 来获取此值。
        """
        pass
        
        
    
class circle:
    def __init__(self):
        """
        请调用 Image.find_circles() 来创建此对象。
        """
        pass
        
        
    def x(self) -> int:
        """
        返回圆的 x 位置。
        您也可以对该对象执行 [0] 来获取此值。
        """
        pass
        
        
    def y(self) -> int:
        """
        返回圆的 y 位置。
        您也可以对该对象执行 [1] 来获取此值。
        """
        pass
        
        
    def r(self) -> int:
        """
        返回圆的半径。
        您也可以对该对象执行 [2] 来获取此值。
        """
        pass
        
        
    def magnitude(self) -> int:
        """
        返回圆的幅度。
        您也可以对该对象执行 [3] 来获取此值。
        """
        pass
        
        
    
class rect:
    def __init__(self):
        """
        请调用 Image.find_rects() 来创建此对象。
        """
        pass
        
        
    def corners(self) -> List[Tuple[int, int]]:
        """
        返回对象的 4 个角的 4 个 (x,y) 元组的列表。角始终按顺时针顺序返回，从左上角开始。
        """
        pass
        
        
    def rect(self) -> Tuple[int, int, int, int]:
        """
        返回一个矩形元组 (x, y, w, h)，可用于其他 image 方法，如 Image.draw_rectangle()，表示 rect 的边界框。
        """
        pass
        
        
    def x(self) -> int:
        """
        返回矩形的左上角的 x 位置。
        您也可以对该对象执行 [0] 来获取此值。
        """
        pass
        
        
    def y(self) -> int:
        """
        返回矩形的左上角的 y 位置。
        您也可以对该对象执行 [1] 来获取此值。
        """
        pass
        
        
    def w(self) -> int:
        """
        返回矩形的宽度。
        您也可以对该对象执行 [2] 来获取此值。
        """
        pass
        
        
    def h(self) -> int:
        """
        返回矩形的高度。
        您也可以对该对象执行 [3] 来获取此值。
        """
        pass
        
        
    def magnitude(self) -> int:
        """
        返回矩形的幅度。
        您也可以对该对象执行 [4] 来获取此值。
        """
        pass
        
        
    
class qrcode:
    def __init__(self):
        """
        请调用 Image.find_qrcodes() 来创建此对象。
        """
        pass
        
        
    def corners(self) -> List[Tuple[int, int]]:
        """
        返回对象的 4 个角的 4 个 (x,y) 元组的列表。角始终按顺时针顺序返回，从左上角开始。
        """
        pass
        
        
    def rect(self) -> Tuple[int, int, int, int]:
        """
        返回一个矩形元组 (x, y, w, h)，可用于其他 image 方法，如 Image.draw_rectangle()，表示 qrcode 的边界框。
        """
        pass
        
        
    def x(self) -> int:
        """
        返回 qrcode 的边界框 x 坐标（int）。
        您也可以对该对象执行 [0] 来获取此值。
        """
        pass
        
        
    def y(self) -> int:
        """
        返回 qrcode 的边界框 y 坐标（int）。
        您也可以对该对象执行 [1] 来获取此值。
        """
        pass
        
        
    def w(self) -> int:
        """
        返回 qrcode 的边界框 w 坐标（int）。
        您也可以对该对象执行 [2] 来获取此值。
        """
        pass
        
        
    def h(self) -> int:
        """
        返回 qrcode 的边界框 h 坐标（int）。
        您也可以对该对象执行 [3] 来获取此值。
        """
        pass
        
        
    def payload(self) -> str:
        """
        返回 qrcode 的有效载荷字符串。例如，URL。
        您也可以对该对象执行 [4] 来获取此值。
        """
        pass
        
        
    def version(self) -> int:
        """
        返回 qrcode 的版本（int）。
        您也可以对该对象执行 [5] 来获取此值。
        """
        pass
        
        
    def ecc_level(self) -> int:
        """
        返回 qrcode 的错误级别（ int）。
        您也可以对该对象执行 [6] 来获取此值。
        """
        pass
        
        
    def mask(self) -> int:
        """
        返回到此 qrcode 的掩码（int）。
        您也可以对该对象执行 [7] 来获取此值。
        """
        pass
        
        
    def data_type(self) -> int:
        """
        返回到此 qrcode 的 数据类型（int）。
        您也可以对该对象执行 [8] 来获取此值。
        """
        pass
        
        
    def eci(self) -> int:
        """
        返回 QR 码的 eci（int）。eci 存储了 QR 码中数据字节的编码方式。如果您计划处理包含非标准 ASCII 文本的 QR 码，您需要查看此值。
        您也可以对该对象执行 [9] 来获取此值。
        """
        pass
        
        
    def is_numeric(self) -> bool:
        """
        如果 QR 码的数据类型为数字，则返回 True。
        """
        pass
        
        
    def is_alphanumeric(self) -> bool:
        """
        如果 QR 码的数据类型为字母数字，则返回 True。
        """
        pass
        
        
    def is_binary(self) -> bool:
        """
        如果 QR 码的数据类型为二进制，则返回 True。如果您严肃对待处理所有类型的文本，需要检查 eci 是否为 True，以确定数据的文本编码。通常情况下，它只是标准的 ASCII，但它也可能是 UTF8，其中包含一些 2 字节的字符。
        """
        pass
        
        
    def is_kanji(self) -> bool:
        """
        如果 QR 码的数据类型为日文（Kanji），则返回 True。如果是 True，则您需要自行解码字符串，因为日文符号每个字符有 10 位，而 MicroPython 没有支持解析这种类型文本的功能。在这种情况下，负载必须被视为一个大字节数组。
        """
        pass
        
        
    
class apriltag:
    def __init__(self):
        """
        请调用 Image.find_apriltags() 来创建此对象。
        """
        pass
        
        
    
class datamatrix:
    def __init__(self):
        """
        请调用 Image.find_datamatrices() 来创建此对象。
        """
        pass
        
        
    def corners(self) -> List[Tuple[int, int]]:
        """
        返回对象的 4 个角的 4 个 (x,y) 元组的列表。角始终按顺时针顺序返回，从左上角开始。
        """
        pass
        
        
    def rect(self) -> Tuple[int, int, int, int]:
        """
        返回一个矩形元组 (x, y, w, h)，可用于其他 image 方法，如 Image.draw_rectangle()，表示 datamatrix 的边界框。
        """
        pass
        
        
    def x(self) -> int:
        """
        返回 datamatrix 的边界框 x 坐标（int）。
        您也可以对该对象执行 [0] 来获取此值。
        """
        pass
        
        
    def y(self) -> int:
        """
        返回 datamatrix 的边界框 y 坐标（int）。
        您也可以对该对象执行 [1] 来获取此值。
        """
        pass
        
        
    def w(self) -> int:
        """
        返回 datamatrix 的边界框 w 坐标（int）。
        您也可以对该对象执行 [2] 来获取此值。
        """
        pass
        
        
    def h(self) -> int:
        """
        返回 datamatrix 的边界框 h 坐标（int）。
        您也可以对该对象执行 [3] 来获取此值。
        """
        pass
        
        
    def payload(self) -> str:
        """
        返回 datamatrix 的有效负载字符串。例如，字符串。
        您也可以对该对象执行 [4] 来获取此值。
        """
        pass
        
        
    def rotation(self) -> float:
        """
        返回 datamatrix 的弧度旋转角度（float）。
        您也可以对该对象执行 [5] 来获取此值。
        """
        pass
        
        
    def rows(self) -> int:
        """
        返回数据矩阵中的行数（int）。
        您也可以对该对象执行 [6] 来获取此值。
        """
        pass
        
        
    def columns(self) -> int:
        """
        返回数据矩阵中的列数（int）。
        您也可以对该对象执行 [7] 来获取此值。
        """
        pass
        
        
    def capacity(self) -> int:
        """
        返回此数据矩阵中可容纳的字符数。
        您也可以对该对象执行 [8] 来获取此值。
        """
        pass
        
        
    def padding(self) -> int:
        """
        返回此数据矩阵中未使用的字符数。
        您也可以对该对象执行 [9] 来获取此值。
        """
        pass
        
        
    
class barcode:
    def __init__(self):
        """
        请调用 Image.find_barcodes() 来创建此对象。
        """
        pass
        
        
    def corners(self) -> List[Tuple[int, int]]:
        """
        返回对象的 4 个角的 4 个 (x,y) 元组的列表。角始终按顺时针顺序返回，从左上角开始。
        """
        pass
        
        
    def rect(self) -> Tuple[int, int, int, int]:
        """
        返回一个矩形元组 (x, y, w, h)，可用于其他 image 方法，如 Image.draw_rectangle()，表示 barcode 的边界框。
        """
        pass
        
        
    def x(self) -> int:
        """
        返回 barcode 的边界框 x 坐标（int）。
        您也可以对该对象执行 [0] 来获取此值。
        """
        pass
        
        
    def y(self) -> int:
        """
        返回 barcode 的边界框 y 坐标（int）。
        您也可以对该对象执行 [1] 来获取此值。
        """
        pass
        
        
    def w(self) -> int:
        """
        返回 barcode 的边界框 w 坐标（int）。
        您也可以对该对象执行 [2] 来获取此值。
        """
        pass
        
        
    def h(self) -> int:
        """
        返回 barcode 的边界框 h 坐标（int）。
        您也可以对该对象执行 [3] 来获取此值。
        """
        pass
        
        
    def payload(self) -> str:
        """
        返回 barcode 的有效负载字符串。例如，数字。
        您也可以对该对象执行 [4] 来获取此值。
        """
        pass
        
        
    def type(self) -> int:
        """
        返回 barcode 的类型枚举（int）。
        您也可以对该对象执行 [5] 来获取此值。
        """
        pass
        
        
    def rotation(self) -> float:
        """
        返回 barcode 的弧度旋转角度（float）。
        您也可以对该对象执行 [6] 来获取此值。
        """
        pass
        
        
    def quality(self) -> int:
        """
        返回此 barcode 在图像中被检测到的次数（int）。
        扫描条形码时，每次新的扫描线都可以解码相同的条形码。对于一个条形码来说，每次这样的情况发生，此值都会递增…
        您也可以对该对象执行 [7] 来获取此值。
        """
        pass
        
        
    
class displacement:
    def __init__(self):
        """
        请调用 Image.find_displacement() 来创建此对象。
        """
        pass
        
        
    def x_translation(self) -> float:
        """
        返回两个图像之间的 x 轴方向的像素平移。这是次像素精度的，因此它是一个浮点数。
        您也可以对该对象执行 [0] 来获取此值。
        """
        pass
        
        
    def y_translation(self) -> float:
        """
        返回两个图像之间的 y 轴方向的像素平移。这是次像素精度的，因此它是一个浮点数。
        您也可以对该对象执行 [1] 来获取此值。
        """
        pass
        
        
    def rotation(self) -> float:
        """
        返回两个图像之间的弧度旋转角度。
        您也可以对该对象执行 [2] 来获取此值。
        """
        pass
        
        
    def scale(self) -> float:
        """
        返回两个图像之间的缩放变化。
        您也可以对该对象执行 [3] 来获取此值。
        """
        pass
        
        
    def response(self) -> float:
        """
        返回两个图像之间的位移匹配结果的质量。在 0-1 之间。响应值小于 0.1 的 displacement 对象可能是噪声。
        您也可以对该对象执行 [4] 来获取此值。
        """
        pass
        
        
    
class kptmatch:
    def __init__(self):
        """
        请调用 image.match_descriptor() 来创建此对象。
        """
        pass
        
        
    def rect(self) -> Tuple[int, int, int, int]:
        """
        返回一个矩形元组 (x, y, w, h)，可用于其他 image 方法，如 Image.draw_rectangle()，表示 kptmatch 的边界框。
        """
        pass
        
        
    def cx(self) -> int:
        """
        返回 kptmatch 的质心 x 位置（int）。
        您也可以对该对象执行 [0] 来获取此值。
        """
        pass
        
        
    def cy(self) -> int:
        """
        返回 kptmatch 的质心 y 位置（int）。
        您也可以对该对象执行 [1] 来获取此值。
        """
        pass
        
        
    def x(self) -> int:
        """
        返回 kptmatch 的边界框 x 坐标（int）。
        您也可以对该对象执行 [2] 来获取此值。
        """
        pass
        
        
    def y(self) -> int:
        """
        返回 kptmatch 的边界框 y 坐标（int）。
        您也可以对该对象执行 [3] 来获取此值。
        """
        pass
        
        
    def w(self) -> int:
        """
        返回 kptmatch 的边界框 w 坐标（int）。
        您也可以对该对象执行 [4] 来获取此值。
        """
        pass
        
        
    def h(self) -> int:
        """
        返回 kptmatch 的边界框 h 坐标（int）。
        您也可以对该对象执行 [5] 来获取此值。
        """
        pass
        
        
    def count(self) -> int:
        """
        返回匹配的关键点数（int）。
        您也可以对该对象执行 [6] 来获取此值。
        """
        pass
        
        
    def theta(self) -> int:
        """
        返回关键点的估计旋转角度（int）。
        您也可以对该对象执行 [7] 来获取此值。
        """
        pass
        
        
    def match(self) -> List[Tuple[int, int]]:
        """
        返回匹配关键点的 (x,y) 元组列表。
        您也可以对该对象执行 [8] 来获取此值。
        """
        pass
        
        
    
class ImageIO:
    FILE_STREAM: int
    """
    ImageIO对象是在文件上打开的。
    """
    
    MEMORY_STREAM: int
    """
    ImageIO 对象已在内存中打开。
    """
    
    def __init__(self, path: str, mode):
        """
        创建一个 ImageIO 对象。
        如果 path 是磁盘上的文件名，则该文件将在 mode 为 'r' 时打开以进行读取，如果 mode 为 'w' 时打开以进行写入。
        path 也可以是一个 3 值元组 (w, h, bpp) 用于图像的内存存储。在这种情况下，mode 是内存中存储图像的数量。请注意，在分配了内存后，不允许内存存储缓冲区增长。对于二进制图像，使用 0 作为 bpp 值，对于灰度图像使用 1，对于 rgb565 图像使用 2。
        """
        pass
        
        
    def type(self) -> int:
        """
        如果 ImageIO 对象是 FILE_STREAM 或 MEMORY_STREAM 则返回。
        """
        pass
        
        
    def is_closed(self) -> bool:
        """
        如果 ImageIO 对象已关闭且不再可用则返回。
        """
        pass
        
        
    def count(self) -> int:
        """
        返回存储的帧数。
        """
        pass
        
        
    def offset(self) -> int:
        """
        返回图像索引偏移量。
        """
        pass
        
        
    def version(self) -> int | None:
        """
        返回对象的版本，如果是 FILE_STREAM。MEMORY_STREAM 版本是 none。
        """
        pass
        
        
    def buffer_size(self) -> int:
        """
        返回单个缓冲区中帧所分配的对象的大小。
        buffer_size() * count() == size()
        """
        pass
        
        
    def size(self) -> int:
        """
        返回 ImageIO 对象使用的磁盘或内存中的字节数。
        """
        pass
        
        
    def write(self,img: Image) -> ImageIO:
        """
        将新图像 img 写入 ImageIO 对象。对于磁盘上的 ImageIO 对象，随着添加新图像，文件将增长。对于内存中的 ImageIO 对象，这只是将图像写入当前预分配的插槽，然后转到下一个插槽。
        返回 ImageIO 对象。
        """
        pass
        
        
    def read(self,copy_to_fb=True,loop=True,pause=True) -> Image:
        """
        从 ImageIO 对象返回图像对象。如果 copy_to_fb 为 False，则新图像将分配在MicroPython 堆上。但是，MicroPython 堆有限，如果耗尽，可能没有空间来存储新图像。相反，将 copy_to_fb 设置为 True 可将帧缓冲区设置为新图像，使该函数的工作方式与 sensor.snapshot() 类似。
        如果 loop 为 True，则会自动导致ImageIO 对象从图像流的末尾查找开头。
        如果 pause 为True，则该方法在写入时暂停先前记录的毫秒数，以匹配捕获图像数据的原始帧速率。
        """
        pass
        
        
    def seek(self,offset) -> None:
        """
        查找ImageIO对象中的图像槽编号为 offset 的位置。
        对于磁盘上或内存中的对象都适用。
        """
        pass
        
        
    def sync(self) -> None:
        """
        将所有待写入磁盘的ImageIO对象数据写出。
        """
        pass
        
        
    def close(self) -> None:
        """
        关闭ImageIO对象。对于内存中的对象，这将释放分配的空间；对于磁盘文件，这将关闭文件并写出所有元数据。
        """
        pass
        
        
    
class Image:
    def __init__(self, arg, buffer: bytes | bytearray | memoryview | None = None, copy_to_fb: bool = False):
        """
        如果 arg 是一个字符串，则会从 arg 路径的文件创建一个新的图像对象。支持从磁盘加载bmp/pgm/ppm/jpg/jpeg/png格式的图像文件。如果 copy_to_fb 为真，则图像将被复制到帧缓冲区，而不是在堆上分配。
        如果 arg 是一个 ndarray ，则会从该 ndarray 创建一个新的图像对象。形状为 (w, h) 的 ndarray 被视为灰度图像，形状为 (w, h, 3) 的 ndarray 被视为RGB565图像。目前仅支持 float32 类型的 ndarray 。以这种方式创建图像时，如果传递了 buffer 参数，则图像数据将存储在该缓冲区中，而不是分配到堆上。如果 copy_to_fb 为真，则图像将被复制到帧缓冲区，而不是分配到堆上或使用 buffer 。
        如果 arg 是一个 int ，则该值被视为新图像的宽度，接下来必须提供 height 和 format 值，以创建一个新的空白图像对象。 format 可以是任何图像像素格式值，例如 image.GRAYSCALE 。图像将初始化为全零。请注意，对于压缩图像格式，需要提供 buffer 值。 buffer 将作为图像数据的来源，用于以这种方式创建图像。如果与 copy_to_fb 一起使用， buffer 中的数据将被复制到帧缓冲区。如果你想从JPEG的`bytes()`或`bytearray()`对象创建JPEG图像，你可以传递 width 、 height 和 image.JPEG 作为JPEG格式，并将 buffer 设置为JPEG字节流，从而创建JPEG图像。
        图像支持”[]” 表示法。执行 image[index] = 8/16位值 以分配图像像素，或执行 image[index] 以获取图像像素，该像素将是灰度/贝叶斯图像的8位值或RGB565/YUV图像的16位值。二进制图像返回1位值。
        对于JPEG图像，”[]” 允许您以字节数组的形式访问压缩的JPEG图像blob。但是，由于JPEG图像是压缩的字节流，因此对数据数组的读写是不透明的。
        图像还支持读缓冲区操作。您可以将图像传递给各种MicroPython函数，就好像图像是字节数组对象一样。特别是，如果您想要传输图像，您可以只将其传递给UART/SPI/I2C写函数，以便自动传输。
        """
        pass
        
        
    def width(self) -> int:
        """
        返回图像的宽度（以像素为单位）。
        """
        pass
        
        
    def height(self) -> int:
        """
        返回图像的高度（以像素为单位）。
        """
        pass
        
        
    def format(self) -> int:
        """
        对于灰度图像，返回 image.GRAYSCALE ；对于RGB565图像，返回 image.RGB565 ；对于贝叶斯模式图像，返回 image.BAYER ；对于JPEG图像，返回 image.JPEG 。
        """
        pass
        
        
    def size(self) -> int:
        """
        返回图像的大小（以字节为单位）。
        """
        pass
        
        
    def bytearray(self) -> bytearray:
        """
        返回一个指向图像数据的 bytearray 对象，用于字节级读/写访问。
        """
        pass
        
        
    def get_pixel(self,x: int,y: int,rgbtuple: bool | None = None) -> int | Tuple[int, int, int]:
        """
        对于灰度图像：返回位置（x，y）处的灰度像素值。对于RGB565图像：返回位置（x，y）处的RGB888像素元组（r，g，b）。对于贝叶斯模式图像：返回位置（x，y）处的像素值。
        如果 x 或 y 在图像外部，则返回None。
        x 和 y 可以单独传递，也可以作为元组传递（例如， (x，y) ）。
        rgbtuple 若为True，则此方法返回RGB888元组。否则，此方法返回底层像素的整数值。例如，对于RGB565图像，此方法返回RGB565值。对于RGB565图像，默认为True，否则为False。
        不支持压缩图像。
        """
        pass
        
        
    def set_pixel(self,x: int,y: int,pixel: int | Tuple[int, int, int]) -> Image:
        """
        对于灰度图像：将位置 (x, y) 处的像素设置为灰度值 pixel 。对于RGB565图像：将位置 (x, y) 处的像素设置为 RGB888 元组 (r, g, b) pixel 。对于 Bayer 模式图像：将位置 (x, y) 处的像素值设置为值 pixel 。
        返回图像对象，以便您可以使用 . 符号调用另一个方法。
        x 和 y 可以单独传递，也可以作为元组传递（例如， (x，y) ）。
        pixel 可以是 RGB888 元组 (r, g, b) 或底层像素值（即 RGB565 图像的 RGB565 值或灰度图像的 8 位值）。
        不支持压缩图像。
        """
        pass
        
        
    def to_ndarray(self,dtype: str,buffer: bytes | bytearray | memoryview | None = None) -> ndarray:
        """
        返回一个由图像创建的 ndarray 对象。目前，仅适用于GRAYSCALE或RGB565格式的图像。
        dtype 可以是 b、B 或 f，分别用于创建有符号 8 位、无符号 8 位或 32 位浮点型的 ndarray。灰度图像会直接转换为无符号 8 位的 ndarray 对象。对于有符号 8 位的 ndarray 对象，值会从 (0:255) 映射到 (-127:128)。对于 32 位浮点型的 ndarray 对象，值会从 (0.0:255.0) 映射。RGB565 图像会转换为 3 通道的 ndarray 对象，并且上述对灰度图像的处理过程会应用到每个通道，具体取决于 dtype。需要注意的是，dtype 也可以接受整数值（例如 ord() 函数的返回值）来表示 b、B 和 f。
        如果 buffer 不为 None ，则它是一个 bytearray 对象，用作 ndarray 的缓冲区。如果 buffer 为 None ，则会在堆上分配一个新的缓冲区来存储 ndarray 图像数据。你可以使用 buffer 参数直接在预分配的缓冲区中分配 ndarray ，从而避免堆分配和复制操作。
        返回的 ndarray 具有以下形状： 对于灰度图像（GRAYSCALE），形状为 (height, width) ；对于RGB565图像，形状为 (height, width, 3) 。
        """
        pass
        
        
    def to_bitmap(self,x_scale: float = 1.0,y_scale: float = 1.0,roi: Tuple[int, int, int, int] | None = None,rgb_channel: int = -1,alpha: int = 256,color_palette=None,alpha_palette=None,hint: int = 0,copy: bool = False,copy_to_fb: bool = False) -> Image:
        """
        将图像转换为位图图像（每个像素 1 位）。
        x_scale 控制图像在 x 方向上的缩放比例（浮动类型）。如果该值为负，图像将水平翻转。请注意，如果没有指定 y_scale ，则其值将与 x_scale 相同，以保持图像的纵横比。
        y_scale 控制图像在 y 方向上的缩放比例（浮动类型）。如果该值为负，图像将垂直翻转。请注意，如果没有指定 x_scale ，则 y_scale 的值将与 x_scale 相同，以保持图像的纵横比。
        roi 是图像的感兴趣区域（ROI）矩形元组 (x, y, w, h)，用于提取图像的一部分。这允许你仅提取ROI中的像素，以便在目标图像上进行缩放和绘制。
        rgb_channel 是要从 RGB565 图像中提取的 RGB 通道（0=红色 R，1=绿色 G，2=蓝色 B），并应用到最终图像上。例如，如果传递 rgb_channel=1 ，则会提取源 RGB565 图像的绿色通道，并以灰度形式应用到最终图像上。
        alpha 控制源图像与最终图像的混合程度。值为 256 时表示完全不透明的源图像，而小于 256 的值会在原图像和最终图像之间产生混合。值为 0 时表示最终图像不受修改。
        color_palette 如果不为 None，可以是 image.PALETTE_RAINBOW、image.PALETTE_IRONBOW，或一个包含 256 个像素的 RGB565 图像，用作图像灰度值的颜色查找表。如果使用了 rgb_channel 提取，该调色板会在提取后应用。
        alpha_palette 如果不为 None ，可以是一个包含 256 个像素的灰度图像，用作 alpha 调色板，按像素级别调节源图像的 alpha 值，使你能够基于灰度值精确控制像素的透明度。alpha 查找表中像素值为 255 时表示不透明，低于 255 的值则使像素变得更加透明，直到 0。此操作会在使用 rgb_channel 提取之后应用。
        hint 可以是标志的逻辑 OR：
        copy 如果为 True，则在堆上创建图像的深拷贝，而不是就地转换原始图像。
        copy_to_fb 如果为 True，图像将直接加载到帧缓冲区。copy_to_fb 优先于 copy。如果图像已经在帧缓冲区中，则此设置不会产生任何特殊效果。
        返回图像对象，以便您可以使用 . 符号调用另一个方法。
        """
        pass
        
        
    def to_grayscale(self,x_scale: float = 1.0,y_scale: float = 1.0,roi: Tuple[int, int, int, int] | None = None,rgb_channel: int = -1,alpha: int = 256,color_palette=None,alpha_palette=None,copy: bool = False,copy_to_fb: bool = False) -> Image:
        """
        将图像转换为灰度图像（每个像素 8 位）。
        x_scale 控制图像在 x 方向上的缩放比例（浮动类型）。如果该值为负，图像将水平翻转。请注意，如果没有指定 y_scale ，则其值将与 x_scale 相同，以保持图像的纵横比。
        y_scale 控制图像在 y 方向上的缩放比例（浮动类型）。如果该值为负，图像将垂直翻转。请注意，如果没有指定 x_scale ，则 y_scale 的值将与 x_scale 相同，以保持图像的纵横比。
        roi 是图像的感兴趣区域（ROI）矩形元组 (x, y, w, h)，用于提取图像的一部分。这允许你仅提取ROI中的像素，以便在目标图像上进行缩放和绘制。
        rgb_channel 是要从 RGB565 图像中提取的 RGB 通道（0=红色 R，1=绿色 G，2=蓝色 B），并应用到最终图像上。例如，如果传递 rgb_channel=1 ，则会提取源 RGB565 图像的绿色通道，并以灰度形式应用到最终图像上。
        alpha 控制源图像与最终图像的混合程度。值为 256 时表示完全不透明的源图像，而小于 256 的值会在原图像和最终图像之间产生混合。值为 0 时表示最终图像不受修改。
        color_palette 如果不为 None，可以是 image.PALETTE_RAINBOW、image.PALETTE_IRONBOW，或一个包含 256 个像素的 RGB565 图像，用作图像灰度值的颜色查找表。如果使用了 rgb_channel 提取，该调色板会在提取后应用。
        alpha_palette 如果不为 None ，可以是一个包含 256 个像素的灰度图像，用作 alpha 调色板，按像素级别调节源图像的 alpha 值，使你能够基于灰度值精确控制像素的透明度。alpha 查找表中像素值为 255 时表示不透明，低于 255 的值则使像素变得更加透明，直到 0。此操作会在使用 rgb_channel 提取之后应用。
        hint 可以是标志的逻辑 OR：
        copy 如果为 True，则在堆上创建图像的深拷贝，而不是就地转换原始图像。
        copy_to_fb 如果为 True，图像将直接加载到帧缓冲区。copy_to_fb 优先于 copy。如果图像已经在帧缓冲区中，则此设置不会产生任何特殊效果。
        返回图像对象，以便您可以使用 . 符号调用另一个方法。
        """
        pass
        
        
    def to_rgb565(self,x_scale: float = 1.0,y_scale: float = 1.0,roi: Tuple[int, int, int, int] | None = None,rgb_channel: int = -1,alpha: int = 256,color_palette=None,alpha_palette=None,hint: int = 0,copy: bool = False,copy_to_fb: bool = False) -> Image:
        """
        将图像转换为 RGB565 图像（每个像素 16 位）。
        x_scale 控制图像在 x 方向上的缩放比例（浮动类型）。如果该值为负，图像将水平翻转。请注意，如果没有指定 y_scale ，则其值将与 x_scale 相同，以保持图像的纵横比。
        y_scale 控制图像在 y 方向上的缩放比例（浮动类型）。如果该值为负，图像将垂直翻转。请注意，如果没有指定 x_scale ，则 y_scale 的值将与 x_scale 相同，以保持图像的纵横比。
        roi 是图像的感兴趣区域（ROI）矩形元组 (x, y, w, h)，用于提取图像的一部分。这允许你仅提取ROI中的像素，以便在目标图像上进行缩放和绘制。
        rgb_channel 是要从 RGB565 图像中提取的 RGB 通道（0=红色 R，1=绿色 G，2=蓝色 B），并应用到最终图像上。例如，如果传递 rgb_channel=1 ，则会提取源 RGB565 图像的绿色通道，并以灰度形式应用到最终图像上。
        alpha 控制源图像与最终图像的混合程度。值为 256 时表示完全不透明的源图像，而小于 256 的值会在原图像和最终图像之间产生混合。值为 0 时表示最终图像不受修改。
        color_palette 如果不为 None，可以是 image.PALETTE_RAINBOW、image.PALETTE_IRONBOW，或一个包含 256 个像素的 RGB565 图像，用作图像灰度值的颜色查找表。如果使用了 rgb_channel 提取，该调色板会在提取后应用。
        alpha_palette 如果不为 None ，可以是一个包含 256 个像素的灰度图像，用作 alpha 调色板，按像素级别调节源图像的 alpha 值，使你能够基于灰度值精确控制像素的透明度。alpha 查找表中像素值为 255 时表示不透明，低于 255 的值则使像素变得更加透明，直到 0。此操作会在使用 rgb_channel 提取之后应用。
        hint 可以是标志的逻辑 OR：
        copy 如果为 True，则在堆上创建图像的深拷贝，而不是就地转换原始图像。
        copy_to_fb 如果为 True，图像将直接加载到帧缓冲区。copy_to_fb 优先于 copy。如果图像已经在帧缓冲区中，则此设置不会产生任何特殊效果。
        返回图像对象，以便您可以使用 . 符号调用另一个方法。
        """
        pass
        
        
    def to_rainbow(self,x_scale: float = 1.0,y_scale: float = 1.0,roi: Tuple[int, int, int, int] | None = None,rgb_channel: int = -1,alpha: int = 256,color_palette=PALETTE_RAINBOW,alpha_palette=None,hint: int = 0,copy: bool = False,copy_to_fb: bool = False) -> Image:
        """
        将图像转换为 RGB565 彩虹图像（每个像素 16 位）。
        x_scale 控制图像在 x 方向上的缩放比例（浮动类型）。如果该值为负，图像将水平翻转。请注意，如果没有指定 y_scale ，则其值将与 x_scale 相同，以保持图像的纵横比。
        y_scale 控制图像在 y 方向上的缩放比例（浮动类型）。如果该值为负，图像将垂直翻转。请注意，如果没有指定 x_scale ，则 y_scale 的值将与 x_scale 相同，以保持图像的纵横比。
        roi 是图像的感兴趣区域（ROI）矩形元组 (x, y, w, h)，用于提取图像的一部分。这允许你仅提取ROI中的像素，以便在目标图像上进行缩放和绘制。
        rgb_channel 是要从 RGB565 图像中提取的 RGB 通道（0=红色 R，1=绿色 G，2=蓝色 B），并应用到最终图像上。例如，如果传递 rgb_channel=1 ，则会提取源 RGB565 图像的绿色通道，并以灰度形式应用到最终图像上。
        alpha 控制源图像与最终图像的混合程度。值为 256 时表示完全不透明的源图像，而小于 256 的值会在原图像和最终图像之间产生混合。值为 0 时表示最终图像不受修改。
        color_palette 如果不为 None，可以是 image.PALETTE_RAINBOW、image.PALETTE_IRONBOW，或一个包含 256 个像素的 RGB565 图像，用作图像灰度值的颜色查找表。如果使用了 rgb_channel 提取，该调色板会在提取后应用。
        alpha_palette 如果不为 None ，可以是一个包含 256 个像素的灰度图像，用作 alpha 调色板，按像素级别调节源图像的 alpha 值，使你能够基于灰度值精确控制像素的透明度。alpha 查找表中像素值为 255 时表示不透明，低于 255 的值则使像素变得更加透明，直到 0。此操作会在使用 rgb_channel 提取之后应用。
        hint 可以是标志的逻辑 OR：
        copy 如果为 True，则在堆上创建图像的深拷贝，而不是就地转换原始图像。
        copy_to_fb 如果为 True，图像将直接加载到帧缓冲区。copy_to_fb 优先于 copy。如果图像已经在帧缓冲区中，则此设置不会产生任何特殊效果。
        返回图像对象，以便您可以使用 . 符号调用另一个方法。
        """
        pass
        
        
    def to_ironbow(self,x_scale: float = 1.0,y_scale: float = 1.0,roi: Tuple[int, int, int, int] | None = None,rgb_channel: int = -1,alpha: int = 256,color_palette=PALETTE_IRONBOW,alpha_palette=None,hint: int = 0,copy: bool = False,copy_to_fb: bool = False) -> Image:
        """
        将图像转换为 RGB565 铁道彩虹（Ironbow）图像（每个像素 16 位）。
        x_scale 控制图像在 x 方向上的缩放比例（浮动类型）。如果该值为负，图像将水平翻转。请注意，如果没有指定 y_scale ，则其值将与 x_scale 相同，以保持图像的纵横比。
        y_scale 控制图像在 y 方向上的缩放比例（浮动类型）。如果该值为负，图像将垂直翻转。请注意，如果没有指定 x_scale ，则 y_scale 的值将与 x_scale 相同，以保持图像的纵横比。
        roi 是图像的感兴趣区域（ROI）矩形元组 (x, y, w, h)，用于提取图像的一部分。这允许你仅提取ROI中的像素，以便在目标图像上进行缩放和绘制。
        rgb_channel 是要从 RGB565 图像中提取的 RGB 通道（0=红色 R，1=绿色 G，2=蓝色 B），并应用到最终图像上。例如，如果传递 rgb_channel=1 ，则会提取源 RGB565 图像的绿色通道，并以灰度形式应用到最终图像上。
        alpha 控制源图像与最终图像的混合程度。值为 256 时表示完全不透明的源图像，而小于 256 的值会在原图像和最终图像之间产生混合。值为 0 时表示最终图像不受修改。
        color_palette 如果不为 None，可以是 image.PALETTE_RAINBOW、image.PALETTE_IRONBOW，或一个包含 256 个像素的 RGB565 图像，用作图像灰度值的颜色查找表。如果使用了 rgb_channel 提取，该调色板会在提取后应用。
        alpha_palette 如果不为 None ，可以是一个包含 256 个像素的灰度图像，用作 alpha 调色板，按像素级别调节源图像的 alpha 值，使你能够基于灰度值精确控制像素的透明度。alpha 查找表中像素值为 255 时表示不透明，低于 255 的值则使像素变得更加透明，直到 0。此操作会在使用 rgb_channel 提取之后应用。
        hint 可以是标志的逻辑 OR：
        copy 如果为 True，则在堆上创建图像的深拷贝，而不是就地转换原始图像。
        copy_to_fb 如果为 True，图像将直接加载到帧缓冲区。copy_to_fb 优先于 copy。如果图像已经在帧缓冲区中，则此设置不会产生任何特殊效果。
        返回图像对象，以便您可以使用 . 符号调用另一个方法。
        """
        pass
        
        
    def to_jpeg(self,x_scale: float = 1.0,y_scale: float = 1.0,roi: Tuple[int, int, int, int] | None = None,rgb_channel: int = -1,alpha: int = 256,color_palette=None,alpha_palette=None,hint: int = 0,copy: bool = False,copy_to_fb: bool = False,quality: int = 90,encode_for_ide: bool = False,subsampling: int = 0) -> Image:
        """
        将图像转换为 JPEG 图像。
        x_scale 控制图像在 x 方向上的缩放比例（浮动类型）。如果该值为负，图像将水平翻转。请注意，如果没有指定 y_scale ，则其值将与 x_scale 相同，以保持图像的纵横比。
        y_scale 控制图像在 y 方向上的缩放比例（浮动类型）。如果该值为负，图像将垂直翻转。请注意，如果没有指定 x_scale ，则 y_scale 的值将与 x_scale 相同，以保持图像的纵横比。
        roi 是图像的感兴趣区域（ROI）矩形元组 (x, y, w, h)，用于提取图像的一部分。这允许你仅提取ROI中的像素，以便在目标图像上进行缩放和绘制。
        rgb_channel 是要从 RGB565 图像中提取的 RGB 通道（0=红色 R，1=绿色 G，2=蓝色 B），并应用到最终图像上。例如，如果传递 rgb_channel=1 ，则会提取源 RGB565 图像的绿色通道，并以灰度形式应用到最终图像上。
        alpha 控制源图像与最终图像的混合程度。值为 256 时表示完全不透明的源图像，而小于 256 的值会在原图像和最终图像之间产生混合。值为 0 时表示最终图像不受修改。
        color_palette 如果不为 None，可以是 image.PALETTE_RAINBOW、image.PALETTE_IRONBOW，或一个包含 256 个像素的 RGB565 图像，用作图像灰度值的颜色查找表。如果使用了 rgb_channel 提取，该调色板会在提取后应用。
        alpha_palette 如果不为 None ，可以是一个包含 256 个像素的灰度图像，用作 alpha 调色板，按像素级别调节源图像的 alpha 值，使你能够基于灰度值精确控制像素的透明度。alpha 查找表中像素值为 255 时表示不透明，低于 255 的值则使像素变得更加透明，直到 0。此操作会在使用 rgb_channel 提取之后应用。
        hint 可以是标志的逻辑 OR：
        copy 如果为 True，则在堆上创建图像的深拷贝，而不是就地转换原始图像。
        copy_to_fb 如果为 True，图像将直接加载到帧缓冲区。copy_to_fb 优先于 copy。如果图像已经在帧缓冲区中，则此设置不会产生任何特殊效果。
        quality 控制 JPEG 图像的压缩质量。该值可以在 0 到 100 之间，值越高表示图像质量越好，压缩率越低；值越低则表示图像质量较差，压缩率较高。
        encode_for_ide 如果为 True，图像将以一种方式进行编码，使得 IDE 可以通过执行 print(image) 来显示图像。这对于通过 UART 进行调试，并通过 IDE 的 Open Terminal 功能查看图像非常有用。
        subsampling 可以是:
        返回图像对象，以便您可以使用 . 符号调用另一个方法。
        """
        pass
        
        
    def to_png(self,x_scale: float = 1.0,y_scale: float = 1.0,roi: Tuple[int, int, int, int] | None = None,rgb_channel: int = -1,alpha: int = 256,color_palette=None,alpha_palette=None,hint: int = 0,copy: bool = False,copy_to_fb: bool = False) -> Image:
        """
        将图像转换为 PNG 图像。
        x_scale 控制图像在 x 方向上的缩放比例（浮动类型）。如果该值为负，图像将水平翻转。请注意，如果没有指定 y_scale ，则其值将与 x_scale 相同，以保持图像的纵横比。
        y_scale 控制图像在 y 方向上的缩放比例（浮动类型）。如果该值为负，图像将垂直翻转。请注意，如果没有指定 x_scale ，则 y_scale 的值将与 x_scale 相同，以保持图像的纵横比。
        roi 是图像的感兴趣区域（ROI）矩形元组 (x, y, w, h)，用于提取图像的一部分。这允许你仅提取ROI中的像素，以便在目标图像上进行缩放和绘制。
        rgb_channel 是要从 RGB565 图像中提取的 RGB 通道（0=红色 R，1=绿色 G，2=蓝色 B），并应用到最终图像上。例如，如果传递 rgb_channel=1 ，则会提取源 RGB565 图像的绿色通道，并以灰度形式应用到最终图像上。
        alpha 控制源图像与最终图像的混合程度。值为 256 时表示完全不透明的源图像，而小于 256 的值会在原图像和最终图像之间产生混合。值为 0 时表示最终图像不受修改。
        color_palette 如果不为 None，可以是 image.PALETTE_RAINBOW、image.PALETTE_IRONBOW，或一个包含 256 个像素的 RGB565 图像，用作图像灰度值的颜色查找表。如果使用了 rgb_channel 提取，该调色板会在提取后应用。
        alpha_palette 如果不为 None ，可以是一个包含 256 个像素的灰度图像，用作 alpha 调色板，按像素级别调节源图像的 alpha 值，使你能够基于灰度值精确控制像素的透明度。alpha 查找表中像素值为 255 时表示不透明，低于 255 的值则使像素变得更加透明，直到 0。此操作会在使用 rgb_channel 提取之后应用。
        hint 可以是标志的逻辑 OR：
        copy 如果为 True，则在堆上创建图像的深拷贝，而不是就地转换原始图像。
        copy_to_fb 如果为 True，图像将直接加载到帧缓冲区。copy_to_fb 优先于 copy。如果图像已经在帧缓冲区中，则此设置不会产生任何特殊效果。
        返回图像对象，以便您可以使用 . 符号调用另一个方法。
        """
        pass
        
        
    def compress(self,x_scale: float = 1.0,y_scale: float = 1.0,roi: Tuple[int, int, int, int] | None = None,rgb_channel: int = -1,alpha: int = 256,color_palette=None,alpha_palette=None,hint: int = 0,copy: bool = False,copy_to_fb: bool = False,quality: int = 90,encode_for_ide: bool = False,subsampling: int = 0) -> Image:
        """
        将图像转换为 JPEG 图像。
        x_scale 控制图像在 x 方向上的缩放比例（浮动类型）。如果该值为负，图像将水平翻转。请注意，如果没有指定 y_scale ，则其值将与 x_scale 相同，以保持图像的纵横比。
        y_scale 控制图像在 y 方向上的缩放比例（浮动类型）。如果该值为负，图像将垂直翻转。请注意，如果没有指定 x_scale ，则 y_scale 的值将与 x_scale 相同，以保持图像的纵横比。
        roi 是图像的感兴趣区域（ROI）矩形元组 (x, y, w, h)，用于提取图像的一部分。这允许你仅提取ROI中的像素，以便在目标图像上进行缩放和绘制。
        rgb_channel 是要从 RGB565 图像中提取的 RGB 通道（0=红色 R，1=绿色 G，2=蓝色 B），并应用到最终图像上。例如，如果传递 rgb_channel=1 ，则会提取源 RGB565 图像的绿色通道，并以灰度形式应用到最终图像上。
        alpha 控制源图像与最终图像的混合程度。值为 256 时表示完全不透明的源图像，而小于 256 的值会在原图像和最终图像之间产生混合。值为 0 时表示最终图像不受修改。
        color_palette 如果不为 None，可以是 image.PALETTE_RAINBOW、image.PALETTE_IRONBOW，或一个包含 256 个像素的 RGB565 图像，用作图像灰度值的颜色查找表。如果使用了 rgb_channel 提取，该调色板会在提取后应用。
        alpha_palette 如果不为 None ，可以是一个包含 256 个像素的灰度图像，用作 alpha 调色板，按像素级别调节源图像的 alpha 值，使你能够基于灰度值精确控制像素的透明度。alpha 查找表中像素值为 255 时表示不透明，低于 255 的值则使像素变得更加透明，直到 0。此操作会在使用 rgb_channel 提取之后应用。
        hint 可以是标志的逻辑 OR：
        copy 如果为 True，则在堆上创建图像的深拷贝，而不是就地转换原始图像。
        copy_to_fb 如果为 True，图像将直接加载到帧缓冲区。copy_to_fb 优先于 copy。如果图像已经在帧缓冲区中，则此设置不会产生任何特殊效果。
        quality 控制 JPEG 图像的压缩质量。该值可以在 0 到 100 之间，值越高表示图像质量越好，压缩率越低；值越低则表示图像质量较差，压缩率较高。
        encode_for_ide 如果为 True，图像将以一种方式进行编码，使得 IDE 可以通过执行 print(image) 来显示图像。这对于通过 UART 进行调试，并通过 IDE 的 Open Terminal 功能查看图像非常有用。
        subsampling 可以是:
        返回图像对象，以便您可以使用 . 符号调用另一个方法。
        """
        pass
        
        
    def copy(self,x_scale: float = 1.0,y_scale: float = 1.0,roi: Tuple[int, int, int, int] | None = None,rgb_channel: int = -1,alpha: int = 256,color_palette=None,alpha_palette=None,hint: int = 0,copy_to_fb: float = False) -> Image:
        """
        创建图像对象的深拷贝。
        x_scale 控制图像在 x 方向上的缩放比例（浮动类型）。如果该值为负，图像将水平翻转。请注意，如果没有指定 y_scale ，则其值将与 x_scale 相同，以保持图像的纵横比。
        y_scale 控制图像在 y 方向上的缩放比例（浮动类型）。如果该值为负，图像将垂直翻转。请注意，如果没有指定 x_scale ，则 y_scale 的值将与 x_scale 相同，以保持图像的纵横比。
        roi 是图像的感兴趣区域（ROI）矩形元组 (x, y, w, h)，用于提取图像的一部分。这允许你仅提取ROI中的像素，以便在目标图像上进行缩放和绘制。
        rgb_channel 是要从 RGB565 图像中提取的 RGB 通道（0=红色 R，1=绿色 G，2=蓝色 B），并应用到最终图像上。例如，如果传递 rgb_channel=1 ，则会提取源 RGB565 图像的绿色通道，并以灰度形式应用到最终图像上。
        alpha 控制源图像与最终图像的混合程度。值为 256 时表示完全不透明的源图像，而小于 256 的值会在原图像和最终图像之间产生混合。值为 0 时表示最终图像不受修改。
        color_palette 如果不为 None，可以是 image.PALETTE_RAINBOW、image.PALETTE_IRONBOW，或一个包含 256 个像素的 RGB565 图像，用作图像灰度值的颜色查找表。如果使用了 rgb_channel 提取，该调色板会在提取后应用。
        alpha_palette 如果不为 None ，可以是一个包含 256 个像素的灰度图像，用作 alpha 调色板，按像素级别调节源图像的 alpha 值，使你能够基于灰度值精确控制像素的透明度。alpha 查找表中像素值为 255 时表示不透明，低于 255 的值则使像素变得更加透明，直到 0。此操作会在使用 rgb_channel 提取之后应用。
        hint 可以是标志的逻辑 OR：
        copy_to_fb 如果为 True，图像将直接加载到帧缓冲区。如果图像已经在帧缓冲区中，则此设置不会产生任何特殊效果。
        返回图像对象，以便您可以使用 . 符号调用另一个方法。
        """
        pass
        
        
    def crop(self,x_scale: float = 1.0,y_scale: float = 1.0,roi: Tuple[int, int, int, int] | None = None,rgb_channel: int = -1,alpha: int = 256,color_palette=None,alpha_palette=None,hint: int = 0,copy: bool = False,copy_to_fb: bool = False) -> Image:
        """
        在不改变图像类型的情况下，就地修改图像。
        x_scale 控制图像在 x 方向上的缩放比例（浮动类型）。如果该值为负，图像将水平翻转。请注意，如果没有指定 y_scale ，则其值将与 x_scale 相同，以保持图像的纵横比。
        y_scale 控制图像在 y 方向上的缩放比例（浮动类型）。如果该值为负，图像将垂直翻转。请注意，如果没有指定 x_scale ，则 y_scale 的值将与 x_scale 相同，以保持图像的纵横比。
        roi 是图像的感兴趣区域（ROI）矩形元组 (x, y, w, h)，用于提取图像的一部分。这允许你仅提取ROI中的像素，以便在目标图像上进行缩放和绘制。
        rgb_channel 是要从 RGB565 图像中提取的 RGB 通道（0=红色 R，1=绿色 G，2=蓝色 B），并应用到最终图像上。例如，如果传递 rgb_channel=1 ，则会提取源 RGB565 图像的绿色通道，并以灰度形式应用到最终图像上。
        alpha 控制源图像与最终图像的混合程度。值为 256 时表示完全不透明的源图像，而小于 256 的值会在原图像和最终图像之间产生混合。值为 0 时表示最终图像不受修改。
        color_palette 如果不为 None，可以是 image.PALETTE_RAINBOW、image.PALETTE_IRONBOW，或一个包含 256 个像素的 RGB565 图像，用作图像灰度值的颜色查找表。如果使用了 rgb_channel 提取，该调色板会在提取后应用。
        alpha_palette 如果不为 None ，可以是一个包含 256 个像素的灰度图像，用作 alpha 调色板，按像素级别调节源图像的 alpha 值，使你能够基于灰度值精确控制像素的透明度。alpha 查找表中像素值为 255 时表示不透明，低于 255 的值则使像素变得更加透明，直到 0。此操作会在使用 rgb_channel 提取之后应用。
        hint 可以是标志的逻辑 OR：
        copy 如果为 True，则在堆上创建图像的深拷贝，而不是就地转换原始图像。
        copy_to_fb 如果为 True，图像将直接加载到帧缓冲区。copy_to_fb 优先于 copy。如果图像已经在帧缓冲区中，则此设置不会产生任何特殊效果。
        返回图像对象，以便您可以使用 . 符号调用另一个方法。
        """
        pass
        
        
    def scale(self,x_scale: float = 1.0,y_scale: float = 1.0,roi: Tuple[int, int, int, int] | None = None,rgb_channel: int = -1,alpha: int = 256,color_palette=None,alpha_palette=None,hint: int = 0,copy: bool = False,copy_to_fb: bool = False) -> Image:
        """
        在不改变图像类型的情况下，就地修改图像。
        x_scale 控制图像在 x 方向上的缩放比例（浮动类型）。如果该值为负，图像将水平翻转。请注意，如果没有指定 y_scale ，则其值将与 x_scale 相同，以保持图像的纵横比。
        y_scale 控制图像在 y 方向上的缩放比例（浮动类型）。如果该值为负，图像将垂直翻转。请注意，如果没有指定 x_scale ，则 y_scale 的值将与 x_scale 相同，以保持图像的纵横比。
        roi 是图像的感兴趣区域（ROI）矩形元组 (x, y, w, h)，用于提取图像的一部分。这允许你仅提取ROI中的像素，以便在目标图像上进行缩放和绘制。
        rgb_channel 是要从 RGB565 图像中提取的 RGB 通道（0=红色 R，1=绿色 G，2=蓝色 B），并应用到最终图像上。例如，如果传递 rgb_channel=1 ，则会提取源 RGB565 图像的绿色通道，并以灰度形式应用到最终图像上。
        alpha 控制源图像与最终图像的混合程度。值为 256 时表示完全不透明的源图像，而小于 256 的值会在原图像和最终图像之间产生混合。值为 0 时表示最终图像不受修改。
        color_palette 如果不为 None，可以是 image.PALETTE_RAINBOW、image.PALETTE_IRONBOW，或一个包含 256 个像素的 RGB565 图像，用作图像灰度值的颜色查找表。如果使用了 rgb_channel 提取，该调色板会在提取后应用。
        alpha_palette 如果不为 None ，可以是一个包含 256 个像素的灰度图像，用作 alpha 调色板，按像素级别调节源图像的 alpha 值，使你能够基于灰度值精确控制像素的透明度。alpha 查找表中像素值为 255 时表示不透明，低于 255 的值则使像素变得更加透明，直到 0。此操作会在使用 rgb_channel 提取之后应用。
        hint 可以是标志的逻辑 OR：
        copy 如果为 True，则在堆上创建图像的深拷贝，而不是就地转换原始图像。
        copy_to_fb 如果为 True，图像将直接加载到帧缓冲区。copy_to_fb 优先于 copy。如果图像已经在帧缓冲区中，则此设置不会产生任何特殊效果。
        返回图像对象，以便您可以使用 . 符号调用另一个方法。
        """
        pass
        
        
    def save(self,path: str,roi: Tuple[int, int, int, int] | None = None,quality=50) -> Image:
        """
        将图像的副本保存到文件系统中的 path 处。
        支持 bmp/pgm/ppm/jpg/jpeg 图像文件。请注意，您不能将 jpeg 压缩图像保存为未压缩格式。
        roi 是要保存的感兴趣区域矩形 (x, y, w, h)。如果未指定，则等于复制整个图像的图像矩形。此参数不适用于 JPEG 图像。
        quality 是要用于将图像保存为 JPEG 格式的 jpeg 压缩质量（0-100）（int）。
        返回图像对象，以便您可以使用 . 符号调用另一个方法。
        """
        pass
        
        
    def flush(self) -> None:
        """
        使用相机上帧缓冲区中的图像更新 IDE 中的帧缓冲区。
        """
        pass
        
        
    def clear(self,mask: Image | None = None) -> Image:
        """
        将图像中的所有像素设置为零（非常快）。
        mask 是另一个图像，用作像素级掩码以进行操作。掩码应该是一个只有黑色或白色像素的图像，应该与正在操作的图像大小相同。仅修改掩码中设置的像素。
        返回图像对象，以便您可以使用 . 符号调用另一个方法。
        不支持压缩图像。
        """
        pass
        
        
    def draw_line(self,x0: int,y0: int,x1: int,y1: int,color: int | Tuple[int, int, int] | None = None,thickness=1) -> Image:
        """
        在图像上从 (x0, y0) 到 (x1, y1) 绘制一条线。您可以分别传递 x0、y0、x1、y1，或作为元组 (x0, y0, x1, y1) 传递。
        color 是 Grayscale 或 RGB565 图像的 RGB888 元组。默认为白色。但是，您还可以传递灰度图像的底层像素值（0-255）或 RGB565 图像的 RGB565 值。
        thickness 控制线的厚度（以像素为单位）。
        返回图像对象，以便您可以使用 . 符号调用另一个方法。
        不支持压缩图像或 Bayer 图像。
        """
        pass
        
        
    def draw_rectangle(self,x: int,y: int,w: int,h: int,color: int | Tuple[int, int, int] | None = None,thickness=1,fill=False) -> Image:
        """
        在图像上绘制一个矩形。您可以分别传递 x、y、w、h，或作为元组 (x、y、w、h) 传递。
        color 是 Grayscale 或 RGB565 图像的 RGB888 元组。默认为白色。但是，您还可以传递灰度图像的底层像素值（0-255）或 RGB565 图像的 RGB565 值。
        thickness 控制线的厚度（以像素为单位）。
        将 fill 设置为 True 以填充矩形。
        返回图像对象，以便您可以使用 . 符号调用另一个方法。
        不支持压缩图像或 Bayer 图像。
        """
        pass
        
        
    def draw_circle(self,x: int,y: int,radius: int,color: int | Tuple[int, int, int] | None = None,thickness=1,fill=False) -> Image:
        """
        在图像上绘制一个圆。您可以分别传递 x、y、半径，或作为元组 (x、y、半径) 传递。
        color 是 Grayscale 或 RGB565 图像的 RGB888 元组。默认为白色。但是，您还可以传递灰度图像的底层像素值（0-255）或 RGB565 图像的 RGB565 值。
        thickness 控制边缘的粗细（以像素为单位）。
        将 fill 设置为 True 以填充圆。
        返回图像对象，以便您可以使用 . 符号调用另一个方法。
        不支持压缩图像或 Bayer 图像。
        """
        pass
        
        
    def draw_ellipse(self,cx: int,cy: int,rx: int,ry: int,rotation: int,color: int | Tuple[int, int, int] | None = None,thickness=1,fill=False) -> Image:
        """
        在图像上绘制一个椭圆。您可以分别传递 cx、cy、rx、ry 和rotation（以度为单位），或作为元组 (cx、cy、rx、ry、rotation) 传递。
        color 是 Grayscale 或 RGB565 图像的 RGB888 元组。默认为白色。但是，您还可以传递灰度图像的底层像素值（0-255）或 RGB565 图像的 RGB565 值。
        thickness 控制边缘的粗细（以像素为单位）。
        将 fill 设置为 True 以填充椭圆。
        返回图像对象，以便您可以使用 . 符号调用另一个方法。
        不支持压缩图像或 Bayer 图像。
        """
        pass
        
        
    def draw_string(self,x: int,y: int,text: str,color: int | Tuple[int, int, int] | None = None,scale=1,x_spacing=0,y_spacing=0,mono_space=True,char_rotation=0,char_hmirror=False,char_vflip=False,string_rotation=0,string_hmirror=False,string_vflip=False) -> Image:
        """
        在图像中的位置 (x, y) 处绘制 8x10 文本。可以分别传递 x 和 y，也可以作为元组 (x, y) 传递。
        text 是要写入图像的字符串。\n、\r 和 \r\n 行结束符将光标移动到下一行。
        color 是 Grayscale 或 RGB565 图像的 RGB888 元组。默认为白色。但是，您还可以传递灰度图像的底层像素值（0-255）或 RGB565 图像的 RGB565 值。
        可以增加 scale 来增加/减小图像上文本的大小。可以传递大于 0 的整数或浮点值。
        x_spacing 允许你在字符之间添加（如果为正值）或减去（如果为负值） x 个像素。
        y_spacing 允许你在字符之间添加（如果为正值）或减去（如果为负值） y 个像素（用于多行文本）。
        mono_space 默认为 True，强制文本为固定间距。对于大文本比例，这看起来很糟糕。将其设置为 False 可以得到非固定宽度字符间距，效果要好得多。
        char_rotation 可以是 0、90、180、270，以按此数量旋转字符串中的每个字符。
        char_hmirror 如果为 True，则水平镜像字符串中的所有字符。
        char_vflip 如果为 True，则垂直翻转字符串中的所有字符。
        string_rotation 可以是 0、90、180、270，以按此数量旋转字符串。
        string_hmirror 如果为 True，则水平镜像字符串。
        string_vflip 如果为 True，则垂直翻转字符串。
        返回图像对象，以便您可以使用 . 符号调用另一个方法。
        不支持压缩图像或 Bayer 图像。
        """
        pass
        
        
    def draw_cross(self,x: int,y: int,color: int | Tuple[int, int, int] | None = None,size=5,thickness=1) -> Image:
        """
        在位置 x、y 处绘制十字。可以分别传递 x 和 y，也可以作为元组 (x, y) 传递。
        color 是 Grayscale 或 RGB565 图像的 RGB888 元组。默认为白色。但是，您还可以传递灰度图像的底层像素值（0-255）或 RGB565 图像的 RGB565 值。
        size 控制十字的线条长度。
        thickness 控制边缘的粗细（以像素为单位）。
        返回图像对象，以便您可以使用 . 符号调用另一个方法。
        不支持压缩图像或 Bayer 图像。
        """
        pass
        
        
    def draw_arrow(self,x0: int,y0: int,x1: int,y1: int,color: int | Tuple[int, int, int] | None = None,thickness=1) -> Image:
        """
        在图像上从 (x0, y0) 到 (x1, y1) 绘制箭头。可以分别传递 x0、y0、x1 和 y1，也可以作为元组 (x0, y0, x1, y1) 传递。
        color 是 Grayscale 或 RGB565 图像的 RGB888 元组。默认为白色。但是，您还可以传递灰度图像的底层像素值（0-255）或 RGB565 图像的 RGB565 值。
        thickness 控制线的厚度（以像素为单位）。
        返回图像对象，以便您可以使用 . 符号调用另一个方法。
        不支持压缩图像或 Bayer 图像。
        """
        pass
        
        
    def draw_edges(self,image: Image,corners,color: int | Tuple[int, int, int] | None = None,size=0,thickness=1,fill=False) -> Image:
        """
        在由像 blob.corners 等方法返回的角点列表之间绘制线条边缘。角点是一个包含四个值的元组，每个值是一个包含 x/y 坐标的二元组。例如：[(x1, y1), (x2, y2), (x3, y3), (x4, y4)]。
        color 是 Grayscale 或 RGB565 图像的 RGB888 元组。默认为白色。但是，您还可以传递灰度图像的底层像素值（0-255）或 RGB565 图像的 RGB565 值。
        size 如果大于 0，则会将角点绘制为半径为 size 的圆。
        thickness 控制线的厚度（以像素为单位）。
        将 fill 设置为 True 以填充角点圆（如果绘制）。
        返回图像对象，以便您可以使用 . 符号调用另一个方法。
        不支持压缩图像或 Bayer 图像。
        """
        pass
        
        
    def draw_image(self,image: Image,x: int = 0,y: int = 0,x_scale: float = 1.0,y_scale: float = 1.0,roi: Tuple[int, int, int, int] | None = None,rgb_channel: int = -1,alpha: int = 256,color_palette=None,alpha_palette=None,hint: int = 0,mask: Image | None = None) -> Image:
        """
        绘制一个 image ，其左上角起始位置为 x 、 y 。此方法会自动处理将传入的图像渲染为目标图像的正确像素格式，同时无缝处理剪裁。 image 也可以是一个 RGB888 元组，用于绘制颜色而不是图像。你还可以传递一个路径，而不是图像对象，这样此方法会自动从磁盘加载图像并在一步中使用它。例如，draw_image("test.jpg") 。
        x_scale 控制源图像在 x 方向上的缩放比例（浮动类型）。如果该值为负，图像将水平翻转。请注意，如果未指定 y_scale ，则 y_scale 将与 x_scale 相同，以保持图像的纵横比。
        y_scale 控制源图像在 y 方向上的缩放比例（浮动类型）。如果该值为负，图像将垂直翻转。请注意，如果未指定 x_scale ，则 y_scale 将与 x_scale 相同，以保持图像的纵横比。
        roi 是源图像要绘制的感兴趣区域的矩形元组（x、y、w、h）。这允许您仅提取感兴趣区域中的像素以在目标图像上进行缩放和绘制。
        rgb_channel 是要从 RGB565 图像中提取的 RGB 通道（0=红色 R，1=绿色 G，2=蓝色 B），并将其应用到目标图像上。例如，如果传递 rgb_channel=1，则会提取源 RGB565 图像的绿色通道，并以灰度形式应用到目标图像上。
        alpha 控制要混合到目标图像中的源图像的程度。256 的值绘制不透明的源图像，而低于 256 的值会在源图像和目标图像之间产生混合。0 表示不对目标图像进行修改。
        color_palette 如果不为 None，可以是 image.PALETTE_RAINBOW、image.PALETTE_IRONBOW，或一个包含 256 个像素的 RGB565 图像，用作源图像的灰度值的颜色查找表。如果使用了 rgb_channel 提取，则该调色板将在提取后应用。
        alpha_palette 如果不为 None ，可以是一个包含 256 个像素的灰度图像，用作 alpha 调色板，按像素级别调节源图像的 alpha 值，使你能够基于灰度值精确控制像素的透明度。alpha 查找表中像素值为 255 时表示不透明，低于 255 的值则使像素变得更加透明，直到 0。此操作会在使用 rgb_channel 提取之后应用。
        hint 可以是标志的逻辑 OR：
        mask 是另一个图像，用作操作的像素级掩码。
        返回图像对象，以便您可以使用 . 符号调用另一个方法。
        不支持压缩图像或 Bayer/YUV 图像。
        """
        pass
        
        
    def draw_keypoints(self,keypoints,color: int | Tuple[int, int, int] | None = None,size=10,thickness=1,fill=False) -> Image:
        """
        在图像上绘制关键点。你还可以传递一个包含三元组的列表，每个三元组包含（x，y，旋转角度_单位为度），以便重用此方法绘制关键点符号，这些符号是一个圆圈，圆圈中有一条指向特定方向的线。
        color 是 Grayscale 或 RGB565 图像的 RGB888 元组。默认为白色。但是，您还可以传递灰度图像的底层像素值（0-255）或 RGB565 图像的 RGB565 值。
        size 控制关键点的大小。
        thickness 控制线的厚度（以像素为单位）。
        设置 fill 为 True 以填充关键点。
        返回图像对象，以便您可以使用 . 符号调用另一个方法。
        不支持压缩图像或 Bayer 图像。
        """
        pass
        
        
    def flood_fill(self,x: int,y: int,seed_threshold=0.05,floating_threshold=0.05,color: int | Tuple[int, int, int] | None = None,invert=False,clear_background=False,mask: Image | None = None) -> Image:
        """
        从位置 x、y 开始填充图像的一个区域。可以单独传递 x、y，也可以传递元组 (x, y)。
        seed_threshold 控制填充区域中的任何像素与原始起始像素的差异程度。
        floating_threshold 控制填充区域中的任何像素与任何相邻像素的差异程度。
        color 是 Grayscale 或 RGB565 图像的 RGB888 元组。默认为白色。但是，您还可以传递灰度图像的底层像素值（0-255）或 RGB565 图像的 RGB565 值。
        设置 invert 为 True 以重新着色填充连接区域之外的所有内容。
        设置 clear_background 为 True 以将泛色填充未重新着色的其余像素设置为零。
        mask 是另一个图像，用作操作像素级掩码。掩码应该是一个只有黑色或白色像素的图像，大小应与正在操作的图像相同。只有在掩码中设置的像素在进行泛色填充时才会被评估。
        返回图像对象，以便您可以使用 . 符号调用另一个方法。
        不支持压缩图像或 Bayer 图像。
        此方法在 OpenMV Cam M4 上不可用。
        """
        pass
        
        
    def mask_rectange(self,x: int,y: int,w: int,h: int) -> Image:
        """
        将图像的矩形部分置零。如果未提供参数，则此方法将图像的中心置零。
        返回图像对象，以便您可以使用 . 符号调用另一个方法。
        不支持压缩图像或 Bayer 图像。
        """
        pass
        
        
    def mask_circle(self,x: int,y: int,radius: int) -> Image:
        """
        将图像的圆形部分置零。如果未提供参数，则此方法将图像的中心置零。
        返回图像对象，以便您可以使用 . 符号调用另一个方法。
        不支持压缩图像或 Bayer 图像。
        """
        pass
        
        
    def mask_ellipse(self,x: int,y: int,radius_x: int,radius_y: int,rotation_angle_in_degrees: int) -> Image:
        """
        将图像的椭圆形状部分置零。如果未提供参数，则此方法将图像的中心置零。
        返回图像对象，以便您可以使用 . 符号调用另一个方法。
        不支持压缩图像或 Bayer 图像。
        """
        pass
        
        
    def binary(self,thresholds: List[Tuple[int, int]],invert=False,zero=False,mask: Image | None = None,to_bitmap=False,copy=False) -> Image:
        """
        根据像素是否在阈值列表 thresholds 范围内，将图像中的所有像素设置为黑色或白色。
        thresholds 必须是包含元组的列表 [(lo, hi), (lo, hi), ..., (lo, hi)]，定义您要跟踪的颜色范围。对于灰度图像，每个元组都需要包含两个值 - 最小灰度值和最大灰度值。仅将处于这些阈值之间的像素区域视为符合条件。对于 RGB565 图像，每个元组需要有六个值（l_lo、l_hi、a_lo、a_hi、b_lo、b_hi） - 分别是 LAB L、A 和 B 通道的最小值和最大值。为了简化使用，此函数将自动修复颠倒的最小值和最大值。此外，如果元组的长度大于六个值，则其余部分将被忽略。反之，如果元组太短，则其余的阈值被假定为在最大范围内。
        invert 反转阈值操作，使得匹配像素不是在某些已知颜色范围内，而是在已知颜色范围之外。
        将 zero 设置为 True，以零化阈值像素，并保持不在阈值列表中的像素不变。
        mask 是另一个图像，用作像素级掩码以进行操作。掩码应该是一个只有黑色或白色像素的图像，应该与正在操作的图像大小相同。仅修改掩码中设置的像素。
        to_bitmap 将图像数据转换为二进制位图图像，其中每个像素都以 1 位存储。对于非常小的图像，新的位图图像可能无法适应原始图像，需要使用 copy 进行out-of-place 操作。
        copy 如果为True，则在堆上创建二值化图像的副本，而不是修改源图像。
        返回图像对象，以便您可以使用 . 符号调用另一个方法。
        不支持压缩图像或 Bayer 图像。
        """
        pass
        
        
    def invert(self) -> Image:
        """
        翻转（对二进制图像进行反转）图像中的所有像素值。请注意，二进制反转对于图像来说与数值反转是相同的，因为：
        (255 - pixel) % 256 == (255 + ~pixel + 1) % 256 == (~pixel + 256) % 256 == ~pixel，并且这个关系对任何在 (0-2^n-1) 范围内的值成立，而这个范围对于所有可变图像数据类型都是适用的。
        返回图像对象，以便您可以使用 . 符号调用另一个方法。
        不支持压缩图像或 Bayer/YUV 图像。
        """
        pass
        
        
    def b_and(self,image: Image,x: int = 0,y: int = 0,x_scale: float = 1.0,y_scale: float = 1.0,roi: Tuple[int, int, int, int] | None = None,rgb_channel: int = -1,alpha: int = 256,color_palette=None,alpha_palette=None,hint: int = 0,mask: Image | None = None) -> Image:
        """
        计算 image 与此图像的逻辑 AND （例如， a & b ），逐个颜色通道进行操作，从左上角位置 x 、 y 开始。此方法会自动处理传入图像的渲染，将其转换为目标图像的正确像素格式，并无缝处理裁剪。 image 也可以是一个RGB888元组，用于绘制颜色而不是图像。你也可以传递一个路径，而不是图像对象，这样该方法会自动从磁盘加载图像并一步到位地使用它。例如， b_and("test.jpg") 。
        x_scale 控制源图像在 x 方向上的缩放比例（浮动类型）。如果该值为负，图像将水平翻转。请注意，如果未指定 y_scale ，则 y_scale 将与 x_scale 相同，以保持图像的纵横比。
        y_scale 控制源图像在 y 方向上的缩放比例（浮动类型）。如果该值为负，图像将垂直翻转。请注意，如果未指定 x_scale ，则 y_scale 将与 x_scale 相同，以保持图像的纵横比。
        roi 是源图像要绘制的感兴趣区域的矩形元组（x、y、w、h）。这允许您仅提取感兴趣区域中的像素以在目标图像上进行缩放和绘制。
        rgb_channel 是要从 RGB565 图像中提取的 RGB 通道（0=红色 R，1=绿色 G，2=蓝色 B），并将其应用到目标图像上。例如，如果传递 rgb_channel=1，则会提取源 RGB565 图像的绿色通道，并以灰度形式应用到目标图像上。
        alpha 控制要混合到目标图像中的源图像的程度。256 的值绘制不透明的源图像，而低于 256 的值会在源图像和目标图像之间产生混合。0 表示不对目标图像进行修改。
        color_palette 如果不为 None，可以是 image.PALETTE_RAINBOW、image.PALETTE_IRONBOW，或一个包含 256 个像素的 RGB565 图像，用作源图像的灰度值的颜色查找表。如果使用了 rgb_channel 提取，则该调色板将在提取后应用。
        alpha_palette 如果不为 None ，可以是一个包含 256 个像素的灰度图像，用作 alpha 调色板，按像素级别调节源图像的 alpha 值，使你能够基于灰度值精确控制像素的透明度。alpha 查找表中像素值为 255 时表示不透明，低于 255 的值则使像素变得更加透明，直到 0。此操作会在使用 rgb_channel 提取之后应用。
        hint 可以是标志的逻辑 OR：
        mask 是另一个图像，用作操作的像素级掩码。
        返回图像对象，以便您可以使用 . 符号调用另一个方法。
        不支持压缩图像或 Bayer/YUV 图像。
        """
        pass
        
        
    def b_nand(self,image: Image,x: int = 0,y: int = 0,x_scale: float = 1.0,y_scale: float = 1.0,roi: Tuple[int, int, int, int] | None = None,rgb_channel: int = -1,alpha: int = 256,color_palette=None,alpha_palette=None,hint: int = 0,mask: Image | None = None) -> Image:
        """
        计算 image 与此图像的逻辑 NAND （例如， ~(a & b) ），逐个颜色通道进行操作，从左上角位置 x 、 y 开始。此方法会自动处理传入图像的渲染，将其转换为目标图像的正确像素格式，并无缝处理裁剪。 image 也可以是一个RGB888元组，用于绘制颜色而不是图像。你也可以传递一个路径，而不是图像对象，这样该方法会自动从磁盘加载图像并一步到位地使用它。例如， b_nand("test.jpg") 。
        x_scale 控制源图像在 x 方向上的缩放比例（浮动类型）。如果该值为负，图像将水平翻转。请注意，如果未指定 y_scale ，则 y_scale 将与 x_scale 相同，以保持图像的纵横比。
        y_scale 控制源图像在 y 方向上的缩放比例（浮动类型）。如果该值为负，图像将垂直翻转。请注意，如果未指定 x_scale ，则 y_scale 将与 x_scale 相同，以保持图像的纵横比。
        roi 是源图像要绘制的感兴趣区域的矩形元组（x、y、w、h）。这允许您仅提取感兴趣区域中的像素以在目标图像上进行缩放和绘制。
        rgb_channel 是要从 RGB565 图像中提取的 RGB 通道（0=红色 R，1=绿色 G，2=蓝色 B），并将其应用到目标图像上。例如，如果传递 rgb_channel=1，则会提取源 RGB565 图像的绿色通道，并以灰度形式应用到目标图像上。
        alpha 控制要混合到目标图像中的源图像的程度。256 的值绘制不透明的源图像，而低于 256 的值会在源图像和目标图像之间产生混合。0 表示不对目标图像进行修改。
        color_palette 如果不为 None，可以是 image.PALETTE_RAINBOW、image.PALETTE_IRONBOW，或一个包含 256 个像素的 RGB565 图像，用作源图像的灰度值的颜色查找表。如果使用了 rgb_channel 提取，则该调色板将在提取后应用。
        alpha_palette 如果不为 None ，可以是一个包含 256 个像素的灰度图像，用作 alpha 调色板，按像素级别调节源图像的 alpha 值，使你能够基于灰度值精确控制像素的透明度。alpha 查找表中像素值为 255 时表示不透明，低于 255 的值则使像素变得更加透明，直到 0。此操作会在使用 rgb_channel 提取之后应用。
        hint 可以是标志的逻辑 OR：
        mask 是另一个图像，用作操作的像素级掩码。
        返回图像对象，以便您可以使用 . 符号调用另一个方法。
        不支持压缩图像或 Bayer/YUV 图像。
        """
        pass
        
        
    def b_or(self,image: Image,x: int = 0,y: int = 0,x_scale: float = 1.0,y_scale: float = 1.0,roi: Tuple[int, int, int, int] | None = None,rgb_channel: int = -1,alpha: int = 256,color_palette=None,alpha_palette=None,hint: int = 0,mask: Image | None = None) -> Image:
        """
        计算 image 与此图像的逻辑 OR （例如， (a | b) ），逐个颜色通道进行操作，从左上角位置 x 、 y 开始。此方法会自动处理传入图像的渲染，将其转换为目标图像的正确像素格式，并无缝处理裁剪。 image 也可以是一个RGB888元组，用于绘制颜色而不是图像。你也可以传递一个路径，而不是图像对象，这样该方法会自动从磁盘加载图像并一步到位地使用它。例如， b_or("test.jpg") 。
        x_scale 控制源图像在 x 方向上的缩放比例（浮动类型）。如果该值为负，图像将水平翻转。请注意，如果未指定 y_scale ，则 y_scale 将与 x_scale 相同，以保持图像的纵横比。
        y_scale 控制源图像在 y 方向上的缩放比例（浮动类型）。如果该值为负，图像将垂直翻转。请注意，如果未指定 x_scale ，则 y_scale 将与 x_scale 相同，以保持图像的纵横比。
        roi 是源图像要绘制的感兴趣区域的矩形元组（x、y、w、h）。这允许您仅提取感兴趣区域中的像素以在目标图像上进行缩放和绘制。
        rgb_channel 是要从 RGB565 图像中提取的 RGB 通道（0=红色 R，1=绿色 G，2=蓝色 B），并将其应用到目标图像上。例如，如果传递 rgb_channel=1，则会提取源 RGB565 图像的绿色通道，并以灰度形式应用到目标图像上。
        alpha 控制要混合到目标图像中的源图像的程度。256 的值绘制不透明的源图像，而低于 256 的值会在源图像和目标图像之间产生混合。0 表示不对目标图像进行修改。
        color_palette 如果不为 None，可以是 image.PALETTE_RAINBOW、image.PALETTE_IRONBOW，或一个包含 256 个像素的 RGB565 图像，用作源图像的灰度值的颜色查找表。如果使用了 rgb_channel 提取，则该调色板将在提取后应用。
        alpha_palette 如果不为 None ，可以是一个包含 256 个像素的灰度图像，用作 alpha 调色板，按像素级别调节源图像的 alpha 值，使你能够基于灰度值精确控制像素的透明度。alpha 查找表中像素值为 255 时表示不透明，低于 255 的值则使像素变得更加透明，直到 0。此操作会在使用 rgb_channel 提取之后应用。
        hint 可以是标志的逻辑 OR：
        mask 是另一个图像，用作操作的像素级掩码。
        返回图像对象，以便您可以使用 . 符号调用另一个方法。
        不支持压缩图像或 Bayer/YUV 图像。
        """
        pass
        
        
    def b_nor(self,image: Image,x: int = 0,y: int = 0,x_scale: float = 1.0,y_scale: float = 1.0,roi: Tuple[int, int, int, int] | None = None,rgb_channel: int = -1,alpha: int = 256,color_palette=None,alpha_palette=None,hint: int = 0,mask: Image | None = None) -> Image:
        """
        计算 image 与此图像的逻辑 NOR （例如， ~(a | b) ），逐个颜色通道进行操作，从左上角位置 x 、 y 开始。此方法会自动处理传入图像的渲染，将其转换为目标图像的正确像素格式，并无缝处理裁剪。 image 也可以是一个RGB888元组，用于绘制颜色而不是图像。你也可以传递一个路径，而不是图像对象，这样该方法会自动从磁盘加载图像并一步到位地使用它。例如， b_nor("test.jpg") 。
        x_scale 控制源图像在 x 方向上的缩放比例（浮动类型）。如果该值为负，图像将水平翻转。请注意，如果未指定 y_scale ，则 y_scale 将与 x_scale 相同，以保持图像的纵横比。
        y_scale 控制源图像在 y 方向上的缩放比例（浮动类型）。如果该值为负，图像将垂直翻转。请注意，如果未指定 x_scale ，则 y_scale 将与 x_scale 相同，以保持图像的纵横比。
        roi 是源图像要绘制的感兴趣区域的矩形元组（x、y、w、h）。这允许您仅提取感兴趣区域中的像素以在目标图像上进行缩放和绘制。
        rgb_channel 是要从 RGB565 图像中提取的 RGB 通道（0=红色 R，1=绿色 G，2=蓝色 B），并将其应用到目标图像上。例如，如果传递 rgb_channel=1，则会提取源 RGB565 图像的绿色通道，并以灰度形式应用到目标图像上。
        alpha 控制要混合到目标图像中的源图像的程度。256 的值绘制不透明的源图像，而低于 256 的值会在源图像和目标图像之间产生混合。0 表示不对目标图像进行修改。
        color_palette 如果不为 None，可以是 image.PALETTE_RAINBOW、image.PALETTE_IRONBOW，或一个包含 256 个像素的 RGB565 图像，用作源图像的灰度值的颜色查找表。如果使用了 rgb_channel 提取，则该调色板将在提取后应用。
        alpha_palette 如果不为 None ，可以是一个包含 256 个像素的灰度图像，用作 alpha 调色板，按像素级别调节源图像的 alpha 值，使你能够基于灰度值精确控制像素的透明度。alpha 查找表中像素值为 255 时表示不透明，低于 255 的值则使像素变得更加透明，直到 0。此操作会在使用 rgb_channel 提取之后应用。
        hint 可以是标志的逻辑 OR：
        mask 是另一个图像，用作操作的像素级掩码。
        返回图像对象，以便您可以使用 . 符号调用另一个方法。
        不支持压缩图像或 Bayer/YUV 图像。
        """
        pass
        
        
    def b_xor(self,image: Image,x: int = 0,y: int = 0,x_scale: float = 1.0,y_scale: float = 1.0,roi: Tuple[int, int, int, int] | None = None,rgb_channel: int = -1,alpha: int = 256,color_palette=None,alpha_palette=None,hint: int = 0,mask: Image | None = None) -> Image:
        """
        计算 image 与此图像的逻辑 XOR （例如， (a ^ b) ），逐个颜色通道进行操作，从左上角位置 x 、 y 开始。此方法会自动处理传入图像的渲染，将其转换为目标图像的正确像素格式，并无缝处理裁剪。 image 也可以是一个RGB888元组，用于绘制颜色而不是图像。你也可以传递一个路径，而不是图像对象，这样该方法会自动从磁盘加载图像并一步到位地使用它。例如， b_xor("test.jpg") 。
        x_scale 控制源图像在 x 方向上的缩放比例（浮动类型）。如果该值为负，图像将水平翻转。请注意，如果未指定 y_scale ，则 y_scale 将与 x_scale 相同，以保持图像的纵横比。
        y_scale 控制源图像在 y 方向上的缩放比例（浮动类型）。如果该值为负，图像将垂直翻转。请注意，如果未指定 x_scale ，则 y_scale 将与 x_scale 相同，以保持图像的纵横比。
        roi 是源图像要绘制的感兴趣区域的矩形元组（x、y、w、h）。这允许您仅提取感兴趣区域中的像素以在目标图像上进行缩放和绘制。
        rgb_channel 是要从 RGB565 图像中提取的 RGB 通道（0=红色 R，1=绿色 G，2=蓝色 B），并将其应用到目标图像上。例如，如果传递 rgb_channel=1，则会提取源 RGB565 图像的绿色通道，并以灰度形式应用到目标图像上。
        alpha 控制要混合到目标图像中的源图像的程度。256 的值绘制不透明的源图像，而低于 256 的值会在源图像和目标图像之间产生混合。0 表示不对目标图像进行修改。
        color_palette 如果不为 None，可以是 image.PALETTE_RAINBOW、image.PALETTE_IRONBOW，或一个包含 256 个像素的 RGB565 图像，用作源图像的灰度值的颜色查找表。如果使用了 rgb_channel 提取，则该调色板将在提取后应用。
        alpha_palette 如果不为 None ，可以是一个包含 256 个像素的灰度图像，用作 alpha 调色板，按像素级别调节源图像的 alpha 值，使你能够基于灰度值精确控制像素的透明度。alpha 查找表中像素值为 255 时表示不透明，低于 255 的值则使像素变得更加透明，直到 0。此操作会在使用 rgb_channel 提取之后应用。
        hint 可以是标志的逻辑 OR：
        mask 是另一个图像，用作操作的像素级掩码。
        返回图像对象，以便您可以使用 . 符号调用另一个方法。
        不支持压缩图像或 Bayer/YUV 图像。
        """
        pass
        
        
    def b_xnor(self,image: Image,x: int = 0,y: int = 0,x_scale: float = 1.0,y_scale: float = 1.0,roi: Tuple[int, int, int, int] | None = None,rgb_channel: int = -1,alpha: int = 256,color_palette=None,alpha_palette=None,hint: int = 0,mask: Image | None = None) -> Image:
        """
        计算 image 与此图像的逻辑 XNOR （例如， ~(a ^ b) ），逐个颜色通道进行操作，从左上角位置 x 、 y 开始。此方法会自动处理传入图像的渲染，将其转换为目标图像的正确像素格式，并无缝处理裁剪。 image 也可以是一个RGB888元组，用于绘制颜色而不是图像。你也可以传递一个路径，而不是图像对象，这样该方法会自动从磁盘加载图像并一步到位地使用它。例如， b_xnor("test.jpg") 。
        x_scale 控制源图像在 x 方向上的缩放比例（浮动类型）。如果该值为负，图像将水平翻转。请注意，如果未指定 y_scale ，则 y_scale 将与 x_scale 相同，以保持图像的纵横比。
        y_scale 控制源图像在 y 方向上的缩放比例（浮动类型）。如果该值为负，图像将垂直翻转。请注意，如果未指定 x_scale ，则 y_scale 将与 x_scale 相同，以保持图像的纵横比。
        roi 是源图像要绘制的感兴趣区域的矩形元组（x、y、w、h）。这允许您仅提取感兴趣区域中的像素以在目标图像上进行缩放和绘制。
        rgb_channel 是要从 RGB565 图像中提取的 RGB 通道（0=红色 R，1=绿色 G，2=蓝色 B），并将其应用到目标图像上。例如，如果传递 rgb_channel=1，则会提取源 RGB565 图像的绿色通道，并以灰度形式应用到目标图像上。
        alpha 控制要混合到目标图像中的源图像的程度。256 的值绘制不透明的源图像，而低于 256 的值会在源图像和目标图像之间产生混合。0 表示不对目标图像进行修改。
        color_palette 如果不为 None，可以是 image.PALETTE_RAINBOW、image.PALETTE_IRONBOW，或一个包含 256 个像素的 RGB565 图像，用作源图像的灰度值的颜色查找表。如果使用了 rgb_channel 提取，则该调色板将在提取后应用。
        alpha_palette 如果不为 None ，可以是一个包含 256 个像素的灰度图像，用作 alpha 调色板，按像素级别调节源图像的 alpha 值，使你能够基于灰度值精确控制像素的透明度。alpha 查找表中像素值为 255 时表示不透明，低于 255 的值则使像素变得更加透明，直到 0。此操作会在使用 rgb_channel 提取之后应用。
        hint 可以是标志的逻辑 OR：
        mask 是另一个图像，用作操作的像素级掩码。
        返回图像对象，以便您可以使用 . 符号调用另一个方法。
        不支持压缩图像或 Bayer/YUV 图像。
        """
        pass
        
        
    def awb(self,max: bool = False) -> Image:
        """
        使用灰世界算法对图像执行自动白平衡。此方法作用于RAW Bayer图像，因此可以在将图像转换为RGB565或将RAW Bayer图像传递给图像处理函数之前提高图像质量。你也可以在RGB565图像上调用此方法。此方法对二值图像或灰度图像没有任何影响。
        如果 max 为 True，则使用白补丁算法。
        返回图像对象，以便您可以使用 . 符号调用另一个方法。
        不支持压缩图像或YUV图像。
        """
        pass
        
        
    def ccm(self,matrix) -> Image:
        """
        将传递的浮点色彩校正矩阵与图像相乘。矩阵可以是以下形式之一：
        CCM 方法为:
        请注意，3x3 矩阵中每行的总和通常应为 -1、+1 或 0。权重可以是正数或负数。
        您可能希望使用此方法消除颜色通道之间的系统性串扰。或者，对整个图像进行颜色校正。
        返回图像对象，以便您可以使用 . 符号调用另一个方法。
        不支持压缩图像或 Bayer/YUV 图像。
        """
        pass
        
        
    def gamma(self,gamma: float = 1.0,contrast: float = 1.0,brightness: float = 0.0) -> Image:
        """
        快速更改图像的 gamma、对比度和亮度。
        gamma 大于 1.0 的值使图像以非线性方式变暗，而小于 1.0 的值使图像变亮。将 gamma 值应用于图像，将所有像素颜色通道缩放到 [0:1) 并在缩放回来之前对所有像素执行 pow(pixel, 1/gamma) 的重映射。
        contrast 大于 1.0 的值使图像以线性方式变亮，而小于 1.0 的值使图像变暗。将对比度值应用于图像，将所有像素颜色通道缩放到 [0:1) 并在缩放回来之前对所有像素执行 pixel * contrast 的重映射。
        brightness 大于 0.0 的值以恒定方式使图像变亮，而小于 0.0 的值使图像变暗。将亮度值应用于图像，将所有像素颜色通道缩放到 [0:1) 并在缩放回来之前对所有像素执行 pixel + brightness 的重映射。
        返回图像对象，以便您可以使用 . 符号调用另一个方法。
        不支持压缩图像或Bayer/YUV图像。
        """
        pass
        
        
    def gamma_corr(self,gamma: float = 1.0,contrast: float = 1.0,brightness: float = 0.0) -> Image:
        """
        快速更改图像的 gamma、对比度和亮度。
        gamma 大于 1.0 的值使图像以非线性方式变暗，而小于 1.0 的值使图像变亮。将 gamma 值应用于图像，将所有像素颜色通道缩放到 [0:1) 并在缩放回来之前对所有像素执行 pow(pixel, 1/gamma) 的重映射。
        contrast 大于 1.0 的值使图像以线性方式变亮，而小于 1.0 的值使图像变暗。将对比度值应用于图像，将所有像素颜色通道缩放到 [0:1) 并在缩放回来之前对所有像素执行 pixel * contrast 的重映射。
        brightness 大于 0.0 的值以恒定方式使图像变亮，而小于 0.0 的值使图像变暗。将亮度值应用于图像，将所有像素颜色通道缩放到 [0:1) 并在缩放回来之前对所有像素执行 pixel + brightness 的重映射。
        返回图像对象，以便您可以使用 . 符号调用另一个方法。
        不支持压缩图像或Bayer/YUV图像。
        """
        pass
        
        
    def negate(self) -> Image:
        """
        翻转（对二进制图像进行反转）图像中的所有像素值。请注意，二进制反转对于图像来说与数值反转是相同的，因为：
        (255 - pixel) % 256 == (255 + ~pixel + 1) % 256 == (~pixel + 256) % 256 == ~pixel，并且这个关系对任何在 (0-2^n-1) 范围内的值成立，而这个范围对于所有可变图像数据类型都是适用的。
        返回图像对象，以便您可以使用 . 符号调用另一个方法。
        不支持压缩图像或 Bayer/YUV 图像。
        """
        pass
        
        
    def replace(self,image: Image,x: int = 0,y: int = 0,x_scale: float = 1.0,y_scale: float = 1.0,roi: Tuple[int, int, int, int] | None = None,rgb_channel: int = -1,alpha: int = 256,color_palette=None,alpha_palette=None,hint: int = 0,mask: Image | None = None) -> Image:
        """
        绘制一张图像，图像的左上角从位置 x 、 y 开始。此方法会自动处理传入图像的渲染，将其转换为目标图像的正确像素格式，并无缝处理裁剪。 image 也可以是一个RGB888元组，用于绘制颜色而不是图像。你也可以传递一个路径，而不是图像对象，这样该方法会自动从磁盘加载图像并一步到位地使用它。例如， replace("test.jpg") 。
        x_scale 控制源图像在 x 方向上的缩放比例（浮动类型）。如果该值为负，图像将水平翻转。请注意，如果未指定 y_scale ，则 y_scale 将与 x_scale 相同，以保持图像的纵横比。
        y_scale 控制源图像在 y 方向上的缩放比例（浮动类型）。如果该值为负，图像将垂直翻转。请注意，如果未指定 x_scale ，则 y_scale 将与 x_scale 相同，以保持图像的纵横比。
        roi 是源图像要绘制的感兴趣区域的矩形元组（x、y、w、h）。这允许您仅提取感兴趣区域中的像素以在目标图像上进行缩放和绘制。
        rgb_channel 是要从 RGB565 图像中提取的 RGB 通道（0=红色 R，1=绿色 G，2=蓝色 B），并将其应用到目标图像上。例如，如果传递 rgb_channel=1，则会提取源 RGB565 图像的绿色通道，并以灰度形式应用到目标图像上。
        alpha 控制要混合到目标图像中的源图像的程度。256 的值绘制不透明的源图像，而低于 256 的值会在源图像和目标图像之间产生混合。0 表示不对目标图像进行修改。
        color_palette 如果不为 None，可以是 image.PALETTE_RAINBOW、image.PALETTE_IRONBOW，或一个包含 256 个像素的 RGB565 图像，用作源图像的灰度值的颜色查找表。如果使用了 rgb_channel 提取，则该调色板将在提取后应用。
        alpha_palette 如果不为 None ，可以是一个包含 256 个像素的灰度图像，用作 alpha 调色板，按像素级别调节源图像的 alpha 值，使你能够基于灰度值精确控制像素的透明度。alpha 查找表中像素值为 255 时表示不透明，低于 255 的值则使像素变得更加透明，直到 0。此操作会在使用 rgb_channel 提取之后应用。
        hint 可以是标志的逻辑 OR：
        mask 是另一个图像，用作操作的像素级掩码。
        返回图像对象，以便您可以使用 . 符号调用另一个方法。
        不支持压缩图像或 Bayer/YUV 图像。
        """
        pass
        
        
    def assign(self,image: Image,x: int = 0,y: int = 0,x_scale: float = 1.0,y_scale: float = 1.0,roi: Tuple[int, int, int, int] | None = None,rgb_channel: int = -1,alpha: int = 256,color_palette=None,alpha_palette=None,hint: int = 0,mask: Image | None = None) -> Image:
        """
        绘制一张图像，图像的左上角从位置 x 、 y 开始。此方法会自动处理传入图像的渲染，将其转换为目标图像的正确像素格式，并无缝处理裁剪。 image 也可以是一个RGB888元组，用于绘制颜色而不是图像。你也可以传递一个路径，而不是图像对象，这样该方法会自动从磁盘加载图像并一步到位地使用它。例如， assign("test.jpg") 。
        x_scale 控制源图像在 x 方向上的缩放比例（浮动类型）。如果该值为负，图像将水平翻转。请注意，如果未指定 y_scale ，则 y_scale 将与 x_scale 相同，以保持图像的纵横比。
        y_scale 控制源图像在 y 方向上的缩放比例（浮动类型）。如果该值为负，图像将垂直翻转。请注意，如果未指定 x_scale ，则 y_scale 将与 x_scale 相同，以保持图像的纵横比。
        roi 是源图像要绘制的感兴趣区域的矩形元组（x、y、w、h）。这允许您仅提取感兴趣区域中的像素以在目标图像上进行缩放和绘制。
        rgb_channel 是要从 RGB565 图像中提取的 RGB 通道（0=红色 R，1=绿色 G，2=蓝色 B），并将其应用到目标图像上。例如，如果传递 rgb_channel=1，则会提取源 RGB565 图像的绿色通道，并以灰度形式应用到目标图像上。
        alpha 控制要混合到目标图像中的源图像的程度。256 的值绘制不透明的源图像，而低于 256 的值会在源图像和目标图像之间产生混合。0 表示不对目标图像进行修改。
        color_palette 如果不为 None，可以是 image.PALETTE_RAINBOW、image.PALETTE_IRONBOW，或一个包含 256 个像素的 RGB565 图像，用作源图像的灰度值的颜色查找表。如果使用了 rgb_channel 提取，则该调色板将在提取后应用。
        alpha_palette 如果不为 None ，可以是一个包含 256 个像素的灰度图像，用作 alpha 调色板，按像素级别调节源图像的 alpha 值，使你能够基于灰度值精确控制像素的透明度。alpha 查找表中像素值为 255 时表示不透明，低于 255 的值则使像素变得更加透明，直到 0。此操作会在使用 rgb_channel 提取之后应用。
        hint 可以是标志的逻辑 OR：
        mask 是另一个图像，用作操作的像素级掩码。
        返回图像对象，以便您可以使用 . 符号调用另一个方法。
        不支持压缩图像或 Bayer/YUV 图像。
        """
        pass
        
        
    def set(self,image: Image,x: int = 0,y: int = 0,x_scale: float = 1.0,y_scale: float = 1.0,roi: Tuple[int, int, int, int] | None = None,rgb_channel: int = -1,alpha: int = 256,color_palette=None,alpha_palette=None,hint: int = 0,mask: Image | None = None) -> Image:
        """
        绘制一张图像，图像的左上角从位置 x 、 y 开始。此方法会自动处理传入图像的渲染，将其转换为目标图像的正确像素格式，并无缝处理裁剪。 image 也可以是一个RGB888元组，用于绘制颜色而不是图像。你也可以传递一个路径，而不是图像对象，这样该方法会自动从磁盘加载图像并一步到位地使用它。例如， set("test.jpg") 。
        x_scale 控制源图像在 x 方向上的缩放比例（浮动类型）。如果该值为负，图像将水平翻转。请注意，如果未指定 y_scale ，则 y_scale 将与 x_scale 相同，以保持图像的纵横比。
        y_scale 控制源图像在 y 方向上的缩放比例（浮动类型）。如果该值为负，图像将垂直翻转。请注意，如果未指定 x_scale ，则 y_scale 将与 x_scale 相同，以保持图像的纵横比。
        roi 是源图像要绘制的感兴趣区域的矩形元组（x、y、w、h）。这允许您仅提取感兴趣区域中的像素以在目标图像上进行缩放和绘制。
        rgb_channel 是要从 RGB565 图像中提取的 RGB 通道（0=红色 R，1=绿色 G，2=蓝色 B），并将其应用到目标图像上。例如，如果传递 rgb_channel=1，则会提取源 RGB565 图像的绿色通道，并以灰度形式应用到目标图像上。
        alpha 控制要混合到目标图像中的源图像的程度。256 的值绘制不透明的源图像，而低于 256 的值会在源图像和目标图像之间产生混合。0 表示不对目标图像进行修改。
        color_palette 如果不为 None，可以是 image.PALETTE_RAINBOW、image.PALETTE_IRONBOW，或一个包含 256 个像素的 RGB565 图像，用作源图像的灰度值的颜色查找表。如果使用了 rgb_channel 提取，则该调色板将在提取后应用。
        alpha_palette 如果不为 None ，可以是一个包含 256 个像素的灰度图像，用作 alpha 调色板，按像素级别调节源图像的 alpha 值，使你能够基于灰度值精确控制像素的透明度。alpha 查找表中像素值为 255 时表示不透明，低于 255 的值则使像素变得更加透明，直到 0。此操作会在使用 rgb_channel 提取之后应用。
        hint 可以是标志的逻辑 OR：
        mask 是另一个图像，用作操作的像素级掩码。
        返回图像对象，以便您可以使用 . 符号调用另一个方法。
        不支持压缩图像或 Bayer/YUV 图像。
        """
        pass
        
        
    def add(self,image: Image,x: int = 0,y: int = 0,x_scale: float = 1.0,y_scale: float = 1.0,roi: Tuple[int, int, int, int] | None = None,rgb_channel: int = -1,alpha: int = 256,color_palette=None,alpha_palette=None,hint: int = 0,mask: Image | None = None) -> Image:
        """
        按数值将 image 与此图像相加（例如， min(a + b, 255) ），逐个颜色通道进行操作，从左上角位置 x 、 y 开始。此方法会自动处理传入图像的渲染，将其转换为目标图像的正确像素格式，并无缝处理裁剪。 image 也可以是一个RGB888元组，用于绘制颜色而不是图像。你也可以传递一个路径，而不是图像对象，这样该方法会自动从磁盘加载图像并一步到位地使用它。例如， add("test.jpg") 。
        x_scale 控制源图像在 x 方向上的缩放比例（浮动类型）。如果该值为负，图像将水平翻转。请注意，如果未指定 y_scale ，则 y_scale 将与 x_scale 相同，以保持图像的纵横比。
        y_scale 控制源图像在 y 方向上的缩放比例（浮动类型）。如果该值为负，图像将垂直翻转。请注意，如果未指定 x_scale ，则 y_scale 将与 x_scale 相同，以保持图像的纵横比。
        roi 是源图像要绘制的感兴趣区域的矩形元组（x、y、w、h）。这允许您仅提取感兴趣区域中的像素以在目标图像上进行缩放和绘制。
        rgb_channel 是要从 RGB565 图像中提取的 RGB 通道（0=红色 R，1=绿色 G，2=蓝色 B），并将其应用到目标图像上。例如，如果传递 rgb_channel=1，则会提取源 RGB565 图像的绿色通道，并以灰度形式应用到目标图像上。
        alpha 控制要混合到目标图像中的源图像的程度。256 的值绘制不透明的源图像，而低于 256 的值会在源图像和目标图像之间产生混合。0 表示不对目标图像进行修改。
        color_palette 如果不为 None，可以是 image.PALETTE_RAINBOW、image.PALETTE_IRONBOW，或一个包含 256 个像素的 RGB565 图像，用作源图像的灰度值的颜色查找表。如果使用了 rgb_channel 提取，则该调色板将在提取后应用。
        alpha_palette 如果不为 None ，可以是一个包含 256 个像素的灰度图像，用作 alpha 调色板，按像素级别调节源图像的 alpha 值，使你能够基于灰度值精确控制像素的透明度。alpha 查找表中像素值为 255 时表示不透明，低于 255 的值则使像素变得更加透明，直到 0。此操作会在使用 rgb_channel 提取之后应用。
        hint 可以是标志的逻辑 OR：
        mask 是另一个图像，用作操作的像素级掩码。
        返回图像对象，以便您可以使用 . 符号调用另一个方法。
        不支持压缩图像或 Bayer/YUV 图像。
        """
        pass
        
        
    def sub(self,image: Image,x: int = 0,y: int = 0,x_scale: float = 1.0,y_scale: float = 1.0,roi: Tuple[int, int, int, int] | None = None,rgb_channel: int = -1,alpha: int = 256,color_palette=None,alpha_palette=None,hint: int = 0,mask: Image | None = None) -> Image:
        """
        按数值将 image 与此图像相减（例如， max(a - b, 0) ），逐个颜色通道进行操作，从左上角位置 x 、 y 开始。此方法会自动处理传入图像的渲染，将其转换为目标图像的正确像素格式，并无缝处理裁剪。 image 也可以是一个RGB888元组，用于绘制颜色而不是图像。你也可以传递一个路径，而不是图像对象，这样该方法会自动从磁盘加载图像并一步到位地使用它。例如， sub("test.jpg") 。
        x_scale 控制源图像在 x 方向上的缩放比例（浮动类型）。如果该值为负，图像将水平翻转。请注意，如果未指定 y_scale ，则 y_scale 将与 x_scale 相同，以保持图像的纵横比。
        y_scale 控制源图像在 y 方向上的缩放比例（浮动类型）。如果该值为负，图像将垂直翻转。请注意，如果未指定 x_scale ，则 y_scale 将与 x_scale 相同，以保持图像的纵横比。
        roi 是源图像要绘制的感兴趣区域的矩形元组（x、y、w、h）。这允许您仅提取感兴趣区域中的像素以在目标图像上进行缩放和绘制。
        rgb_channel 是要从 RGB565 图像中提取的 RGB 通道（0=红色 R，1=绿色 G，2=蓝色 B），并将其应用到目标图像上。例如，如果传递 rgb_channel=1，则会提取源 RGB565 图像的绿色通道，并以灰度形式应用到目标图像上。
        alpha 控制要混合到目标图像中的源图像的程度。256 的值绘制不透明的源图像，而低于 256 的值会在源图像和目标图像之间产生混合。0 表示不对目标图像进行修改。
        color_palette 如果不为 None，可以是 image.PALETTE_RAINBOW、image.PALETTE_IRONBOW，或一个包含 256 个像素的 RGB565 图像，用作源图像的灰度值的颜色查找表。如果使用了 rgb_channel 提取，则该调色板将在提取后应用。
        alpha_palette 如果不为 None ，可以是一个包含 256 个像素的灰度图像，用作 alpha 调色板，按像素级别调节源图像的 alpha 值，使你能够基于灰度值精确控制像素的透明度。alpha 查找表中像素值为 255 时表示不透明，低于 255 的值则使像素变得更加透明，直到 0。此操作会在使用 rgb_channel 提取之后应用。
        hint 可以是标志的逻辑 OR：
        mask 是另一个图像，用作操作的像素级掩码。
        返回图像对象，以便您可以使用 . 符号调用另一个方法。
        不支持压缩图像或 Bayer/YUV 图像。
        """
        pass
        
        
    def rsub(self,image: Image,x: int = 0,y: int = 0,x_scale: float = 1.0,y_scale: float = 1.0,roi: Tuple[int, int, int, int] | None = None,rgb_channel: int = -1,alpha: int = 256,color_palette=None,alpha_palette=None,hint: int = 0,mask: Image | None = None) -> Image:
        """
        按数值反向将 image 与此图像相减（例如， max(b - a, 0) ），逐个颜色通道进行操作，从左上角位置 x 、 y 开始。此方法会自动处理传入图像的渲染，将其转换为目标图像的正确像素格式，并无缝处理裁剪。 image 也可以是一个RGB888元组，用于绘制颜色而不是图像。你也可以传递一个路径，而不是图像对象，这样该方法会自动从磁盘加载图像并一步到位地使用它。例如， rsub("test.jpg") 。
        x_scale 控制源图像在 x 方向上的缩放比例（浮动类型）。如果该值为负，图像将水平翻转。请注意，如果未指定 y_scale ，则 y_scale 将与 x_scale 相同，以保持图像的纵横比。
        y_scale 控制源图像在 y 方向上的缩放比例（浮动类型）。如果该值为负，图像将垂直翻转。请注意，如果未指定 x_scale ，则 y_scale 将与 x_scale 相同，以保持图像的纵横比。
        roi 是源图像要绘制的感兴趣区域的矩形元组（x、y、w、h）。这允许您仅提取感兴趣区域中的像素以在目标图像上进行缩放和绘制。
        rgb_channel 是要从 RGB565 图像中提取的 RGB 通道（0=红色 R，1=绿色 G，2=蓝色 B），并将其应用到目标图像上。例如，如果传递 rgb_channel=1，则会提取源 RGB565 图像的绿色通道，并以灰度形式应用到目标图像上。
        alpha 控制要混合到目标图像中的源图像的程度。256 的值绘制不透明的源图像，而低于 256 的值会在源图像和目标图像之间产生混合。0 表示不对目标图像进行修改。
        color_palette 如果不为 None，可以是 image.PALETTE_RAINBOW、image.PALETTE_IRONBOW，或一个包含 256 个像素的 RGB565 图像，用作源图像的灰度值的颜色查找表。如果使用了 rgb_channel 提取，则该调色板将在提取后应用。
        alpha_palette 如果不为 None ，可以是一个包含 256 个像素的灰度图像，用作 alpha 调色板，按像素级别调节源图像的 alpha 值，使你能够基于灰度值精确控制像素的透明度。alpha 查找表中像素值为 255 时表示不透明，低于 255 的值则使像素变得更加透明，直到 0。此操作会在使用 rgb_channel 提取之后应用。
        hint 可以是标志的逻辑 OR：
        mask 是另一个图像，用作操作的像素级掩码。
        返回图像对象，以便您可以使用 . 符号调用另一个方法。
        不支持压缩图像或 Bayer/YUV 图像。
        """
        pass
        
        
    def min(self,image: Image,x: int = 0,y: int = 0,x_scale: float = 1.0,y_scale: float = 1.0,roi: Tuple[int, int, int, int] | None = None,rgb_channel: int = -1,alpha: int = 256,color_palette=None,alpha_palette=None,hint: int = 0,mask: Image | None = None) -> Image:
        """
        按数值计算 image 与此图像的最小值（例如， min(a, b) ），逐个颜色通道进行操作，从左上角位置 x 、 y 开始。此方法会自动处理传入图像的渲染，将其转换为目标图像的正确像素格式，并无缝处理裁剪。 image 也可以是一个RGB888元组，用于绘制颜色而不是图像。你也可以传递一个路径，而不是图像对象，这样该方法会自动从磁盘加载图像并一步到位地使用它。例如， min("test.jpg") 。
        x_scale 控制源图像在 x 方向上的缩放比例（浮动类型）。如果该值为负，图像将水平翻转。请注意，如果未指定 y_scale ，则 y_scale 将与 x_scale 相同，以保持图像的纵横比。
        y_scale 控制源图像在 y 方向上的缩放比例（浮动类型）。如果该值为负，图像将垂直翻转。请注意，如果未指定 x_scale ，则 y_scale 将与 x_scale 相同，以保持图像的纵横比。
        roi 是源图像要绘制的感兴趣区域的矩形元组（x、y、w、h）。这允许您仅提取感兴趣区域中的像素以在目标图像上进行缩放和绘制。
        rgb_channel 是要从 RGB565 图像中提取的 RGB 通道（0=红色 R，1=绿色 G，2=蓝色 B），并将其应用到目标图像上。例如，如果传递 rgb_channel=1，则会提取源 RGB565 图像的绿色通道，并以灰度形式应用到目标图像上。
        alpha 控制要混合到目标图像中的源图像的程度。256 的值绘制不透明的源图像，而低于 256 的值会在源图像和目标图像之间产生混合。0 表示不对目标图像进行修改。
        color_palette 如果不为 None，可以是 image.PALETTE_RAINBOW、image.PALETTE_IRONBOW，或一个包含 256 个像素的 RGB565 图像，用作源图像的灰度值的颜色查找表。如果使用了 rgb_channel 提取，则该调色板将在提取后应用。
        alpha_palette 如果不为 None ，可以是一个包含 256 个像素的灰度图像，用作 alpha 调色板，按像素级别调节源图像的 alpha 值，使你能够基于灰度值精确控制像素的透明度。alpha 查找表中像素值为 255 时表示不透明，低于 255 的值则使像素变得更加透明，直到 0。此操作会在使用 rgb_channel 提取之后应用。
        hint 可以是标志的逻辑 OR：
        mask 是另一个图像，用作操作的像素级掩码。
        返回图像对象，以便您可以使用 . 符号调用另一个方法。
        不支持压缩图像或 Bayer/YUV 图像。
        """
        pass
        
        
    def max(self,image: Image,x: int = 0,y: int = 0,x_scale: float = 1.0,y_scale: float = 1.0,roi: Tuple[int, int, int, int] | None = None,rgb_channel: int = -1,alpha: int = 256,color_palette=None,alpha_palette=None,hint: int = 0,mask: Image | None = None) -> Image:
        """
        按数值计算 image 与此图像的最大值（例如， max(a, b) ），逐个颜色通道进行操作，从左上角位置 x 、 y 开始。此方法会自动处理传入图像的渲染，将其转换为目标图像的正确像素格式，并无缝处理裁剪。 image 也可以是一个RGB888元组，用于绘制颜色而不是图像。你也可以传递一个路径，而不是图像对象，这样该方法会自动从磁盘加载图像并一步到位地使用它。例如， max("test.jpg") 。
        x_scale 控制源图像在 x 方向上的缩放比例（浮动类型）。如果该值为负，图像将水平翻转。请注意，如果未指定 y_scale ，则 y_scale 将与 x_scale 相同，以保持图像的纵横比。
        y_scale 控制源图像在 y 方向上的缩放比例（浮动类型）。如果该值为负，图像将垂直翻转。请注意，如果未指定 x_scale ，则 y_scale 将与 x_scale 相同，以保持图像的纵横比。
        roi 是源图像要绘制的感兴趣区域的矩形元组（x、y、w、h）。这允许您仅提取感兴趣区域中的像素以在目标图像上进行缩放和绘制。
        rgb_channel 是要从 RGB565 图像中提取的 RGB 通道（0=红色 R，1=绿色 G，2=蓝色 B），并将其应用到目标图像上。例如，如果传递 rgb_channel=1，则会提取源 RGB565 图像的绿色通道，并以灰度形式应用到目标图像上。
        alpha 控制要混合到目标图像中的源图像的程度。256 的值绘制不透明的源图像，而低于 256 的值会在源图像和目标图像之间产生混合。0 表示不对目标图像进行修改。
        color_palette 如果不为 None，可以是 image.PALETTE_RAINBOW、image.PALETTE_IRONBOW，或一个包含 256 个像素的 RGB565 图像，用作源图像的灰度值的颜色查找表。如果使用了 rgb_channel 提取，则该调色板将在提取后应用。
        alpha_palette 如果不为 None ，可以是一个包含 256 个像素的灰度图像，用作 alpha 调色板，按像素级别调节源图像的 alpha 值，使你能够基于灰度值精确控制像素的透明度。alpha 查找表中像素值为 255 时表示不透明，低于 255 的值则使像素变得更加透明，直到 0。此操作会在使用 rgb_channel 提取之后应用。
        hint 可以是标志的逻辑 OR：
        mask 是另一个图像，用作操作的像素级掩码。
        返回图像对象，以便您可以使用 . 符号调用另一个方法。
        不支持压缩图像或 Bayer/YUV 图像。
        """
        pass
        
        
    def difference(self,image: Image,x: int = 0,y: int = 0,x_scale: float = 1.0,y_scale: float = 1.0,roi: Tuple[int, int, int, int] | None = None,rgb_channel: int = -1,alpha: int = 256,color_palette=None,alpha_palette=None,hint: int = 0,mask: Image | None = None) -> Image:
        """
        按数值计算 image 与此图像的绝对差值（例如， |a - b| ），逐个颜色通道进行操作，从左上角位置 x 、 y 开始。此方法会自动处理传入图像的渲染，将其转换为目标图像的正确像素格式，并无缝处理裁剪。 image 也可以是一个RGB888元组，用于绘制颜色而不是图像。你也可以传递一个路径，而不是图像对象，这样该方法会自动从磁盘加载图像并一步到位地使用它。例如， difference("test.jpg") 。
        x_scale 控制源图像在 x 方向上的缩放比例（浮动类型）。如果该值为负，图像将水平翻转。请注意，如果未指定 y_scale ，则 y_scale 将与 x_scale 相同，以保持图像的纵横比。
        y_scale 控制源图像在 y 方向上的缩放比例（浮动类型）。如果该值为负，图像将垂直翻转。请注意，如果未指定 x_scale ，则 y_scale 将与 x_scale 相同，以保持图像的纵横比。
        roi 是源图像要绘制的感兴趣区域的矩形元组（x、y、w、h）。这允许您仅提取感兴趣区域中的像素以在目标图像上进行缩放和绘制。
        rgb_channel 是要从 RGB565 图像中提取的 RGB 通道（0=红色 R，1=绿色 G，2=蓝色 B），并将其应用到目标图像上。例如，如果传递 rgb_channel=1，则会提取源 RGB565 图像的绿色通道，并以灰度形式应用到目标图像上。
        alpha 控制要混合到目标图像中的源图像的程度。256 的值绘制不透明的源图像，而低于 256 的值会在源图像和目标图像之间产生混合。0 表示不对目标图像进行修改。
        color_palette 如果不为 None，可以是 image.PALETTE_RAINBOW、image.PALETTE_IRONBOW，或一个包含 256 个像素的 RGB565 图像，用作源图像的灰度值的颜色查找表。如果使用了 rgb_channel 提取，则该调色板将在提取后应用。
        alpha_palette 如果不为 None ，可以是一个包含 256 个像素的灰度图像，用作 alpha 调色板，按像素级别调节源图像的 alpha 值，使你能够基于灰度值精确控制像素的透明度。alpha 查找表中像素值为 255 时表示不透明，低于 255 的值则使像素变得更加透明，直到 0。此操作会在使用 rgb_channel 提取之后应用。
        hint 可以是标志的逻辑 OR：
        mask 是另一个图像，用作操作的像素级掩码。
        返回图像对象，以便您可以使用 . 符号调用另一个方法。
        不支持压缩图像或 Bayer/YUV 图像。
        """
        pass
        
        
    def blend(self,image: Image,x: int = 0,y: int = 0,x_scale: float = 1.0,y_scale: float = 1.0,roi: Tuple[int, int, int, int] | None = None,rgb_channel: int = -1,alpha: int = 256,color_palette=None,alpha_palette=None,hint: int = 0,mask: Image | None = None) -> Image:
        """
        绘制一张图像，图像的左上角从位置 x 、 y 开始。此方法会自动处理传入图像的渲染，将其转换为目标图像的正确像素格式，并无缝处理裁剪。 image 也可以是一个RGB888元组，用于绘制颜色而不是图像。你也可以传递一个路径，而不是图像对象，这样该方法会自动从磁盘加载图像并一步到位地使用它。例如，blend("test.jpg") 。
        x_scale 控制源图像在 x 方向上的缩放比例（浮动类型）。如果该值为负，图像将水平翻转。请注意，如果未指定 y_scale ，则 y_scale 将与 x_scale 相同，以保持图像的纵横比。
        y_scale 控制源图像在 y 方向上的缩放比例（浮动类型）。如果该值为负，图像将垂直翻转。请注意，如果未指定 x_scale ，则 y_scale 将与 x_scale 相同，以保持图像的纵横比。
        roi 是源图像要绘制的感兴趣区域的矩形元组（x、y、w、h）。这允许您仅提取感兴趣区域中的像素以在目标图像上进行缩放和绘制。
        rgb_channel 是要从 RGB565 图像中提取的 RGB 通道（0=红色 R，1=绿色 G，2=蓝色 B），并将其应用到目标图像上。例如，如果传递 rgb_channel=1，则会提取源 RGB565 图像的绿色通道，并以灰度形式应用到目标图像上。
        alpha 控制要混合到目标图像中的源图像的程度。256 的值绘制不透明的源图像，而低于 256 的值会在源图像和目标图像之间产生混合。0 表示不对目标图像进行修改。
        color_palette 如果不为 None，可以是 image.PALETTE_RAINBOW、image.PALETTE_IRONBOW，或一个包含 256 个像素的 RGB565 图像，用作源图像的灰度值的颜色查找表。如果使用了 rgb_channel 提取，则该调色板将在提取后应用。
        alpha_palette 如果不为 None ，可以是一个包含 256 个像素的灰度图像，用作 alpha 调色板，按像素级别调节源图像的 alpha 值，使你能够基于灰度值精确控制像素的透明度。alpha 查找表中像素值为 255 时表示不透明，低于 255 的值则使像素变得更加透明，直到 0。此操作会在使用 rgb_channel 提取之后应用。
        hint 可以是标志的逻辑 OR：
        mask 是另一个图像，用作操作的像素级掩码。
        返回图像对象，以便您可以使用 . 符号调用另一个方法。
        不支持压缩图像或 Bayer/YUV 图像。
        """
        pass
        
        
    def histeq(self,adaptive=False,clip_limit=-1,mask: Image | None = None) -> Image:
        """
        在图像上运行直方图均衡算法。直方图均衡将图像中的对比度和亮度标准化。
        如果将 adaptive 设置为 True，则会在图像上运行自适应直方图均衡方法，其结果通常比非自适应直方图均衡具有更好的结果，但运行时间较长。
        clip_limit 提供了一种限制自适应直方图均衡的对比度的方法。使用一个较小的值，如 10，可以产生对比度限制良好的直方图均衡的图像。
        mask 是另一个图像，用作像素级掩码以进行操作。掩码应该是一个只有黑色或白色像素的图像，应该与正在操作的图像大小相同。仅修改掩码中设置的像素。
        返回图像对象，以便您可以使用 . 符号调用另一个方法。
        不支持压缩图像或 Bayer 图像。
        """
        pass
        
        
    def erode(self,size: int,threshold: int | None = None,mask: Image | None = None) -> Image:
        """
        移除分段区域的边缘像素。
        此方法通过对图像进行卷积，使用一个大小为 ((size*2)+1) x ((size*2)+1) 的内核，并在相邻像素的和大于 threshold 时，将内核的中心像素置为零。
        如果没有设置 threshold ，此方法的工作方式与标准的腐蚀（erode）方法相同。如果设置了 threshold ，则可以指定仅对内核区域中清晰像素超过指定数量的像素进行腐蚀，例如，当内核区域中有超过2个清晰像素且阈值为2时，才执行腐蚀操作。
        mask 是另一个图像，用作像素级掩码以进行操作。掩码应该是一个只有黑色或白色像素的图像，应该与正在操作的图像大小相同。仅修改掩码中设置的像素。
        返回图像对象，以便您可以使用 . 符号调用另一个方法。
        不支持压缩图像或 Bayer/YUV 图像。
        """
        pass
        
        
    def dilate(self,size: int,threshold: int | None = None,mask: Image | None = None) -> Image:
        """
        在分段区域的边缘添加像素。
        此方法通过对图像进行卷积，使用一个大小为 ((size*2)+1) x ((size*2)+1) 的内核，并在相邻像素的和大于 threshold 时，将内核的中心像素设置为1（或“激活”）。
        如果没有设置 threshold ，此方法的工作方式与标准的膨胀（dilate）方法相同。如果设置了 threshold ，则可以指定仅对内核区域中有超过指定数量已激活像素的像素进行膨胀操作。例如，当内核区域中有超过2个激活像素，且阈值为2时，才执行膨胀操作。
        mask 是另一个图像，用作像素级掩码以进行操作。掩码应该是一个只有黑色或白色像素的图像，应该与正在操作的图像大小相同。仅修改掩码中设置的像素。
        返回图像对象，以便您可以使用 . 符号调用另一个方法。
        不支持压缩图像或 Bayer/YUV 图像。
        """
        pass
        
        
    def open(self,size: int,threshold: int | None = None,mask: Image | None = None) -> Image:
        """
        依次执行图像上的腐蚀和膨胀。有关更多信息，请参阅 Image.erode() 和 Image.dilate()。
        mask 是另一个图像，用作像素级掩码以进行操作。掩码应该是一个只有黑色或白色像素的图像，应该与正在操作的图像大小相同。仅修改掩码中设置的像素。
        返回图像对象，以便您可以使用 . 符号调用另一个方法。
        不支持压缩图像或 Bayer/YUV 图像。
        """
        pass
        
        
    def close(self,size: int,threshold: int | None = None,mask: Image | None = None) -> Image:
        """
        依次执行图像上的膨胀和腐蚀。有关更多信息，请参阅 Image.dilate() 和 Image.erode()。
        mask 是另一个图像，用作像素级掩码以进行操作。掩码应该是一个只有黑色或白色像素的图像，应该与正在操作的图像大小相同。仅修改掩码中设置的像素。
        返回图像对象，以便您可以使用 . 符号调用另一个方法。
        不支持压缩图像或 Bayer/YUV 图像。
        """
        pass
        
        
    def top_hat(self,size: int,threshold: int | None = None,mask: Image | None = None) -> Image:
        """
        返回图像与 Image.open() 的图像之间的差异。
        mask 是另一个图像，用作像素级掩码以进行操作。掩码应该是一个只有黑色或白色像素的图像，应该与正在操作的图像大小相同。仅修改掩码中设置的像素。
        不支持压缩图像或 Bayer/YUV 图像。
        """
        pass
        
        
    def black_hat(self,size: int,threshold: int | None = None,mask: Image | None = None) -> Image:
        """
        返回图像与 Image.close() 的图像之间的差异。
        mask 是另一个图像，用作像素级掩码以进行操作。掩码应该是一个只有黑色或白色像素的图像，应该与正在操作的图像大小相同。仅修改掩码中设置的像素。
        不支持压缩图像或 Bayer/YUV 图像。
        """
        pass
        
        
    def mean(self,size: int,threshold: bool | None = False,offset: int | None = 0,invert: bool | None = False,mask: Image | None = None) -> Image:
        """
        使用框滤波器进行标准均值模糊滤波。
        size 是内核大小。使用 1 (3x3 内核)，2 (5x5 内核)，等等。
        如果您想要在滤波器输出端对图像自适应阈值处理，您可以传递 threshold=True，这将启用自适应阈值化，根据像素的亮度与周围像素的内核亮度之间的关系将像素设置为一或零。负 offset 值会随着您将其设置为负值而将更多像素设置为 1，而正值仅将最锐利的对比度变化设置为 1。设置 invert 以反转二值图像的输出结果。
        mask 是另一个图像，用作像素级掩码以进行操作。掩码应该是一个只有黑色或白色像素的图像，应该与正在操作的图像大小相同。仅修改掩码中设置的像素。
        返回图像对象，以便您可以使用 . 符号调用另一个方法。
        不支持压缩图像或 Bayer/YUV 图像。
        """
        pass
        
        
    def median(self,size: int,percentile: float | None = 0.5,threshold: bool | None = False,offset: int | None = 0,invert: bool | None = False,mask: Image | None = None) -> Image:
        """
        在图像上运行中值滤波器。中值滤波器是平滑表面同时保持边缘的最佳滤波器，但速度很慢。
        size 是内核大小。使用 1 (3x3 内核)，2 (5x5 内核)，等等。
        percentile 控制内核中使用的值的百分位数。默认情况下，每个像素将替换为其邻居的第 50个 百分位数（中心）。您可以将此设置为 0 进行最小值滤波器，0.25 进行下四分位数滤波器，0.75 进行上四分位数滤波器，以及 1.0 进行最大值滤波器。
        如果您想要在滤波器输出端对图像自适应阈值处理，您可以传递 threshold=True，这将启用自适应阈值化，根据像素的亮度与周围像素的内核亮度之间的关系将像素设置为一或零。负 offset 值会随着您将其设置为负值而将更多像素设置为 1，而正值仅将最锐利的对比度变化设置为 1。设置 invert 以反转二值图像的输出结果。
        mask 是另一个图像，用作像素级掩码以进行操作。掩码应该是一个只有黑色或白色像素的图像，应该与正在操作的图像大小相同。仅修改掩码中设置的像素。
        返回图像对象，以便您可以使用 . 符号调用另一个方法。
        不支持压缩图像或 Bayer/YUV 图像。
        """
        pass
        
        
    def mode(self,size: int,threshold: bool | None = False,offset: int | None = 0,invert: bool | None = False,mask: Image | None = Nonee) -> Image:
        """
        通过将每个像素替换为其邻居的模式来运行模式滤波器。该方法在灰度图像上效果很好。但是，在 RGB 图像上，由于操作的非线性特性，它在边缘上产生许多伪影。
        size 是内核大小。使用 1 (3x3 内核)，2 (5x5 内核)，等等。
        如果您想要在滤波器输出端对图像自适应阈值处理，您可以传递 threshold=True，这将启用自适应阈值化，根据像素的亮度与周围像素的内核亮度之间的关系将像素设置为一或零。负 offset 值会随着您将其设置为负值而将更多像素设置为 1，而正值仅将最锐利的对比度变化设置为 1。设置 invert 以反转二值图像的输出结果。
        mask 是另一个图像，用作像素级掩码以进行操作。掩码应该是一个只有黑色或白色像素的图像，应该与正在操作的图像大小相同。仅修改掩码中设置的像素。
        返回图像对象，以便您可以使用 . 符号调用另一个方法。
        不支持压缩图像或 Bayer/YUV 图像。
        """
        pass
        
        
    def midpoint(self,size: int,bias: float | None = 0.5,threshold: bool | None = False,offset: int | None = 0,invert: bool | None = False,mask: Image | None = None) -> Image:
        """
        在图像上运行中点滤波器。该滤波器在图像中的每个像素邻域中找到中点((max-min)/2)。
        size 是内核大小。使用 1 (3x3 内核)，2 (5x5 内核)，等等。
        bias 控制最小/最大混合。0 仅用于最小滤波，1.0 仅用于最大滤波。通过使用 bias 您可以对图像进行最小/最大滤波。
        如果您想要在滤波器输出端对图像自适应阈值处理，您可以传递 threshold=True，这将启用自适应阈值化，根据像素的亮度与周围像素的内核亮度之间的关系将像素设置为一或零。负 offset 值会随着您将其设置为负值而将更多像素设置为 1，而正值仅将最锐利的对比度变化设置为 1。设置 invert 以反转二值图像的输出结果。
        mask 是另一个图像，用作像素级掩码以进行操作。掩码应该是一个只有黑色或白色像素的图像，应该与正在操作的图像大小相同。仅修改掩码中设置的像素。
        返回图像对象，以便您可以使用 . 符号调用另一个方法。
        不支持压缩图像或 Bayer/YUV 图像。
        """
        pass
        
        
    def morph(self,size: int,kernel: list,mul: float | None = 1.0,add: float | None = 0.0,threshold: bool | None = False,offset: int | None = 0,invert: bool | None = False,mask: Image | None = None) -> Image:
        """
        使用滤波器内核对图像进行卷积。这允许您在图像上进行常规用途的卷积。
        size 控制内核的大小，内核的尺寸必须为 ((size*2)+1) x ((size*2)+1) 元素。
        kernel 是用于卷积图像的内核。内核可以是 1D 元组或列表，也可以是 2D 元组或列表。对于 1D 内核，元组/列表的大小必须为 ((size*2)+1) x ((size*2)+1) 元素。对于 2D 元组/列表，每行必须有 ((size*2)+1) 个元素，并且必须有 ((size*2)+1) 行。
        mul 允许你进行全局对比度调整。它的值应该大于 0.0。默认值为 1.0，表示不做任何调整。
        add 允许你进行全局亮度调整。它的值应该在 0.0 到 1.0 之间。默认值为 0.0，表示不做任何调整。
        如果您想要在滤波器输出端对图像自适应阈值处理，您可以传递 threshold=True，这将启用自适应阈值化，根据像素的亮度与周围像素的内核亮度之间的关系将像素设置为一或零。负 offset 值会随着您将其设置为负值而将更多像素设置为 1，而正值仅将最锐利的对比度变化设置为 1。设置 invert 以反转二值图像的输出结果。
        mask 是另一个图像，用作像素级掩码以进行操作。掩码应该是一个只有黑色或白色像素的图像，应该与正在操作的图像大小相同。仅修改掩码中设置的像素。
        返回图像对象，以便您可以使用 . 符号调用另一个方法。
        不支持压缩图像或 Bayer/YUV 图像。
        """
        pass
        
        
    def gaussian(self,size: int,unsharp: bool | None = False,mul: float | None = 1.0,add: float | None = 0.0,threshold: bool | None = False,offset: int | None = 0,invert: bool | None = False,mask: Image | None = None) -> Image:
        """
        使用平滑的高斯内核对图像进行卷积。
        size 是内核大小。使用 1 (3x3 内核)，2 (5x5 内核)，等等。
        如果 unsharp 设置为True，则此方法不仅执行高斯滤波操作，还会执行反锐化掩模（unsharp mask）操作，从而增强图像边缘的锐度。
        mul 允许你进行全局对比度调整。它的值应该大于 0.0。默认值为 1.0，表示不做任何调整。
        add 允许你进行全局亮度调整。它的值应该在 0.0 到 1.0 之间。默认值为 0.0，表示不做任何调整。
        如果您想要在滤波器输出端对图像自适应阈值处理，您可以传递 threshold=True，这将启用自适应阈值化，根据像素的亮度与周围像素的内核亮度之间的关系将像素设置为一或零。负 offset 值会随着您将其设置为负值而将更多像素设置为 1，而正值仅将最锐利的对比度变化设置为 1。设置 invert 以反转二值图像的输出结果。
        mask 是另一个图像，用作像素级掩码以进行操作。掩码应该是一个只有黑色或白色像素的图像，应该与正在操作的图像大小相同。仅修改掩码中设置的像素。
        返回图像对象，以便您可以使用 . 符号调用另一个方法。
        不支持压缩图像或 Bayer/YUV 图像。
        """
        pass
        
        
    def laplacian(self,size: int,sharpen: bool | None = False,mul: float | None = 1.0,add: float | None = 0.0,threshold: bool | None = False,offset: int | None = 0,invert: bool | None = False,mask: Image | None = None) -> Image:
        """
        不支持压缩图像或 Bayer/YUV 图像。
        """
        pass
        
        
    def bilateral(self,size: int,color_sigma: float | None = 0.1,space_sigma: float | None = 1.0,threshold: bool | None = False,offset: int | None = 0,invert: bool | None = False,mask: Image | None = None) -> Image:
        """
        使用双边滤波器对图像进行卷积。双边滤波器平滑图像同时保持图像中的边缘。
        size 是内核大小。使用 1 (3x3 内核)，2 (5x5 内核)，等等。
        color_sigma 控制使用双边滤波器时颜色匹配的紧密程度。增加此值可增加颜色模糊。
        space_sigma 控制像素空间之间模糊程度。增加此值可增加像素模糊。
        如果您想要在滤波器输出端对图像自适应阈值处理，您可以传递 threshold=True，这将启用自适应阈值化，根据像素的亮度与周围像素的内核亮度之间的关系将像素设置为一或零。负 offset 值会随着您将其设置为负值而将更多像素设置为 1，而正值仅将最锐利的对比度变化设置为 1。设置 invert 以反转二值图像的输出结果。
        mask 是另一个图像，用作像素级掩码以进行操作。掩码应该是一个只有黑色或白色像素的图像，应该与正在操作的图像大小相同。仅修改掩码中设置的像素。
        返回图像对象，以便您可以使用 . 符号调用另一个方法。
        不支持压缩图像或 Bayer/YUV 图像。
        """
        pass
        
        
    def linpolar(self,reverse: bool = False) -> Image:
        """
        将图像从笛卡尔坐标重新投影到线性极坐标。
        设置 reverse=True 以在相反方向重新投影。
        线性极坐标重新投影将图像的旋转转换为 x 平移。
        不支持压缩图像或 Bayer 图像。
        此方法在 OpenMV Cam M4 上不可用。
        """
        pass
        
        
    def logpolar(self,reverse: bool = False) -> Image:
        """
        将图像从笛卡尔坐标重新投影到对数极坐标。
        设置 reverse=True 以在相反方向重新投影。
        对数极坐标重新投影将图像的旋转转换为 x 平移，并将缩放/缩放转换为 y 平移。
        不支持压缩图像或 Bayer 图像。
        此方法在 OpenMV Cam M4 上不可用。
        """
        pass
        
        
    def lens_corr(self,strength: float = 1.8,zoom: float = 1.0,x_corr: float = 0.0,y_corr: float = 0.0) -> Image:
        """
        对图像进行镜头校正，以消除由于镜头畸变而产生的鱼眼效果。
        strength 是一个浮点数，定义了要对图像进行多少程度的鱼眼效果消除。默认为 1.8，您可以从这个值开始，并根据需要增加或减少，直到图像看起来良好为止。
        zoom 是图像缩放的大小。默认为 1.0。
        x_corr 是从中心点偏移的浮点像素值。可以是负数或正数。
        y_corr 是从中心点偏移的浮点像素值。可以是负数或正数。
        返回图像对象，以便您可以使用 . 符号调用另一个方法。
        不支持压缩图像或 Bayer 图像。
        """
        pass
        
        
    def rotation_corr(self,x_rotation=0.0,y_rotation=0.0,z_rotation=0.0,x_translation=0.0,y_translation=0.0,zoom=1.0,fov=60.0,corners: List[Tuple[int, int]] | None = None) -> Image:
        """
        通过对帧缓冲区进行3D旋转来校正图像的透视问题。
        x_rotation 是在帧缓冲区中旋转图像的度数，绕x轴旋转（即上下旋转图像）。
        y_rotation 是在帧缓冲区中旋转图像的度数，绕y轴旋转（即左右旋转图像）。
        z_rotation 是在帧缓冲区中旋转图像的度数，绕z轴旋转（即原地旋转图像）。
        x_translation 是旋转后将图像向左或向右移动的单位数。由于此平移是在3D空间中应用的，单位不是像素…
        y_translation 是旋转后将图像向上或向下移动的单位数。由于此平移是在3D空间中应用的，单位不是像素…
        zoom 是图像缩放的大小。默认为 1.0。
        fov 是在3D空间中旋转图像之前进行2D->3D投影时使用的内部视场。当此值接近0时，图像被放置在视口的无限远处。当此值接近180时，图像被放置在视口内部。通常情况下，您不应更改此值，但可以修改它以更改2D->3D映射效果。
        corners 是一个包含四个(x,y)元组的列表，表示用于创建四点对应单应性的四个角，第一个角映射到(0,0)，第二个角映射到(image_width-1,0)，第三个角映射到(image_width-1,image_height-1)，第四个角映射到(0,image_height-1)。然后在图像重新映射后应用3D旋转。此参数允许您可以使用 rotation_corr 执行类似鸟瞰变换的操作。例如:
        返回图像对象，以便您可以使用 . 符号调用另一个方法。
        不支持压缩图像或 Bayer 图像。
        此方法在 OpenMV Cam M4 上不可用。
        """
        pass
        
        
    def get_similarity(self,image: Image,x: int | None = 0,y: int | None = 0,x_scale: float = 1.0,y_scale: float = 1.0,roi: Tuple[int, int, int, int] | None = None,rgb_channel: int = -1,alpha: int = 256,color_palette=None,alpha_palette=None,hint: int = 0,dssim: bool = False) -> Similarity:
        """
        计算两张图像之间的相似度。相似度是通过使用结构相似性指数（SSIM）来计算的。SSIM 是一种度量方法，用于比较两张图像之间的结构相似性。SSIM 的值范围在 -1 和 1 之间。值为 1 表示两张图像完全相同，值为 0 表示两张图像不相似，值为 -1 表示两张图像完全相反。通常，如果你想检查两张图像是否不同，应该查看 SSIM 值的负值程度。
        image 是要进行比较的图像。
        你也可以传递一个路径，而不是图像对象，这样该方法会自动从磁盘加载图像并一步到位地使用它。例如，get_similarity("test.jpg")。
        x 是开始比较图像的 x 偏移量。
        y 是开始比较图像的 y 偏移量。
        x_scale 控制源图像在 x 方向上的缩放比例（浮动类型）。如果该值为负，图像将水平翻转。请注意，如果未指定 y_scale ，则 y_scale 将与 x_scale 相同，以保持图像的纵横比。
        y_scale 控制源图像在 y 方向上的缩放比例（浮动类型）。如果该值为负，图像将垂直翻转。请注意，如果未指定 x_scale ，则 y_scale 将与 x_scale 相同，以保持图像的纵横比。
        roi 是源图像的感兴趣区域（ROI）矩形元组 (x, y, w, h)。它允许你仅提取 ROI 区域内的像素。
        rgb_channel 是要从 RGB565 图像中提取的 RGB 通道（0=红色，1=绿色，2=蓝色）。例如，如果传递 rgb_channel=1 ，则会提取源 RGB565 图像的绿色通道并将其应用为灰度图像。
        alpha 控制源图像与目标图像的混合程度。值为 256 时表示完全不透明的源图像，而值小于 256 时会在源图像和目标图像之间进行混合。值为 0 时表示仅显示目标图像。
        color_palette 如果不为 None，可以是 image.PALETTE_RAINBOW、image.PALETTE_IRONBOW，或一个包含 256 个像素的 RGB565 图像，用作源图像的灰度值的颜色查找表。如果使用了 rgb_channel 提取，则该调色板将在提取后应用。
        alpha_palette 如果不是 None，可以是一个包含 256 个像素的灰度图像，用作 alpha 调色板。该调色板会根据每个像素的灰度值调节源图像的 alpha 值，允许你在像素级别上精确控制透明度。调色板中的像素值为 255 时表示完全不透明，而任何小于 255 的值会使该像素逐渐变得更加透明，直到 0 完全透明。如果使用了 rgb_channel 提取，这将在该提取后应用。
        hint 可以是标志的逻辑 OR：
        dssim 如果设置为 true，将计算结构性不相似度指数（DSSIM）而不是 SSIM。值为 0 表示图像完全相同，值为 1 表示图像完全不同。
        返回一个 image.Similarity 对象。
        """
        pass
        
        
    def get_histogram(self,thresholds: List[Tuple[int, int]] | None = None,invert=False,roi: Tuple[int, int, int, int] | None = None,bins=256,l_bins=256,a_bins=256,b_bins=256,difference: Image | None = None) -> histogram:
        """
        计算 roi 中所有颜色通道的归一化直方图，并返回一个 image.histogram 对象。请参阅 image.histogram 对象获取更多信息。您还可以通过使用 Image.get_hist() 或 Image.histogram() 来调用此方法。如果传递了 thresholds 的列表，则直方图信息将仅计算来自阈值列表内的像素。
        thresholds 必须是包含元组的列表 [(lo, hi), (lo, hi), ..., (lo, hi)]，定义您要跟踪的颜色范围。对于灰度图像，每个元组都需要包含两个值 - 最小灰度值和最大灰度值。仅将处于这些阈值之间的像素区域视为符合条件。对于 RGB565 图像，每个元组需要有六个值（l_lo、l_hi、a_lo、a_hi、b_lo、b_hi） - 分别是 LAB L、A 和 B 通道的最小值和最大值。为了简化使用，此函数将自动修复颠倒的最小值和最大值。此外，如果元组的长度大于六个值，则其余部分将被忽略。反之，如果元组太短，则其余的阈值被假定为在最大范围内。
        invert 反转阈值操作，使得匹配像素不是在某些已知颜色范围内，而是在已知颜色范围之外。
        除非您需要对颜色统计执行一些高级操作，否则只需使用 Image.get_statistics() 方法而不是此方法来查看图像中的像素区域。
        roi 是感兴趣区域的矩形元组(x, y, w, h)。如果未指定，则等于图像矩形。仅操作 roi 内的像素。
        bins 和其他参数是用于直方图通道的 bin 数量。对于灰度图像使用 bins，对于 RGB565 图像则使用其他参数分别设置每个通道的 bin 数量。每个通道的 bin 数量必须大于 2。此外，将 bin 数量设置为大于每个通道的唯一像素值数量是没有意义的。默认情况下，直方图将使用每个通道的最大 bin 数量。
        可以设置 difference 为一个图像对象，以使此方法对当前图像和 difference 图像对象之间的差异图像上操作。这样可以避免使用单独的缓冲区。
        不支持压缩图像或 Bayer 图像。
        """
        pass
        
        
    def get_statistics(self,thresholds: List[Tuple[int, int]] | None = None,invert=False,roi: Tuple[int, int, int, int] | None = None,bins=256,l_bins=256,a_bins=256,b_bins=256,difference: Image | None = None) -> statistics:
        """
        计算 roi 中所有颜色通道的均值、中位数、模式、标准差、最小值、最大值、下四分位数和上四分位数，并返回一个 image.statistics 对象。更多信息请参阅 image.statistics 对象。也可以通过 Image.get_stats() 或 Image.statistics() 调用此方法。如果传递了 thresholds 的列表，则直方图信息将仅计算在阈值列表内的像素。
        thresholds 必须是包含元组的列表 [(lo, hi), (lo, hi), ..., (lo, hi)]，定义您要跟踪的颜色范围。对于灰度图像，每个元组都需要包含两个值 - 最小灰度值和最大灰度值。仅将处于这些阈值之间的像素区域视为符合条件。对于 RGB565 图像，每个元组需要有六个值（l_lo、l_hi、a_lo、a_hi、b_lo、b_hi） - 分别是 LAB L、A 和 B 通道的最小值和最大值。为了简化使用，此函数将自动修复颠倒的最小值和最大值。此外，如果元组的长度大于六个值，则其余部分将被忽略。反之，如果元组太短，则其余的阈值被假定为在最大范围内。
        invert 反转阈值操作，使得匹配像素不是在某些已知颜色范围内，而是在已知颜色范围之外。
        每当需要获取图像中像素区域的值的信息时，您都会使用此方法。例如，如果您正在使用帧差法检测运动，那么您将使用此方法来确定图像的颜色通道的变化以触发您的运动检测阈值。
        roi 是感兴趣区域的矩形元组(x, y, w, h)。如果未指定，则等于图像矩形。仅操作 roi 内的像素。
        bins 和其他参数是用于直方图通道的 bin 数量。对于灰度图像使用 bins，对于 RGB565 图像则使用其他参数分别设置每个通道的 bin 数量。每个通道的 bin 数量必须大于 2。此外，将 bin 数量设置为大于每个通道的唯一像素值数量是没有意义的。默认情况下，直方图将使用每个通道的最大 bin 数量。
        可以设置 difference 为一个图像对象，以使此方法对当前图像和 difference 图像对象之间的差异图像上操作。这样可以避免使用单独的缓冲区。
        不支持压缩图像或 Bayer 图像。
        """
        pass
        
        
    def get_regression(self,thresholds: List[Tuple[int, int]],invert=False,roi: Tuple[int, int, int, int] | None = None,x_stride=2,y_stride=1,area_threshold=10,pixels_threshold=10,robust=False) -> line:
        """
        在图像中的所有阈值化像素上计算线性回归。线性回归通常使用最小二乘法计算，这很快，但不能处理任何异常值。如果 robust 为 True，则改用 Theil–Sen 线性回归，它计算图像中所有阈值化像素之间的所有斜率的中值。这是一个 N^2 的操作，即使在80×60的图像上，如果阈值化后设置太多像素，也可能将您的 FPS 降低到 5 以下。然而，只要阈值化后的像素数保持较低，即使在阈值化后的像素中有多达 30% 的异常值（例如，它是鲁棒的），线性回归也将有效。
        此方法返回一个 image.line 对象。请参阅此博客文章，了解如何轻松使用线对象：https://openmv.io/blogs/news/linear-regression-line-following
        thresholds 必须是包含元组的列表 [(lo, hi), (lo, hi), ..., (lo, hi)]，定义您要跟踪的颜色范围。对于灰度图像，每个元组都需要包含两个值 - 最小灰度值和最大灰度值。仅将处于这些阈值之间的像素区域视为符合条件。对于 RGB565 图像，每个元组需要有六个值（l_lo、l_hi、a_lo、a_hi、b_lo、b_hi） - 分别是 LAB L、A 和 B 通道的最小值和最大值。为了简化使用，此函数将自动修复颠倒的最小值和最大值。此外，如果元组的长度大于六个值，则其余部分将被忽略。反之，如果元组太短，则其余的阈值被假定为在最大范围内。
        invert 反转阈值操作，使得匹配像素不是在某些已知颜色范围内，而是在已知颜色范围之外。
        roi 是感兴趣区域的矩形元组(x, y, w, h)。如果未指定，则等于图像矩形。仅操作 roi 内的像素。
        x_stride 是在评估图像时要跳过的x像素数。
        y_stride 是在评估图像时要跳过的y像素数。
        如果回归的边界框面积小于 area_threshold ，则返回None。
        如果回归的像素计数少于 pixels_threshold ，则返回None。
        不支持压缩图像或 Bayer 图像。
        """
        pass
        
        
    def find_blobs(self,thresholds: List[Tuple[int, int]],invert=False,roi: Tuple[int, int, int, int] | None = None,x_stride=2,y_stride=1,area_threshold=10,pixels_threshold=10,merge=False,margin=0,threshold_cb=None,merge_cb=None,x_hist_bins_max=0,y_hist_bins_max=0) -> List[blob]:
        """
        在图像中查找所有blob（通过阈值测试的连接像素区域）并返回描述每个blob的 image.blob 对象列表。有关更多信息，请参阅 image.blob 对象。
        thresholds 必须是元组列表 [(lo, hi), (lo, hi), ..., (lo, hi)]，定义要跟踪的颜色范围。您可以在一次调用中传递多达32个阈值元组。对于灰度图像，每个元组需要包含两个值 - 最小灰度值和最大灰度值。只有落在这些阈值之间的像素区域才会被考虑。对于RGB565图像，每个元组需要有六个值（l_lo，l_hi，a_lo，a_hi，b_lo，b_hi） - 分别是LAB L，A和B通道的最小值和最大值。为了方便使用，此函数将自动修复交换的最小和最大值。此外，如果元组大于六个值，则其余的值将被忽略。相反，如果元组太短，则其余的阈值将被假定为最大范围。
        invert 反转阈值操作，使得匹配像素不是在某些已知颜色范围内，而是在已知颜色范围之外。
        roi 是感兴趣区域的矩形元组(x, y, w, h)。如果未指定，则等于图像矩形。仅操作 roi 内的像素。
        x_stride 是在搜索blob时要跳过的x像素数。一旦找到一个blob，线填充算法将是像素精确的。如果已知blob很大，则增加 x_stride 以加快查找blob的速度。
        y_stride 是在搜索blob时要跳过的y像素数。一旦找到一个blob，线填充算法将是像素精确的。如果已知blob很大，则增加 y_stride 以加快查找blob的速度。
        如果blob的边界框面积小于 area_threshold ，则过滤掉它。
        如果blob的像素计数少于 pixels_threshold ，则过滤掉它。
        merge 如果为 True，则会合并所有未被过滤掉且其边界矩形相互交叉的斑点。margin 可用于在交叉测试期间增加或减少斑点边界矩形的大小。例如，当 margin 为 1 时，边界矩形相距 1 像素的斑点将被合并。
        合并blob允许您实现颜色代码跟踪。每个blob对象都有一个 code 值，它是由每个颜色阈值的1组成的位向量。例如，如果向 Image.find_blobs 传递两个颜色阈值，则第一个阈值的代码为1，第二个为2（第三个阈值为4，第四个为8，依此类推）。合并的blob逻辑OR它们的代码，以便您知道产生它们的颜色。这样，如果您得到一个具有两种颜色的blob对象，则知道它可能是一个颜色代码。
        如果您使用的颜色边界较窄，无法完全跟踪所要跟踪对象的所有像素，您可能还需要合并 Blobs。
        最后，如果您想要合并blob，但不想合并两个颜色阈值，则只需两次调用 Image.find_blobs ，每次使用不同的阈值，以便不合并blob。
        threshold_cb 可以设置为在每个blob阈值化后调用的函数，以将其从要合并的blob列表中筛选出来。回调函数将接收一个参数 - 要过滤的blob对象。然后，回调必须返回True以保留blob，False以过滤它。
        merge_cb 可以设置为在每两个即将合并的blob上调用的函数，以防止或允许合并。回调函数将接收两个参数 - 即将合并的两个blob对象。然后，回调必须返回True以合并blob，False以防止合并blob。
        x_hist_bins_max 如果设置为非零，则在每个blob对象中填充一个直方图缓冲区，其中包含对象中所有列的x_histogram投影。然后，此值设置该投影的bin数。
        y_hist_bins_max 如果设置为非零，则在每个blob对象中填充一个直方图缓冲区，其中包含对象中所有行的y_histogram投影。然后，此值设置该投影的bin数。
        不支持压缩图像或 Bayer 图像。
        """
        pass
        
        
    def find_lines(self,roi: Tuple[int, int, int, int] | None = None,x_stride=2,y_stride=1,threshold=1000,theta_margin=25,rho_margin=25) -> List[line]:
        """
        使用霍夫变换在图像中查找所有无限线条。返回 image.line 对象的列表。
        roi 是感兴趣区域的矩形元组(x, y, w, h)。如果未指定，则等于图像矩形。仅操作 roi 内的像素。
        x_stride 是在进行霍夫变换时要跳过的x像素数。仅当要搜索的线条较大且笨重时才增加此值。
        y_stride 是在进行霍夫变换时要跳过的y像素数。仅当要搜索的线条较大且笨重时才增加此值。
        threshold 控制从霍夫变换中检测到的线条。仅返回幅度大于或等于 threshold 的线条。对于您的应用程序， threshold 的正确值取决于图像。请注意，线的幅度是由构成该线的所有sobel滤波器幅度的像素的总和。
        theta_margin 控制检测到的线条的合并。相隔 theta_margin 度且相隔 rho_margin rho的线条将被合并。
        rho_margin 控制检测到的线条的合并。相隔 theta_margin 度且相隔 rho_margin rho的线条将被合并。
        此方法通过对图像运行sobel滤波器并从sobel滤波器中获取幅度和梯度响应来进行霍夫变换。它不需要对图像进行任何预处理。但是，通过使用滤波器清理图像，您可能会获得更稳定的结果。
        不支持压缩图像或 Bayer 图像。
        此方法在 OpenMV Cam M4 上不可用。
        """
        pass
        
        
    def find_line_segments(self,roi: Tuple[int, int, int, int] | None = None,merge_distance=0,max_theta_difference=15) -> List[line]:
        """
        使用霍夫变换在图像中查找线段。返回 image.line 对象的列表。
        roi 是感兴趣区域的矩形元组(x, y, w, h)。如果未指定，则等于图像矩形。仅操作 roi 内的像素。
        merge_distance 指定两条线段在任意一点的最大像素间距，只有在此距离内它们才会被合并。
        max_theta_difference 是两条线段在 merge_distance 范围内被合并时的最大角度差（以度为单位）。
        此方法使用 LSD 库（OpenCV 也使用该库）在图像中查找线段。尽管速度较慢，但精度非常高，而且线段不会出现跳动。
        此方法在 OpenMV Cam M4 上不可用。
        """
        pass
        
        
    def find_circles(self,roi: Tuple[int, int, int, int] | None = None,x_stride=2,y_stride=1,threshold=2000,x_margin=10,y_margin=10,r_margin=10,r_min=2,r_max: int | None = None,r_step=2) -> List[circle]:
        """
        使用霍夫变换在图像中查找圆。返回 image.circle 对象的列表。
        roi 是感兴趣区域的矩形元组(x, y, w, h)。如果未指定，则等于图像矩形。仅操作 roi 内的像素。
        x_stride 是在进行霍夫变换时要跳过的x像素数。仅当要搜索的圆较大且笨重时才增加此值。
        y_stride 是在进行霍夫变换时要跳过的y像素数。仅当要搜索的圆较大且笨重时才增加此值。
        threshold 控制从霍夫变换中检测到的圆。仅返回幅度大于或等于 threshold 的圆。对于您的应用程序，threshold 的正确值取决于图像。请注意，圆的幅度是由构成该圆的所有sobel滤波器幅度的像素的总和。
        x_margin 控制检测到的圆的合并。相隔 x_margin 、 y_margin 和 r_margin 像素的圆将被合并。
        y_margin 控制检测到的圆的合并。相隔 x_margin 、 y_margin 和 r_margin 像素的圆将被合并。
        r_margin 控制检测到的圆的合并。相隔 x_margin 、 y_margin 和 r_margin 像素的圆将被合并。
        r_min 控制检测到的最小圆半径。增加此值以加快算法。默认为2。
        r_max 控制检测到的最大圆半径。减小此值以加快算法。默认为min(roi.w/2, roi.h/2)。
        r_step 控制半径检测的步长。默认为2。
        此方法在 OpenMV Cam M4 上不可用。
        """
        pass
        
        
    def find_rects(self,roi: Tuple[int, int, int, int] | None = None,threshold=10000) -> List[rect]:
        """
        使用用于查找apriltags的相同四边形检测算法来查找图像中的矩形。对于对背景具有良好对比度的矩形效果最佳。apriltag四边形检测算法可以处理任何矩形的缩放/旋转/剪切。返回 image.rect 对象的列表。
        roi 是感兴趣区域的矩形元组(x, y, w, h)。如果未指定，则等于图像矩形。仅操作 roi 内的像素。
        边缘幅度（通过在矩形边缘上的所有像素上滑动sobel运算符并将其值求和来计算）小于 threshold 的矩形将被过滤出返回列表。 threshold 的正确值取决于您的应用程序/场景。
        此方法在 OpenMV Cam M4 上不可用。
        """
        pass
        
        
    def find_qrcodes(self,roi: Tuple[int, int, int, int] | None = None) -> List[qrcode]:
        """
        查找 roi 内的所有qrcodes，并返回一个 image.qrcode 对象列表。请参阅 image.qrcode 对象以获取更多信息。
        为使此方法有效工作，图像中的QR码需要相对平坦。您可以通过以下方式实现图像更平坦，不受镜头畸变影响：使用 sensor.set_windowing() 函数放大镜头中心，使用 Image.lens_corr() 消除镜头桶形失真，或者更换镜头为具有较窄视场的镜头。有一些机器视觉镜头可用，它们不会导致桶形失真，但价格比OpenMV提供的标准镜头高得多。
        roi 是感兴趣区域的矩形元组(x, y, w, h)。如果未指定，则等于图像矩形。仅操作 roi 内的像素。
        此方法在 OpenMV Cam M4 上不可用。
        """
        pass
        
        
    def find_apriltags(self,roi: Tuple[int, int, int, int] | None = None,families=TAG36H11,fx=0.0,fy=0.0,cx: int | None = None,cy: int | None = None) -> List[apriltag]:
        """
        查找 roi 内的所有AprilTags，并返回一个 image.apriltag 对象列表。请参阅 image.apriltag 对象以获取更多信息。
        与QR码不同，AprilTags可以在距离更远的情况下、光照更差的情况下、变形的图像中等情况下被检测到。AprilTags对各种图像失真问题都非常强大，而QR码则不是。即便如此，AprilTags只能将数值ID编码为其有效载荷。
        AprilTags也可用于定位目的。每个 image.apriltag 对象都会返回相机的平移和旋转。平移的单位由 fx、fy、cx 和 cy 确定，它们分别是图像在X和Y方向上的焦距和中心点。
        roi 是感兴趣区域的矩形元组(x, y, w, h)。如果未指定，则等于图像矩形。仅操作 roi 内的像素。
        families 是要解码的标签族的位掩码。它是以下内容的逻辑或：
        默认值仅为 image.TAG36H11，这是最佳标签族。请注意，每启用一个标签族，Image.find_apriltags() 的速度就会减慢。
        fx 是相机X方向的焦距（像素）。对于标准的OpenMV Cam，这是 (2.8 / 3.984) * 656。这是以mm为单位的镜头焦距，除以X方向的相机传感器长度，再乘以X方向上相机传感器的像素数（适用于OV7725相机）。
        fy 是相机Y方向的焦距（像素）。对于标准的OpenMV Cam，这是 (2.8 / 2.952) * 488。这是以mm为单位的镜头焦距，除以Y方向的相机传感器长度，再乘以Y方向上相机传感器的像素数（适用于OV7725相机）。
        cx 是图像中心，即 image.width()/2。这不是 roi.w()/2。
        cy 是图像中心，即 image.height()/2。这不是 roi.h()/2。
        不支持压缩图像。
        此方法在 OpenMV Cam M4 上不可用。
        """
        pass
        
        
    def find_datamatrices(self,roi: Tuple[int, int, int, int] | None = None,effort=200) -> List[datamatrix]:
        """
        查找 roi 内的所有数据矩阵，并返回一个 image.datamatrix 对象列表。请参阅 image.datamatrix 对象以获取更多信息。
        为使此方法有效工作，图像中的数据矩阵需要相对平坦。您可以通过以下方式实现图像更平坦，不受镜头畸变影响：使用 sensor.set_windowing() 函数放大镜头中心，使用 Image.lens_corr() 消除镜头桶形失真，或者更换镜头为具有较窄视场的镜头。有一些机器视觉镜头可用，它们不会导致桶形失真，但价格比OpenMV提供的标准镜头高得多。
        roi 是感兴趣区域的矩形元组(x, y, w, h)。如果未指定，则等于图像矩形。仅操作 roi 内的像素。
        effort 控制尝试查找数据矩阵匹配的时间量。默认200对于所有用例应该很好。但是，您可以增加effort，以牺牲帧速率来增加检测。您也可以降低effort来增加帧速率，但是会牺牲检测率……请注意，当 effort 设置低于160左右时，将不再检测到任何内容。还要注意，可以使 effort 设置的尽可能高。但是，高于240左右的任何值都不会导致检测率显著增加。
        此方法在 OpenMV Cam M4 上不可用。
        """
        pass
        
        
    def find_barcodes(self,roi: Tuple[int, int, int, int] | None = None) -> List[barcode]:
        """
        查找 roi 内的所有一维条形码，并返回一个 image.barcode 对象列表。请参阅 image.barcode 对象以获取更多信息。
        为获得最佳结果，请使用640 x 40/80/160窗口。垂直分辨率越低，所有操作运行速度越快。由于条形码是线性1D图像，因此您只需在一个方向上拥有很高的分辨率，在另一个方向上只需要很少的分辨率。请注意，此函数水平和垂直扫描，因此您可以使用40/80/160 x 480窗口。最后，请确保调整镜头，使条形码位于焦距产生最清晰图像的位置。模糊的条形码无法解码。
        此函数支持所有这些一维条形码（基本上是所有条形码）：
        roi 是感兴趣区域的矩形元组(x, y, w, h)。如果未指定，则等于图像矩形。仅操作 roi 内的像素。
        此方法在 OpenMV Cam M4 上不可用。
        """
        pass
        
        
    def find_displacement(self,template: Image,roi: Tuple[int, int, int, int] | None = None,template_roi: Tuple[int, int, int, int] | None = None,logpolar=False) -> List[displacement]:
        """
        查找此图像相对于模板的平移偏移。此方法可用于光流。此方法返回一个包含使用相位相关性进行位移计算结果的 image.displacement 对象。
        roi 是要处理的感兴趣区域矩形 (x, y, w, h)。如果未指定，则等于图像矩形。
        template_roi 是要处理的模板感兴趣区域矩形 (x, y, w, h)。如果未指定，则等于图像矩形。
        roi 和 template 的区域必须具有相同的宽度和高度，但在图像中可以具有任意的 x/y 位置。您可以在较大的图像中滑动较小的区域，以获取光流梯度图像……
        Image.find_displacement() 通常用于计算两幅图像之间的 x/y 平移。然而，如果传入 logpolar=True，它将改为查找两幅图像之间的旋转和缩放变化。相同的 image.displacement 对象结果会同时编码这两种可能的响应。
        不支持压缩图像或 Bayer 图像。
        不支持压缩图像或 Bayer 图像。
        此方法在 OpenMV Cam M4 上不可用。
        """
        pass
        
        
    def find_template(self,template: Image,threshold: float,roi: Tuple[int, int, int, int] | None = None,step=2,search=SEARCH_EX) -> Tuple[int, int, int, int]:
        """
        尝试在图像中找到模板匹配的第一个位置，使用归一化互相关。如果找到匹配位置，则返回一个边界框元组 (x, y, w, h)，否则返回None。
        template 是要与此图像对象匹配的小图像对象。请注意，两个图像都必须是灰度图像。
        threshold 是一个浮点数（0.0-1.0），其中较高的阈值可以防止错误的正检率，同时降低检测率，而较低的阈值则相反。
        roi 是感兴趣区域的矩形元组(x, y, w, h)。如果未指定，则等于图像矩形。仅操作 roi 内的像素。
        step 是在查找模板时要跳过的像素数。跳过像素可以大大加快算法速度。这仅影响SEARCH_EX模式下的算法。
        search 可以是 image.SEARCH_DS 或 image.SEARCH_EX。 image.SEARCH_DS 使用比 image.SEARCH_EX 更快的算法搜索模板，但可能无法在图像边缘附近找到模板。 image.SEARCH_EX 对图像进行穷举搜索，但比 image.SEARCH_DS 慢得多。
        仅适用于灰度图像。
        """
        pass
        
        
    def find_features(self,cascade,threshold=0.5,scale=1.5,roi: Tuple[int, int, int, int] | None = None) -> List[Tuple[int, int, int, int]]:
        """
        此方法在图像中搜索所有与传入的Haar级联匹配的区域，并返回一个围绕这些特征的边界框矩形元组列表 (x, y, w, h)。如果未找到特征，则返回一个空列表。
        cascade 是一个Haar级联对象。有关详细信息，请参阅 image.HaarCascade()。
        threshold 是一个阈值（0.0-1.0），较小的值会增加检测率，但会提高误检率。相反，较高的值会降低检测率，但会降低误检率。
        scale 是一个浮点数，必须大于1.0。较高的比例因子会运行得更快，但图像匹配效果会大打折扣。一个好的值介于1.35和1.5之间。
        roi 是感兴趣区域的矩形元组(x, y, w, h)。如果未指定，则等于图像矩形。仅操作 roi 内的像素。
        """
        pass
        
        
    def find_eye(self,roi: Tuple[int, int, int, int]) -> Tuple[int, int]:
        """
        在眼睛周围的感兴趣区域 (x, y, w, h) 元组中搜索瞳孔。返回一个元组，其中包含图像中瞳孔的 (x, y) 位置。如果找不到瞳孔，则返回 (0,0)。
        要使用此函数，首先使用 Image.find_features() 和 frontalface HaarCascade找到某人的面部。然后使用 Image.find_features() 和 eye HaarCascade找到面部上的眼睛。最后，在由 Image.find_features() 返回的眼睛ROI上调用此方法，以获取瞳孔坐标。
        roi 是感兴趣区域的矩形元组(x, y, w, h)。如果未指定，则等于图像矩形。仅操作 roi 内的像素。
        仅适用于灰度图像。
        """
        pass
        
        
    def find_lbp(self,roi: Tuple[int, int, int, int]):
        """
        从感兴趣区域 (x, y, w, h) 元组中提取LBP（局部二值模式）关键点。然后可以使用 image.match_descriptor() 函数比较两组关键点以获取匹配距离。
        roi 是感兴趣区域的矩形元组(x, y, w, h)。如果未指定，则等于图像矩形。仅操作 roi 内的像素。
        仅适用于灰度图像。
        """
        pass
        
        
    def find_keypoints(self,roi: Tuple[int, int, int, int] | None = None,threshold=20,normalized=False,scale_factor=1.5,max_keypoints=100,corner_detector=CORNER_AGAST):
        """
        从感兴趣区域 (x, y, w, h) 元组中提取ORB关键点。然后可以使用 image.match_descriptor() 函数比较两组关键点以获取匹配区域。如果未找到关键点，则返回None。
        roi 是感兴趣区域的矩形元组(x, y, w, h)。如果未指定，则等于图像矩形。仅操作 roi 内的像素。
        threshold 是一个数字（介于0 - 255之间），控制提取的角点数量。对于默认的AGAST角点检测器，此值应该大约为20。对于FAST角点检测器，此值应该大约为60-80。阈值越低，提取的角点就越多。
        normalized 是一个布尔值，如果为True，则关闭在多个分辨率提取关键点。如果您不关心处理缩放问题，并希望算法运行得更快，则将其设置为true。
        scale_factor 是一个浮点数，必须大于1.0。较高的比例因子会运行得更快，但图像匹配效果会大打折扣。一个好的值介于1.35和1.5之间。
        max_keypoints 是一个关键点对象可以持有的最大关键点数。如果关键点对象太大并导致内存不足问题，则减小此值。
        corner_detector 是用于提取图像关键点的角点检测算法。可以是 image.CORNER_FAST 或 image.CORNER_AGAST。FAST角点检测算法速度更快，但准确度较低。
        仅适用于灰度图像。
        """
        pass
        
        
    def find_edges(self,edge_type,threshold=(100, 200)):
        """
        将图像转换为黑白图像，仅保留边缘为白色像素。
        threshold 是包含低阈值和高阈值的两个值的元组，您可以通过调整这些值来控制边缘的质量。默认为 (100, 200)。
        仅适用于灰度图像。
        """
        pass
        
        
    def find_hog(self,roi: Tuple[int, int, int, int] | None = None,size=8):
        """
        用HOG（方向梯度直方图）线替换ROI中的像素。
        roi 是感兴趣区域的矩形元组(x, y, w, h)。如果未指定，则等于图像矩形。仅操作 roi 内的像素。
        仅适用于灰度图像。
        此方法在 OpenMV Cam M4 上不可用。
        """
        pass
        
        
    def stero_disparity(self,reversed: bool = False,max_disparity: int = 64,threshold: int = 64):
        """
        处理一个双宽灰度图像，该图像由两个摄像头传感器的输出并排组成，并用立体视差图像替换双宽图像中的其中一个图像，其中每个像素表示深度。例如，如果您有两个 320x240 的摄像头，那么此方法将处理一个 640x240 的图像。
        reversed 默认情况下，将左图像与右图像进行比较，然后替换右图像。传递true以将右图像与左图像进行比较并替换左图像。
        max_disparity 是使用绝对差值和算法搜索匹配像素块时的最大距离。较大的值会显著增加搜索时间，但能生成更高质量的图像；较小的值会加快算法运行速度，但可能产生无意义的输出。
        threshold 如果两个块之间的绝对差值之和小于或等于此阈值，则认为它们匹配。
        此方法仅适用于Arduino Portenta。
        """
        pass
        
        
    
