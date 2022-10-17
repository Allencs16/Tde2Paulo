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
    licycle = cycle(array)
    nextelem = next(licycle)
    dict = {'multMatrix': []}
    for i in matrix:
        thiselem, nextelem = nextelem, next(licycle)
        print(thiselem)
        if thiselem.shape[1] == nextelem.shape[0]:
            multMtrix = thiselem.dot(nextelem)
            dict['multMatrix'].append(multMtrix)
            print(multMtrix)
    np.array(dict)
    df = pd.DataFrame(dict)
    df.to_csv('multMatrix.csv')

def matrixSum(matrix):
    array = matrix
    licycle = cycle(array)
    nextelem = next(licycle)
    dict = {'sumMatrix': []}
    for i in matrix:
        thiselem, nextelem = nextelem, next(licycle)
        if thiselem.shape[0] == nextelem.shape[0]:
            sumMatrix = thiselem + nextelem
            dict['sumMatrix'].append(sumMatrix)
            print(sumMatrix)
    np.array(dict)
    df = pd.DataFrame(dict)
    df.to_csv('sumMatrix.csv')
            
def matrixSub(matrix):
    array = matrix
    licycle = cycle(array)
    nextelem = next(licycle)
    dict = {'subMatrix': []}
    for i in matrix:
        thiselem, nextelem = nextelem, next(licycle)
        if thiselem.shape[0] == nextelem.shape[0]:
            subMatrix = thiselem - nextelem
            dict['subMatrix'].append(subMatrix)
            print(subMatrix)
    np.array(dict)
    df = pd.DataFrame(dict)
    df.to_csv('subMatrix.csv')

def matrixInv(matrix):
    dict = {'inversedMtrix': []}
    for i in matrix:
        inversedMatrix = np.linalg.inv(i)
        dict['inversedMtrix'].append(inversedMatrix)
        print(inversedMatrix)
    np.array(dict)
    df = pd.DataFrame(dict)
    df.to_csv('inversedMatrix.csv')
