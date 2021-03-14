from data.grid import TPMSGrid
from functions.tpms import *
from vis.base_vis import vis_image_key_press, array_to_pseudocolor_range

grid = TPMSGrid(500, 500)
grid_a = grid.clone()
grid_b = grid.clone()
grid_b.apply_function(Gyroid(.02, max_val=5.))
grid_b.visualize()

grid.apply_function(Gyroid(grid_b, max_val=5.))
grid.visualize()

grid.binary_slice_at(0.).visualize()