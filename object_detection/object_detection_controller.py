import cherrypy
import logging
import tensorflow as tf
from src.object_detection.object_detection_processor import ObjectDetectionProcessor
from src.object_detection.object_detection_processor_beta import ObjectDetectionProcessorBeta
from src.utils import image_utils
LOGGER = logging.getLogger('ObjectDetectionController')

class ObjectDetectionController():

    # def __init__(self):
    #     self.graph = tf.get_default_graph()


    @cherrypy.expose()
    @cherrypy.tools.json_out()
    @cherrypy.tools.response_headers(headers=[
        ('Access-Control-Allow-Origin', '*'),
        ('Access-Control-Allow-Methods','GET,POST,PUT,DELETE,OPTIONS')])
        
    def initialize_detection(self, image, response_speed):

        try:
            LOGGER.info("Initiating Object Detecttion")
            # Passing the image file for image verification
            # return ObjectDetectionProcessor.detect_objects(image_utils.fileparam_to_cv(image), self.graph)
            return ObjectDetectionProcessorBeta.detect_objects(image.file.read(), response_speed.lower())
  
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
            "prediction": "detects the presence of 80 common objects and its location in an image",
            "objects_detected" : "[person, bicycle, car, motorcycle, airplane, bus, train, truck, boat, traffic light, fire hydrant, stop_sign, parking meter, bench,   bird,   cat,   dog,   horse,   sheep,   cow,   elephant,   bear,   zebra, giraffe,   backpack,   umbrella,   handbag,   tie,   suitcase,   frisbee,   skis,   snowboard, sports ball,   kite,   baseball bat,   baseball glove,   skateboard,   surfboard,   tennis racket, bottle,   wine glass,   cup,   fork,   knife,   spoon,   bowl,   banana,   apple,   sandwich,   orange, broccoli,   carrot,   hot dog,   pizza,   donot,   cake,   chair,   couch,   potted plant,   bed, dining table,   toilet,   tv,   laptop,   mouse,   remote,   keyboard,   cell phone,   microwave, oven,   toaster,   sink,   refrigerator,   book,   clock,   vase,   scissors,   teddy bear,   hair dryer, toothbrush]",
            "confidence_score": "the probability value for individual objects detected in an image",
            "co_ordinates": "(x1, y1, x2, y2) [top_left_corner and bottom_right_corner]",
            "accepted_image_type": ".jpg, .jpeg and .png"
        }

           