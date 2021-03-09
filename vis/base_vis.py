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

def array_prop(array):
    max_val = np.max(array)
    min_val = np.min(array)
    delta = max_val - min_val

    return max_val, min_val, delta

def array_to_unit_interval(array):
    max_val, min_val, delta = array_prop(array)

    if delta != 0.:
        vis_grid = array - min_val
        vis_grid /= delta
    else:
        print("when converting to interval gradient grid, found no delta!, just a gray one!")
        vis_grid=np.ones(array.shape, dtype=np.float64)*.5

    return vis_grid

def array_to_stepped_unit_interval(array, steps=8):
    max_val, min_val, delta = array_prop(array)

    steps *= 1.

    if delta != 0.:
        vis_grid = array - min_val
        vis_grid /= delta
        vis_grid *= steps
        vis_grid = vis_grid.astype(np.uint8).astype(np.float64)
        vis_grid /=steps
    else:
        print("when converting to interval gradient grid, found no delta!, just a gray one!")
        vis_grid=np.ones(array.shape, dtype=np.float64)*.5

    return vis_grid

def array_to_pseudocolor_range(array):
    array = array_to_unit_interval(array)
    array *= 255.
    array=array.astype(np.uint8)

    return pseudocoloring(array)

def array_to_stepped_pseudecolor_range(array, values = 6):
    array = array_to_stepped_unit_interval(array, values)
    array *= 255.
    # print(np.uint8)
    array=array.astype(np.uint8)
    
    return pseudocoloring(array)

def pseudocoloring(img):
    global color_map
    img = cv.applyColorMap(img, color_map)
    return img

def display_swapping(ndarray):
    ndarray=cv.transpose(ndarray)
    ndarray=cv.flip(ndarray, flipCode=1)

    return ndarray

def vis_image_key_press(ndarray, name = 'key_press_vis'):
    ndarray=display_swapping(ndarray)

    cv.imshow(name, ndarray)
    cv.waitKey(0)
    cv.destroyAllWindows()

if __name__ == "__main__":
    xs, ys = [np_a for np_a in np.indices( (100,100), dtype = np.float64 )]

    print(xs)
    print(ys)
    xs_array=array_to_pseudocolor_range(xs)
    print(xs_array)

    vis_image_key_press(xs_array)
    vis_image_key_press(array_to_pseudocolor_range(ys))