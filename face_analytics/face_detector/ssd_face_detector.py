import sys
import time
import numpy as np
import tensorflow as tf
import cv2
import cherrypy

from src.face_analytics.face_detector.utils import label_map_util
from src.face_analytics.face_detector.utils import visualization_utils_color as vis_util
from src.face_analytics.face_detector.models import FaceDetectorModel

label_map = label_map_util.load_labelmap(FaceDetectorModel().PATH_TO_LABELS)
categories = label_map_util.convert_label_map_to_categories(label_map, max_num_classes=FaceDetectorModel().NUM_CLASSES, use_display_name=True)
category_index = label_map_util.create_category_index(categories)

class FaceDetector():

    @cherrypy.expose()
    @cherrypy.tools.json_out() 
    @cherrypy.tools.response_headers(headers=[
        ('Access-Control-Allow-Origin', '*'),
        ('Access-Control-Allow-Methods','GET,POST,PUT,DELETE,OPTIONS')])

    def ssd_face_detection(image):
        """Detects the presence of face and its co-ordinates in the image
    
        Arguments:
            image {[type]} -- OpenCV image
        
        Returns:
            [type] -- list of face boundaries
        """
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        image_np_expanded = np.expand_dims(image, axis=0)

        (boxes, scores, classes) = FaceDetectorModel().sess.run(
            [FaceDetectorModel().boxes, FaceDetectorModel().scores, FaceDetectorModel().classes],feed_dict={FaceDetectorModel().image_tensor: image_np_expanded})

        face_list = vis_util.visualize_boxes_and_labels_on_image_array(
                image,
                np.squeeze(boxes),
                np.squeeze(classes).astype(np.int32),
                np.squeeze(scores),
                category_index,
                use_normalized_coordinates=True,
                line_thickness=4)

        return face_list
