# Pruebas unitarias con unittest.
import unittest
from .metricas import calcular_emisiones_carbono


class TestCalculoEmisiones(unittest.TestCase):

    def test_calculo_correcto(self):
        self.assertEqual(calcular_emisiones_carbono(100.0, 0.4), 40.0)

    def test_factor_por_defecto(self):
        self.assertEqual(calcular_emisiones_carbono(50.0), 20.0)

    def test_consumo_negativo(self):
        with self.assertRaises(ValueError):
            calcular_emisiones_carbono(-5.0)
