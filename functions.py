import numpy as np
import pandas as pd
import random
from itertools import cycle

def matrixDet(matrix):
    array = matrix
    licycle = cycle(array)
    nextelem = next(licycle)
    for i in matrix:
            thiselem, nextelem = nextelem, next(licycle)
            det  = np.linalg.det(thiselem)    
            i += 1
            print('matriz = {} determinante = {}'.format(thiselem,det))
            
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
            print('Impossivel Somar')
            
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
            print('Impossivel Subtrair')
            