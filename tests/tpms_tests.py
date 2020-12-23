from tpms.grid import TPMSGrid
from vis.grid import vis_grid, vis_grid_idx, vis_grid_pseudocolors, video_output_grid_pseudocoloring
from tpms.functions import Gyroid, SchwarzP, SchwarzD

grid = TPMSGrid(1000, 1000)
# vis_grid(grid)
# print(grid.grid)

grid3 = TPMSGrid(1000, 1000)
gyroid3 = SchwarzP(50.0, 2.0, 25.0)
gyroid3.apply(grid3, .5)

grid2 = TPMSGrid(1000, 1000)
gyroid2 = SchwarzD(grid3.grid, 15.0, 80.0)
gyroid2.apply(grid2, .2)

gyroid = SchwarzD(grid2.grid, 1.0, 1.0)
gyroid.apply(grid, .5)
# vis_grid(grid)
# vis_grid_pseudocolors(grid)
video_output_grid_pseudocoloring(grid, gyroid, z_vals = [z * 5 for z in range(200)])
# print(grid.grid)