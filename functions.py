from itertools import combinations
from itertools import cycle
import numpy as np
import pandas as pd

def matrixDet(matrix):
    array = matrix
    licycle = cycle(array)
    nextelem = next(licycle)
    dict = {'detMatrix': [], 'matrix': []}
    for i in matrix:
            thiselem, nextelem = nextelem, next(licycle)
            det = np.linalg.det(thiselem)
            print('matriz = {} determinante = {}'.format(thiselem,det))
            detMtrix = np.linalg.det(thiselem)
            dict['detMatrix'].append(detMtrix)
            dict['matrix'].append(thiselem)
            print(detMtrix)
            i += 1
    np.array(dict)
    df = pd.DataFrame(dict)
    df.to_csv('detMatrix.csv')

def matrixmult(matrix):
    array = matrix
    combinacao = list(combinations(array, 2))
    licycle = cycle(combinacao)
    nextelem = next(licycle)
    for i in matrix:
        thiselem, nextelem = nextelem, next(licycle)
        if thiselem[0].shape[1] == thiselem[1].shape[0]:
            multMtrix = thiselem[0].dot(thiselem[1])
            dict['multMatrix'].append(multMtrix)
            print(multMtrix)
    np.array(dict)
    df = pd.DataFrame(dict)
    df.to_csv('multMatrix.csv')

def matrixSum(matrix):
    array = matrix
    combinacao = list(combinations(array, 2))
    licycle = cycle(combinacao)
    nextelem = next(licycle)
    dict = {'sumMatrix': []}
    for i in matrix:
        thiselem, nextelem = nextelem, next(licycle)
        if thiselem[0].shape == thiselem[1].shape:
            sumMatrix = thiselem[0] + thiselem[1]
            dict['sumMatrix'].append(sumMatrix)
            print(sumMatrix)
    np.array(dict)
    df = pd.DataFrame(dict)
    df.to_csv('sumMatrix.csv')
            
def matrixSub(matrix):
    array = matrix
    combinacao = list(combinations(array, 2))
    licycle = cycle(combinacao)
    nextelem = next(licycle)
    dict = {'subMatrix': []}
    for i in matrix:
        thiselem, nextelem = nextelem, next(licycle)
        if thiselem[0].shape == nextelem[1]:
            subMatrix = thiselem[0] + thiselem[1]
            dict['subMatrix'].append(subMatrix)
            print(subMatrix)
    np.array(dict)
    df = pd.DataFrame(dict)
    df.to_csv('subMatrix.csv')

def matrixInv(matrix):
    array = matrix
    licycle = cycle(array)
    nextelem = next(licycle)
    dict = {'inversedMtrix': []}
    for i in matrix:
        thiselem, nextelem = nextelem, next(licycle)
        det = np.linalg.det(thiselem)
        if det != 0:
            inversedMatrix = np.linalg.inv(i)
            dict['inversedMtrix'].append(inversedMatrix)
            print(inversedMatrix)
    np.array(dict)
    df = pd.DataFrame(dict)
    df.to_csv('inversedMatrix.csv')
