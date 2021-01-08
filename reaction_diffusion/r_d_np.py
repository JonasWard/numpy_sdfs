import numpy as np
from vis.base_vis import array_to_pseudcolors_rounded, pseudocoloring, vis_image_key_press

class RDF:
    def __init__(self, d_u = 1.0, d_v = .5, f = .055, k = .62):
        self.d_u = d_u
        self.d_v = d_v
        self.f = f
        self.k = k
    
    def apply(self, u_grid, v_grid):
        n_u, n_v = -4*u_grid, -4*v_grid
        
        for i in range(2):
            for j in range(2):
                n_u += section(u_grid, (i, j))
                n_v += section(v_grid, (i, j))

        uv_2 = u_grid * v_grid * v_grid

        ouput_v_grid = self.d_u * n_u * n_u - uv_2 + self.f * (1. - u_grid)
        ouput_u_grid = self.d_v * n_v * n_v + uv_2 - (self.f + self.k) * v_grid

        return ouput_u_grid, ouput_v_grid

def section(array, idx_tuple = (0,0) ):
    base = array.copy()
    a_0, a_1 = idx_tuple[0], array.shape[0] + idx_tuple[0] - 1
    b_0, b_1 = idx_tuple[1], array.shape[1] + idx_tuple[1] - 1
    sec = array[a_0 : a_1, b_0: b_1]
    base[a_0 : a_1, b_0: b_1] = sec

    return base

xy_dim = 50
itertions = 100

u_grid, v_grid = np.random.rand( xy_dim, xy_dim ), np.random.rand( xy_dim, xy_dim )
u_grid *= .1
v_grid *= .1

print(u_grid)
rd = RDF()
for i in range(itertions):
    u_grid, v_grid = rd.apply(u_grid, v_grid)
    print(u_grid)

vis_image_key_press( pseudocoloring( array_to_pseudcolors_rounded(u_grid) ) )