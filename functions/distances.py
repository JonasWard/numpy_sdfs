import numpy as np

class Line:
    def __init__(self, pt0, pt1, scale_a, max_val, shift = 0.0):
        self.x_0, self.y_0, self.z_0 = pt0
        self.x_1, self.y_1, self.z_1 = pt1

        self.s_a = scale_a
        self.m_v = max_val
        self.s = shift

    def apply_grid(self, tpms_grid, z = 0.0):
        _x = tpms_grid.idx_grid[0] / self.s_a
        _y = tpms_grid.idx_grid[1] / self.s_a
        _z = z / self.s_a
        
        x, y, z = self.x_1 - self.x_0, self.y_1 - self.y_0, self.z_1 - self.z_0
        d_01 = np.sqrt( x ** 2 + y ** 2 + z ** 2 )
        d_x, d_y, d_z = x / d_01, y / d_01, z / d_01

        v_x, v_y, v_z = _x - self.x_0, _y - self.y_0, _z - self.z_0

        t = d_x * v_x + d_y * v_y + d_z * v_z
        p_x, p_y, p_z = self.x_0 + t * d_x, self.y_0 + t * d_y, self.z_0 + t * d_z
        _x, _y, _z = p_x - x, p_y - y, p_z - z
        d = np.sqrt( _x ** 2 + _y ** 2 + _z ** 2 )

        d *= self.s_a
        d -= self.s
        d [ d > self.m_v ] = self.m_v
        tpms_grid.grid += d

class Sphere:
    def __init__(self, c_pt, r, scale_a, strength = .1, max_val = 200.0):
        self.x, self.y, self.z = c_pt

        self.s_a = scale_a
        self.m_v = max_val
        self.s = r
        self.mag = strength

    def apply_grid(self, tpms_grid, z = 0.0):
        _x = tpms_grid.idx_grid[0] / self.s_a
        _y = tpms_grid.idx_grid[1] / self.s_a
        _z = z / self.s_a

        _x -= self.x
        _y -= self.y
        _z -= self.z

        d = np.sqrt( _x ** 2 + _y ** 2 + _z ** 2 )
        d *= self.s_a
        d -= self.s
        d [ d > self.m_v ] = self.m_v
        d *= self.mag
        tpms_grid.grid += d