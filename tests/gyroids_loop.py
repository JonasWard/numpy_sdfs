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
gyroid3 = Gyroid(50.0, 12.0, 35.0)

gyroid3.apply_grid(grid3, .5)

grid2 = TPMSGrid(x_dim, y_dim)
grid2.transform_idx_grid(rotation, translation)
gyroid2 = Gyroid(grid3.grid, 10.0, 30.0)
gyroid2.apply_grid(grid2, .2)

gyroid = Gyroid(grid3.grid, 1.0, 1.0)
gyroid.apply_grid(grid, 0)
# vis_grid(grid)
vis_grid_pseudocolors(grid)
# vis_grid_pseudocolors_rounded(grid, 9)
# z_vals = [(math.cos(z * math.pi / 100.0) + 1) * 500 for z in range(200)]

# print(z_vals)
# video_output_grid_pseudocoloring(grid, gyroid, z_vals, "gyroid_3_integers.mp4")
# print(grid.grid)

# ToDo: json saving configuration of different tpmses, grid and pseudocolor map 