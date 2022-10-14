import functions
import numpy as np
import pandas as pd
import random

matrizes = []
n = int(input('Digite o número de matrizes a serem geradas: '))
for i in range(0,n):
    dimensao  = random.randint(2, 5)
    a = np.random.randint(5, size=(dimensao, dimensao))
    matrizes.append(a)

if __name__ == '__main__':
    functions.determinant([[1, 3, 7, 1], [4.5, 10, -10, 5], [32, 9, -1, -4], [0, 3, -8, 2]])