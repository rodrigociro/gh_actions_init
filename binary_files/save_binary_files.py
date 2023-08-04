import pickle

lista_colors = ["rojo","verde","azul","amarillo"]

fichero_binario = open("fichero_colores.pckl","wb")
#graba la lista dentro del fichero binario
pickle.dump(lista_colors,fichero_binario)

fichero_binario.close()