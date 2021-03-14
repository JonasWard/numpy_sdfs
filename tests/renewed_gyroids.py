from data.grid import TPMSGrid
from functions.tpms import *
from functions.uv_mapping import *
from vis.base_vis import vis_image_key_press, array_to_pseudocolor_range

grid = TPMSGrid(1000, 1000)
grid.uv_map_coordinates(UVSpiderMapping(
        r_base = 1., 
        m_cyl = 20., 
        n_cyl = 200., 
        direction='x', 
        m_remap = 6, 
        n_remap = 8
    ))
# grid_a = grid.clone()
grid_b = grid.clone()
grid.idx_grid.visualizeXYZ()

grid.apply_function(
    Gyroid(grid_b.apply_function(
            Gyroid(.2, max_val=5.)
        ), max_val=1.))
grid.visualize()

# print(grid)
grid.binary_slice_at(grid.get_domain()[3]).visualize()