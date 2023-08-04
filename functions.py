#functions. bloque de código que se ejecuta cuando es llamado

def saludar():
    print("buenos días")

saludar()

def saludar2(nombre):
    print("buenos días "+nombre)
pepito = "antonio"

saludar2(pepito)

#def sumar(numero1,numero2):
#    suma = numero1 + numero2
#    return suma

#hola = int(input("introduce un numero: "))
#hola2 = int(input("introduce otro numero a sumar: "))
#
#resultado = sumar(hola,hola2)
#print(resultado)

colores = ["rojo","verde","azul"]
def incluir_color(lista, cadena_de_texto):
    lista.append(cadena_de_texto)
print(colores)
color ="negro"
incluir_color(colores,color)
print(colores)

print ("ejercicios -------------")

media_de_notas = lambda nota1,nota2,nota3: (nota1+nota2+nota3)/3
print("la media es",media_de_notas(4,5,6))