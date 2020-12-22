import numpy as np
import cv2 as cv

def vis_grid(tpms_grid):
    cv.imshow('tpms_grid',tpms_grid.grid)
    cv.waitKey(0)
    cv.destroyAllWindows()
