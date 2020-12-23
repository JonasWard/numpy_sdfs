import numpy as np
import cv2 as cv

def grid_to_pseudcolors(tpms_grid):
    max_val = np.max(tpms_grid.grid)
    min_val = np.min(tpms_grid.grid)
    delta = max_val - min_val

    print("max : {}, min : {}, delta : {}".format(max_val, min_val, delta) )

    vis_grid = tpms_grid.grid - min_val
    vis_grid *= 255.0 / delta

    vis_grid = vis_grid.astype(np.uint8)

    return pseudocoloring(vis_grid)

def pseudocoloring(img):
    img = cv.applyColorMap(img, cv.COLORMAP_JET)
    return img

def vis_image_key_press(ndarray, name = 'key_press_vis'):
    cv.imshow(name, ndarray)
    cv.waitKey(0)
    cv.destroyAllWindows()