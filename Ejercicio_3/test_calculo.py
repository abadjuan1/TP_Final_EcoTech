# PRUEBAS UNITARIAS DEL CALCULO DE EMISIONES
import unittest


def calcular_emisiones_carbono(consumo_kwh, factor_emision=0.4):
    if consumo_kwh < 0:
        raise ValueError("El consumo no puede ser negativo.")
    return consumo_kwh * factor_emision


class TestCalculoEmisiones(unittest.TestCase):

    def test_calculo_correcto(self):
        resultado = calcular_emisiones_carbono(100.0, 0.4)
        self.assertEqual(resultado, 40.0)

    def test_calculo_con_factor_por_defecto(self):
        resultado = calcular_emisiones_carbono(50.0)
        self.assertEqual(resultado, 20.0)

    def test_consumo_negativo_lanza_error(self):
        with self.assertRaises(ValueError):
            calcular_emisiones_carbono(-10.0)


if __name__ == "__main__":
    unittest.main()