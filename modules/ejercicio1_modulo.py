#ejercicios modulos

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

media_de_notas = lambda nota1,nota2,nota3: (nota1+nota2+nota3)/3