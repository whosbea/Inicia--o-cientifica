import pandas as pd
#Questão 12: Ordene o DataFrame df por idade em ordem decrescente.

def DataFrame(dicionario):
    df = pd.DataFrame(dicionario)
    return df

x= {
    'Nome':['Ana', 'Bartolomeu', 'Caio', 'Dora'],
    'Idade': [28, 32, 25, 60],
    'Sexo': ['F', 'M', 'F', 'F'],
    'Medicamento': ['A', 'B', 'A', 'B'],
    'Curado': [True, True, False, False]
}
df = DataFrame(x)
ordenado = df.sort_values(by='Idade', ascending=False)
print(ordenado)