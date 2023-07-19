import pandas as pd
#Questão 8: Crie um DataFrame Pandas chamdo df com as seguintes colunas: ‘Nome’, ‘Idade’, ‘Sexo’, ‘Medicamento’.

def DataFrame(dicionario):
    df = pd.DataFrame(dicionario)
    return df

x= {
    'Nome': [],
    'Idade': [],
    'Sexo': [],
    'Medicamento': []
}

print(DataFrame(x))
