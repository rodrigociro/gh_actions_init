import numpy as np

#lista 10.19
lista1 = [10,11,12,13,14,15,16,17,18,19]
lista2 = [50,51,52,53,54,55,56,57,58,59]

lista_doble = (lista1,lista2)
array_doble = np.array(lista_doble)

print("arraydoble: " ,array_doble)
print("arraydoble * 2: ",array_doble*2)

print(array_doble.shape)