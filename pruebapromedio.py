import unittest
from promedio import promedio
class Testcontador(unittest.TestCase):

    def setUp(self):
        self.promedio = promedio()

    def test_cont_1(self):
        self.contt([10,10,10],"Aprobado")

    def test_cont_2(self):
        self.contt([5.5,5,4],"Reprobado")

    def test_cont_3(self):
        self.contt([5.5,5],"Deben ser 3")

    def contt(self,i, res):
        resultado = self.promedio.calcularPromedio(i)
        self.assertEqual(res,resultado)

if __name__ == '__main__':
    unittest.main()
