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
        mensaje_obtenido, descuento_obtenido=calcular_descuento(edad, valor_cotizado, dependientes)
        mensaje_esperado= "Descuento clientes iniciales"
        self.assertEqual(mensaje_obtenido, mensaje_esperado)



if __name__ == '__main__':
    unittest.main(testRunner=xmlrunner.XMLTestRunner(output='reporte-pruebas'))
