import numpy as np

def determinant(matrix):
    array = np.array(matrix)
    print(np.linalg.det(array))

def matrixSum(matrix):
    array = matrix
    while i <= len(array):
        if i + 1 != None: 
            if array[i].shape[0] == array[i+1].shape[0]:
                print(array[i]+array[i+1])
def matrixSubt(matrix):
    array = matrix
    while i <= len(array):
        if i + 1 != None: 
            if array[i].shape[0] == array[i+1].shape[0]:
                print(array[i] - array[i+1])
def matrixmult(matrix):
    array = matrix
    while i <= len(array):
        if i + 1 != None: 
            if array[i].shape[1] == array[i+1].shape[0]:
                array[i].dot(array[i+1])
                print(array[i].dot(array[i+1]))
            else:
                print('Impossivel multiplicar')