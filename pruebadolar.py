import unittest
from dolares import dolares


class Testcontador(unittest.TestCase):

    def setUp(self):
        self.dolares = dolares()

    def test_cont_1(self):
        self.contt(100, 10, 1000)

    def contt(self, i, j, res):
        resultado = self.dolares.calcularDivisas(i, j)
        self.assertEqual(res, resultado)

if __name__ == '__main__':
    unittest.main()
