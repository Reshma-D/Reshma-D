import dlib
import face_recognition
import face_recognition_models

from mtcnn.mtcnn import MTCNN
from src.utils.singleton import Singleton

class FaceAnalyticsModels(metaclass=Singleton):

    def __init__(self):
        self.MTCNN_MODEL = MTCNN()

        predictor_68_point_model = face_recognition_models.pose_predictor_model_location()
        self.LANDMARK_68_POINTS = dlib.shape_predictor(predictor_68_point_model)


        

        


        
    
