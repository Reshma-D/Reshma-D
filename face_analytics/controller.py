import cherrypy
import logging
import os
import cv2
import numpy as np
import imutils
import tensorflow as tf

from src.utils import image_utils
from keras.models import load_model, model_from_json
from resources.handlers.zos.zosmanager import ZosManager as zm
from src.face_analytics.face_landmark.face_landmark_processor import FaceLandmarkDetector
from src.face_analytics.face_detector.ssd_face_detector import FaceDetector
LOGGER = logging.getLogger('FaceAnalyticsController')

class FaceAnalyticsController():

    @cherrypy.expose()
    @cherrypy.tools.json_out() 
    @cherrypy.tools.response_headers(headers=[
        ('Access-Control-Allow-Origin', '*'),
        ('Access-Control-Allow-Methods','GET,POST,PUT,DELETE,OPTIONS')])
         
    def initialize_detection(self, image, landmark_mode):

        try:
            LOGGER.info("Initiating Face Detecttion")

            image_file = image_utils.fileparam_to_cv(image)
            copy_image = image_file

            face_detector = FaceDetector.ssd_face_detection(copy_image)
            face_landmark = FaceLandmarkDetector.detect_landmarks(image_file, landmark_mode.lower(), face_detector)

            return face_landmark  
   
        except Exception as exception:
            LOGGER.info(exception)
            cherrypy.response.status = 500
            return {
                "status": "failure"
            }


    @cherrypy.expose()
    @cherrypy.tools.json_out()
    @cherrypy.tools.response_headers(headers=[
        ('Access-Control-Allow-Origin', '*'),
        ('Access-Control-Allow-Methods','GET,POST,PUT,DELETE,OPTIONS')])

    def describe_feature(self):

        return {
            "input": {
                "image": "an image of max size 5 MB"
            },
            "prediction": "predicts the presence of face, facial landmarks and facial contour in an image",
            "supported_landmark_detection": ['0', '5', '68'],
            "face_boundary": "[x, y, width, height]",
            "5_points_landmarks_detected": {
                "right_eye_right_tip": "[x, y]",
                "right_eye_left_tip": "[x, y]",
                "left_eye_left_tip": "[x, y]",
                "left_eye_right_tip": "[x, y]",
                "nose_tip": "[x, y]"
            },
            "68_points_landmarks_detected": {
                "face_margin": "[x1, y1] ... [x17, y17]",
                "left_eyebrow": "[x18, y18] ... [x22, y22]",
                "right_eyebrow": "[x23, y23] ... [x27, y27]",
                "nose_bridge": "[x28, y28] ... [x31, y31]",
                "nostril_line": "[x32, y32] ... [x36, y36]",
                "left_eye": "[x37, y37] ... [x42, y42]",
                "right_eye": "[x43, y43] ... [x48, y48]",
                "upper_lips_upper_edge": "[x49, y49] ... [x55, y55]",
                "lower_lips_upper_edge": "[x56, y56] ... [x60, y60]",
                "upper_lips_lower_edge": "[x61, y61] ... [x65, y65]",
                "lower_lips_lower_edge": "[x66, y66] ... [x68, y68]"
            },
            "accepted_image_type": ".jpg, .jpeg and .png"
        }



        # string = "Reshma"
        # bytes1 = bytes(string, 'utf-8')
        # put_response = zm.put_object("common-bucket", "f1", string, is_pickle_needed=False)
        # get_response = zm.get_object("common-bucket","f1", is_pickle_needed=False)
        # print(put_response)
        # print(get_response)
        # return get_response

        # path = "/Users/reshma-8192/Desktop/yolov3.h5"
        # key = "yolov3_model"
        # model= load_model(path)
        # weights = model.get_weights()   
        # json= model.to_json()
        # architecture_response = zm.put_object("common-bucket",key, json, True)
        # weights_response = zm.put_object("common-bucket",key+"_weights",weights, True)
        # print(architecture_response)
        # print(weights_response)

        # # For updating our model in IDC
        # self.detection_graph = tf.Graph()
        # with self.detection_graph.as_default():
        #     od_graph_def = tf.GraphDef()
        #     with tf.gfile.GFile("/Users/reshma-8192/Desktop/frozen_inference_graph_face.pb", 'rb') as fid:
        #         serialized_graph = fid.read()
        #         od_graph_def.ParseFromString(serialized_graph)
        #         put_response = zm.put_object("common-bucket", "face_detector_ssd", od_graph_def, is_pickle_needed=True)
        #         # get_response = zm.get_object("common-bucket","ssd_face_detector", is_pickle_needed=True)
            
