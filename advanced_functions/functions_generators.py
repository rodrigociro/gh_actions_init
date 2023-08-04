#range
range(0,11)
for numero in range(0,11):
    print(numero)

#range(0,11) = range(11)

#crea mi funcion generador
def pares(maximo):
    for numero in range(maximo):
        if numero % 2 == 0:
            yield numero

pares(7)
for a in pares(7):
    print(a) 