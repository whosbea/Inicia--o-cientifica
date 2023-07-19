import numpy as np

#Questão 1: Crie um array NumPy chamado arr1 de 1D com os números de 1 a 50000.
def arr(x,y):
    arr1 = np.arange(x,y)
    return arr1

print(arr(1,50001))
