import numpy as np

class TPMS:
    def __init__(self, scale_a, max_val, shift = 0.0):
        self.s_a = scale_a
        self.m_v = max_val
        self.s = shift

    def get_idx_grid(self, tpms_grid, z):
        _x = tpms_grid.idx_grid[0] / self.s_a
        _y = tpms_grid.idx_grid[1] / self.s_a
        _z = z / self.s_a

        return _x, _y, _z

    def get_sin(self, *args):
        output = []
        for arg in args:
            output.append(np.sin(arg) )
        return output

    def get_cos(self, *args):
        output = []
        for arg in args:
            output.append(np.cos(arg))
        return output

    def save_to_grid(self, grid, ds):
        ds *= self.m_v
        ds += self.s
        grid.grid += ds

class Gyroid(TPMS):        
    def apply_grid(self, tpms_grid, z = 0.0):
        _x, _y, _z = self.get_idx_grid(tpms_grid, z)

        s_x, s_y, s_z = self.get_sin(_x, _y, _z)
        c_x, c_y, c_z = self.get_cos(_x, _y, _z)

        ds = (
            s_x * c_y + 
            s_y * c_z + 
            s_z * c_x
        )
        self.save_to_grid(tpms_grid, ds)

class SchwarzD(TPMS):
    def apply_grid(self, tpms_grid, z = 0.0):
        _x, _y, _z = self.get_idx_grid(tpms_grid, z)

        s_x, s_y, s_z = self.get_sin(_x, _y, _z)
        c_x, c_y, c_z = self.get_cos(_x, _y, _z)

        ds = (  
            s_x * s_y * c_z + 
            s_x * c_y * c_z + 
            c_x * s_y * c_z + 
            c_x * c_y * s_z
        )
        self.save_to_grid(tpms_grid, ds)

class SchwarzP(TPMS):
    def apply_grid(self, tpms_grid, z = 0.0):
        _x, _y, _z = self.get_idx_grid(tpms_grid, z)
        
        c_x, c_y, c_z = self.get_cos(_x, _y, _z)

        ds = c_x + c_y + c_z
        self.save_to_grid(tpms_grid, ds)

class Neovius(TPMS):
    def apply_grid(self, tpms_grid, z = 0.0):
        _x, _y, _z = self.get_idx_grid(tpms_grid, z)

        c_x, c_y, c_z = self.get_cos(_x, _y, _z)

        ds = (
            3.0 * c_x + c_y + c_z +
            4.0 * c_x * c_y * c_z
        )
        self.save_to_grid(tpms_grid, ds)

class FischerKoch(TPMS):
    def apply_grid(self, tpms_grid, z = 0.0):
        _x, _y, _z = self.get_idx_grid(tpms_grid, z)

        c_2x, c_2y, c_2z = self.get_cos(2.0 * _x, 2.0 * _y, 2.0 * _z)
        s_x, s_y, s_z = self.get_sin(_x, _y, _z)
        c_x, c_y, c_z = self.get_cos(_x, _y, _z)

        ds = (
            c_2x * s_y * c_z +
            c_2y * s_z * c_x +
            c_2y * s_x * c_y
        )
        self.save_to_grid(tpms_grid, ds)