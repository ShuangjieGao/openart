"""
The ml module contains functionality for processing machine learning models on the OpenMV Cam.
The heart of the ml module is the Model() object which is used to load and execute
TensorFlow Lite models. The Model() object accepts a list of up to 4D input tensors for
each model input tensor and returns a list of up to 4D output tensors for each model output
tensor. Each input/output tensor works using a numpy ndarray.
For TensorFlow Lite models, the Model() object handles all ops enabled
here. The Model()
object will automatically leverage CMSIS-NN, Helium, and an Ethos NPU if available to speed up
inference. Availability of these accelerators is dependent on the OpenMV Cam model.
For image processing support the ml module automatically converts passed image objects to numpy
ndarray objects by wrapping them with the Normalization() object which handles this conversion. The
Normalization() object can also be manually created to control the conversion process, select an
ROI, and etc.
For more information on ndarray objects see the
ulab documentation. All OpenMV Cams support
ndarray objects up to rank 4 (meaning 4D tensors).
"""

from typing import Tuple
from typing import List
from typing import Optional
from typing import Any
import image

class Model:
    def __init__(self, path: str, load_to_fb: bool = False):
        """
        Loads a model from path into memory and prepares it for being executed. path can either
        be a file on disk or the name of a built-in model which will be loaded from internal flash. Models that are
        built-in to the internal flash firmware image do not take up RAM to store the model weights when used.
        If the model you are trying to load is very large and doesn’t fit in the MicroPython heap you
        can set load_to_fb to True to load the model into the frame buffer stack instead. This allows
        you to get around the heap size limitations. However, models loaded this way need to be deallocated
        in-order with anything else that uses the frame buffer stack versus the MicroPython heap. Typically,
        the frame buffer stack is much larger than the MicroPython heap so you can load much larger models
        using this option, but, you need to be careful if you deallocate.
        Once a model is loaded you can execute it multiple times with different inputs using predict().
        The model will remember its internal state between calls to predict().
        When deleted the model will automatically free up any memory it used from the heap or frame buffer stack.
        """
        pass
        
        
    def predict(self,inputs: list,callback=None) -> list:
        """
        Executes the model with the given inputs. The inputs should be a list of numpy ndarray objects corresponding
        to the number of input tensors the model supports. The method returns a list of numpy ndarray objects
        corresponding to the number of output tensors the model has.
        The model input tensors can be up to 4D tensors of uint8, int8, uint16, int16, or float32 values. The passed
        numpy ndarray for an input tensor is then converted to floating point and scaled/offset based on
        the input tensor’s scale and zero point values before being passed to the model. For example, an ndarray
        of uint8 values will be converted to float32s between 0.0-255.0, divided by the input tensor’s scale, and
        then have the input tensor’s zero point added to it. The same process is done for int8, uint16, and int16 values
        whereas float32 values are passed directly to the model ignoring the scale and zero point values.
        The model’s output tensors can be up to 4D tensors of uint8, int8, uint16, int16, or float32 values. For uint8,
        int8, uint16, and int16 tensors the returned numpy ndarray is created by subtracting the output tensor’s zero
        point value before multiplying by the output tensor’s scale value. For float32 tensors, values are
        passed directly to the output without any scaling or offset being applied.
        Note that predict() requires the shape of the input ndarray objects to match the shape of the model
        input tensors exactly. You can use the reshape() method of an ndarray with the input_shape
        attribute of the model to reshape the input data to the correct shape if necessary.
        If a callback is passed then it will receive the Model, inputs, and outputs as arguments
        which allows for custom post-processing of the model outputs. The callback may then return
        whatever it likes which will be returned by predict(). The callback method allows for building
        up a library of post-processing functions that can be used on demand for different models.
        For custom pre-processing, predict() also accepts “callable” objects as inputs. Any object
        implementing the __call__ method can be passed to predict() as an input. predict() will
        then call the object with a writeable bytearray representing the input tensor, the input tensor’s shape tuple,
        and the input tensors data type value (as an int). The object should then set the input tensor data in the
        bytearray to what the model expects. This is how Normalization() converts image objects to input tensors.
        """
        pass
        
        
    
"""
The ml.apps module contains various ML application classes.
"""

from typing import Tuple
from typing import List
from typing import Optional
from typing import Any
import image

class MicroSpeech:
    def __init__(self, preprocessor: str = None, micro_speech: str = None, labels: list[str, ...] = None):
        """
        Creates a MicroSpeech object. If no preprocessor is provided, the default preprocessor is used.
        If no micro_speech model is provided, the default model is used. If no labels are provided, the
        default labels are used from the default model.
        """
        pass
        
        
    def listen(self,timeout: int = 0,callback=None,threshold: float = 0.65,filter: list[str, ...] = ['Yes', 'No']) -> tuple[str, float]:
        """
        Listens for a spoken word and returns the word and confidence level as a tuple if the
        confidence level is above the threshold and the word is in the filter list.
        timeout is the maximum time in milliseconds to listen for a word. If zero, the method
        will listen indefinitely until a word is recognized. If -1 is passed, the method will not
        block and will return immediately with the result tuple which may contain None if no
        word is recognized. If a positive value is passed, the method will listen for that amount
        of time in milliseconds and then return the result tuple.
        callback is a function that will be called with the word and confidence level instead
        of returning the result. When combined with a timeout of zero, this allows you to listen
        for words indefinitely and process them as they are recognized.
        threshold is the minimum confidence level required to return a result.
        filter is a list of words that the model should recognize. If the recognized word is
        not in the filter list, the result is ignored.
        """
        pass
        
        
    
"""
The ml module contains functionality for processing machine learning models on the OpenMV Cam.
The heart of the ml module is the Model() object which is used to load and execute
TensorFlow Lite models. The Model() object accepts a list of up to 4D input tensors for
each model input tensor and returns a list of up to 4D output tensors for each model output
tensor. Each input/output tensor works using a numpy ndarray.
For TensorFlow Lite models, the Model() object handles all ops enabled
here. The Model()
object will automatically leverage CMSIS-NN, Helium, and an Ethos NPU if available to speed up
inference. Availability of these accelerators is dependent on the OpenMV Cam model.
For image processing support the ml module automatically converts passed image objects to numpy
ndarray objects by wrapping them with the Normalization() object which handles this conversion. The
Normalization() object can also be manually created to control the conversion process, select an
ROI, and etc.
For more information on ndarray objects see the
ulab documentation. All OpenMV Cams support
ndarray objects up to rank 4 (meaning 4D tensors).
"""

from typing import Tuple
from typing import List
from typing import Optional
from typing import Any
import image

class Model:
    def __init__(self, path: str, load_to_fb: bool = False):
        """
        Loads a model from path into memory and prepares it for being executed. path can either
        be a file on disk or the name of a built-in model which will be loaded from internal flash. Models that are
        built-in to the internal flash firmware image do not take up RAM to store the model weights when used.
        If the model you are trying to load is very large and doesn’t fit in the MicroPython heap you
        can set load_to_fb to True to load the model into the frame buffer stack instead. This allows
        you to get around the heap size limitations. However, models loaded this way need to be deallocated
        in-order with anything else that uses the frame buffer stack versus the MicroPython heap. Typically,
        the frame buffer stack is much larger than the MicroPython heap so you can load much larger models
        using this option, but, you need to be careful if you deallocate.
        Once a model is loaded you can execute it multiple times with different inputs using predict().
        The model will remember its internal state between calls to predict().
        When deleted the model will automatically free up any memory it used from the heap or frame buffer stack.
        """
        pass
        
        
    def predict(self,inputs: list,callback=None) -> list:
        """
        Executes the model with the given inputs. The inputs should be a list of numpy ndarray objects corresponding
        to the number of input tensors the model supports. The method returns a list of numpy ndarray objects
        corresponding to the number of output tensors the model has.
        The model input tensors can be up to 4D tensors of uint8, int8, uint16, int16, or float32 values. The passed
        numpy ndarray for an input tensor is then converted to floating point and scaled/offset based on
        the input tensor’s scale and zero point values before being passed to the model. For example, an ndarray
        of uint8 values will be converted to float32s between 0.0-255.0, divided by the input tensor’s scale, and
        then have the input tensor’s zero point added to it. The same process is done for int8, uint16, and int16 values
        whereas float32 values are passed directly to the model ignoring the scale and zero point values.
        The model’s output tensors can be up to 4D tensors of uint8, int8, uint16, int16, or float32 values. For uint8,
        int8, uint16, and int16 tensors the returned numpy ndarray is created by subtracting the output tensor’s zero
        point value before multiplying by the output tensor’s scale value. For float32 tensors, values are
        passed directly to the output without any scaling or offset being applied.
        Note that predict() requires the shape of the input ndarray objects to match the shape of the model
        input tensors exactly. You can use the reshape() method of an ndarray with the input_shape
        attribute of the model to reshape the input data to the correct shape if necessary.
        If a callback is passed then it will receive the Model, inputs, and outputs as arguments
        which allows for custom post-processing of the model outputs. The callback may then return
        whatever it likes which will be returned by predict(). The callback method allows for building
        up a library of post-processing functions that can be used on demand for different models.
        For custom pre-processing, predict() also accepts “callable” objects as inputs. Any object
        implementing the __call__ method can be passed to predict() as an input. predict() will
        then call the object with a writeable bytearray representing the input tensor, the input tensor’s shape tuple,
        and the input tensors data type value (as an int). The object should then set the input tensor data in the
        bytearray to what the model expects. This is how Normalization() converts image objects to input tensors.
        """
        pass
        
        
    
"""
The ml.preprocessing module contains classes for preprocessing images for use with machine learning models.
"""

from typing import Tuple
from typing import List
from typing import Optional
from typing import Any
import image

class Normalization:
    def __init__(self, scale: tuple[float, float] = (0.0, 1.0), mean: tuple[float, float, float] = (0.0, 0.0, 0.0), stdev: tuple[float, float, float] = (1.0, 1.0, 1.0), roi: tuple[int, int, int, int] = None):
        """
        Creates a Normalization object which is used to convert image objects to numpy arrays for use with the
        predict(). The object can also be used to select a region of interest (ROI) in the image to
        convert to a numpy array.
        The Normalization object automatically converts any image type passed (including compressed images)
        into either a single channel (grayscale) or three channel (RGB888) image which is passed to the tensor
        input of the model. Images are centered, scaled up/down (using bilinear/area scaling), and cropped as
        necessary to match the input tensor size of the model.
        For uint8 input tensors the image is directly passed ignoring scale and mean/stdev. For int8
        input tensors the image is shifted to be within the int8 range from the uint8 range and
        then directly passed ignoring scale and mean/stdev. Tensors that accept either of these formats
        can be processed more quickly than tensors that require floating point inputs.
        For floating point input tensors it’s not possible to guess the correct range that the model
        expects. While each input tensor encodes a scale and zero point value that can be used to
        convert the input to the correct range, these values do not tell you what the range
        of the input data should be in floating point. E.g. should image RGB values be within the range
        of (0.0, 1.0), (-1.0, 1.0), (0.0, 255.0), and etc. before applying a scale and zero point? The
        answer is that it depends on the model and how it was trained. So, the normalization object instead
        allows you to directly specify the range of the input data, the mean, and the standard deviation. The
        Grayscale or RGB88 image is then converted into a floating point tensor for the model to process
        based on these values.
        uint16 and int16 input tensors are not supported.
        """
        pass
        
        
    
"""
The ml module contains functionality for processing machine learning models on the OpenMV Cam.
The heart of the ml module is the Model() object which is used to load and execute
TensorFlow Lite models. The Model() object accepts a list of up to 4D input tensors for
each model input tensor and returns a list of up to 4D output tensors for each model output
tensor. Each input/output tensor works using a numpy ndarray.
For TensorFlow Lite models, the Model() object handles all ops enabled
here. The Model()
object will automatically leverage CMSIS-NN, Helium, and an Ethos NPU if available to speed up
inference. Availability of these accelerators is dependent on the OpenMV Cam model.
For image processing support the ml module automatically converts passed image objects to numpy
ndarray objects by wrapping them with the Normalization() object which handles this conversion. The
Normalization() object can also be manually created to control the conversion process, select an
ROI, and etc.
For more information on ndarray objects see the
ulab documentation. All OpenMV Cams support
ndarray objects up to rank 4 (meaning 4D tensors).
"""

from typing import Tuple
from typing import List
from typing import Optional
from typing import Any
import image

class Model:
    def __init__(self, path: str, load_to_fb: bool = False):
        """
        Loads a model from path into memory and prepares it for being executed. path can either
        be a file on disk or the name of a built-in model which will be loaded from internal flash. Models that are
        built-in to the internal flash firmware image do not take up RAM to store the model weights when used.
        If the model you are trying to load is very large and doesn’t fit in the MicroPython heap you
        can set load_to_fb to True to load the model into the frame buffer stack instead. This allows
        you to get around the heap size limitations. However, models loaded this way need to be deallocated
        in-order with anything else that uses the frame buffer stack versus the MicroPython heap. Typically,
        the frame buffer stack is much larger than the MicroPython heap so you can load much larger models
        using this option, but, you need to be careful if you deallocate.
        Once a model is loaded you can execute it multiple times with different inputs using predict().
        The model will remember its internal state between calls to predict().
        When deleted the model will automatically free up any memory it used from the heap or frame buffer stack.
        """
        pass
        
        
    def predict(self,inputs: list,callback=None) -> list:
        """
        Executes the model with the given inputs. The inputs should be a list of numpy ndarray objects corresponding
        to the number of input tensors the model supports. The method returns a list of numpy ndarray objects
        corresponding to the number of output tensors the model has.
        The model input tensors can be up to 4D tensors of uint8, int8, uint16, int16, or float32 values. The passed
        numpy ndarray for an input tensor is then converted to floating point and scaled/offset based on
        the input tensor’s scale and zero point values before being passed to the model. For example, an ndarray
        of uint8 values will be converted to float32s between 0.0-255.0, divided by the input tensor’s scale, and
        then have the input tensor’s zero point added to it. The same process is done for int8, uint16, and int16 values
        whereas float32 values are passed directly to the model ignoring the scale and zero point values.
        The model’s output tensors can be up to 4D tensors of uint8, int8, uint16, int16, or float32 values. For uint8,
        int8, uint16, and int16 tensors the returned numpy ndarray is created by subtracting the output tensor’s zero
        point value before multiplying by the output tensor’s scale value. For float32 tensors, values are
        passed directly to the output without any scaling or offset being applied.
        Note that predict() requires the shape of the input ndarray objects to match the shape of the model
        input tensors exactly. You can use the reshape() method of an ndarray with the input_shape
        attribute of the model to reshape the input data to the correct shape if necessary.
        If a callback is passed then it will receive the Model, inputs, and outputs as arguments
        which allows for custom post-processing of the model outputs. The callback may then return
        whatever it likes which will be returned by predict(). The callback method allows for building
        up a library of post-processing functions that can be used on demand for different models.
        For custom pre-processing, predict() also accepts “callable” objects as inputs. Any object
        implementing the __call__ method can be passed to predict() as an input. predict() will
        then call the object with a writeable bytearray representing the input tensor, the input tensor’s shape tuple,
        and the input tensors data type value (as an int). The object should then set the input tensor data in the
        bytearray to what the model expects. This is how Normalization() converts image objects to input tensors.
        """
        pass
        
        
    
"""
The ml.apps module contains various ML application classes.
"""

from typing import Tuple
from typing import List
from typing import Optional
from typing import Any
import image

class MicroSpeech:
    def __init__(self, preprocessor: str = None, micro_speech: str = None, labels: list[str, ...] = None):
        """
        Creates a MicroSpeech object. If no preprocessor is provided, the default preprocessor is used.
        If no micro_speech model is provided, the default model is used. If no labels are provided, the
        default labels are used from the default model.
        """
        pass
        
        
    def listen(self,timeout: int = 0,callback=None,threshold: float = 0.65,filter: list[str, ...] = ['Yes', 'No']) -> tuple[str, float]:
        """
        Listens for a spoken word and returns the word and confidence level as a tuple if the
        confidence level is above the threshold and the word is in the filter list.
        timeout is the maximum time in milliseconds to listen for a word. If zero, the method
        will listen indefinitely until a word is recognized. If -1 is passed, the method will not
        block and will return immediately with the result tuple which may contain None if no
        word is recognized. If a positive value is passed, the method will listen for that amount
        of time in milliseconds and then return the result tuple.
        callback is a function that will be called with the word and confidence level instead
        of returning the result. When combined with a timeout of zero, this allows you to listen
        for words indefinitely and process them as they are recognized.
        threshold is the minimum confidence level required to return a result.
        filter is a list of words that the model should recognize. If the recognized word is
        not in the filter list, the result is ignored.
        """
        pass
        
        
    
"""
The ml module contains functionality for processing machine learning models on the OpenMV Cam.
The heart of the ml module is the Model() object which is used to load and execute
TensorFlow Lite models. The Model() object accepts a list of up to 4D input tensors for
each model input tensor and returns a list of up to 4D output tensors for each model output
tensor. Each input/output tensor works using a numpy ndarray.
For TensorFlow Lite models, the Model() object handles all ops enabled
here. The Model()
object will automatically leverage CMSIS-NN, Helium, and an Ethos NPU if available to speed up
inference. Availability of these accelerators is dependent on the OpenMV Cam model.
For image processing support the ml module automatically converts passed image objects to numpy
ndarray objects by wrapping them with the Normalization() object which handles this conversion. The
Normalization() object can also be manually created to control the conversion process, select an
ROI, and etc.
For more information on ndarray objects see the
ulab documentation. All OpenMV Cams support
ndarray objects up to rank 4 (meaning 4D tensors).
"""

from typing import Tuple
from typing import List
from typing import Optional
from typing import Any
import image

class Model:
    def __init__(self, path: str, load_to_fb: bool = False):
        """
        Loads a model from path into memory and prepares it for being executed. path can either
        be a file on disk or the name of a built-in model which will be loaded from internal flash. Models that are
        built-in to the internal flash firmware image do not take up RAM to store the model weights when used.
        If the model you are trying to load is very large and doesn’t fit in the MicroPython heap you
        can set load_to_fb to True to load the model into the frame buffer stack instead. This allows
        you to get around the heap size limitations. However, models loaded this way need to be deallocated
        in-order with anything else that uses the frame buffer stack versus the MicroPython heap. Typically,
        the frame buffer stack is much larger than the MicroPython heap so you can load much larger models
        using this option, but, you need to be careful if you deallocate.
        Once a model is loaded you can execute it multiple times with different inputs using predict().
        The model will remember its internal state between calls to predict().
        When deleted the model will automatically free up any memory it used from the heap or frame buffer stack.
        """
        pass
        
        
    def predict(self,inputs: list,callback=None) -> list:
        """
        Executes the model with the given inputs. The inputs should be a list of numpy ndarray objects corresponding
        to the number of input tensors the model supports. The method returns a list of numpy ndarray objects
        corresponding to the number of output tensors the model has.
        The model input tensors can be up to 4D tensors of uint8, int8, uint16, int16, or float32 values. The passed
        numpy ndarray for an input tensor is then converted to floating point and scaled/offset based on
        the input tensor’s scale and zero point values before being passed to the model. For example, an ndarray
        of uint8 values will be converted to float32s between 0.0-255.0, divided by the input tensor’s scale, and
        then have the input tensor’s zero point added to it. The same process is done for int8, uint16, and int16 values
        whereas float32 values are passed directly to the model ignoring the scale and zero point values.
        The model’s output tensors can be up to 4D tensors of uint8, int8, uint16, int16, or float32 values. For uint8,
        int8, uint16, and int16 tensors the returned numpy ndarray is created by subtracting the output tensor’s zero
        point value before multiplying by the output tensor’s scale value. For float32 tensors, values are
        passed directly to the output without any scaling or offset being applied.
        Note that predict() requires the shape of the input ndarray objects to match the shape of the model
        input tensors exactly. You can use the reshape() method of an ndarray with the input_shape
        attribute of the model to reshape the input data to the correct shape if necessary.
        If a callback is passed then it will receive the Model, inputs, and outputs as arguments
        which allows for custom post-processing of the model outputs. The callback may then return
        whatever it likes which will be returned by predict(). The callback method allows for building
        up a library of post-processing functions that can be used on demand for different models.
        For custom pre-processing, predict() also accepts “callable” objects as inputs. Any object
        implementing the __call__ method can be passed to predict() as an input. predict() will
        then call the object with a writeable bytearray representing the input tensor, the input tensor’s shape tuple,
        and the input tensors data type value (as an int). The object should then set the input tensor data in the
        bytearray to what the model expects. This is how Normalization() converts image objects to input tensors.
        """
        pass
        
        
    
"""
The ml.utils module contains utility classes and functions for machine learning.
"""

from typing import Tuple
from typing import List
from typing import Optional
from typing import Any
import image

class NMS:
    def __init__(self, window_w: int, window_h: int, roi: tuple[int, int, int, int]):
        """
        Creates a NMS object with the given window size and region of interest (ROI). The window is
        width/height of the input tensor of image model. The ROI is the region of interest that returned by the
        Normalization() object which corresponds to the region of the image that the model was run on.
        This allows the NMS object to remap bounding boxes detected in a sub-window back to the original
        image coordinates.
        """
        pass
        
        
    def add_bounding_boxes(self,xmin: float,ymin: float,xmax: float,ymax: float,score: float,label_index: int) -> None:
        """
        Adds a bounding box to the NMS object with the given coordinates, score, and label index.
        xmin, ymin, xmax, and ymax are the bounding box coordinates in the range of 0.0 to 1.0
        where (0.0, 0.0) is the top-left corner of the image and (1.0, 1.0) is the bottom-right corner of the image.
        score is the confidence score of the bounding box (0.0-1.0).
        label_index is the index of the label associated with the bounding box.
        """
        pass
        
        
    def get_bounding_boxes(self,threshold: float = 0.1,sigma: float = 0.1) -> list[tuple[int, int, int, int, float, int]]:
        """
        Returns a list of bounding boxes that have been filtered by the NMS object and remapped
        to the original image coordinates. Bounding box tuples are
        (x, y, w, h, score, label_index). After calling this method you should create a new
        NMS object if you want to process a new set of bounding boxes.
        Bounding boxes must have a higher score then threshold to be kept.
        sigma controls the gaussian used to apply a score penalty to overlapping bounding boxes
        using the Soft-Non-Maximum-Suppression algorithm. A higher sigma will result in a more
        aggressive suppression of overlapping bounding boxes.
        """
        pass
        
        
    
"""
The ml module contains functionality for processing machine learning models on the OpenMV Cam.
The heart of the ml module is the Model() object which is used to load and execute
TensorFlow Lite models. The Model() object accepts a list of up to 4D input tensors for
each model input tensor and returns a list of up to 4D output tensors for each model output
tensor. Each input/output tensor works using a numpy ndarray.
For TensorFlow Lite models, the Model() object handles all ops enabled
here. The Model()
object will automatically leverage CMSIS-NN, Helium, and an Ethos NPU if available to speed up
inference. Availability of these accelerators is dependent on the OpenMV Cam model.
For image processing support the ml module automatically converts passed image objects to numpy
ndarray objects by wrapping them with the Normalization() object which handles this conversion. The
Normalization() object can also be manually created to control the conversion process, select an
ROI, and etc.
For more information on ndarray objects see the
ulab documentation. All OpenMV Cams support
ndarray objects up to rank 4 (meaning 4D tensors).
"""

from typing import Tuple
from typing import List
from typing import Optional
from typing import Any
import image

class Model:
    def __init__(self, path: str, load_to_fb: bool = False):
        """
        Loads a model from path into memory and prepares it for being executed. path can either
        be a file on disk or the name of a built-in model which will be loaded from internal flash. Models that are
        built-in to the internal flash firmware image do not take up RAM to store the model weights when used.
        If the model you are trying to load is very large and doesn’t fit in the MicroPython heap you
        can set load_to_fb to True to load the model into the frame buffer stack instead. This allows
        you to get around the heap size limitations. However, models loaded this way need to be deallocated
        in-order with anything else that uses the frame buffer stack versus the MicroPython heap. Typically,
        the frame buffer stack is much larger than the MicroPython heap so you can load much larger models
        using this option, but, you need to be careful if you deallocate.
        Once a model is loaded you can execute it multiple times with different inputs using predict().
        The model will remember its internal state between calls to predict().
        When deleted the model will automatically free up any memory it used from the heap or frame buffer stack.
        """
        pass
        
        
    def predict(self,inputs: list,callback=None) -> list:
        """
        Executes the model with the given inputs. The inputs should be a list of numpy ndarray objects corresponding
        to the number of input tensors the model supports. The method returns a list of numpy ndarray objects
        corresponding to the number of output tensors the model has.
        The model input tensors can be up to 4D tensors of uint8, int8, uint16, int16, or float32 values. The passed
        numpy ndarray for an input tensor is then converted to floating point and scaled/offset based on
        the input tensor’s scale and zero point values before being passed to the model. For example, an ndarray
        of uint8 values will be converted to float32s between 0.0-255.0, divided by the input tensor’s scale, and
        then have the input tensor’s zero point added to it. The same process is done for int8, uint16, and int16 values
        whereas float32 values are passed directly to the model ignoring the scale and zero point values.
        The model’s output tensors can be up to 4D tensors of uint8, int8, uint16, int16, or float32 values. For uint8,
        int8, uint16, and int16 tensors the returned numpy ndarray is created by subtracting the output tensor’s zero
        point value before multiplying by the output tensor’s scale value. For float32 tensors, values are
        passed directly to the output without any scaling or offset being applied.
        Note that predict() requires the shape of the input ndarray objects to match the shape of the model
        input tensors exactly. You can use the reshape() method of an ndarray with the input_shape
        attribute of the model to reshape the input data to the correct shape if necessary.
        If a callback is passed then it will receive the Model, inputs, and outputs as arguments
        which allows for custom post-processing of the model outputs. The callback may then return
        whatever it likes which will be returned by predict(). The callback method allows for building
        up a library of post-processing functions that can be used on demand for different models.
        For custom pre-processing, predict() also accepts “callable” objects as inputs. Any object
        implementing the __call__ method can be passed to predict() as an input. predict() will
        then call the object with a writeable bytearray representing the input tensor, the input tensor’s shape tuple,
        and the input tensors data type value (as an int). The object should then set the input tensor data in the
        bytearray to what the model expects. This is how Normalization() converts image objects to input tensors.
        """
        pass
        
        
    
"""
The ml.apps module contains various ML application classes.
"""

from typing import Tuple
from typing import List
from typing import Optional
from typing import Any
import image

class MicroSpeech:
    def __init__(self, preprocessor: str = None, micro_speech: str = None, labels: list[str, ...] = None):
        """
        Creates a MicroSpeech object. If no preprocessor is provided, the default preprocessor is used.
        If no micro_speech model is provided, the default model is used. If no labels are provided, the
        default labels are used from the default model.
        """
        pass
        
        
    def listen(self,timeout: int = 0,callback=None,threshold: float = 0.65,filter: list[str, ...] = ['Yes', 'No']) -> tuple[str, float]:
        """
        Listens for a spoken word and returns the word and confidence level as a tuple if the
        confidence level is above the threshold and the word is in the filter list.
        timeout is the maximum time in milliseconds to listen for a word. If zero, the method
        will listen indefinitely until a word is recognized. If -1 is passed, the method will not
        block and will return immediately with the result tuple which may contain None if no
        word is recognized. If a positive value is passed, the method will listen for that amount
        of time in milliseconds and then return the result tuple.
        callback is a function that will be called with the word and confidence level instead
        of returning the result. When combined with a timeout of zero, this allows you to listen
        for words indefinitely and process them as they are recognized.
        threshold is the minimum confidence level required to return a result.
        filter is a list of words that the model should recognize. If the recognized word is
        not in the filter list, the result is ignored.
        """
        pass
        
        
    
"""
The ml module contains functionality for processing machine learning models on the OpenMV Cam.
The heart of the ml module is the Model() object which is used to load and execute
TensorFlow Lite models. The Model() object accepts a list of up to 4D input tensors for
each model input tensor and returns a list of up to 4D output tensors for each model output
tensor. Each input/output tensor works using a numpy ndarray.
For TensorFlow Lite models, the Model() object handles all ops enabled
here. The Model()
object will automatically leverage CMSIS-NN, Helium, and an Ethos NPU if available to speed up
inference. Availability of these accelerators is dependent on the OpenMV Cam model.
For image processing support the ml module automatically converts passed image objects to numpy
ndarray objects by wrapping them with the Normalization() object which handles this conversion. The
Normalization() object can also be manually created to control the conversion process, select an
ROI, and etc.
For more information on ndarray objects see the
ulab documentation. All OpenMV Cams support
ndarray objects up to rank 4 (meaning 4D tensors).
"""

from typing import Tuple
from typing import List
from typing import Optional
from typing import Any
import image

class Model:
    def __init__(self, path: str, load_to_fb: bool = False):
        """
        Loads a model from path into memory and prepares it for being executed. path can either
        be a file on disk or the name of a built-in model which will be loaded from internal flash. Models that are
        built-in to the internal flash firmware image do not take up RAM to store the model weights when used.
        If the model you are trying to load is very large and doesn’t fit in the MicroPython heap you
        can set load_to_fb to True to load the model into the frame buffer stack instead. This allows
        you to get around the heap size limitations. However, models loaded this way need to be deallocated
        in-order with anything else that uses the frame buffer stack versus the MicroPython heap. Typically,
        the frame buffer stack is much larger than the MicroPython heap so you can load much larger models
        using this option, but, you need to be careful if you deallocate.
        Once a model is loaded you can execute it multiple times with different inputs using predict().
        The model will remember its internal state between calls to predict().
        When deleted the model will automatically free up any memory it used from the heap or frame buffer stack.
        """
        pass
        
        
    def predict(self,inputs: list,callback=None) -> list:
        """
        Executes the model with the given inputs. The inputs should be a list of numpy ndarray objects corresponding
        to the number of input tensors the model supports. The method returns a list of numpy ndarray objects
        corresponding to the number of output tensors the model has.
        The model input tensors can be up to 4D tensors of uint8, int8, uint16, int16, or float32 values. The passed
        numpy ndarray for an input tensor is then converted to floating point and scaled/offset based on
        the input tensor’s scale and zero point values before being passed to the model. For example, an ndarray
        of uint8 values will be converted to float32s between 0.0-255.0, divided by the input tensor’s scale, and
        then have the input tensor’s zero point added to it. The same process is done for int8, uint16, and int16 values
        whereas float32 values are passed directly to the model ignoring the scale and zero point values.
        The model’s output tensors can be up to 4D tensors of uint8, int8, uint16, int16, or float32 values. For uint8,
        int8, uint16, and int16 tensors the returned numpy ndarray is created by subtracting the output tensor’s zero
        point value before multiplying by the output tensor’s scale value. For float32 tensors, values are
        passed directly to the output without any scaling or offset being applied.
        Note that predict() requires the shape of the input ndarray objects to match the shape of the model
        input tensors exactly. You can use the reshape() method of an ndarray with the input_shape
        attribute of the model to reshape the input data to the correct shape if necessary.
        If a callback is passed then it will receive the Model, inputs, and outputs as arguments
        which allows for custom post-processing of the model outputs. The callback may then return
        whatever it likes which will be returned by predict(). The callback method allows for building
        up a library of post-processing functions that can be used on demand for different models.
        For custom pre-processing, predict() also accepts “callable” objects as inputs. Any object
        implementing the __call__ method can be passed to predict() as an input. predict() will
        then call the object with a writeable bytearray representing the input tensor, the input tensor’s shape tuple,
        and the input tensors data type value (as an int). The object should then set the input tensor data in the
        bytearray to what the model expects. This is how Normalization() converts image objects to input tensors.
        """
        pass
        
        
    
"""
The ml.preprocessing module contains classes for preprocessing images for use with machine learning models.
"""

from typing import Tuple
from typing import List
from typing import Optional
from typing import Any
import image

class Normalization:
    def __init__(self, scale: tuple[float, float] = (0.0, 1.0), mean: tuple[float, float, float] = (0.0, 0.0, 0.0), stdev: tuple[float, float, float] = (1.0, 1.0, 1.0), roi: tuple[int, int, int, int] = None):
        """
        Creates a Normalization object which is used to convert image objects to numpy arrays for use with the
        predict(). The object can also be used to select a region of interest (ROI) in the image to
        convert to a numpy array.
        The Normalization object automatically converts any image type passed (including compressed images)
        into either a single channel (grayscale) or three channel (RGB888) image which is passed to the tensor
        input of the model. Images are centered, scaled up/down (using bilinear/area scaling), and cropped as
        necessary to match the input tensor size of the model.
        For uint8 input tensors the image is directly passed ignoring scale and mean/stdev. For int8
        input tensors the image is shifted to be within the int8 range from the uint8 range and
        then directly passed ignoring scale and mean/stdev. Tensors that accept either of these formats
        can be processed more quickly than tensors that require floating point inputs.
        For floating point input tensors it’s not possible to guess the correct range that the model
        expects. While each input tensor encodes a scale and zero point value that can be used to
        convert the input to the correct range, these values do not tell you what the range
        of the input data should be in floating point. E.g. should image RGB values be within the range
        of (0.0, 1.0), (-1.0, 1.0), (0.0, 255.0), and etc. before applying a scale and zero point? The
        answer is that it depends on the model and how it was trained. So, the normalization object instead
        allows you to directly specify the range of the input data, the mean, and the standard deviation. The
        Grayscale or RGB88 image is then converted into a floating point tensor for the model to process
        based on these values.
        uint16 and int16 input tensors are not supported.
        """
        pass
        
        
    
"""
The ml module contains functionality for processing machine learning models on the OpenMV Cam.
The heart of the ml module is the Model() object which is used to load and execute
TensorFlow Lite models. The Model() object accepts a list of up to 4D input tensors for
each model input tensor and returns a list of up to 4D output tensors for each model output
tensor. Each input/output tensor works using a numpy ndarray.
For TensorFlow Lite models, the Model() object handles all ops enabled
here. The Model()
object will automatically leverage CMSIS-NN, Helium, and an Ethos NPU if available to speed up
inference. Availability of these accelerators is dependent on the OpenMV Cam model.
For image processing support the ml module automatically converts passed image objects to numpy
ndarray objects by wrapping them with the Normalization() object which handles this conversion. The
Normalization() object can also be manually created to control the conversion process, select an
ROI, and etc.
For more information on ndarray objects see the
ulab documentation. All OpenMV Cams support
ndarray objects up to rank 4 (meaning 4D tensors).
"""

from typing import Tuple
from typing import List
from typing import Optional
from typing import Any
import image

class Model:
    def __init__(self, path: str, load_to_fb: bool = False):
        """
        Loads a model from path into memory and prepares it for being executed. path can either
        be a file on disk or the name of a built-in model which will be loaded from internal flash. Models that are
        built-in to the internal flash firmware image do not take up RAM to store the model weights when used.
        If the model you are trying to load is very large and doesn’t fit in the MicroPython heap you
        can set load_to_fb to True to load the model into the frame buffer stack instead. This allows
        you to get around the heap size limitations. However, models loaded this way need to be deallocated
        in-order with anything else that uses the frame buffer stack versus the MicroPython heap. Typically,
        the frame buffer stack is much larger than the MicroPython heap so you can load much larger models
        using this option, but, you need to be careful if you deallocate.
        Once a model is loaded you can execute it multiple times with different inputs using predict().
        The model will remember its internal state between calls to predict().
        When deleted the model will automatically free up any memory it used from the heap or frame buffer stack.
        """
        pass
        
        
    def predict(self,inputs: list,callback=None) -> list:
        """
        Executes the model with the given inputs. The inputs should be a list of numpy ndarray objects corresponding
        to the number of input tensors the model supports. The method returns a list of numpy ndarray objects
        corresponding to the number of output tensors the model has.
        The model input tensors can be up to 4D tensors of uint8, int8, uint16, int16, or float32 values. The passed
        numpy ndarray for an input tensor is then converted to floating point and scaled/offset based on
        the input tensor’s scale and zero point values before being passed to the model. For example, an ndarray
        of uint8 values will be converted to float32s between 0.0-255.0, divided by the input tensor’s scale, and
        then have the input tensor’s zero point added to it. The same process is done for int8, uint16, and int16 values
        whereas float32 values are passed directly to the model ignoring the scale and zero point values.
        The model’s output tensors can be up to 4D tensors of uint8, int8, uint16, int16, or float32 values. For uint8,
        int8, uint16, and int16 tensors the returned numpy ndarray is created by subtracting the output tensor’s zero
        point value before multiplying by the output tensor’s scale value. For float32 tensors, values are
        passed directly to the output without any scaling or offset being applied.
        Note that predict() requires the shape of the input ndarray objects to match the shape of the model
        input tensors exactly. You can use the reshape() method of an ndarray with the input_shape
        attribute of the model to reshape the input data to the correct shape if necessary.
        If a callback is passed then it will receive the Model, inputs, and outputs as arguments
        which allows for custom post-processing of the model outputs. The callback may then return
        whatever it likes which will be returned by predict(). The callback method allows for building
        up a library of post-processing functions that can be used on demand for different models.
        For custom pre-processing, predict() also accepts “callable” objects as inputs. Any object
        implementing the __call__ method can be passed to predict() as an input. predict() will
        then call the object with a writeable bytearray representing the input tensor, the input tensor’s shape tuple,
        and the input tensors data type value (as an int). The object should then set the input tensor data in the
        bytearray to what the model expects. This is how Normalization() converts image objects to input tensors.
        """
        pass
        
        
    
"""
The ml.apps module contains various ML application classes.
"""

from typing import Tuple
from typing import List
from typing import Optional
from typing import Any
import image

class MicroSpeech:
    def __init__(self, preprocessor: str = None, micro_speech: str = None, labels: list[str, ...] = None):
        """
        Creates a MicroSpeech object. If no preprocessor is provided, the default preprocessor is used.
        If no micro_speech model is provided, the default model is used. If no labels are provided, the
        default labels are used from the default model.
        """
        pass
        
        
    def listen(self,timeout: int = 0,callback=None,threshold: float = 0.65,filter: list[str, ...] = ['Yes', 'No']) -> tuple[str, float]:
        """
        Listens for a spoken word and returns the word and confidence level as a tuple if the
        confidence level is above the threshold and the word is in the filter list.
        timeout is the maximum time in milliseconds to listen for a word. If zero, the method
        will listen indefinitely until a word is recognized. If -1 is passed, the method will not
        block and will return immediately with the result tuple which may contain None if no
        word is recognized. If a positive value is passed, the method will listen for that amount
        of time in milliseconds and then return the result tuple.
        callback is a function that will be called with the word and confidence level instead
        of returning the result. When combined with a timeout of zero, this allows you to listen
        for words indefinitely and process them as they are recognized.
        threshold is the minimum confidence level required to return a result.
        filter is a list of words that the model should recognize. If the recognized word is
        not in the filter list, the result is ignored.
        """
        pass
        
        
    
"""
The ml module contains functionality for processing machine learning models on the OpenMV Cam.
The heart of the ml module is the Model() object which is used to load and execute
TensorFlow Lite models. The Model() object accepts a list of up to 4D input tensors for
each model input tensor and returns a list of up to 4D output tensors for each model output
tensor. Each input/output tensor works using a numpy ndarray.
For TensorFlow Lite models, the Model() object handles all ops enabled
here. The Model()
object will automatically leverage CMSIS-NN, Helium, and an Ethos NPU if available to speed up
inference. Availability of these accelerators is dependent on the OpenMV Cam model.
For image processing support the ml module automatically converts passed image objects to numpy
ndarray objects by wrapping them with the Normalization() object which handles this conversion. The
Normalization() object can also be manually created to control the conversion process, select an
ROI, and etc.
For more information on ndarray objects see the
ulab documentation. All OpenMV Cams support
ndarray objects up to rank 4 (meaning 4D tensors).
"""

from typing import Tuple
from typing import List
from typing import Optional
from typing import Any
import image

class Model:
    def __init__(self, path: str, load_to_fb: bool = False):
        """
        Loads a model from path into memory and prepares it for being executed. path can either
        be a file on disk or the name of a built-in model which will be loaded from internal flash. Models that are
        built-in to the internal flash firmware image do not take up RAM to store the model weights when used.
        If the model you are trying to load is very large and doesn’t fit in the MicroPython heap you
        can set load_to_fb to True to load the model into the frame buffer stack instead. This allows
        you to get around the heap size limitations. However, models loaded this way need to be deallocated
        in-order with anything else that uses the frame buffer stack versus the MicroPython heap. Typically,
        the frame buffer stack is much larger than the MicroPython heap so you can load much larger models
        using this option, but, you need to be careful if you deallocate.
        Once a model is loaded you can execute it multiple times with different inputs using predict().
        The model will remember its internal state between calls to predict().
        When deleted the model will automatically free up any memory it used from the heap or frame buffer stack.
        """
        pass
        
        
    def predict(self,inputs: list,callback=None) -> list:
        """
        Executes the model with the given inputs. The inputs should be a list of numpy ndarray objects corresponding
        to the number of input tensors the model supports. The method returns a list of numpy ndarray objects
        corresponding to the number of output tensors the model has.
        The model input tensors can be up to 4D tensors of uint8, int8, uint16, int16, or float32 values. The passed
        numpy ndarray for an input tensor is then converted to floating point and scaled/offset based on
        the input tensor’s scale and zero point values before being passed to the model. For example, an ndarray
        of uint8 values will be converted to float32s between 0.0-255.0, divided by the input tensor’s scale, and
        then have the input tensor’s zero point added to it. The same process is done for int8, uint16, and int16 values
        whereas float32 values are passed directly to the model ignoring the scale and zero point values.
        The model’s output tensors can be up to 4D tensors of uint8, int8, uint16, int16, or float32 values. For uint8,
        int8, uint16, and int16 tensors the returned numpy ndarray is created by subtracting the output tensor’s zero
        point value before multiplying by the output tensor’s scale value. For float32 tensors, values are
        passed directly to the output without any scaling or offset being applied.
        Note that predict() requires the shape of the input ndarray objects to match the shape of the model
        input tensors exactly. You can use the reshape() method of an ndarray with the input_shape
        attribute of the model to reshape the input data to the correct shape if necessary.
        If a callback is passed then it will receive the Model, inputs, and outputs as arguments
        which allows for custom post-processing of the model outputs. The callback may then return
        whatever it likes which will be returned by predict(). The callback method allows for building
        up a library of post-processing functions that can be used on demand for different models.
        For custom pre-processing, predict() also accepts “callable” objects as inputs. Any object
        implementing the __call__ method can be passed to predict() as an input. predict() will
        then call the object with a writeable bytearray representing the input tensor, the input tensor’s shape tuple,
        and the input tensors data type value (as an int). The object should then set the input tensor data in the
        bytearray to what the model expects. This is how Normalization() converts image objects to input tensors.
        """
        pass
        
        
    
