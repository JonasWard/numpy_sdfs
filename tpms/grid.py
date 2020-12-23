import numpy as np

class TPMSGrid:
    def __init__(self, x_dim, y_dim):
        self.x_dim = int(x_dim)
        self.y_dim = int(y_dim)
        self.grid = np.zeros(shape = (x_dim, y_dim), dtype = np.float )
        self.idx_grid = np.indices( (self.x_dim, self.y_dim), dtype = np.float )

    def __repr__(self):
        return "TPMSGrid with dimensions {} x {}".format(self.x_dim, self.y_dim)

if __name__ == "__main__":
    TPMSGrid(100, 100)