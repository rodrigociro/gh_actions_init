import pandas as pd
import numpy as np

lista_valores = np.arange(3)
print(lista_valores)
lista_indices = ['i1','i2','i3']

serie1 = pd.Series(lista_valores,index=lista_indices)
print(serie1)

serie1 = serie1 * 2
print(serie1)

print(serie1['i2'])
print(serie1[serie1 > 3])