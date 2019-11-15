import pathlib
import tensorflow as tf
import tensorflow_hub as hub
from src.utils import load_model_from_zos as zm
from src.utils.singleton import Singleton
from imageai.Detection import ObjectDetection

class ObjectDetectionModel(metaclass=Singleton):
    

    """ Model for Object Detection """

    # def __init__(self):
    #     MODEL_PATH = "saved/models/object/"
    #     pathlib.Path(MODEL_PATH).mkdir(parents=True, exist_ok=True)
    #     OD_MODEL = zm.retrieve_from_zos("crmdi-image-models","yolov3_model")
    #     OD_MODEL.save(MODEL_PATH + "/OD_yolov3_model.h5")
    #     self.detector = ObjectDetection()
    #     self.detector.setModelTypeAsYOLOv3()
    #     self.detector.setModelPath(MODEL_PATH + "/OD_yolov3_model.h5")
    #     self.detector.loadModel()



    """ Model for Object Detection Beta"""

    def __init__(self):
        self.detection_graph = tf.Graph()
        with self.detection_graph.as_default():
            self.detector_1 = hub.Module("https://tfhub.dev/google/openimages_v4/ssd/mobilenet_v2/1")
            self.detector_2 = hub.Module("https://tfhub.dev/google/faster_rcnn/openimages_v4/inception_resnet_v2/1")

            self.image_string_placeholder = tf.placeholder(tf.string)
            self.decoded_image = tf.image.decode_jpeg(self.image_string_placeholder)

            self.decoded_image_float = tf.image.convert_image_dtype(image=self.decoded_image, dtype=tf.float32)
            module_input = tf.expand_dims(self.decoded_image_float, 0)
            

            self.result_1 = self.detector_1(module_input, as_dict=True)
            self.result_2 = self.detector_2(module_input, as_dict=True)

            init_ops = [tf.global_variables_initializer(), tf.tables_initializer()]

            self.session = tf.Session()
            self.session.run(init_ops)





        


        
    
