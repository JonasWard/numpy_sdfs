import numpy as np
from vis.base_vis import vis_image_key_press, pseudocoloring

def vis_grid(tpms_grid):
    vis_image_key_press(tpms_grid.grid, "tpms_grid")

def vis_grid_pseudocolors(tpms_grid):
    max_val = np.max(tpms_grid.grid)
    min_val = np.min(tpms_grid.grid)
    delta = max_val - min_val

    print("max : {}, min : {}, delta : {}".format(max_val, min_val, delta) )

    vis_grid = tpms_grid.grid - min_val
    vis_grid *= 255.0 / delta

    vis_grid = vis_grid.astype(np.uint8)
    
    vis_image_key_press(pseudocoloring(vis_grid), "tpms_grid")

def vis_grid_idx(tpms_grid):
    vis_array = np.zeros( (tpms_grid.x_dim, tpms_grid.y_dim), dtype = np.float)
    vis_array += tpms_grid.idx_grid[0]
    vis_array += tpms_grid.idx_grid[1]
    vis_array /= float(tpms_grid.x_dim + tpms_grid.y_dim)
    vis_array *= 255.0

    vis_image_key_press( pseudocoloring(vis_array), "idx_grid")
