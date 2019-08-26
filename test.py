# -*- coding: utf-8 -*-
"""Archivo de pruebas."""
from __future__ import unicode_literals

import unittest
import xmlrunner
import src.descuento as descuentos



class TestDescuentos(unittest.TestCase):
    ''' Pruebas para calculo del descuento para clientes '''

    def test_nombre_casos_prueba(self):
        ''' Caso de prueba '''
        self.assertEqual('', '')

    def test_calcular_descuento_clientes_iniciales(self):
        msj_esperado = "Descuento clientes iniciales"
        edad = 19
        valor_cotizado = 751
        dependientes = 0
        descuento_esperado = valor_cotizado*0.2
        msj, descuento = descuentos(edad, valor_cotizado, dependientes)

        self.assertEqual(msj, msj_esperado)
        self.assertEqual(descuento, descuento_esperado)

    def test_calcular_descuento_familias(self):
        msj_esperado = "Descuento para familias"
        edad = 35
        valor_cotizado = 1001
        dependientes = 6
        descuento_esperado = valor_cotizado*(0.1*dependientes)
        msj, descuento = descuentos(edad, valor_cotizado, dependientes)

        self.assertEqual(msj, msj_esperado)
        self.assertEqual(descuento, descuento_esperado)

    def test_calcular_descuento_familias_pequenias(self):
        msj_esperado = "Descuento para familias"
        edad = 35
        valor_cotizado = 1001
        dependientes = 5
        descuento_esperado = valor_cotizado*(0.05*dependientes)
        msj, descuento = descuentos(edad, valor_cotizado, dependientes)

        self.assertEqual(msj, msj_esperado)
        self.assertEqual(descuento, descuento_esperado)

    def test_calcular_descuento_especiales(self):
        msj_esperado = "Descuento especiales"
        edad = 50
        valor_cotizado = 1001
        dependientes = 5
        descuento_esperado = valor_cotizado*(0.35)
        msj, descuento = descuentos(edad, valor_cotizado, dependientes)

        self.assertEqual(msj, msj_esperado)
        self.assertEqual(descuento, descuento_esperado)

    def test_calcular_descuento_no_aplica(self):
        msj_esperado = "No aplica"
        edad = 76
        valor_cotizado = 1001
        dependientes = 5
        descuento_esperado = 0
        msj, descuento = descuentos(edad, valor_cotizado, dependientes)

        self.assertEqual(msj, msj_esperado)
        self.assertEqual(descuento, descuento_esperado)

    def test_calcular_descuento_mayores_edad(self):
        msj_esperado = "Descuento para mayores de edad"
        edad = 66
        valor_cotizado = 1001
        dependientes = 0
        descuento_esperado = 0
        msj, descuento = descuentos(edad, valor_cotizado, dependientes)

        self.assertEqual(msj, msj_esperado)
        self.assertEqual(descuento, descuento_esperado)

if __name__ == '__main__':
    unittest.main(testRunner=xmlrunner.XMLTestRunner(output='reporte-pruebas'))
