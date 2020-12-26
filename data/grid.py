import numpy as np

class TPMSGrid:
    def __init__(self, x_dim, y_dim, index_grid = None):
        self.x_dim = int(x_dim)
        self.y_dim = int(y_dim)
        self.grid = np.zeros(shape = (x_dim, y_dim), dtype = np.float )

        if index_grid is None:
            self._idx_grid_state = "default"
            self.idx_grid = np.indices( (self.x_dim, self.y_dim), dtype = np.float )
        else:
            self._idx_grid_state = "cloned"
            self.idx_grid = index_grid

    def transform_idx_grid(self, rotation = .25 * np.pi, translation = (.5, 0.0) ):
        c = np.cos(rotation)
        s = np.sin(rotation)

        x = translation[0] * self.x_dim
        y = translation[1] * self.y_dim

        print("translation : {}, {}".format(x, y) )
        print("rotation    : {}, {}".format(c, s) )

        idx_grid_dup = []
        idx_grid_dup.append( self.idx_grid[0] * c - self.idx_grid[1] * s )
        idx_grid_dup.append( self.idx_grid[0] * s + self.idx_grid[1] * c )

        self.idx_grid = idx_grid_dup

        self.idx_grid[0] -= x
        self.idx_grid[1] -= y

        self._idx_grid_state = "transformed"

        print("grid updated")

    def clone(self):
        return TPMSGrid(self.x_dim, self.y_dim, self.idx_grid)

    def __repr__(self):
        return "TPMSGrid with dimensions {} x {}".format(self.x_dim, self.y_dim)

if __name__ == "__main__":
    TPMSGrid(100, 100)