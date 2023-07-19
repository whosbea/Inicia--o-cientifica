import numpy as np
#Questão 3: Qual é o valor máximo no array arr1?

def arr(x,y):
    arr1 = np.arange(x,y)
    return arr1

arr1 = arr(1,50001)

def valorMaximo(a):
    return max(a)

print(valorMaximo(arr1))
