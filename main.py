import functions
import numpy as np
import pandas as pd
import random


if __name__ == '__main__':

    matrizes = []
    n = int(input('Digite o número de matrizes a serem geradas: '))
    for i in range(0,n):
        dimensao  = random.randint(2, 5)
        a = np.random.randint(5, size=(dimensao, dimensao))
        matrizes.append(a)
    running = True

    while running:
        controles = int(input('Digite 1 para soma \n Digite 2 para subtração \n Digite 3 para multiplicar \n Digite 4 para obter o determinante \n Digite 5 para obter as inversas \n Digite 6 para sair \n Opção: '))
        if controles == 6:
            running = False

        if controles == 1:
            functions.matrixSum(matrizes)
        if controles == 2:
            functions.matrixSum(matrizes)
        if controles == 3:
            functions.matrixSum(matrizes)
        if controles == 4:
            functions.matrixSum(matrizes)
        if controles == 5:
            functions.matrixInv(matrizes)
