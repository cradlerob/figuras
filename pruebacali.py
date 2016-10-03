import unittest
from calificaciones import calificaciones


class Testcalificaciones(unittest.TestCase):

    def setUp(self):
        self.calificaciones = calificaciones()

    def test_cal_1(self):
        self.calt([10, 9.5, 8], 9.166666666666666)

    def test_cal_2(self):
        self.calt([8, 9, 8], 8.333333333333334)

    def test_cal_3(self):
        self.calt([10, 9, 8], 9)

    def test_cal_3_inval(self):
        self.calt(['diez', 'nueve', 'ocho'], "Dato invalido")

    def test_cal_3_inval(self):
        self.calt([11, 20, 10], "Calificacion erronea")

    def calt(self, i, res):
        resultado = self.calificaciones.mostrarCalificacion(i)
        self.assertEqual(res, resultado)

if __name__ == '__main__':
    unittest.main()
