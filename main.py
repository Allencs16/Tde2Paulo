import functions
import csv
import numpy as np
import random
import pandas as pd

if __name__ == '__main__':



    matrizes = []
    n = int(input('Digite o número de matrizes a serem geradas: '))
    for i in range(0,n):
        dimensao1  = random.randint(2, 5)
        dimensao2  = random.randint(2, 5)
        a = np.random.randint(99, size=(dimensao1, dimensao2))
        matrizes.append(a)
    dict = {'matrix': matrizes}
    df = pd.DataFrame(dict)
    df.to_csv('matrix.csv')
    print(df)
    running = True

    while running:
        controles = int(input('1 para soma \n 2 para subtração \n 3 para multiplicar \n 4 para obter o determinante \n 5 para obter as inversas \n 6 para sair \n Opção: '))
        if controles == 6:
            running = False

        if controles == 1:
            functions.matrixSum(matrizes)
        if controles == 2:
            functions.matrixSub(matrizes)
        if controles == 3:
            functions.matrixmult(matrizes)
        if controles == 4:
            functions.matrixDet(matrizes)
        if controles == 5:
            functions.matrixInv(matrizes)
