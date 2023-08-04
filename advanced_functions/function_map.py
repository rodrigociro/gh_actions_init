#
def multi (parametro):
    return parametro * 2

print(multi(2))

numeros = [
    2,4,6
]

mapeo = map(multi,numeros)
resultado = list(mapeo)
print(resultado)

# se utiliza mucho lambda con map

lista_resultado = list(map(lambda numero : numero * 2,numeros))
print(lista_resultado)