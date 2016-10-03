import unittest
from parentesis import parentesis


class Testcontador(unittest.TestCase):

    def setUp(self):
        self.parentesis = parentesis()

    def test_cont_1(self):
        self.contt("(Ho(la))", 'OK')

    def contt(self, i, res):
        resultado = self.parentesis.searchstring(i)
        self.assertEqual(res, resultado)

if __name__ == '__main__':
    unittest.main()
