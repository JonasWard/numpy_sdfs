import numpy as np
from vis.base_vis import vis_image_key_press, array_to_pseudocolor_range

class CoordinateGrid():
    def __init__(self, x_dim, y_dim, z_value=0.):
        self.x_dim = x_dim
        self.y_dim = y_dim

        self.x, self.y = [np_a for np_a in np.indices( (self.x_dim, self.y_dim), dtype = np.float64 )]
        self.z = [np.ones((self.x_dim, self.y_dim), dtype=np.float64)*z_value]

        #centralize
        self.x-=self.x_dim * .5
        self.y-=self.x_dim * .5

    def rotate_xy(self, b_pt=(0,0,0), angle=1.):
        self.x-=b_pt[0]
        self.y-=b_pt[1]

        c,s = np.cos(angle), np.sin(angle)

        self.x, self.y = ( self.x * c - self.y * s ), ( self.x * s + self.y * c )
        
        self.x+=b_pt[0]
        self.y+=b_pt[1]

    def translate(self, pt=(0,0,0)):
        self.x+=pt[0]
        self.y+=pt[1]
        self.z+=pt[2]

    def uv_map(self, uv_map_function):
        self.x, self.y, self.z = uv_map_function.map(self.x, self.y, self.z)

    def visualizeX(self):
        vis_image_key_press(array_to_pseudocolor_range(self.x))

    def visualizeY(self):
        vis_image_key_press(array_to_pseudocolor_range(self.y))

    def visualizeZ(self):
        vis_image_key_press(array_to_pseudocolor_range(self.z))

    def visualizeXY(self):
        pass

    def visualizeXZ(self):
        pass

    def visualizeYZ(self):
        pass

    def visualizeXYZ(self):
        pass

if __name__ == "__main__":
    c_grid = CoordinateGrid(150, 150)