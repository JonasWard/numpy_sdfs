from data.grid import TPMSGrid
from vis.grid import vis_grid, vis_grid_idx, vis_grid_pseudocolors, video_output_grid_pseudocoloring
from functions.tpms import Gyroid, SchwarzP, SchwarzD
from functions.distances import Line, Sphere
import math

x_dim, y_dim = 1280, 720

translation = .0, .0
rotation = 0.

grid = TPMSGrid(x_dim, y_dim)
grid.transform_idx_grid(rotation, translation)
# vis_grid(grid)
# print(grid.grid)

grid3 = TPMSGrid(x_dim, y_dim)
grid3.transform_idx_grid(rotation, translation)
gyroid3 = Gyroid(50.0, 4.0, 50.0)
gyroid3.apply(grid3, .5)

grid2 = TPMSGrid(x_dim, y_dim)
grid2.transform_idx_grid(rotation, translation)
gyroid2 = Gyroid(grid3.grid, 10.0, 40.0)
gyroid2.apply(grid2, .2)

# ln = Line( (0,0,0), (-100, 100.0, 10.0), 5., max_val=200.0)
sp = Sphere( (200,200,0), 200, 1.0, .01, 200)
# sp.apply(grid2, 0.0)
# vis_grid(grid)
vis_grid_pseudocolors(grid2)
z_vals = [math.sin(z / 435.0) * 2000 for z in range(100)]

# # print(z_vals)
video_output_grid_pseudocoloring(grid2, gyroid2, z_vals)
# print(grid.grid)

# ToDo: json saving configuration of different tpmses, grid and pseudocolor map 