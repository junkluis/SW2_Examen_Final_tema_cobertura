# -*- coding: utf-8 -*-
"""Archivo de pruebas."""
from __future__ import unicode_literals

import unittest
import xmlrunner
import src.descuento as descuentos


class TestDescuentos(unittest.TestCase):
    ''' Pruebas para calculo del descuento para clientes '''

    def test_descuento_clientes_principales(self):
        edad = 19
        valor = 800
        dependientes = 0
        result = descuentos.calcular_descuento(edad, valor, dependientes)
        self.assertEqual(result[0], "Descuento clientes iniciales")
        self.assertEqual(result[1], valor*0.2)

    def test_descuento_no_valido(self):
        edad = 12
        valor = 800
        dependientes = 0
        result = descuentos.calcular_descuento(edad, valor, dependientes)
        self.assertEqual(result[0], "Descuento no valido")
        self.assertEqual(result[1], 0)

    def test_descuento_famiias_menora6(self):
        edad = 36
        valor = 1200
        dependientes = 4
        result = descuentos.calcular_descuento(edad, valor, dependientes)
        self.assertEqual(result[0], "Descuento para familias")
        self.assertEqual(result[1], valor*0.05*dependientes)

    def test_descuento_famiias_mayora6(self):
        edad = 36
        valor = 1200
        dependientes = 7
        result = descuentos.calcular_descuento(edad, valor, dependientes)
        self.assertEqual(result[0], "Descuento para familias")
        self.assertAlmostEqual(result[1], valor*0.1*dependientes)

    def test_descuento_especiales(self):
        edad = 55
        valor = 1200
        dependientes = 0
        result = descuentos.calcular_descuento(edad, valor, dependientes)
        self.assertEqual(result[0], "Descuento especiales")
        self.assertAlmostEqual(result[1], valor*0.35)

    def test_descuento_no_aplica(self):
        edad = 28
        valor = 1200
        dependientes = 3
        result = descuentos.calcular_descuento(edad, valor, dependientes)
        self.assertEqual(result[0], "No aplica")
        self.assertEqual(result[1], 0)

    def test_descuento_mayores_mayora2000(self):
        edad = 80
        valor = 3000
        dependientes = 3
        result = descuentos.calcular_descuento(edad, valor, dependientes)
        self.assertEqual(result[0], "Descuento para mayores de edad")
        self.assertAlmostEqual(result[1], valor*0.5)

    def test_descuento_mayores_menor2000(self):
        edad = 80
        valor = 1500
        dependientes = 3
        result = descuentos.calcular_descuento(edad, valor, dependientes)
        self.assertEqual(result[0], "Descuento para mayores de edad")
        self.assertEqual(result[1], valor*0.25)

    def test_descuento_clientes_mayor5000(self):
        edad = 70
        valor = 6000
        dependientes = 3
        result = descuentos.calcular_descuento(edad, valor, dependientes)
        self.assertEqual(result[0], "Descuento para clientes")
        self.assertEqual(result[1], valor*0.02)

    def test_descuento_clientes_menor5000(self):
        edad = 70
        valor = 3000
        dependientes = 3
        result = descuentos.calcular_descuento(edad, valor, dependientes)
        self.assertEqual(result[0], "Descuento para clientes")
        self.assertEqual(result[1], valor*0.01)


if __name__ == '__main__':
    unittest.main(testRunner=xmlrunner.XMLTestRunner(output='reporte-pruebas'))
