import unittest
from tienda import tienda
class Testcontador(unittest.TestCase):

    def setUp(self):
        self.tienda = tienda()

    def test_cont_1(self):
        self.contt(1000,1150.0)

    def test_cont_2(self):
        self.contt("cien","Error: dato invalido")

    def contt(self,i, res):
        resultado = self.tienda.calculaTotal(i)
        self.assertEqual(res,resultado)

if __name__ == '__main__':
    unittest.main()
