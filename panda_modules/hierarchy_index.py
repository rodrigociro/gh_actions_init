import pandas as pd
import numpy as np

valores = np.random.rand(6)

indice = [[1,1,1,2,2,2],['a','b','c','a','b','c']]
serie = pd.Series(valores,index=indice)
print(serie)
print(serie[1]['b'])

dataframe = serie.unstack()
print(dataframe)

valores1 = np.arange(16).reshape(4,4)
indices1 = list('1234')
columnas = list('abcd')
dataframe1 = pd.DataFrame(valores1,index=indices1,columns=columnas)
print(dataframe1)

serie2 = dataframe1.stack()
print(serie2)