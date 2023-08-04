#ejemplo clase
separador="----------------------------------"
class clasecilla:
    color="blanco"
    precio = 100

objetoSilla = clasecilla()
print(objetoSilla.color)
print(objetoSilla.precio)

objetoSilla2 = clasecilla()
objetoSilla2.color="verde"
objetoSilla2.precio=120

print(objetoSilla2.color)
print(objetoSilla2.precio)
print(separador)
class Persona:
    def __init__(self,nombre,edad):
        self.nombre = nombre
        self.edad = edad
    def saludar(self):
        print("hola! me llamo {} y mi edad es {}".format(self.nombre,self.edad))

persona1 = Persona('Juan',37)   
print(persona1.nombre)
print(persona1.edad)
persona1.saludar()

print(separador," Ejercicios")

class coche:
    def __init__(self,primer_parametro,segundo_parametro,tercer_parametro,cuarto_parametro):
        self.marca = primer_parametro
        self.color = segundo_parametro
        self.combustilbe = tercer_parametro
        self.cilindrada = cuarto_parametro
    def mostrar_caracteristicas(self):
        print("el coche es de marca: {}".format(self.marca))
        print("el coche color: {}".format(self.color))
        print("tiene de combustile: {}".format(self.combustilbe))
        print("cilindrada de: {}".format(self.cilindrada))
              
coche1 = coche("Opel","rojo","gasolina","1,6")
coche1.mostrar_caracteristicas()
