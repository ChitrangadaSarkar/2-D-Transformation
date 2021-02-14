def translate_x(tx):
    trans_matrix = [[1, 0, tx],[0, 1, 0],[0, 0, 1]]
    return trans_matrix


def translate_y(ty):
    trans_matrix = [[1, 0, 0], [0, 1, ty], [0, 0, 1]]
    return trans_matrix

def translate_xy(tx, ty):
    trans_matrix = [[1, 0, tx],[0, 1, ty],[0, 0, 1]]
    return trans_matrix