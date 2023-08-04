try:
    numero1 = 5
    numero2 = 0
    division = numero1 / numero2
    print(division)
except ZeroDivisionError:
    print("error division entre cero")
except:
    print("ha habido un errº.ºr")
else:
    print("la división funciono correctamente")
#el finally se ejecutara independientemente del resultado del try
finally:
    print("esta prueba del try se ha terminado")
