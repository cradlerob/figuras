import unittest
from contadorPalabras import contador


class Testcontador(unittest.TestCase):

    def setUp(self):
        self.contador = contador()

    def test_cont_1(self):
        self.contt("Que lindo dia que hace hoy", [
                   ('hace', 1), ('hoy', 1), ('que', 2), ('dia', 1), ('lindo', 1)])

    def contt(self, i, res):
        resultado = self.contador.contador(i)
        self.assertEqual(res, resultado)

if __name__ == '__main__':
    unittest.main()
