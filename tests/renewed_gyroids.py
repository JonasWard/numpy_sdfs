from data.grid import TPMSGrid
from functions.tpms import *

grid = TPMSGrid(500, 500)
grid_a = grid.clone()
grid_b = grid.clone()
grid_b.apply_function(Gyroid(5., max_val=5.))
grid_b.visualize()

grid.apply_function(Gyroid(grid_b, max_val=5.))
grid.visualize()