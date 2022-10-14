import csv
import random
from itertools import cycle
import numpy as np

with open('countries.csv', 'w', encoding='UTF8') as f:
    writer = csv.writer(f)


def matrixDet(matrix):
    array = matrix
    licycle = cycle(array)
    nextelem = next(licycle)
    for i in matrix:
            thiselem, nextelem = nextelem, next(licycle)
            det  = np.linalg.det(thiselem)    
            writer.writerow(det)
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
            writer.writerow(thiselem.dot(nextelem))
def matrixSum(matrix):
    array = matrix
    licycle = cycle(array)
    nextelem = next(licycle)
    for i in matrix:
        thiselem, nextelem = nextelem, next(licycle)
        if thiselem.shape[0] == nextelem.shape[0]:
            writer.writerow(thiselem + nextelem)
            
def matrixSub(matrix):
    array = matrix
    licycle = cycle(array)
    nextelem = next(licycle)
    for i in matrix:
        thiselem, nextelem = nextelem, next(licycle)
        if thiselem.shape[0] == nextelem.shape[0]:
            writer.writerow(thiselem - nextelem)

def matrixInv(matrix):
    for i in matrix:
        if matrixDet(i) != 0:
            writer.writerow(np.linalg.inv(i))
