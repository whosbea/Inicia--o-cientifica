import pandas as pd
#Questão 13: Faça o pivoteamento do dataframe df de acordo com a coluna Medicamento

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

pivotDataFrame = df.pivot(index='Nome', columns='Medicamento', values=['Sexo', 'Idade', 'Curado'])

print(pivotDataFrame)
