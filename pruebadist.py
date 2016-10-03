import unittest
from distancia import distancia
class Testcontador(unittest.TestCase):

    def setUp(self):
        self.distancia = distancia()

    def test_cont_1(self):
        self.contt(-10, "pies=-32.81 pulgadas=-393.70")

    def contt(self,i,res):
        resultado = self.distancia.calcularDistancia(i)
        self.assertEqual(res,resultado)

if __name__ == '__main__':
    unittest.main()
