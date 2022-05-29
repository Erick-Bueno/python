import pandas as pd

abrir_arq = pd.read_excel("C:/Users/Pichau/Documents/Linguas/python/pandas/arquivo1.xlsx")

ler_linhas = abrir_arq.head(2)

lista = [[1,2,3,6,4,5],[6,7,8,9,10]]

#obj2 = pd.DataFrame(lista)
#print(obj2)

obj = pd.Series(lista)
print(obj)
