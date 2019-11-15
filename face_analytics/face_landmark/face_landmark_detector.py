import dlib
import time
import cv2
import numpy
import logging
import face_recognition
import face_recognition_models

from imutils import face_utils
from src.face_analytics.models import FaceAnalyticsModels

LOGGER = logging.getLogger('FaceLandmarkDetector')

def get_face_landmarks(category, image, face_details_list):
    """Locates the facial landmark based on categories
    
        Arguments:
            category {integer} -- face landmark mode (0/ 5/ 68)
            image {[type]} -- OpenCV image
            face_details_list -- face boundaries detected by ssd face detector
        
        Returns:
            [type] -- list of facial landmarks
        """
    face_landmark_list = []
    for faces  in face_details_list:
        shape = FaceAnalyticsModels().LANDMARK_68_POINTS(image, dlib.rectangle(faces["face_boundary"][0], faces["face_boundary"][1], faces["face_boundary"][2], faces["face_boundary"][3]))
        shape = face_utils.shape_to_np(shape)

        if(category == "68"):
            LOGGER.info("Landmark mode is 68, returns face boundary and 68 facial landmarks")
            face_landmarks_attribute_name = ["face_margin", "left_eyebrow", "right_eyebrow", "nose_bridge", "nostril_line", "left_eye", "right_eye", "upper_lips_upper_edge", "lower_lips_upper_edge", "upper_lips_lower_edge", "lower_lips_lower_edge"]
            face_landmarks_attribute_value = [(shape[0:17]).tolist(), shape[17:22].tolist(), shape[22:27].tolist(), shape[27:31].tolist(), shape[31:36].tolist(), shape[36:42].tolist(), shape[42:48].tolist(), shape[48:55].tolist(), shape[55:60].tolist(), shape[60:65].tolist(), shape[65:68].tolist()]
        elif(category == "5"):
            LOGGER.info("Landmark mode is 5, returns face boundary and 5 facial landmarks")
            face_landmarks_attribute_name = ["right_eye_right_tip", "right_eye_left_tip", "left_eye_left_tip", "left_eye_right_tip", "nose_tip"]
            face_landmarks_attribute_value = [shape[45].tolist(), shape[42].tolist(), shape[36].tolist(), shape[39].tolist(), shape[33].tolist()]

        face_details_attribute_name = ["face_boundary", "face_landmarks"]
        face_details_attribute_value = [faces['face_boundary'], dict(zip(face_landmarks_attribute_name, face_landmarks_attribute_value))]
        face_landmark_list.append(dict(zip(face_details_attribute_name, face_details_attribute_value)))
    return face_landmark_list




