import time
import logging
import numpy as np
import tensorflow as tf
import tensorflow_hub as hub

from PIL import Image
from src.object_detection.constants import ConstantClass
from src.object_detection.models import ObjectDetectionModel

LOGGER = logging.getLogger('ObjectDetectionProcessorBeta')

class ObjectDetectionProcessorBeta():
    """Detects objects and their bounding box in the image
    
        Arguments:
            image {[type]} -- OpenCV image
            boxes {type]} -- list of predicted bounding boxes in pixels
            class_names {type]} -- list of predicted classes 
            scores {type]} -- list of confidence score
            max_boxes {Integer} - maximum no of boxes drawn on the image for a particular class
            min_score {Float} - Minimum threshold value for considering our prediction as an object
        
        Returns:
            [type] -- list of objects with their type, confidence_score & bounding box.
    """
    def get_bounding_boxes(image, boxes, class_names, scores, max_boxes=10, min_score=0.1):

        object_details = []

        for i in range(min(boxes.shape[0], max_boxes)):
                cls_lable = class_names[i].decode("utf-8")
                if (cls_lable in ConstantClass.class_labels) and (scores[i] >= min_score):
                    print((class_names[i]).decode("utf-8"))
                    ymin, xmin, ymax, xmax = tuple(boxes[i].tolist())
                    
                    image_pil = Image.fromarray(np.uint8(image)).convert("RGB")
                    im_width, im_height = image_pil.size
                    
                    (left, right, top, bottom) = (xmin * im_width, xmax * im_width,
                                            ymin * im_height, ymax * im_height)
                    
                    attribute_name = ["object_type", "confidence", "co_ordinates"]
                    attribute_value = [cls_lable, str(round(scores[i],2)), [int(left), int(top), int(right), int(bottom)]]
                    object_details.append(dict(zip(attribute_name, attribute_value)))
                    # bounding_boxes.append([cls_lable, int(scores[i]*100), int(left), int(top), int(right), int(bottom)])

        response_msg = ["status", "response"]
        response_list = ["success",  {"objects" : object_details}]
                    
        return dict(zip(response_msg, response_list))



    def detect_objects(image, response_speed):
        """Detects objects and their bounding box in the image
    
        Arguments:
            image {[type]} -- OpenCV image
            response_speed {String} -- model prediction speed (slow / fast)
        
        Returns:
            [type] -- list of objects with their type, confidence_score & bounding box.
        """

        LOGGER.info("Detecting objects in image uploaded")

        if(response_speed == "fast"):
            start_time = time.time()
            result_out, image_out = ObjectDetectionModel().session.run(
                    [ObjectDetectionModel().result_1, ObjectDetectionModel().decoded_image],
                    feed_dict={ObjectDetectionModel().image_string_placeholder: image})
            LOGGER.info("Prediction time is %s seconds" % (time.time() - start_time))
        else:
            start_time = time.time()
            result_out, image_out = ObjectDetectionModel().session.run(
                    [ObjectDetectionModel().result_2, ObjectDetectionModel().decoded_image],
                    feed_dict={ObjectDetectionModel().image_string_placeholder: image})
            LOGGER.info("Prediction time is %s seconds" % (time.time() - start_time))


        image_with_boxes = ObjectDetectionProcessorBeta.get_bounding_boxes(
            np.array(image_out), result_out["detection_boxes"],
            result_out["detection_class_entities"], result_out["detection_scores"])
                
        
        return image_with_boxes
