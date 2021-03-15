import numpy as np
from data.grid import TPMSGrid

class TPMS:
    def __init__(self, scale_a, max_val, shift = 0.0):
        self.s_a = scale_a
        self.m_v = max_val
        self.s = shift

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

    def get_values(self, tpms_grid):
        _x, _y, _z = tpms_grid.get_values()

        if isinstance(self.s_a, TPMSGrid):
            s_d = self.s_a.grid

            _x*=s_d
            _y*=s_d
            _z*=s_d

        else:
            _x*=self.s_a
            _y*=self.s_a
            _z*=self.s_a        

        return _x, _y, _z

    def assign_value(self, tpms_grid, ds):
        tpms_grid.grid = ds * self.m_v


class Gyroid(TPMS):        
    def apply_grid(self, tpms_grid):
        print("applying gyroid grid")
        _x, _y, _z = self.get_values(tpms_grid)

        s_x, s_y, s_z = self.get_sin(_x, _y, _z)
        c_x, c_y, c_z = self.get_cos(_x, _y, _z)

        ds = (
            s_x * c_y + 
            s_y * c_z + 
            s_z * c_x
        )
        
        self.assign_value(tpms_grid, ds)

class SchwarzD(TPMS):
    def apply_grid(self, tpms_grid):
        _x, _y, _z = self.get_values(tpms_grid)

        s_x, s_y, s_z = self.get_sin(_x, _y, _z)
        c_x, c_y, c_z = self.get_cos(_x, _y, _z)

        ds = (  
            s_x * s_y * c_z + 
            s_x * c_y * c_z + 
            c_x * s_y * c_z + 
            c_x * c_y * s_z
        )
        
        self.assign_value(tpms_grid, ds)

class SchwarzP(TPMS):
    def apply_grid(self, tpms_grid):
        _x, _y, _z = self.get_values(tpms_grid)
        
        c_x, c_y, c_z = self.get_cos(_x, _y, _z)

        ds = c_x + c_y + c_z
        
        self.assign_value(tpms_grid, ds)

class Neovius(TPMS):
    def apply_grid(self, tpms_grid):
        _x, _y, _z = self.get_values(tpms_grid)

        c_x, c_y, c_z = self.get_cos(_x, _y, _z)

        ds = (
            3.0 * c_x + c_y + c_z +
            4.0 * c_x * c_y * c_z
        )
        
        self.assign_value(tpms_grid, ds)

class FischerKoch(TPMS):
    def apply_grid(self, tpms_grid):
        _x, _y, _z = self.get_values(tpms_grid)

        c_2x, c_2y, c_2z = self.get_cos(2.0 * _x, 2.0 * _y, 2.0 * _z)
        s_x, s_y, s_z = self.get_sin(_x, _y, _z)
        c_x, c_y, c_z = self.get_cos(_x, _y, _z)

        ds = (
            c_2x * s_y * c_z +
            c_2y * s_z * c_x +
            c_2y * s_x * c_y
        )
        
        self.assign_value(tpms_grid, ds)