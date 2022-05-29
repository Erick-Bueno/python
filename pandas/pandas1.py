import pandas as pd
import numpy  as np
teste = pd.read_excel('C:/Users/Pichau/Documents/Linguas/python/pandas/arquivo1.xlsx')

#print(teste.head())

dic = {"Nomes":["marcos", "Daniel","Erick"],
       "Notas":[7, 8, 6],
       "Aprovados":["Sim", "Sim", "Não"]}


dataframe = pd.DataFrame(dic)  #transforma dicionarios em dataframe
#print(dataframe)


obj1 = pd.Series([1,5,8,5,6,7]) #transforma lista em formato series
#print(obj1)


array1 = np.array([(1,2,3,4),(5,6,7,8),(9,10,11,12)])  #criando um vetor
array2 = np.array([1,2,3,4]) #array

obj2 = pd.Series(array2) #transforma o array em formato series
#print(obj2)

