import pickle
frutas = {
    "manzana":"apple",
    "platano":"banana",
    "piña":"pineapple",
    "limon":"lemon",
}

fichero = open("fichero.pckl","wb")
pickle.dump(frutas,fichero)

fichero.close()