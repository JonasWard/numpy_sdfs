import numpy as np

class Gyroid:
    def __init__(self, scale_a, max_val, shift = 0.0):
        self.s_a = scale_a
        self.m_v = max_val
        self.s = shift

    def apply(self, tpms_grid, z = 0.0):
        _x = tpms_grid.idx_grid[0] / self.s_a
        _y = tpms_grid.idx_grid[1] / self.s_a

        s_x = np.sin(_x)
        s_y = np.sin(_y)
        s_z = np.sin(z)
        
        c_x = np.cos(_x)
        c_y = np.cos(_y)
        c_z = np.cos(z)

        tpms_grid.grid += s_x * c_y + s_y * c_z + s_z * c_x
        tpms_grid.grid *= self.m_v
        tpms_grid.grid += self.s