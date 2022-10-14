import numpy as np
import pandas as pd
import random
from itertools import cycle

def determinant(matrix):
    array = np.array(matrix)
    shape = array.shape
    if (shape[0] != shape[1]):
        print('Você deve enviar um array quadrado')
        return
    else:
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