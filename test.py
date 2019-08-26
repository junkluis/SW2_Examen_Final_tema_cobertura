# -*- coding: utf-8 -*-
"""Archivo de pruebas."""
from __future__ import unicode_literals

import unittest
import xmlrunner
import src.descuento as descuentos

'''
caso 1, entre 18 y 27 mayor a 500
'''

class TestDescuentos(unittest.TestCase):
    ''' Pruebas para calculo del descuento para clientes '''

    def test_descuento1(self):
        edad =20
        valor_cotizado = 600
        dependientes = 0
        mensaje_obtenido, descuento_obtenido=descuentos.calcular_descuento(edad, valor_cotizado, dependientes)
        mensaje_esperado= "Descuento clientes iniciales"
        self.assertEqual(mensaje_obtenido, mensaje_esperado)

    def test_descuento2(self):
        edad =35
        valor_cotizado = 800
        dependientes = 0
        mensaje_obtenido, descuento_obtenido=descuentos.calcular_descuento(edad, valor_cotizado, dependientes)
        mensaje_esperado= "Descuento clientes iniciales"
        self.assertEqual(mensaje_obtenido, mensaje_esperado)

    def test_descuento_familias1(self):
        edad =35
        valor_cotizado = 1200
        dependientes = 1
        mensaje_obtenido, descuento_obtenido=descuentos.calcular_descuento(edad, valor_cotizado, dependientes)
        mensaje_esperado= "Descuento para familias"
        self.assertEqual(mensaje_obtenido, mensaje_esperado)

    def test_descuento_familias2(self):
        edad =35
        valor_cotizado = 1200
        dependientes = 5
        mensaje_obtenido, descuento_obtenido=descuentos.calcular_descuento(edad, valor_cotizado, dependientes)
        mensaje_esperado= "Descuento para familias"
        self.assertEqual(mensaje_obtenido, mensaje_esperado)

    def test_descuento_especiales(self):
        edad =50
        valor_cotizado = 1200
        dependientes = 1
        mensaje_obtenido, descuento_obtenido=descuentos.calcular_descuento(edad, valor_cotizado, dependientes)
        mensaje_esperado= "Descuento especiales"
        self.assertEqual(mensaje_obtenido, mensaje_esperado)

    def test_descuento_no_aplica(self):
        edad =45
        valor_cotizado = 1200
        dependientes = 0
        mensaje_obtenido, descuento_obtenido=descuentos.calcular_descuento(edad, valor_cotizado, dependientes)
        mensaje_esperado= "No aplica"
        self.assertEqual(mensaje_obtenido, mensaje_esperado)

    def test_descuento_no_valido1(self):
        edad =18
        valor_cotizado = 600
        dependientes = 0
        mensaje_obtenido, descuento_obtenido=descuentos.calcular_descuento(edad, valor_cotizado, dependientes)
        mensaje_esperado= "Descuento no valido"
        self.assertEqual(mensaje_obtenido, mensaje_esperado)

    def test_descuento_no_valido2(self):
        edad =35
        valor_cotizado = 400
        dependientes = 0
        mensaje_obtenido, descuento_obtenido=descuentos.calcular_descuento(edad, valor_cotizado, dependientes)
        mensaje_esperado= "Descuento no valido"
        self.assertEqual(mensaje_obtenido, mensaje_esperado)

if __name__ == '__main__':
    unittest.main(testRunner=xmlrunner.XMLTestRunner(output='reporte-pruebas'))
