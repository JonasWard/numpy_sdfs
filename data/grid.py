import numpy as np
from data.coordinate_grid import *
from vis.base_vis import vis_image_key_press, array_to_pseudocolor_range

class TPMSGrid:
    def __init__(self, x_dim, y_dim, z_value=0., index_grid=None):
        self.x_dim = int(x_dim)
        self.y_dim = int(y_dim)
        self.grid = np.zeros(shape = (x_dim, y_dim), dtype = np.float16 )

        if index_grid is None:
            self._idx_grid_state = "default"
            # by default the index grid is loaded in centrelized
            self.idx_grid = CoordinateGrid(self.x_dim, self.y_dim, z_value)
        else:
            self._idx_grid_state = "cloned"
            self.idx_grid = index_grid

        self._applied = False

    @property
    def applied(self):
        return self._applied

    def shift_to_corner(self, corner="top_right"):
        if corner == "top_left":
            x_mul, y_mul = -1., -1.
        elif corner == "top_right":
            x_mul, y_mul = 1., -1.
        elif corner == "bottom_right":
            x_mul, y_mul = 1., 1.
        elif corner == "bottom_left":
            x_mul, y_mul = -1., 1.
        else:
            x_mul, y_mul = 0., 0.

        self.idx_grid.translate(pt=(self.x_dim*(.5*x_mul), self.x_dim*(.5*y_mul), 0.))

    def transform_idx_grid(self, rotation = .25 * np.pi, translation = None ):
        translation = (0,0,0) if translation is None else translation

        if isinstance(rotation, float) or isinstance(rotation, int):
            self.idx_grid.rotate_xy(b_pt=translation, angle=rotation)
        elif isinstance(rotation, tuple):
            self.idx_grid.rotate_angles(b_pt=translation, angles=rotation)

    def uv_map_coordinates(self, uv_function):
        self.idx_grid.uv_map(uv_function)

    def apply_function(self, function):
        self._applied = True
        function.apply_grid(self)
        return self

    def get_domain(self):
        return np.min(self.grid), np.max(self.grid), np.mean(self.grid), np.median(self.grid)

    def binary_slice_at(self, value):
        n_grid = self.clone()
        n_grid.grid = np.less_equal(self.grid, value).astype(np.uint8) * 255.
        return n_grid

    def clone(self):
        return TPMSGrid(self.x_dim, self.y_dim, index_grid=self.idx_grid)

    def get_values(self):
        if self._applied:
            return self.idx_grid.x, self.idx_grid.y, self.idx_grid.z
        else:
            return self.grid, self.grid, self.grid

    def visualize(self):
        vis_image_key_press(array_to_pseudocolor_range(self.grid))

    def __repr__(self):
        mn, mx, mean, med = self.get_domain()
        return '\n'.join(["TPMSGrid with dimensions {} x {}".format(self.x_dim, self.y_dim),
        " min_val: {}, max_val: {}, mean_val: {}, median_val: {}".format(mn, mx, mean, med)])

if __name__ == "__main__":
    TPMSGrid(100, 100)