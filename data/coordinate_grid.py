import numpy as np

class CoordinateGrid():
    def __init__(self, x_dim, y_dim, z_value=0.):
        self.x_dim = x_dim
        self.y_dim = y_dim

        self.x, self.y = [np_a for np_a in np.indices( (self.x_dim, self.y_dim), dtype = np.float )]
        self.z = [np.ones((self.x_dim, self.y_dim), dtype=np.float)*z_value]

        #centralize
        self.x-=self.x_dim * .5
        self.y-=self.x_dim * .5

    def rotate_xy(self, b_pt=(0,0,0), angle=1.):
        self.x-=b_pt[0]
        self.y-=b_pt[1]

        c = np.cos(angle)
        s = np.sin(angle)

        self.x, self.y = ( self.x * c - self.y * s ), ( self.x * s + self.y * c )
        
        self.x+=b_pt[0]
        self.y+=b_pt[1]

    def translate(self, pt=(0,0,0)):
        self.x+=pt[0]
        self.y+=pt[1]
        self.z+=pt[2]

    def uv_map(self, uv_map_function):
        self.x, self.y, self.z = uv_map_function.map(self.x, self.y, self.z)