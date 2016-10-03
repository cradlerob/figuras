import unittest
from calculadora import calculadora


class TestFiguras(unittest.TestCase):

    def setUp(self):
        self.calculadora = calculadora()

    def test_suma_1_1(self):
        self.sumat(1, 1, 2)

    def test_suma_4_5_2(self):
        self.sumat(4.5, 2, 6.5)

    def test_suma_10_0(self):
        self.sumat(10, 0, 10)

    def test_resta_1_1(self):
        self.restat(1, 1, 0)

    def test_resta_4_5_2(self):
        self.restat(4.5, 2, 2.5)

    def test_resta_neg_1_2(self):
        self.restat(-1, 2, -3)

    def sumat(self, i, j, res):
        resultado = self.calculadora.sumar(i, j)
        self.assertEqual(res, resultado)

    def restat(self, i, j, res):
        resultado = self.calculadora.restar(i, j)
        self.assertEqual(res, resultado)

if __name__ == '__main__':
    unittest.main()
