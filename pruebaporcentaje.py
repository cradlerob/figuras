import unittest
from porcentajes import porcentajes


class Testcontador(unittest.TestCase):

    def setUp(self):
        self.porcentajes = porcentajes()

    def test_cont_1(self):
        self.contt(50, 50, "Porc. Hombres 50.00 Porc. Mujeres 50.00")

    def contt(self, i, j, res):
        resultado = self.porcentajes.calcularPorcentaje(i, j)
        self.assertEqual(res, resultado)

if __name__ == '__main__':
    unittest.main()
