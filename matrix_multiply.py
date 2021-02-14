import numpy as np
def matrix_mul(matrix1,matrix2):
	new_matrix = [[0,0,0],[0,0,0],[0,0,0]]
	for i in range(len(matrix1)):
	    for j in range(len(matrix2[0])):
	        for k in range(len(matrix2)):
	            new_matrix[i][j] += matrix1[i][k]*matrix2[k][j]
	return np.around(new_matrix,decimals=1)