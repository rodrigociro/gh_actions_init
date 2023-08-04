import pickle

fichero_binario = open ("fichero_colores.pckl","rb")
leido = pickle.load(fichero_binario)
print(leido)