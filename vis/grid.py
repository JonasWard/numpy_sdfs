import numpy as np
from vis.base_vis import vis_image_key_press

def vis_grid(tpms_grid):
    vis_image_key_press(tpms_grid.grid, "tpms_grid")

def vis_idx_grid(tpms_grid):
    vis_array = np.zeros( (tpms_grid.x_dim, tpms_grid.y_dim), dtype = np.float)
    vis_array += tpms_grid.idx_grid[0]
    vis_array += tpms_grid.idx_grid[1]
    vis_array /= float(tpms_grid.x_dim + tpms_grid.y_dim)

    vis_image_key_press(vis_array, "idx_grid")
