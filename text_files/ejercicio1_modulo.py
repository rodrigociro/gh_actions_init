class fichero():
    def __init__(self,parametro1):
        self.nombre = parametro1

    def leer_fichero(self):
        fichero = open(self.nombre,"rt")
        texto = fichero.read()
        return texto
    
    def crear_fichero(self,texto):
        fichero = open(self.nombre,"wt")
        fichero.write(texto)
        fichero.close()

    def incluir_datos(self,texto):
        fichero = open(self.nombre,"at")
        fichero.write(texto)
        fichero.close()
    