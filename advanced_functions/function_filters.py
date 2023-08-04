#filtar lista con condiciones y rsultado igual a lista
def positivo(numero):
    if numero > 0:
        return True
    else:
        return False

print(positivo(5))
print(positivo(-3))  

lista_numeros = [4,-2,8,-3,-5,-7,1,9]

filtro = filter(positivo, lista_numeros)
resultado = list(filtro)
print(resultado)