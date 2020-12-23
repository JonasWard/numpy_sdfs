from tpms.grid import TPMSGrid
from vis.grid import vis_grid, vis_grid_idx, vis_grid_pseudocolors, video_output_grid_pseudocoloring
from tpms.functions import Gyroid, SchwarzP, SchwarzD
import math

x_dim, y_dim = 1080, 1920

grid = TPMSGrid(x_dim, y_dim)
grid.transform_idx_grid()
# vis_grid(grid)
# print(grid.grid)

grid3 = TPMSGrid(x_dim, y_dim)
grid3.transform_idx_grid()
gyroid3 = Gyroid(50.0, 4.0, 50.0)
gyroid3.apply(grid3, .5)

grid2 = TPMSGrid(x_dim, y_dim)
# grid2.transform_idx_grid()
gyroid2 = Gyroid(grid3.grid, 15.0, 80.0)
gyroid2.apply(grid2, .2)

gyroid = Gyroid(grid2.grid, 1.0, 1.0)
gyroid.apply(grid, .5)
# vis_grid(grid)
vis_grid_pseudocolors(grid)
z_vals = [math.sin(z / 435.0) * 10000 for z in range(100)]

# print(z_vals)
video_output_grid_pseudocoloring(grid, gyroid, z_vals)
# print(grid.grid)

# ToDo: json saving configuration of different tpmses, grid and pseudocolor map 