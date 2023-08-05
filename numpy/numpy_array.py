import numpy as np

a = np.zeros(4)
b = np.ones(4)
c = np.arange(5)
d = np.arange(3,20)
print(a)
print(c)
print(d)

#list a Array -->
lista1 = [1,2,3,4]
lista2 = [5,6,7,8]
array1 = np.array(lista1)
print(array1)

lista_doble = (lista1,lista2)
array_doble = np.array(lista_doble)
print(array_doble)
print(array_doble.shape)
print(array_doble.dtype)