import pandas as pd
import numpy as np

valores = ['1','2',np.nan,'4']

serie=pd.Series(valores,index=list('abcd'))
print(serie)
print(serie.isnull())

print(serie.dropna())

array = [['1,','2','3'],['4',np.nan,'6'],['7','8',np.nan]]
dataframe = pd.DataFrame(array,index=list('123'),columns=list('abc'))
print(dataframe)

print(dataframe.isnull())
print(dataframe.fillna(0))
print(dataframe.dropna())