import pandas as pd

serie1 = [1,2,3]
lista_indices = ['a','b','c']
serie = pd.Series(lista_indices,serie1)
print(serie)

print(serie.index[0])

lista_valores = [[6,7,8],[8,9,5],[6,9,7]]
lista_indices = ["matematicas","historia","fisica"]
lista_nombres = ["Rodrigo","paula","andres"]

dataframe = pd.DataFrame(lista_valores,index=lista_indices,columns=lista_nombres)
print(dataframe)
print(dataframe.index[2])