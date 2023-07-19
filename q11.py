import pandas as pd
#Questão 11: Selecione apenas as linhas do DataFrame df em que o sexo seja 'F'.

def DataFrame(dicionario):
    df = pd.DataFrame(dicionario)
    return df

def feminino(dicionario):
    sexos = dicionario.get('Sexo')
    indices = []
    for i, sexo in enumerate(sexos):
        if sexo == 'F':
            indices.append(i)
    return indices

x= {
    'Nome':['Ana', 'Bartolomeu', 'Caio', 'Dora'],
    'Idade': [28, 32, 25, 60],
    'Sexo': ['F', 'M', 'F', 'F'],
    'Medicamento': ['A', 'B', 'A', 'B'],
    'Curado': [True, True, False, False]
}

df = DataFrame(x)
indices = feminino(x)

for indice in indices:
    print(f'{df.loc[indice]}\n')
