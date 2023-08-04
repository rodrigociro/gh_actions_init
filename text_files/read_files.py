#leer ficheros de textos "file_test.txt" mediante al funcion open

fichero = open("texto.txt","rt")

datos_fichero = fichero.read()
print(datos_fichero)
