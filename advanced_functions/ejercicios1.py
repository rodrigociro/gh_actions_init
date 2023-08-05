
numeros_primos = [2,3,5,7,11,13,17,23,29,31,37,41,43,47,53,59,61,67,71,73,83,89,97]

def primos(maximo):
    for n in range(maximo):
        if(n in numeros_primos):
            yield n
        if(n > 100):
            break    

maximo = 50
for numero in primos(maximo):
    print(numero)