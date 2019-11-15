import numpy as np
import imutils
import dlib
import cv2
import logging
import time
import face_recognition
import face_recognition_models

from mtcnn.mtcnn import MTCNN
from imutils import face_utils
from src.face_analytics.face_landmark.face_landmark_detector import *
from src.face_analytics.models import FaceAnalyticsModels


LOGGER = logging.getLogger('FaceLandmarkDetector')

class FaceLandmarkDetector():

    def detect_landmarks(image, landmark_mode, face_boundary):
        """Locates the facial landmarks on the faces detected by ssd face detector 
    
        Arguments:
            image {[type]} -- OpenCV image
            landmark_mode {integer} -- face landmark mode (0/ 5/ 68)
            face_boundary -- face boundaries detected by ssd face detector
 
        Returns:
            [type] -- list of face boundaries and their facial landmarks
        """
        face_details_list = []
        for faces in face_boundary:
            face_details_list.append(dict(zip(["face_boundary"], [[int(faces[0]), int(faces[1]), int(faces[2]), int(faces[3])]])))
            
        LOGGER.info("Detecting landmark on the detected faces")
        if(landmark_mode != "0"):
            face_details_list = get_face_landmarks(landmark_mode, image, face_details_list)

        response_list = ["success", {"face" : face_details_list}]
        response_msg = ["status", "response"]
        return dict(zip(response_msg, response_list))



    