import numpy as np

def determinant(matrix):
    array = np.array(matrix)
    shape = array.shape
    if(shape[0] != shape[1]):
        print('Você deve enviar um array quadrado')
        return
    else:
        print(np.linalg.det(array))

def somaMatrix(matrix1):
    array1 = np.array(matrix1)
    print(array1[0])
    print(array1[1])
    print(array1[0] + array1[1])

