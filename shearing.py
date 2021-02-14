def shear_x(shx):
    trans_matrix = [[1, shx, 0],[0, 1, 0],[0, 0, 1]]
    return trans_matrix

def shear_y(shy):
    trans_matrix = [[1, 0, 0], [shy, 1, 0], [0, 0, 1]]
    return trans_matrix

def shear_xy(shx, shy):
    trans_matrix = [[1, shx, 0],[shy, 1, 0],[0, 0, 1]]
    return trans_matrix