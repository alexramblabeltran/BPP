import unittest
import funciones

class PruebasFunciones(unittest.TestCase):

    def test_coseno(self):
        self.assertEqual(funciones.coseno(0),1)
    def test_seno(self):
        self.assertEqual(funciones.seno(0),0)
    def test_tangente(self):
        self.assertEqual(funciones.tangente(0),0)
    def test_logaritmo_decimal(self):
        self.assertEqual(funciones.logaritmo_decimal(1000),3)
    def test_raíz_cuadrada(self):
        self.assertEqual(funciones.raíz_cuadrada(49),7)

if __name__ == '__main__':
    unittest.main()