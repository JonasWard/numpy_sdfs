# functions that remap 2D coordinate to a 3D space
from numpy import cos, sin, pi

def rotate(tpms_grid, angle):
    p=tpms_grid.idx_grid
    c_a, s_a = cos(a), sin(a)
    tpms_grid.idx_grid[0], tpms_grid.idx_grid[1] = (
        p[0] * c_a - p[1] * s_a,
        p[0] * s_a + p[1] * c_a
    )