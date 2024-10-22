import unittest
from src.calculadora import calcular_promedio, calcular_desviacion_estandar
from tests.excepcion import NoSePuedeCalcular  # Asegúrate de que este nombre coincide con tu archivo

class TestCalculos(unittest.TestCase):

    def test_promedio_vacio(self):
        with self.assertRaises(NoSePuedeCalcular):
            calcular_promedio([])

    def test_promedio_un_elemento(self):
        self.assertEqual(calcular_promedio([42]), 42)

    def test_promedio_dos_elementos(self):
        self.assertEqual(calcular_promedio([10, 20]), 15)

    def test_promedio_n_elementos(self):
        self.assertEqual(calcular_promedio([10, 20, 30, 40, 50]), 30)

    def test_promedio_todos_ceros(self):
        self.assertEqual(calcular_promedio([0, 0, 0, 0]), 0)

    def test_promedio_elementos_positivos_y_negativos(self):
        self.assertEqual(calcular_promedio([-10, 0, 10]), 0)

    def test_promedio_no_numericos(self):
        with self.assertRaises(TypeError):
            calcular_promedio([10, 'a', 30])

    def test_desviacion_estandar_vacio(self):
        with self.assertRaises(NoSePuedeCalcular):
            calcular_desviacion_estandar([])

    def test_desviacion_estandar_un_elemento(self):
        self.assertEqual(calcular_desviacion_estandar([42]), 0.0)

    def test_desviacion_estandar_dos_elementos(self):
        self.assertAlmostEqual(calcular_desviacion_estandar([10, 20]), 5.0)

    def test_desviacion_estandar_n_elementos(self):
        self.assertAlmostEqual(calcular_desviacion_estandar([10, 20, 30, 40, 50]), 14.142135623730951)

    def test_desviacion_estandar_todos_ceros(self):
        self.assertEqual(calcular_desviacion_estandar([0, 0, 0, 0]), 0.0)

    def test_desviacion_estandar_elementos_positivos_y_negativos(self):
        self.assertAlmostEqual(calcular_desviacion_estandar([-10, 0, 10]), 8.16496580927726)

    def test_desviacion_estandar_no_numericos(self):
        with self.assertRaises(TypeError):
            calcular_desviacion_estandar([10, 'a', 30])

if __name__ == "__main__":
    unittest.main()
