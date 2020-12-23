import numpy as np
import cv2 as cv
from vis.base_vis import vis_image_key_press, pseudocoloring, grid_to_pseudcolors

def vis_grid(tpms_grid):
    vis_image_key_press(tpms_grid.grid, "tpms_grid")

def vis_grid_pseudocolors(tpms_grid):
    vis_image_key_press(grid_to_pseudcolors(tpms_grid), "tpms_grid")

def vis_grid_idx(tpms_grid):
    vis_array = np.zeros( (tpms_grid.x_dim, tpms_grid.y_dim), dtype = np.float)
    vis_array += tpms_grid.idx_grid[0]
    vis_array += tpms_grid.idx_grid[1]
    vis_array /= float(tpms_grid.x_dim + tpms_grid.y_dim)
    vis_array *= 255.0

    vis_image_key_press( pseudocoloring(vis_array), "idx_grid")

def video_output_grid_pseudocoloring(tpms_grid, tpms_f, z_vals = [.1, .2, .3, .4, .5], name = "try_out.mp4"):
    out = cv.VideoWriter(name, cv.VideoWriter_fourcc(*'MP4V'), 10, (tpms_grid.y_dim, tpms_grid.x_dim) )
    for z in z_vals:
        loc_grid = tpms_grid.clone()
        tpms_f.apply(loc_grid, z)
        frame = grid_to_pseudcolors(loc_grid)
        # vis_image_key_press(frame)
        out.write(frame)
    out.release()