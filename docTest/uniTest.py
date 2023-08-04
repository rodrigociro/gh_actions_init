def multiplicar(x,y):
    return x * y

resultado = multiplicar(2,5)
print(resultado)

import unittest
class pruebas(unittest.TestCase):
    def test(self):
        self.assertEqual(multiplicar(2,4),8)
        self.assertEqual(multiplicar(2,4),9)

if __name__ == '__main__':
    unittest.main()
