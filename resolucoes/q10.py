import pandas as pd
#Questão 10: Crie uma nova coluna no dataframe df com os seguintes dados: curado = [True, True, False, False]

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

print(DataFrame(x))
