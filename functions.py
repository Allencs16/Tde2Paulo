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
def matrixmult(matrix):
    array = matrix
    licycle = cycle(array)
    nextelem = next(licycle)
    for i in matrix:
        thiselem, nextelem = nextelem, next(licycle)
        print(thiselem)
        if thiselem.shape[1] == nextelem.shape[0]:
            thiselem.dot(nextelem)
            print(thiselem.dot(nextelem))
        else:
            print('Impossivel multiplicar')

def matrixSum(matrix):
    array = matrix
    licycle = cycle(array)
    nextelem = next(licycle)
    for i in matrix:
        thiselem, nextelem = nextelem, next(licycle)
        if thiselem.shape[0] == nextelem.shape[0]:
            thiselem + nextelem
            print(thiselem + nextelem)
        else:
            i += 1
            print('Impossivel multiplicar')
            
def matrixSub(matrix):
    array = matrix
    licycle = cycle(array)
    nextelem = next(licycle)
    for i in matrix:
        thiselem, nextelem = nextelem, next(licycle)
        if thiselem.shape[0] == nextelem.shape[0]:
            thiselem + nextelem
            print(thiselem - nextelem)
        else:
            i += 1
            print('Impossivel multiplicar')
            