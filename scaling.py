def scale_x(Sx):
    trans_matrix = [[Sx, 0, 0],[0, 1, 0],[0, 0, 1]]
    return trans_matrix

def scale_y(Sy):
    trans_matrix = [[1, 0, 0], [0, Sy, 0], [0, 0, 1]]
    return trans_matrix

def scale_xy(Sx, Sy):
    trans_matrix = [[Sx, 0, 0],[0, Sy, 0],[0, 0, 1]]
    return trans_matrix

