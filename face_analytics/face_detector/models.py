import tensorflow as tf
from src.utils.singleton import Singleton
from src.utils import load_model_from_zos as zm
from resources.handlers.zos.zosmanager import ZosManager as zm

class FaceDetectorModel(metaclass=Singleton):

    def __init__(self):

        # List of the strings that is used to add correct label for each box.
        self.PATH_TO_LABELS = 'src/face_analytics/face_detector/protos/face_label_map.pbtxt'
        self.NUM_CLASSES = 2

        self.detection_graph = tf.Graph()
        with self.detection_graph.as_default():
            get_response = zm.get_object("crmdi-image-models","face_detector_ssd", is_pickle_needed=True)
            tf.import_graph_def(get_response, name='')
            config = tf.ConfigProto()
            self.sess = tf.Session(config=config, graph=self.detection_graph)


        self.image_tensor = self.detection_graph.get_tensor_by_name('image_tensor:0')
        # Each box represents a part of the image where a particular object was detected.
        self.boxes = self.detection_graph.get_tensor_by_name('detection_boxes:0')
        # Each score represent how level of confidence for each of the objects.
        # Score SSDFaceLandmarkModel() shown on the result image, together with the class label.
        self.scores = self.detection_graph.get_tensor_by_name('detection_scores:0')
        self.classes = self.detection_graph.get_tensor_by_name('detection_classes:0')
        

