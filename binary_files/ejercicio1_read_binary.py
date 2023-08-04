import pickle

fichero = open("fichero.pckl","rb")
datos = pickle.load(fichero)
print(datos)
print(datos.values())