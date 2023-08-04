
def sumar(numero1,numero2):
    """
    documentación de esta función
    recibe dos numeros como parametros y devuelve su suma

    >>> sumar(4,3)
    7

    """
    return numero1 + numero2

resultado = sumar(2,4)
print(resultado)

import doctest
doctest.testmod()

