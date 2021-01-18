import numpy as np

edge_mapper = {
    0: [],
    1: [(2, 3)],
    2: [(1, 2)],
    3: [(1, 3)],
    4: [(0, 3)],
    5: [(0, 2)],
    6: [(0, 3), (1, 2)],
    7: [(0, 1)],
    8: [(0, 1)],
    9: [(0, 1), (2, 3)],
    10:[(0, 2)],
    11:[(0, 3)],
    12:[(1, 3)],
    13:[(1, 2)],
    14:[(2, 3)],
    15:[]
}

vertex_mapper = {
    0: [0, 1],
    1: [1, 2],
    2: [3, 2],
    3: [0, 3]
}

def interpolate_edge(v_a, v_b):
    return v_a / (v_a - v_b)

def calculate_vertexes(cell_values, cell_type, b_pt):
    all_pairs = []
    for e_s in edge_mapper[cell_type]:
        n_pair = []

        for e_idx in e_s:
            v_idx_a = vertex_mapper[e_idx][0]
            v_idx_b = vertex_mapper[e_idx][1]

            v = interpolate_edge(
                cell_values[v_idx_a],
                cell_values[v_idx_b]
            )

            if e_idx % 2 == 0:
                n_pair.append([
                    b_pt[0],
                    b_pt[1] + v
                ])

            else:
                n_pair.append([
                    b_pt[0] + v,
                    b_pt[1]
                ])

        all_pairs.append(n_pair)

    return all_pairs

def line_list_slice(tpmg_grid, cut_off_value = 0.):
    cell_counts = np.zeros( (tpmg_grid.x_dim - 1, tpmg_grid.y_dim - 1), dtype = np.int8)

    cell_values = tpmg_grid.grid - cut_off_value

    values = np.less_equal(cell_values, 0.0).astype(np.uint8)

    top_right = section(values, (0,0) )
    top_left = section(values, (1,0) )
    bot_right = section(values, (0,1) )
    bot_left = section(values, (1,1) )

    cell_counts += top_right * 1
    cell_counts += top_left * 2
    cell_counts += bot_right * 4
    cell_counts += bot_left * 8

    top_right = section(cell_values, (0,0) )
    top_left = section(cell_values, (1,0) )
    bot_right = section(cell_values, (0,1) )
    bot_left = section(cell_values, (1,1) )

    edge_list = []

    for i in range(cell_counts.shape[0]):
        for j in range(cell_counts.shape[1]):
            if not(cell_counts[i][j] % 15 == 0):
                edge_list.extend(calculate_vertexes(
                    cell_values = [
                        cell_values[i][j],
                        cell_values[i+1][j],
                        cell_values[i+1][j+1],
                        cell_values[i][j+1],
                    ],
                    cell_type = cell_counts[i][j],
                    b_pt = [i, j]
                ))

    return edge_list

def section(array, idx_tuple = (0,0) ):
    a_0, a_1 = idx_tuple[0], array.shape[0] + idx_tuple[0] - 1
    b_0, b_1 = idx_tuple[1], array.shape[1] + idx_tuple[1] - 1
    return array[a_0 : a_1, b_0: b_1]

if __name__ == "__main__":
    from data.grid import TPMSGrid
    from vis.grid import *
    from functions.tpms import *
    import math

    # x_dim, y_dim = 1280, 720
    x_dim, y_dim = 1000, 1000

    translation = .5, .5
    rotation = 0.

    grid = TPMSGrid(x_dim, y_dim)
    grid.transform_idx_grid(rotation, translation)
    # vis_grid(grid)
    # print(grid.grid)

    grid3 = TPMSGrid(x_dim, y_dim)
    grid3.transform_idx_grid(rotation, translation)
    gyroid3 = FischerKoch(50.0, 4.0, 50.0)
    gyroid3.apply_grid(grid3, .5)

    # n_grid = binary_grid(grid3, 50.0)

    print(line_list_slice(grid3, 50.) )
    