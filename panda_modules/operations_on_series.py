import pandas as pd
import numpy as np

serie1 = pd.Series([0,1,2],index=['a','b','c'])
print(serie1)

serie2 = pd.Series([3,4,5,6],index=['a','b','c','d'])

print(serie1+serie2)
lista_valores = np.arange(4).reshape(2,2)
print(lista_valores)
lista_indices = list('ab')
lista_columna = list('12')

dataframe1 = pd.DataFrame(lista_valores,index=lista_indices,columns=lista_columna)
print(dataframe1)

lista_valores_2= np.arange(9).reshape(3,3)
lista_indices2 = list('ab3')
lista_columna2 = list('123')

dataframe2 = pd.DataFrame(lista_valores_2,index=lista_indices2,columns=lista_columna2)
print(dataframe2)

print(dataframe1+dataframe2)