import numpy as np
import cv2 as cv
import math
import vis.colormap as cm

color_map = cm.color_d["OCEAN"]

def grid_to_pseudcolors(tpms_grid):
    max_val = np.max(tpms_grid.grid)
    min_val = np.min(tpms_grid.grid)
    delta = max_val - min_val

    print("max : {}, min : {}, delta : {}".format(max_val, min_val, delta) )

    # fix delta = 0.0
    if delta == 0.0:
        multiplier = 1.0
        print("[DEBUG] - value range is 0")
    else:
        multiplier = 255.0 / delta

    vis_grid = tpms_grid.grid - min_val
    vis_grid *= multiplier

    vis_grid = vis_grid.astype(np.uint8)

    max_val = np.max(vis_grid)
    min_val = np.min(vis_grid)
    delta = max_val - min_val

    print("REGRADED - max : {}, min : {}, delta : {}".format(max_val, min_val, delta) )

    return pseudocoloring(vis_grid)

def grid_to_pseudcolors_rounded(tpms_grid, values = 6):
    return array_to_pseudcolors_rounded(tpms_grid.grid, values)

def array_to_pseudcolors_rounded(array, values = 6):
    max_val = np.max(array)
    min_val = np.min(array)
    delta = max_val - min_val

    print("max : {}, min : {}, delta : {}".format(max_val, min_val, delta) )

    # fix delta = 0.0
    if delta == 0.0:
        multiplier = 1.0
        print("[DEBUG] - value range is 0")
    else:
        multiplier = values / (delta)

    print(array)

    vis_grid = array - min_val
    vis_grid *= multiplier

    vis_grid = vis_grid.astype(np.uint8)

    vis_grid *= math.floor(255.0 / values)

    max_val = np.max(vis_grid)
    min_val = np.min(vis_grid)
    delta = max_val - min_val

    print("REGRADED - max : {}, min : {}, delta : {}".format(max_val, min_val, delta) )
    
    return pseudocoloring(vis_grid)

def pseudocoloring(img):
    global color_map
    img = cv.applyColorMap(img, color_map)
    return img

def vis_image_key_press(ndarray, name = 'key_press_vis'):
    cv.imshow(name, ndarray)
    cv.waitKey(0)
    cv.destroyAllWindows()