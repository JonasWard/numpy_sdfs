# take a tpms grid
# set every value that is larger than 0 to 1, all other to to 0
import numpy as np

def binary_grid(tpms_grid, value = 0.0):
    n_grid = tpms_grid.clone()
    n_grid.grid = np.less_equal(tpms_grid.grid, value).astype(np.uint8) * 255.
    return n_grid

if __name__ == "__main__":
    from data.grid import TPMSGrid
    from vis.grid import *
    from functions.tpms import *
    import math

    # x_dim, y_dim = 1280, 720
    x_dim, y_dim = 1000, 1000

    translation = .5, .5
    rotation = 0.

    grid = TPMSGrid(x_dim, y_dim)
    grid.transform_idx_grid(rotation, translation)
    # vis_grid(grid)
    # print(grid.grid)

    grid3 = TPMSGrid(x_dim, y_dim)
    grid3.transform_idx_grid(rotation, translation)
    gyroid3 = FischerKoch(50.0, 4.0, 50.0)
    gyroid3.apply_grid(grid3, .5)

    n_grid = binary_grid(grid3, 50.0)

    vis_grid_pseudocolors(n_grid)
    vis_grid_pseudocolors(grid3)
    