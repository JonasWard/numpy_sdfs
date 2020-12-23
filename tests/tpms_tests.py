from tpms.grid import TPMSGrid
from vis.grid import vis_grid, vis_grid_idx, vis_grid_pseudocolors
from tpms.functions import Gyroid

grid = TPMSGrid(1000, 1000)
# vis_grid(grid)
# print(grid.grid)

grid3 = TPMSGrid(1000, 1000)
gyroid3 = Gyroid(50.0, 2.0, 25.0)
gyroid3.apply(grid3, .5)

grid2 = TPMSGrid(1000, 1000)
gyroid2 = Gyroid(grid3.grid, 1.0, 8.0)
gyroid2.apply(grid2, .2)

gyroid = Gyroid(grid2.grid, 1.0)
gyroid.apply(grid, .9)
# vis_grid(grid)
vis_grid_pseudocolors(grid)
# print(grid.grid)