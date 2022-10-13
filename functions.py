import numpy as np

def determinant(matrix):
    array = np.array(matrix)
    print(np.linalg.det(array))