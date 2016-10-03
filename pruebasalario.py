import unittest
from salario import salario
class Testcontador(unittest.TestCase):

    def setUp(self):
        self.salario = salario()

    def test_cont_1(self):
        self.contt(100.1,"nuevo Salario 125.125")

    def test_cont_2(self):
        self.contt("cien","Datos invalidos")

    def contt(self,i, res):
        resultado = self.salario.calcularAumento(i)
        self.assertEqual(res,resultado)

if __name__ == '__main__':
    unittest.main()
