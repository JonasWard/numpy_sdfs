import numpy as np
import cv2 as cv

def pseudocoloring(img):
    img = cv.applyColorMap(img, cv.COLORMAP_JET)
    return img

def vis_image_key_press(ndarray, name = 'key_press_vis'):
    cv.imshow(name, ndarray)
    cv.waitKey(0)
    cv.destroyAllWindows()