import ejercicio1_modulo

nombre_fichero = "prueba.txt"
fichero1 = ejercicio1_modulo.fichero(nombre_fichero)


fichero1.crear_fichero("buenos días ")

fichero1.incluir_datos("adios")

texto_leido=(fichero1.leer_fichero())
print(texto_leido)