import unittest
from peso import peso
class Testcontador(unittest.TestCase):

    def setUp(self):
        self.peso = peso()

    def test_cont_1(self):
        self.contt(2,"gramos=2000.00 libras=4.41 toneladas=0.00")

    def contt(self,i, res):
        resultado = self.peso.calcularPeso(i)
        self.assertEqual(res,resultado)

if __name__ == '__main__':
    unittest.main()
