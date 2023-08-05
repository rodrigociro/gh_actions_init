import numpy as np

#respuesta
def pares(inicio,fin):
    c = []
    a = np.arange(inicio,fin)
    for b in a:
        if(b % 2 == 0):
            c.append(b)
    return c

print(pares(0,30))
print(pares(2,40))

#solucion

def pares2(inicio,fin):
    if(inicio % 2 == 0):
        array1 = np.arange(inicio,fin,2)
    else:
        inicio = inicio + 1
        array1 = np.arange(inicio,fin,2)
    return array1

print(pares2(0,30))
print(pares2(2,40))