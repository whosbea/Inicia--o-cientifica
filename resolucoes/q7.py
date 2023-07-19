import numpy as np
#Questão 7: Calcule o determinante da mat1.

mat1 = np.random.random((3,3))

def determinante3x3(matriz):
    diagonaisPositivas = (matriz[0, 0] * matriz[1, 1] * matriz[2, 2]) + (matriz[0, 1] * matriz[1, 2] * matriz[2, 0]) + (matriz[0, 2] * matriz[1, 0] * matriz[2, 1])
    diagonaisNegativas = (matriz[0, 1] * matriz[1, 0] * matriz[2, 2]) + (matriz[0, 0] * matriz[1, 2] * matriz[2, 1]) + (matriz[0, 2] * matriz[1, 1] * matriz[2, 0])
    determinante = diagonaisPositivas - diagonaisNegativas
    return determinante

print(f'Matriz: {mat1}')
print(f'Determinante da matriz: {determinante3x3(mat1)}')
