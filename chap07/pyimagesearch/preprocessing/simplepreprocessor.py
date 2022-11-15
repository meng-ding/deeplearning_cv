from configparser import Interpolation
import cv2

class SimplePreprocessor:
    def __init__(self, width, height, inter=cv2.INTER_AREA):
        # store the target image width, height, interpolation
        self.width = width
        self.height = height
        self.inter = inter

    def preprocess(self, image):
        # resize the image to a fixed size, ignoring the aspect 
        # ratio
        return cv.resize(image, (self.width, self.height), interpolation = self.inter)
        
