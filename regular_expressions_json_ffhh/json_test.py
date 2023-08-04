import json
#json, convertir datos de un diccionario de python a una estructura JSON
# <<< si llamas a tu archivo "json.py" e importas la librería te dará error >>>


#crear diccionario
producto1 = {
    "nombre" : "silla",
    "color" : "blanco",
    "precio" : 80
}

#importar la librería de json 
formateado = json.dumps(producto1)
print(formateado)

#se ve como una lista pero no es accesible desde python

#convetir de json a diccionario
diccionario = json.loads(formateado)

#al ser un diccionario ya es accesible desde python :)
print(diccionario["nombre"])
