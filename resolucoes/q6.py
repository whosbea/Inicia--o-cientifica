import numpy as np
#Questão 6: Multiplique todos os elementos da matriz mat 1 por 2.

mat1 = np.random.random((3,3))

def multiplicaMatriz(matriz,fator):
    mat_2 = matriz * fator
    return mat_2

print(f'Matriz inicial: {mat1}')
print(f'Matriz duplicada: {multiplicaMatriz(mat1,2)}')
