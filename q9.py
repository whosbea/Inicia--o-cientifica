import pandas as pd
#Questão 9: Preencha o dataframe df com os seguintes dados: 
# data = {
# 'Nome': ['Ana', Bartolomeu', ‘Caio’, ‘Dora’'],
# 'Idade': [28, 32, 25, 60],

# 'Sexo': ['F', 'M', 'F', ‘F’],
# 'Medicamento’: ['A', 'B', 'A', ‘B’]
# }

def DataFrame(dicionario):
    df = pd.DataFrame(dicionario)
    return df

x= {
    'Nome':['Ana', 'Bartolomeu', 'Caio', 'Dora'],
    'Idade': [28, 32, 25, 60],
    'Sexo': ['F', 'M', 'F', 'F'],
    'Medicamento': ['A', 'B', 'A', 'B']
}

print(DataFrame(x))
