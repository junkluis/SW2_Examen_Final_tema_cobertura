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

    def test_menor_edad(self):
        '''Caso 1: Menor de edad'''
        mensaje, descuento = descuentos.calcular_descuento(17, 1000, 0)
        self.assertEqual('Descuento no valido', mensaje)
        self.assertEqual(0, descuento)


if __name__ == '__main__':
    unittest.main(testRunner=xmlrunner.XMLTestRunner(output='reporte-pruebas'))
