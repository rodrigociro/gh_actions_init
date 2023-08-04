def saludar(nombre):
    """
    Esto será un comentario de la función saludar.
    esta funcion recibirá como parametro una cadena con el nombre
    e imprimirá por pantalla un saludo con el nombre concatenado
    """
    print("hola ",nombre)

help(saludar)
saludar("Rodrigo")

class Saludos:
    """
    Esta clase tendra dos funciones:
    -buenos días
    -adios
    """
    def buenosdias(self,parametro1):
        """funcion de holaaa"""
        self.nombre = parametro1
        print("buenos días ",self.nombre)

    def adios(self,parametro1):
        """funcion de adios"""
        self.nombre = parametro1
        print("adios ",self.nombre)

objeto1 = Saludos()
objeto1.buenosdias("Randyy")
help(Saludos)