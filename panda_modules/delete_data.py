import pandas as pd
import numpy as np

#series
array1 = np.arange(4)
print(array1)
serie1 = pd.Series(array1,index=['a','b','c','d'])
print(serie1)

print(serie1.drop('c'))

#dataframes

lista_valores  = np.arange(9).reshape(3,3)
lista_indices = ['a','b','c']
lista_columnas = ['c1','c2','c3']

dataframe1 = pd.DataFrame(lista_valores,index=lista_indices,columns=lista_columnas)
print(dataframe1)
print(dataframe1.drop('b'))
