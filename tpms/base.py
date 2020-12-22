import numpy as np

class TPMSGrid:
    def __init__(self, x_dim, y_dim):
        self.x_dim = int(x_dim)
        self.y_dim = int(y_dim)
        self.grid = np.ndarray(shape = (x_dim, y_dim), dtype = np.float )