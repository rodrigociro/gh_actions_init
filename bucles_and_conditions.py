a = 8
b = 4
f = True
if f:
    if (b<a):
        print("hola")
else:
    print("no entro")

print("===test de FOR===")

cadena = "hola mundo"
for a in cadena:
    if (a=="o"):
        print(a)
    else:
        continue
for numero1 in range(4):
    for numero2 in range(3):
        print(numero1," - - > ", numero2)

print("===test de WHILE===")

valor = 1
fin = 10
while(valor < fin):
    print("el valor es: ",valor)
    if (valor == 5):
        break
    valor = valor + 1
    if (valor==3):
        print(valor)

print("===Ejercicio 1===")

diccionario = {
    "naranja":"orange",
    "manzana":"apple",
    "platano":"banana",
    "limon":"lemon"
}

for traducido in diccionario:
    print(diccionario[traducido])

diccionario['piña'] = "pineapple"

for elementos in diccionario:
    print(elementos,"=>",diccionario[elementos])


print("===test clave/valor===")
for clave,valor in diccionario.items():
    print("{} en inglés es {}".format(clave,valor))

print("===Ejercicio 2===")

nota = 4.5
trabajo_realizado = "si"
if (nota >= 4 and trabajo_realizado == "si"):
    nota_final = "aprobado"
else:
    nota_final = "suspenso"

print(nota_final)


print("===Ejercicio 3===")

inicio = 1
fin = 6
while(inicio < fin):
    print("esta es la fila {}".format(inicio))
    inicio = inicio + 1