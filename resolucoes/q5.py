import numpy as np
#Questão 5: Multiplique todos os elementos do array arr1 por 2.

def arr(x,y):
    arr1 = np.arange(x,y)
    return arr1

arr1 = arr(1,50001)

def multiplicaArr(arr, fator):
    arr_2 = arr * fator
    return arr_2

print(multiplicaArr(arr1,2))



#Outra forma que pensei em fazer:
# def multiplicaArr(arr,fator):
#     arr_2 = np.array([], dtype= int)
#     for i in range(len(arr)):
#         a = arr[i] * fator
#         arr_2 = np.append(arr_2, a)
#     return arr_2
