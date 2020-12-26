from data.grid import TPMSGrid
from vis.grid import vis_grid, vis_grid_idx, vis_grid_pseudocolors, video_output_grid_pseudocoloring
from functions.tpms import *
import math

# x_dim, y_dim = 1280, 720
x_dim, y_dim = 1080, 1920

translation = .5, .5
rotation = 0.

grid = TPMSGrid(x_dim, y_dim)
grid.transform_idx_grid(rotation, translation)
# vis_grid(grid)
# print(grid.grid)

# grid3 = TPMSGrid(x_dim, y_dim)
# grid3.transform_idx_grid(rotation, translation)
# gyroid3 = FischerKoch(50.0, 4.0, 50.0)
# gyroid3.apply_grid(grid3, .5)

grid2 = TPMSGrid(x_dim, y_dim)
grid2.transform_idx_grid(rotation, translation)
gyroid2 = Neovius(grid.grid, 10.0, 40.0)
gyroid2.apply_grid(grid2, .2)

gyroid = Gyroid(grid2.grid, 1.0, 1.0)
gyroid.apply_grid(grid, .5)
# vis_grid(grid)
vis_grid_pseudocolors(grid)
z_vals = [math.sin(z / 435.0) * 12000 for z in range(50)]

# print(z_vals)
video_output_grid_pseudocoloring(grid, gyroid, z_vals, "neovius.mp4")
# print(grid.grid)

# ToDo: json saving configuration of different tpmses, grid and pseudocolor map 