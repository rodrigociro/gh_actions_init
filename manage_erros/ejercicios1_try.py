def operacion(parametro1, parametro2, parametro3):
    try:
        opera = parametro1 / (parametro2 - parametro3)
        print(opera)
    except:
        print("ha habido un error")

operacion(5,4,2)
operacion(6,3,3)