import numpy as np
#Questão 4: Calcule a média dos valores no array arr1.

def arr(x,y):
    arr1 = np.arange(x,y)
    return arr1

arr1 = arr(1,50001)

def media(arr):
    soma = sum(arr)
    qntElementos = len(arr)
    return soma / qntElementos

print(media(arr1))
