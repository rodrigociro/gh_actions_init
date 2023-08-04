import re

def buscar(palabra, frase):

    resultado = re.search(palabra,frase)
    if(resultado):
        print("la palabra está en la frase {}".format(resultado))
        inicial = resultado.start()
        final = resultado.end()
        print("la posicion incial es {} y la posicion final es {}".format(inicial,final))
    else:
        print("la palabra no está en la frase")
    

texto = "esto es una frase  de pruebas para hacer busquedas"
palabra_a_buscar = "una"

buscar(palabra_a_buscar,texto)