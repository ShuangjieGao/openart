"""
ml 模块包含在 OpenMV Cam 上处理机器学习模型的功能。
ml 模块的核心是 Model() 对象，用于加载和执行 TensorFlow Lite 模型。Model() 对象接受一个最多为 4D 的输入张量列表，表示每个模型输入张量，并返回一个最多为 4D 的输出张量列表，表示每个模型输出张量。每个输入/输出张量都使用 numpy 的 ndarray 进行操作。
对于 TensorFlow Lite 模型，Model() 对象处理所有启用的操作，具体见 [此处](https://github.com/openmv/openmv/blob/master/src/lib/tflm/tflm_backend.cc)。Model() 对象会自动利用 CMSIS-NN、Helium 和 Ethos NPU（如果可用）来加速推理。这些加速器的可用性取决于 OpenMV Cam 的型号。
对于图像处理支持，ml 模块会通过将传递的图像对象包装在 Normalization() 对象中，自动将其转换为 numpy ndarray 对象，Normalization() 对象负责处理这一转换过程。Normalization() 对象也可以手动创建，以便控制转换过程、选择感兴趣区域（ROI）等。
有关 ndarray 对象的更多信息，请参阅 ulab 文档。所有 OpenMV Cam 都支持最多 4 维的 ndarray 对象（即 4D 张量）。
"""

from typing import Tuple
from typing import List
from typing import Optional
from typing import Any
import image

class Model:
    def __init__(self, path: str, load_to_fb: bool = False):
        """
        从 path 加载模型到内存并准备执行。path 可以是磁盘上的文件路径，也可以是内置模型的名称，内置模型会从内部闪存加载。内置于内部闪存固件映像中的模型在使用时不会占用 RAM 来存储模型权重。
        如果您尝试加载的模型非常大，无法适应 MicroPython 堆（heap），可以将 load_to_fb 设置为 True，将模型加载到帧缓冲区栈（frame buffer stack）中。这可以绕过堆大小的限制。然而，采用这种方式加载的模型需要与其他使用帧缓冲区栈的对象一起按顺序释放，而不是与 MicroPython 堆一起释放。通常，帧缓冲区栈比 MicroPython 堆要大得多，因此使用此选项可以加载更大的模型，但在释放时需要小心。
        一旦模型加载完成，您可以使用 predict() 多次执行它，并传入不同的输入。模型将在多次调用 predict() 之间记住其内部状态。
        当模型被删除时，它将自动释放其使用的内存，无论是来自堆（heap）还是帧缓冲区栈（frame buffer stack）。
        """
        pass
        
        
    def predict(self,inputs: list,callback=None) -> list:
        """
        使用给定的输入执行模型。输入应该是一个 numpy ndarray 对象的列表，数量对应模型支持的输入张量数。该方法返回一个 numpy ndarray 对象的列表，数量对应模型的输出张量数。
        模型的输入张量可以是最大为 4D 的 uint8、int8、uint16、int16 或 float32 类型的张量。传递的 numpy ndarray 对象会根据输入张量的缩放（scale）和零点（zero point）值，先转换为浮点数，并进行缩放/偏移，然后传递给模型。例如，一个 ndarray 类型的 uint8 值会被转换为 0.0 到 255.0 之间的 float32 值，再除以输入张量的缩放因子，然后加上输入张量的零点值。对于 int8、uint16 和 int16 值，也会执行相同的过程，而 float32 值则直接传递给模型，忽略缩放和零点值。
        模型的输出张量可以是最大为 4D 的 uint8、int8、uint16、int16 或 float32 类型的张量。对于 uint8、int8、uint16 和 int16 张量，返回的 numpy ndarray 会通过先减去输出张量的零点值，再乘以输出张量的缩放值来创建。对于 float32 张量，值会直接传递到输出，不进行任何缩放或偏移。
        请注意，predict() 方法要求输入的 ndarray 对象的形状必须与模型输入张量的形状完全匹配。如果需要，您可以使用 ndarray 的 reshape() 方法，结合模型的 input_shape 属性，将输入数据重塑为正确的形状。
        如果传递了一个 callback，它将接收 Model、inputs 和 outputs 作为参数，这允许对模型输出进行自定义后处理。然后，回调函数可以返回任何它想要的内容，这将作为 predict() 的返回值。callback 方法使得可以构建一个后处理函数库，可以根据不同模型的需求随时调用。
        对于自定义预处理，predict() 也接受可调用（”callable”）对象作为输入。任何实现了 __call__ 方法的对象都可以作为输入传递给 predict()。predict() 会使用一个可写的字节数组（bytearray）表示输入张量，并传递该张量的形状元组和数据类型值（作为整数）来调用该对象。然后，该对象应该将字节数组中的输入张量数据设置为模型所期望的内容。这就是 Normalization() 如何将图像对象转换为输入张量的方式。
        """
        pass
        
        
    
"""
ml.apps 模块包含各种机器学习应用类。
"""

from typing import Tuple
from typing import List
from typing import Optional
from typing import Any
import image

class MicroSpeech:
    def __init__(self, preprocessor: str = None, micro_speech: str = None, labels: list[str, ...] = None):
        """
        创建一个MicroSpeech对象。如果没有提供预处理器，则使用默认的预处理器。如果没有提供micro_speech模型，则使用默认模型。如果没有提供标签，则使用默认模型中的默认标签。
        """
        pass
        
        
    def listen(self,timeout: int = 0,callback=None,threshold: float = 0.65,filter: list[str, ...] = ['Yes', 'No']) -> tuple[str, float]:
        """
        监听一个口语单词，并在置信度超过阈值且该单词在过滤列表中时，返回该单词和置信度水平的元组。
        timeout``是监听一个单词的最大时间（以毫秒为单位）。如果为零，则该方法将无限期地监听，直到识别到一个单词。如果传入-1，该方法将不会阻塞，并会立即返回结果元组，如果未识别到任何单词，元组中可能包含``None。如果传入一个正值，该方法将在该时间（以毫秒为单位）内监听，然后返回结果元组。
        callback 是一个函数，当识别到单词时，它将被调用，并传入单词和置信度水平，而不是返回结果。当与零超时结合使用时，这允许您无限期地监听单词，并在单词被识别时进行处理。
        threshold 是返回结果所需的最低置信度水平。
        filter 是一个单词列表，模型应该识别这些单词。如果识别到的单词不在过滤列表中，则该结果将被忽略。
        """
        pass
        
        
    
"""
ml 模块包含在 OpenMV Cam 上处理机器学习模型的功能。
ml 模块的核心是 Model() 对象，用于加载和执行 TensorFlow Lite 模型。Model() 对象接受一个最多为 4D 的输入张量列表，表示每个模型输入张量，并返回一个最多为 4D 的输出张量列表，表示每个模型输出张量。每个输入/输出张量都使用 numpy 的 ndarray 进行操作。
对于 TensorFlow Lite 模型，Model() 对象处理所有启用的操作，具体见 [此处](https://github.com/openmv/openmv/blob/master/src/lib/tflm/tflm_backend.cc)。Model() 对象会自动利用 CMSIS-NN、Helium 和 Ethos NPU（如果可用）来加速推理。这些加速器的可用性取决于 OpenMV Cam 的型号。
对于图像处理支持，ml 模块会通过将传递的图像对象包装在 Normalization() 对象中，自动将其转换为 numpy ndarray 对象，Normalization() 对象负责处理这一转换过程。Normalization() 对象也可以手动创建，以便控制转换过程、选择感兴趣区域（ROI）等。
有关 ndarray 对象的更多信息，请参阅 ulab 文档。所有 OpenMV Cam 都支持最多 4 维的 ndarray 对象（即 4D 张量）。
"""

from typing import Tuple
from typing import List
from typing import Optional
from typing import Any
import image

class Model:
    def __init__(self, path: str, load_to_fb: bool = False):
        """
        从 path 加载模型到内存并准备执行。path 可以是磁盘上的文件路径，也可以是内置模型的名称，内置模型会从内部闪存加载。内置于内部闪存固件映像中的模型在使用时不会占用 RAM 来存储模型权重。
        如果您尝试加载的模型非常大，无法适应 MicroPython 堆（heap），可以将 load_to_fb 设置为 True，将模型加载到帧缓冲区栈（frame buffer stack）中。这可以绕过堆大小的限制。然而，采用这种方式加载的模型需要与其他使用帧缓冲区栈的对象一起按顺序释放，而不是与 MicroPython 堆一起释放。通常，帧缓冲区栈比 MicroPython 堆要大得多，因此使用此选项可以加载更大的模型，但在释放时需要小心。
        一旦模型加载完成，您可以使用 predict() 多次执行它，并传入不同的输入。模型将在多次调用 predict() 之间记住其内部状态。
        当模型被删除时，它将自动释放其使用的内存，无论是来自堆（heap）还是帧缓冲区栈（frame buffer stack）。
        """
        pass
        
        
    def predict(self,inputs: list,callback=None) -> list:
        """
        使用给定的输入执行模型。输入应该是一个 numpy ndarray 对象的列表，数量对应模型支持的输入张量数。该方法返回一个 numpy ndarray 对象的列表，数量对应模型的输出张量数。
        模型的输入张量可以是最大为 4D 的 uint8、int8、uint16、int16 或 float32 类型的张量。传递的 numpy ndarray 对象会根据输入张量的缩放（scale）和零点（zero point）值，先转换为浮点数，并进行缩放/偏移，然后传递给模型。例如，一个 ndarray 类型的 uint8 值会被转换为 0.0 到 255.0 之间的 float32 值，再除以输入张量的缩放因子，然后加上输入张量的零点值。对于 int8、uint16 和 int16 值，也会执行相同的过程，而 float32 值则直接传递给模型，忽略缩放和零点值。
        模型的输出张量可以是最大为 4D 的 uint8、int8、uint16、int16 或 float32 类型的张量。对于 uint8、int8、uint16 和 int16 张量，返回的 numpy ndarray 会通过先减去输出张量的零点值，再乘以输出张量的缩放值来创建。对于 float32 张量，值会直接传递到输出，不进行任何缩放或偏移。
        请注意，predict() 方法要求输入的 ndarray 对象的形状必须与模型输入张量的形状完全匹配。如果需要，您可以使用 ndarray 的 reshape() 方法，结合模型的 input_shape 属性，将输入数据重塑为正确的形状。
        如果传递了一个 callback，它将接收 Model、inputs 和 outputs 作为参数，这允许对模型输出进行自定义后处理。然后，回调函数可以返回任何它想要的内容，这将作为 predict() 的返回值。callback 方法使得可以构建一个后处理函数库，可以根据不同模型的需求随时调用。
        对于自定义预处理，predict() 也接受可调用（”callable”）对象作为输入。任何实现了 __call__ 方法的对象都可以作为输入传递给 predict()。predict() 会使用一个可写的字节数组（bytearray）表示输入张量，并传递该张量的形状元组和数据类型值（作为整数）来调用该对象。然后，该对象应该将字节数组中的输入张量数据设置为模型所期望的内容。这就是 Normalization() 如何将图像对象转换为输入张量的方式。
        """
        pass
        
        
    
"""
`ml.preprocessing`模块包含用于图像预处理的类，以便与机器学习模型一起使用。
"""

from typing import Tuple
from typing import List
from typing import Optional
from typing import Any
import image

class Normalization:
    def __init__(self, scale: tuple[float, float] = (0.0, 1.0), mean: tuple[float, float, float] = (0.0, 0.0, 0.0), stdev: tuple[float, float, float] = (1.0, 1.0, 1.0), roi: tuple[int, int, int, int] = None):
        """
        创建一个 Normalization 对象，用于将图像对象转换为 numpy 数组，以供 predict() 使用。该对象还可用于选择图像中的感兴趣区域 (ROI) 并将其转换为 numpy 数组。
        Normalization 对象会自动将传入的任何图像类型（包括压缩图像）转换为单通道（灰度）或三通道（RGB888）图像，并将其传递到模型的张量输入中。图像会根据需要居中、按比例放大/缩小（使用双线性或区域缩放）、并裁剪，以匹配模型输入张量的大小。
        对于 uint8 输入张量，图像会被直接传递，忽略缩放和均值/标准差处理。对于 int8 输入张量，图像会从 uint8 范围平移到 int8 范围，然后直接传递，同样忽略缩放和均值/标准差处理。接受这些格式的张量比需要浮点数输入的张量处理速度更快。
        对于浮点数输入张量，无法推测模型期望的正确范围。虽然每个输入张量都编码了一个缩放值和零点值，可用于将输入转换到正确范围，但这些值并未指示浮点数输入数据应处于何种范围。例如，图像的 RGB 值在应用缩放和零点之前，应该在 (0.0, 1.0)、(-1.0, 1.0)、(0.0, 255.0) 等范围内？答案取决于模型及其训练方式。因此，Normalization 对象允许您直接指定输入数据的范围、均值和标准差。然后，灰度图像或 RGB888 图像会根据这些值转换为浮点数张量，以供模型处理。
        不支持 uint16 和 int16 输入张量。
        """
        pass
        
        
    
"""
ml 模块包含在 OpenMV Cam 上处理机器学习模型的功能。
ml 模块的核心是 Model() 对象，用于加载和执行 TensorFlow Lite 模型。Model() 对象接受一个最多为 4D 的输入张量列表，表示每个模型输入张量，并返回一个最多为 4D 的输出张量列表，表示每个模型输出张量。每个输入/输出张量都使用 numpy 的 ndarray 进行操作。
对于 TensorFlow Lite 模型，Model() 对象处理所有启用的操作，具体见 [此处](https://github.com/openmv/openmv/blob/master/src/lib/tflm/tflm_backend.cc)。Model() 对象会自动利用 CMSIS-NN、Helium 和 Ethos NPU（如果可用）来加速推理。这些加速器的可用性取决于 OpenMV Cam 的型号。
对于图像处理支持，ml 模块会通过将传递的图像对象包装在 Normalization() 对象中，自动将其转换为 numpy ndarray 对象，Normalization() 对象负责处理这一转换过程。Normalization() 对象也可以手动创建，以便控制转换过程、选择感兴趣区域（ROI）等。
有关 ndarray 对象的更多信息，请参阅 ulab 文档。所有 OpenMV Cam 都支持最多 4 维的 ndarray 对象（即 4D 张量）。
"""

from typing import Tuple
from typing import List
from typing import Optional
from typing import Any
import image

class Model:
    def __init__(self, path: str, load_to_fb: bool = False):
        """
        从 path 加载模型到内存并准备执行。path 可以是磁盘上的文件路径，也可以是内置模型的名称，内置模型会从内部闪存加载。内置于内部闪存固件映像中的模型在使用时不会占用 RAM 来存储模型权重。
        如果您尝试加载的模型非常大，无法适应 MicroPython 堆（heap），可以将 load_to_fb 设置为 True，将模型加载到帧缓冲区栈（frame buffer stack）中。这可以绕过堆大小的限制。然而，采用这种方式加载的模型需要与其他使用帧缓冲区栈的对象一起按顺序释放，而不是与 MicroPython 堆一起释放。通常，帧缓冲区栈比 MicroPython 堆要大得多，因此使用此选项可以加载更大的模型，但在释放时需要小心。
        一旦模型加载完成，您可以使用 predict() 多次执行它，并传入不同的输入。模型将在多次调用 predict() 之间记住其内部状态。
        当模型被删除时，它将自动释放其使用的内存，无论是来自堆（heap）还是帧缓冲区栈（frame buffer stack）。
        """
        pass
        
        
    def predict(self,inputs: list,callback=None) -> list:
        """
        使用给定的输入执行模型。输入应该是一个 numpy ndarray 对象的列表，数量对应模型支持的输入张量数。该方法返回一个 numpy ndarray 对象的列表，数量对应模型的输出张量数。
        模型的输入张量可以是最大为 4D 的 uint8、int8、uint16、int16 或 float32 类型的张量。传递的 numpy ndarray 对象会根据输入张量的缩放（scale）和零点（zero point）值，先转换为浮点数，并进行缩放/偏移，然后传递给模型。例如，一个 ndarray 类型的 uint8 值会被转换为 0.0 到 255.0 之间的 float32 值，再除以输入张量的缩放因子，然后加上输入张量的零点值。对于 int8、uint16 和 int16 值，也会执行相同的过程，而 float32 值则直接传递给模型，忽略缩放和零点值。
        模型的输出张量可以是最大为 4D 的 uint8、int8、uint16、int16 或 float32 类型的张量。对于 uint8、int8、uint16 和 int16 张量，返回的 numpy ndarray 会通过先减去输出张量的零点值，再乘以输出张量的缩放值来创建。对于 float32 张量，值会直接传递到输出，不进行任何缩放或偏移。
        请注意，predict() 方法要求输入的 ndarray 对象的形状必须与模型输入张量的形状完全匹配。如果需要，您可以使用 ndarray 的 reshape() 方法，结合模型的 input_shape 属性，将输入数据重塑为正确的形状。
        如果传递了一个 callback，它将接收 Model、inputs 和 outputs 作为参数，这允许对模型输出进行自定义后处理。然后，回调函数可以返回任何它想要的内容，这将作为 predict() 的返回值。callback 方法使得可以构建一个后处理函数库，可以根据不同模型的需求随时调用。
        对于自定义预处理，predict() 也接受可调用（”callable”）对象作为输入。任何实现了 __call__ 方法的对象都可以作为输入传递给 predict()。predict() 会使用一个可写的字节数组（bytearray）表示输入张量，并传递该张量的形状元组和数据类型值（作为整数）来调用该对象。然后，该对象应该将字节数组中的输入张量数据设置为模型所期望的内容。这就是 Normalization() 如何将图像对象转换为输入张量的方式。
        """
        pass
        
        
    
"""
ml.apps 模块包含各种机器学习应用类。
"""

from typing import Tuple
from typing import List
from typing import Optional
from typing import Any
import image

class MicroSpeech:
    def __init__(self, preprocessor: str = None, micro_speech: str = None, labels: list[str, ...] = None):
        """
        创建一个MicroSpeech对象。如果没有提供预处理器，则使用默认的预处理器。如果没有提供micro_speech模型，则使用默认模型。如果没有提供标签，则使用默认模型中的默认标签。
        """
        pass
        
        
    def listen(self,timeout: int = 0,callback=None,threshold: float = 0.65,filter: list[str, ...] = ['Yes', 'No']) -> tuple[str, float]:
        """
        监听一个口语单词，并在置信度超过阈值且该单词在过滤列表中时，返回该单词和置信度水平的元组。
        timeout``是监听一个单词的最大时间（以毫秒为单位）。如果为零，则该方法将无限期地监听，直到识别到一个单词。如果传入-1，该方法将不会阻塞，并会立即返回结果元组，如果未识别到任何单词，元组中可能包含``None。如果传入一个正值，该方法将在该时间（以毫秒为单位）内监听，然后返回结果元组。
        callback 是一个函数，当识别到单词时，它将被调用，并传入单词和置信度水平，而不是返回结果。当与零超时结合使用时，这允许您无限期地监听单词，并在单词被识别时进行处理。
        threshold 是返回结果所需的最低置信度水平。
        filter 是一个单词列表，模型应该识别这些单词。如果识别到的单词不在过滤列表中，则该结果将被忽略。
        """
        pass
        
        
    
"""
ml 模块包含在 OpenMV Cam 上处理机器学习模型的功能。
ml 模块的核心是 Model() 对象，用于加载和执行 TensorFlow Lite 模型。Model() 对象接受一个最多为 4D 的输入张量列表，表示每个模型输入张量，并返回一个最多为 4D 的输出张量列表，表示每个模型输出张量。每个输入/输出张量都使用 numpy 的 ndarray 进行操作。
对于 TensorFlow Lite 模型，Model() 对象处理所有启用的操作，具体见 [此处](https://github.com/openmv/openmv/blob/master/src/lib/tflm/tflm_backend.cc)。Model() 对象会自动利用 CMSIS-NN、Helium 和 Ethos NPU（如果可用）来加速推理。这些加速器的可用性取决于 OpenMV Cam 的型号。
对于图像处理支持，ml 模块会通过将传递的图像对象包装在 Normalization() 对象中，自动将其转换为 numpy ndarray 对象，Normalization() 对象负责处理这一转换过程。Normalization() 对象也可以手动创建，以便控制转换过程、选择感兴趣区域（ROI）等。
有关 ndarray 对象的更多信息，请参阅 ulab 文档。所有 OpenMV Cam 都支持最多 4 维的 ndarray 对象（即 4D 张量）。
"""

from typing import Tuple
from typing import List
from typing import Optional
from typing import Any
import image

class Model:
    def __init__(self, path: str, load_to_fb: bool = False):
        """
        从 path 加载模型到内存并准备执行。path 可以是磁盘上的文件路径，也可以是内置模型的名称，内置模型会从内部闪存加载。内置于内部闪存固件映像中的模型在使用时不会占用 RAM 来存储模型权重。
        如果您尝试加载的模型非常大，无法适应 MicroPython 堆（heap），可以将 load_to_fb 设置为 True，将模型加载到帧缓冲区栈（frame buffer stack）中。这可以绕过堆大小的限制。然而，采用这种方式加载的模型需要与其他使用帧缓冲区栈的对象一起按顺序释放，而不是与 MicroPython 堆一起释放。通常，帧缓冲区栈比 MicroPython 堆要大得多，因此使用此选项可以加载更大的模型，但在释放时需要小心。
        一旦模型加载完成，您可以使用 predict() 多次执行它，并传入不同的输入。模型将在多次调用 predict() 之间记住其内部状态。
        当模型被删除时，它将自动释放其使用的内存，无论是来自堆（heap）还是帧缓冲区栈（frame buffer stack）。
        """
        pass
        
        
    def predict(self,inputs: list,callback=None) -> list:
        """
        使用给定的输入执行模型。输入应该是一个 numpy ndarray 对象的列表，数量对应模型支持的输入张量数。该方法返回一个 numpy ndarray 对象的列表，数量对应模型的输出张量数。
        模型的输入张量可以是最大为 4D 的 uint8、int8、uint16、int16 或 float32 类型的张量。传递的 numpy ndarray 对象会根据输入张量的缩放（scale）和零点（zero point）值，先转换为浮点数，并进行缩放/偏移，然后传递给模型。例如，一个 ndarray 类型的 uint8 值会被转换为 0.0 到 255.0 之间的 float32 值，再除以输入张量的缩放因子，然后加上输入张量的零点值。对于 int8、uint16 和 int16 值，也会执行相同的过程，而 float32 值则直接传递给模型，忽略缩放和零点值。
        模型的输出张量可以是最大为 4D 的 uint8、int8、uint16、int16 或 float32 类型的张量。对于 uint8、int8、uint16 和 int16 张量，返回的 numpy ndarray 会通过先减去输出张量的零点值，再乘以输出张量的缩放值来创建。对于 float32 张量，值会直接传递到输出，不进行任何缩放或偏移。
        请注意，predict() 方法要求输入的 ndarray 对象的形状必须与模型输入张量的形状完全匹配。如果需要，您可以使用 ndarray 的 reshape() 方法，结合模型的 input_shape 属性，将输入数据重塑为正确的形状。
        如果传递了一个 callback，它将接收 Model、inputs 和 outputs 作为参数，这允许对模型输出进行自定义后处理。然后，回调函数可以返回任何它想要的内容，这将作为 predict() 的返回值。callback 方法使得可以构建一个后处理函数库，可以根据不同模型的需求随时调用。
        对于自定义预处理，predict() 也接受可调用（”callable”）对象作为输入。任何实现了 __call__ 方法的对象都可以作为输入传递给 predict()。predict() 会使用一个可写的字节数组（bytearray）表示输入张量，并传递该张量的形状元组和数据类型值（作为整数）来调用该对象。然后，该对象应该将字节数组中的输入张量数据设置为模型所期望的内容。这就是 Normalization() 如何将图像对象转换为输入张量的方式。
        """
        pass
        
        
    
"""
ml.utils 模块包含用于机器学习的工具类和函数。
"""

from typing import Tuple
from typing import List
from typing import Optional
from typing import Any
import image

class NMS:
    def __init__(self, window_w: int, window_h: int, roi: tuple[int, int, int, int]):
        """
        创建一个 NMS 对象，指定给定的窗口大小和感兴趣区域（ROI）。窗口的宽度/高度与图像模型的输入张量相同。ROI 是由 Normalization() 对象返回的感兴趣区域，它对应于模型运行时图像的区域。这允许 NMS 对象将子窗口中检测到的边界框重新映射回原始图像坐标。
        """
        pass
        
        
    def add_bounding_boxes(self,xmin: float,ymin: float,xmax: float,ymax: float,score: float,label_index: int) -> None:
        """
        向 NMS 对象添加一个边界框，包含给定的坐标、分数和标签索引。
        xmin、ymin、xmax 和 ymax 是边界框的坐标，范围为 0.0 到 1.0，其中 (0.0, 0.0) 是图像的左上角，(1.0, 1.0) 是图像的右下角。
        score 是边界框的置信度分数（0.0-1.0）。
        label_index 是与边界框相关联的标签索引。
        """
        pass
        
        
    def get_bounding_boxes(self,threshold: float = 0.1,sigma: float = 0.1) -> list[tuple[int, int, int, int, float, int]]:
        """
        返回一个已被 NMS 对象过滤并重新映射到原始图像坐标的边界框列表。边界框元组为 (x, y, w, h, score, label_index)。调用此方法后，如果您希望处理一组新的边界框，应创建一个新的 NMS 对象。
        边界框的分数必须高于 threshold 才会被保留。
        sigma 控制用于通过软非最大抑制算法对重叠边界框应用分数惩罚的高斯函数。较高的 sigma 值将导致对重叠边界框进行更强烈的抑制。
        """
        pass
        
        
    
"""
ml 模块包含在 OpenMV Cam 上处理机器学习模型的功能。
ml 模块的核心是 Model() 对象，用于加载和执行 TensorFlow Lite 模型。Model() 对象接受一个最多为 4D 的输入张量列表，表示每个模型输入张量，并返回一个最多为 4D 的输出张量列表，表示每个模型输出张量。每个输入/输出张量都使用 numpy 的 ndarray 进行操作。
对于 TensorFlow Lite 模型，Model() 对象处理所有启用的操作，具体见 [此处](https://github.com/openmv/openmv/blob/master/src/lib/tflm/tflm_backend.cc)。Model() 对象会自动利用 CMSIS-NN、Helium 和 Ethos NPU（如果可用）来加速推理。这些加速器的可用性取决于 OpenMV Cam 的型号。
对于图像处理支持，ml 模块会通过将传递的图像对象包装在 Normalization() 对象中，自动将其转换为 numpy ndarray 对象，Normalization() 对象负责处理这一转换过程。Normalization() 对象也可以手动创建，以便控制转换过程、选择感兴趣区域（ROI）等。
有关 ndarray 对象的更多信息，请参阅 ulab 文档。所有 OpenMV Cam 都支持最多 4 维的 ndarray 对象（即 4D 张量）。
"""

from typing import Tuple
from typing import List
from typing import Optional
from typing import Any
import image

class Model:
    def __init__(self, path: str, load_to_fb: bool = False):
        """
        从 path 加载模型到内存并准备执行。path 可以是磁盘上的文件路径，也可以是内置模型的名称，内置模型会从内部闪存加载。内置于内部闪存固件映像中的模型在使用时不会占用 RAM 来存储模型权重。
        如果您尝试加载的模型非常大，无法适应 MicroPython 堆（heap），可以将 load_to_fb 设置为 True，将模型加载到帧缓冲区栈（frame buffer stack）中。这可以绕过堆大小的限制。然而，采用这种方式加载的模型需要与其他使用帧缓冲区栈的对象一起按顺序释放，而不是与 MicroPython 堆一起释放。通常，帧缓冲区栈比 MicroPython 堆要大得多，因此使用此选项可以加载更大的模型，但在释放时需要小心。
        一旦模型加载完成，您可以使用 predict() 多次执行它，并传入不同的输入。模型将在多次调用 predict() 之间记住其内部状态。
        当模型被删除时，它将自动释放其使用的内存，无论是来自堆（heap）还是帧缓冲区栈（frame buffer stack）。
        """
        pass
        
        
    def predict(self,inputs: list,callback=None) -> list:
        """
        使用给定的输入执行模型。输入应该是一个 numpy ndarray 对象的列表，数量对应模型支持的输入张量数。该方法返回一个 numpy ndarray 对象的列表，数量对应模型的输出张量数。
        模型的输入张量可以是最大为 4D 的 uint8、int8、uint16、int16 或 float32 类型的张量。传递的 numpy ndarray 对象会根据输入张量的缩放（scale）和零点（zero point）值，先转换为浮点数，并进行缩放/偏移，然后传递给模型。例如，一个 ndarray 类型的 uint8 值会被转换为 0.0 到 255.0 之间的 float32 值，再除以输入张量的缩放因子，然后加上输入张量的零点值。对于 int8、uint16 和 int16 值，也会执行相同的过程，而 float32 值则直接传递给模型，忽略缩放和零点值。
        模型的输出张量可以是最大为 4D 的 uint8、int8、uint16、int16 或 float32 类型的张量。对于 uint8、int8、uint16 和 int16 张量，返回的 numpy ndarray 会通过先减去输出张量的零点值，再乘以输出张量的缩放值来创建。对于 float32 张量，值会直接传递到输出，不进行任何缩放或偏移。
        请注意，predict() 方法要求输入的 ndarray 对象的形状必须与模型输入张量的形状完全匹配。如果需要，您可以使用 ndarray 的 reshape() 方法，结合模型的 input_shape 属性，将输入数据重塑为正确的形状。
        如果传递了一个 callback，它将接收 Model、inputs 和 outputs 作为参数，这允许对模型输出进行自定义后处理。然后，回调函数可以返回任何它想要的内容，这将作为 predict() 的返回值。callback 方法使得可以构建一个后处理函数库，可以根据不同模型的需求随时调用。
        对于自定义预处理，predict() 也接受可调用（”callable”）对象作为输入。任何实现了 __call__ 方法的对象都可以作为输入传递给 predict()。predict() 会使用一个可写的字节数组（bytearray）表示输入张量，并传递该张量的形状元组和数据类型值（作为整数）来调用该对象。然后，该对象应该将字节数组中的输入张量数据设置为模型所期望的内容。这就是 Normalization() 如何将图像对象转换为输入张量的方式。
        """
        pass
        
        
    
"""
ml.apps 模块包含各种机器学习应用类。
"""

from typing import Tuple
from typing import List
from typing import Optional
from typing import Any
import image

class MicroSpeech:
    def __init__(self, preprocessor: str = None, micro_speech: str = None, labels: list[str, ...] = None):
        """
        创建一个MicroSpeech对象。如果没有提供预处理器，则使用默认的预处理器。如果没有提供micro_speech模型，则使用默认模型。如果没有提供标签，则使用默认模型中的默认标签。
        """
        pass
        
        
    def listen(self,timeout: int = 0,callback=None,threshold: float = 0.65,filter: list[str, ...] = ['Yes', 'No']) -> tuple[str, float]:
        """
        监听一个口语单词，并在置信度超过阈值且该单词在过滤列表中时，返回该单词和置信度水平的元组。
        timeout``是监听一个单词的最大时间（以毫秒为单位）。如果为零，则该方法将无限期地监听，直到识别到一个单词。如果传入-1，该方法将不会阻塞，并会立即返回结果元组，如果未识别到任何单词，元组中可能包含``None。如果传入一个正值，该方法将在该时间（以毫秒为单位）内监听，然后返回结果元组。
        callback 是一个函数，当识别到单词时，它将被调用，并传入单词和置信度水平，而不是返回结果。当与零超时结合使用时，这允许您无限期地监听单词，并在单词被识别时进行处理。
        threshold 是返回结果所需的最低置信度水平。
        filter 是一个单词列表，模型应该识别这些单词。如果识别到的单词不在过滤列表中，则该结果将被忽略。
        """
        pass
        
        
    
"""
ml 模块包含在 OpenMV Cam 上处理机器学习模型的功能。
ml 模块的核心是 Model() 对象，用于加载和执行 TensorFlow Lite 模型。Model() 对象接受一个最多为 4D 的输入张量列表，表示每个模型输入张量，并返回一个最多为 4D 的输出张量列表，表示每个模型输出张量。每个输入/输出张量都使用 numpy 的 ndarray 进行操作。
对于 TensorFlow Lite 模型，Model() 对象处理所有启用的操作，具体见 [此处](https://github.com/openmv/openmv/blob/master/src/lib/tflm/tflm_backend.cc)。Model() 对象会自动利用 CMSIS-NN、Helium 和 Ethos NPU（如果可用）来加速推理。这些加速器的可用性取决于 OpenMV Cam 的型号。
对于图像处理支持，ml 模块会通过将传递的图像对象包装在 Normalization() 对象中，自动将其转换为 numpy ndarray 对象，Normalization() 对象负责处理这一转换过程。Normalization() 对象也可以手动创建，以便控制转换过程、选择感兴趣区域（ROI）等。
有关 ndarray 对象的更多信息，请参阅 ulab 文档。所有 OpenMV Cam 都支持最多 4 维的 ndarray 对象（即 4D 张量）。
"""

from typing import Tuple
from typing import List
from typing import Optional
from typing import Any
import image

class Model:
    def __init__(self, path: str, load_to_fb: bool = False):
        """
        从 path 加载模型到内存并准备执行。path 可以是磁盘上的文件路径，也可以是内置模型的名称，内置模型会从内部闪存加载。内置于内部闪存固件映像中的模型在使用时不会占用 RAM 来存储模型权重。
        如果您尝试加载的模型非常大，无法适应 MicroPython 堆（heap），可以将 load_to_fb 设置为 True，将模型加载到帧缓冲区栈（frame buffer stack）中。这可以绕过堆大小的限制。然而，采用这种方式加载的模型需要与其他使用帧缓冲区栈的对象一起按顺序释放，而不是与 MicroPython 堆一起释放。通常，帧缓冲区栈比 MicroPython 堆要大得多，因此使用此选项可以加载更大的模型，但在释放时需要小心。
        一旦模型加载完成，您可以使用 predict() 多次执行它，并传入不同的输入。模型将在多次调用 predict() 之间记住其内部状态。
        当模型被删除时，它将自动释放其使用的内存，无论是来自堆（heap）还是帧缓冲区栈（frame buffer stack）。
        """
        pass
        
        
    def predict(self,inputs: list,callback=None) -> list:
        """
        使用给定的输入执行模型。输入应该是一个 numpy ndarray 对象的列表，数量对应模型支持的输入张量数。该方法返回一个 numpy ndarray 对象的列表，数量对应模型的输出张量数。
        模型的输入张量可以是最大为 4D 的 uint8、int8、uint16、int16 或 float32 类型的张量。传递的 numpy ndarray 对象会根据输入张量的缩放（scale）和零点（zero point）值，先转换为浮点数，并进行缩放/偏移，然后传递给模型。例如，一个 ndarray 类型的 uint8 值会被转换为 0.0 到 255.0 之间的 float32 值，再除以输入张量的缩放因子，然后加上输入张量的零点值。对于 int8、uint16 和 int16 值，也会执行相同的过程，而 float32 值则直接传递给模型，忽略缩放和零点值。
        模型的输出张量可以是最大为 4D 的 uint8、int8、uint16、int16 或 float32 类型的张量。对于 uint8、int8、uint16 和 int16 张量，返回的 numpy ndarray 会通过先减去输出张量的零点值，再乘以输出张量的缩放值来创建。对于 float32 张量，值会直接传递到输出，不进行任何缩放或偏移。
        请注意，predict() 方法要求输入的 ndarray 对象的形状必须与模型输入张量的形状完全匹配。如果需要，您可以使用 ndarray 的 reshape() 方法，结合模型的 input_shape 属性，将输入数据重塑为正确的形状。
        如果传递了一个 callback，它将接收 Model、inputs 和 outputs 作为参数，这允许对模型输出进行自定义后处理。然后，回调函数可以返回任何它想要的内容，这将作为 predict() 的返回值。callback 方法使得可以构建一个后处理函数库，可以根据不同模型的需求随时调用。
        对于自定义预处理，predict() 也接受可调用（”callable”）对象作为输入。任何实现了 __call__ 方法的对象都可以作为输入传递给 predict()。predict() 会使用一个可写的字节数组（bytearray）表示输入张量，并传递该张量的形状元组和数据类型值（作为整数）来调用该对象。然后，该对象应该将字节数组中的输入张量数据设置为模型所期望的内容。这就是 Normalization() 如何将图像对象转换为输入张量的方式。
        """
        pass
        
        
    
"""
`ml.preprocessing`模块包含用于图像预处理的类，以便与机器学习模型一起使用。
"""

from typing import Tuple
from typing import List
from typing import Optional
from typing import Any
import image

class Normalization:
    def __init__(self, scale: tuple[float, float] = (0.0, 1.0), mean: tuple[float, float, float] = (0.0, 0.0, 0.0), stdev: tuple[float, float, float] = (1.0, 1.0, 1.0), roi: tuple[int, int, int, int] = None):
        """
        创建一个 Normalization 对象，用于将图像对象转换为 numpy 数组，以供 predict() 使用。该对象还可用于选择图像中的感兴趣区域 (ROI) 并将其转换为 numpy 数组。
        Normalization 对象会自动将传入的任何图像类型（包括压缩图像）转换为单通道（灰度）或三通道（RGB888）图像，并将其传递到模型的张量输入中。图像会根据需要居中、按比例放大/缩小（使用双线性或区域缩放）、并裁剪，以匹配模型输入张量的大小。
        对于 uint8 输入张量，图像会被直接传递，忽略缩放和均值/标准差处理。对于 int8 输入张量，图像会从 uint8 范围平移到 int8 范围，然后直接传递，同样忽略缩放和均值/标准差处理。接受这些格式的张量比需要浮点数输入的张量处理速度更快。
        对于浮点数输入张量，无法推测模型期望的正确范围。虽然每个输入张量都编码了一个缩放值和零点值，可用于将输入转换到正确范围，但这些值并未指示浮点数输入数据应处于何种范围。例如，图像的 RGB 值在应用缩放和零点之前，应该在 (0.0, 1.0)、(-1.0, 1.0)、(0.0, 255.0) 等范围内？答案取决于模型及其训练方式。因此，Normalization 对象允许您直接指定输入数据的范围、均值和标准差。然后，灰度图像或 RGB888 图像会根据这些值转换为浮点数张量，以供模型处理。
        不支持 uint16 和 int16 输入张量。
        """
        pass
        
        
    
"""
ml 模块包含在 OpenMV Cam 上处理机器学习模型的功能。
ml 模块的核心是 Model() 对象，用于加载和执行 TensorFlow Lite 模型。Model() 对象接受一个最多为 4D 的输入张量列表，表示每个模型输入张量，并返回一个最多为 4D 的输出张量列表，表示每个模型输出张量。每个输入/输出张量都使用 numpy 的 ndarray 进行操作。
对于 TensorFlow Lite 模型，Model() 对象处理所有启用的操作，具体见 [此处](https://github.com/openmv/openmv/blob/master/src/lib/tflm/tflm_backend.cc)。Model() 对象会自动利用 CMSIS-NN、Helium 和 Ethos NPU（如果可用）来加速推理。这些加速器的可用性取决于 OpenMV Cam 的型号。
对于图像处理支持，ml 模块会通过将传递的图像对象包装在 Normalization() 对象中，自动将其转换为 numpy ndarray 对象，Normalization() 对象负责处理这一转换过程。Normalization() 对象也可以手动创建，以便控制转换过程、选择感兴趣区域（ROI）等。
有关 ndarray 对象的更多信息，请参阅 ulab 文档。所有 OpenMV Cam 都支持最多 4 维的 ndarray 对象（即 4D 张量）。
"""

from typing import Tuple
from typing import List
from typing import Optional
from typing import Any
import image

class Model:
    def __init__(self, path: str, load_to_fb: bool = False):
        """
        从 path 加载模型到内存并准备执行。path 可以是磁盘上的文件路径，也可以是内置模型的名称，内置模型会从内部闪存加载。内置于内部闪存固件映像中的模型在使用时不会占用 RAM 来存储模型权重。
        如果您尝试加载的模型非常大，无法适应 MicroPython 堆（heap），可以将 load_to_fb 设置为 True，将模型加载到帧缓冲区栈（frame buffer stack）中。这可以绕过堆大小的限制。然而，采用这种方式加载的模型需要与其他使用帧缓冲区栈的对象一起按顺序释放，而不是与 MicroPython 堆一起释放。通常，帧缓冲区栈比 MicroPython 堆要大得多，因此使用此选项可以加载更大的模型，但在释放时需要小心。
        一旦模型加载完成，您可以使用 predict() 多次执行它，并传入不同的输入。模型将在多次调用 predict() 之间记住其内部状态。
        当模型被删除时，它将自动释放其使用的内存，无论是来自堆（heap）还是帧缓冲区栈（frame buffer stack）。
        """
        pass
        
        
    def predict(self,inputs: list,callback=None) -> list:
        """
        使用给定的输入执行模型。输入应该是一个 numpy ndarray 对象的列表，数量对应模型支持的输入张量数。该方法返回一个 numpy ndarray 对象的列表，数量对应模型的输出张量数。
        模型的输入张量可以是最大为 4D 的 uint8、int8、uint16、int16 或 float32 类型的张量。传递的 numpy ndarray 对象会根据输入张量的缩放（scale）和零点（zero point）值，先转换为浮点数，并进行缩放/偏移，然后传递给模型。例如，一个 ndarray 类型的 uint8 值会被转换为 0.0 到 255.0 之间的 float32 值，再除以输入张量的缩放因子，然后加上输入张量的零点值。对于 int8、uint16 和 int16 值，也会执行相同的过程，而 float32 值则直接传递给模型，忽略缩放和零点值。
        模型的输出张量可以是最大为 4D 的 uint8、int8、uint16、int16 或 float32 类型的张量。对于 uint8、int8、uint16 和 int16 张量，返回的 numpy ndarray 会通过先减去输出张量的零点值，再乘以输出张量的缩放值来创建。对于 float32 张量，值会直接传递到输出，不进行任何缩放或偏移。
        请注意，predict() 方法要求输入的 ndarray 对象的形状必须与模型输入张量的形状完全匹配。如果需要，您可以使用 ndarray 的 reshape() 方法，结合模型的 input_shape 属性，将输入数据重塑为正确的形状。
        如果传递了一个 callback，它将接收 Model、inputs 和 outputs 作为参数，这允许对模型输出进行自定义后处理。然后，回调函数可以返回任何它想要的内容，这将作为 predict() 的返回值。callback 方法使得可以构建一个后处理函数库，可以根据不同模型的需求随时调用。
        对于自定义预处理，predict() 也接受可调用（”callable”）对象作为输入。任何实现了 __call__ 方法的对象都可以作为输入传递给 predict()。predict() 会使用一个可写的字节数组（bytearray）表示输入张量，并传递该张量的形状元组和数据类型值（作为整数）来调用该对象。然后，该对象应该将字节数组中的输入张量数据设置为模型所期望的内容。这就是 Normalization() 如何将图像对象转换为输入张量的方式。
        """
        pass
        
        
    
"""
ml.apps 模块包含各种机器学习应用类。
"""

from typing import Tuple
from typing import List
from typing import Optional
from typing import Any
import image

class MicroSpeech:
    def __init__(self, preprocessor: str = None, micro_speech: str = None, labels: list[str, ...] = None):
        """
        创建一个MicroSpeech对象。如果没有提供预处理器，则使用默认的预处理器。如果没有提供micro_speech模型，则使用默认模型。如果没有提供标签，则使用默认模型中的默认标签。
        """
        pass
        
        
    def listen(self,timeout: int = 0,callback=None,threshold: float = 0.65,filter: list[str, ...] = ['Yes', 'No']) -> tuple[str, float]:
        """
        监听一个口语单词，并在置信度超过阈值且该单词在过滤列表中时，返回该单词和置信度水平的元组。
        timeout``是监听一个单词的最大时间（以毫秒为单位）。如果为零，则该方法将无限期地监听，直到识别到一个单词。如果传入-1，该方法将不会阻塞，并会立即返回结果元组，如果未识别到任何单词，元组中可能包含``None。如果传入一个正值，该方法将在该时间（以毫秒为单位）内监听，然后返回结果元组。
        callback 是一个函数，当识别到单词时，它将被调用，并传入单词和置信度水平，而不是返回结果。当与零超时结合使用时，这允许您无限期地监听单词，并在单词被识别时进行处理。
        threshold 是返回结果所需的最低置信度水平。
        filter 是一个单词列表，模型应该识别这些单词。如果识别到的单词不在过滤列表中，则该结果将被忽略。
        """
        pass
        
        
    
"""
ml 模块包含在 OpenMV Cam 上处理机器学习模型的功能。
ml 模块的核心是 Model() 对象，用于加载和执行 TensorFlow Lite 模型。Model() 对象接受一个最多为 4D 的输入张量列表，表示每个模型输入张量，并返回一个最多为 4D 的输出张量列表，表示每个模型输出张量。每个输入/输出张量都使用 numpy 的 ndarray 进行操作。
对于 TensorFlow Lite 模型，Model() 对象处理所有启用的操作，具体见 [此处](https://github.com/openmv/openmv/blob/master/src/lib/tflm/tflm_backend.cc)。Model() 对象会自动利用 CMSIS-NN、Helium 和 Ethos NPU（如果可用）来加速推理。这些加速器的可用性取决于 OpenMV Cam 的型号。
对于图像处理支持，ml 模块会通过将传递的图像对象包装在 Normalization() 对象中，自动将其转换为 numpy ndarray 对象，Normalization() 对象负责处理这一转换过程。Normalization() 对象也可以手动创建，以便控制转换过程、选择感兴趣区域（ROI）等。
有关 ndarray 对象的更多信息，请参阅 ulab 文档。所有 OpenMV Cam 都支持最多 4 维的 ndarray 对象（即 4D 张量）。
"""

from typing import Tuple
from typing import List
from typing import Optional
from typing import Any
import image

class Model:
    def __init__(self, path: str, load_to_fb: bool = False):
        """
        从 path 加载模型到内存并准备执行。path 可以是磁盘上的文件路径，也可以是内置模型的名称，内置模型会从内部闪存加载。内置于内部闪存固件映像中的模型在使用时不会占用 RAM 来存储模型权重。
        如果您尝试加载的模型非常大，无法适应 MicroPython 堆（heap），可以将 load_to_fb 设置为 True，将模型加载到帧缓冲区栈（frame buffer stack）中。这可以绕过堆大小的限制。然而，采用这种方式加载的模型需要与其他使用帧缓冲区栈的对象一起按顺序释放，而不是与 MicroPython 堆一起释放。通常，帧缓冲区栈比 MicroPython 堆要大得多，因此使用此选项可以加载更大的模型，但在释放时需要小心。
        一旦模型加载完成，您可以使用 predict() 多次执行它，并传入不同的输入。模型将在多次调用 predict() 之间记住其内部状态。
        当模型被删除时，它将自动释放其使用的内存，无论是来自堆（heap）还是帧缓冲区栈（frame buffer stack）。
        """
        pass
        
        
    def predict(self,inputs: list,callback=None) -> list:
        """
        使用给定的输入执行模型。输入应该是一个 numpy ndarray 对象的列表，数量对应模型支持的输入张量数。该方法返回一个 numpy ndarray 对象的列表，数量对应模型的输出张量数。
        模型的输入张量可以是最大为 4D 的 uint8、int8、uint16、int16 或 float32 类型的张量。传递的 numpy ndarray 对象会根据输入张量的缩放（scale）和零点（zero point）值，先转换为浮点数，并进行缩放/偏移，然后传递给模型。例如，一个 ndarray 类型的 uint8 值会被转换为 0.0 到 255.0 之间的 float32 值，再除以输入张量的缩放因子，然后加上输入张量的零点值。对于 int8、uint16 和 int16 值，也会执行相同的过程，而 float32 值则直接传递给模型，忽略缩放和零点值。
        模型的输出张量可以是最大为 4D 的 uint8、int8、uint16、int16 或 float32 类型的张量。对于 uint8、int8、uint16 和 int16 张量，返回的 numpy ndarray 会通过先减去输出张量的零点值，再乘以输出张量的缩放值来创建。对于 float32 张量，值会直接传递到输出，不进行任何缩放或偏移。
        请注意，predict() 方法要求输入的 ndarray 对象的形状必须与模型输入张量的形状完全匹配。如果需要，您可以使用 ndarray 的 reshape() 方法，结合模型的 input_shape 属性，将输入数据重塑为正确的形状。
        如果传递了一个 callback，它将接收 Model、inputs 和 outputs 作为参数，这允许对模型输出进行自定义后处理。然后，回调函数可以返回任何它想要的内容，这将作为 predict() 的返回值。callback 方法使得可以构建一个后处理函数库，可以根据不同模型的需求随时调用。
        对于自定义预处理，predict() 也接受可调用（”callable”）对象作为输入。任何实现了 __call__ 方法的对象都可以作为输入传递给 predict()。predict() 会使用一个可写的字节数组（bytearray）表示输入张量，并传递该张量的形状元组和数据类型值（作为整数）来调用该对象。然后，该对象应该将字节数组中的输入张量数据设置为模型所期望的内容。这就是 Normalization() 如何将图像对象转换为输入张量的方式。
        """
        pass
        
        
    
