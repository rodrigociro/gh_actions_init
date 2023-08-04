import re

texto = "hola, mi nombre es Rodrigo"

resultado = re.search("nombre",texto)
print(resultado)

if(resultado):
    print("Cadena encontrada")
else:
    print("Cadena no encontrada")

#buscar por el ultimo
re.search("Rodrigo$",texto)

#buscar por el principio
re.search("^Rodrigo$",texto)

#buscar por el principio
re.search("mi.*es",texto)


#todas las ocurrencias y devuelve lista
contenido = """
blancno rojo
rojo
rojo 1
"""
datos = re.findall("o.*.o",contenido)
print(datos)

#split
texto2 = "la silla es blanca y vale 8€"
spliteado = re.split("\s",texto2)
print(spliteado)

print("hola\n como estas\nRodrigo")

#sub sustituye 
sustitur = re.sub("blanca","roja",texto2)
print(sustitur)