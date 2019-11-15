import logging
import numpy as np
import cv2
import time
import os
import pathlib
import tensorflow as tf
from imageai.Detection import ObjectDetection
from src.utils import load_model_from_zos as zm
from keras.models import load_model, model_from_json
from resources.handlers.zos.zosmanager import ZosManager as zm
from src.object_detection.models import ObjectDetectionModel

models = ObjectDetectionModel()

LOGGER = logging.getLogger('ObjectDetectionProcessor')

class ObjectDetectionProcessor():

    def detect_objects(image, graph):
        """Detects objects and their bounding box in the image
    
        Arguments:
            image {[type]} -- OpenCV image
        
        Returns:
            [type] -- list of objects with their type, confidence_score & bounding box.
        """
        LOGGER.info("Detecting objects in image uploaded")
        start_time = time.time()

        with graph.as_default():
            detections = models.detector.detectObjectsFromImage(input_type = "array", input_image = image, output_type="array", minimum_percentage_probability=30)

        LOGGER.info("Object Detector took {0} ms".format(str((time.time() - start_time) * 1000)))
        response_msg = ["status", "response"]

        LOGGER.info("Objects detected in image")
        object_details = []
        for objects in detections[1]:
            attribute_name = ["object_type", "confidence", "co_ordinates"]
            attribute_value = [str(objects['name']), str(round(objects['percentage_probability'],2)), [int(objects["box_points"][0]), int(objects["box_points"][1]), int(objects["box_points"][2]), int(objects["box_points"][3])]]
            object_details.append(dict(zip(attribute_name, attribute_value)))

        response_msg = ["status", "response"]
        response_list = ["success",  {"objects" : object_details}]
        
        return dict(zip(response_msg, response_list))



