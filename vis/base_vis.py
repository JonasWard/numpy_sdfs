import numpy as np
import cv2 as cv

def vis_image_key_press(ndarray, name = 'key_press_vis'):
    cv.imshow(name, ndarray)
    cv.waitKey(0)
    cv.destroyAllWindows()