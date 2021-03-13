import numpy as np
from vis.base_vis import vis_image_key_press, array_to_pseudocolor_range, merge_channels

class CoordinateGrid():
    def __init__(self, x_dim, y_dim, z_value=0.):
        self.x_dim = x_dim
        self.y_dim = y_dim

        self.x, self.y = [np_a for np_a in np.indices( (self.x_dim, self.y_dim), dtype = np.float64 )]
        self.z = np.ones((self.x_dim, self.y_dim), dtype=np.float64)*z_value

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

    def rotate_angles(self, b_pt=(0,0,0), angles=(.5,0.,1.5)):
        pitch, yaw, roll = angles
        d_x, d_y, d_z = b_pt

        c1, s1 = np.cos(pitch), np.sin(pitch)
        c2, s2 = np.cos(yaw), np.sin(yaw)
        c3, s3 = np.cos(roll), np.sin(roll)

        self.x -= d_x
        self.y -= d_y
        self.z -= d_z

        # Tait-Bryan angles XYZ
        a, b, c = c2 * c3, - c2 * s3, s2
        d, e, f = c1*s3 + c3*s1*s2, c1*c3 - s1*s2*s3, - c2*s1
        g, h, i = s1*s3 - c1*c3*s2, c3*s1 + c1*s2*s3, c1*c2
        
        self.x, self.y, self.z = (
            self.x * a + self.y * b + self.y * c,
            self.x * d + self.y * e + self.y * f,
            self.x * g + self.y * h + self.y * i
        )

        self.x += d_x
        self.y += d_y
        self.z += d_z

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
        vis_image_key_press(merge_channels(self.x, self.y))

    def visualizeXZ(self):
        vis_image_key_press(merge_channels(self.x, None, self.z))

    def visualizeYZ(self):
        vis_image_key_press(merge_channels(None, self.y, self.z))

    def visualizeXYZ(self):
        vis_image_key_press(merge_channels(self.x, self.y, self.z))

if __name__ == "__main__":
    c_grid = CoordinateGrid(150, 150)
    c_grid.visualizeX()
    c_grid.rotate_xy(angle=np.pi*.5)
    c_grid.visualizeX()
    # c_grid.visualizeXZ()
    # c_grid.visualizeYZ()
    # c_grid.visualizeXYZ()
