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
        mensaje, descuento = descuentos.calcular_descuento(17, 500, 0)
        self.assertEqual('Descuento no valido', mensaje)
        self.assertNotEqual(9, descuento)
        mensaje1, descuento1 = descuentos.calcular_descuento(19, 751, 0)
        self.assertEqual('Descuento clientes iniciales', mensaje1)
        self.assertNotEqual(20, descuento1)
        mensaje2, descuento2 = descuentos.calcular_descuento(40, 1001, 5)
        self.assertEqual('Descuento para familias', mensaje2)
        self.assertEqual(250.25, descuento2)
        mensaje3, descuento3 = descuentos.calcular_descuento(50, 2000, 0)
        self.assertEqual('Descuento especiales', mensaje3)
        self.assertEqual(700, descuento3)
        mensaje4, descuento4 = descuentos.calcular_descuento(40, 1001, 0)
        self.assertEqual('No aplica', mensaje4)
        self.assertEqual(0, descuento4)
        mensaje5, descuento5 = descuentos.calcular_descuento(81, 1001, 0)
        self.assertEqual('Descuento para mayores de edad', mensaje5)
        self.assertEqual(250.25, descuento5)
        mensaje6, descuento6 = descuentos.calcular_descuento(81, 2001, 5)
        self.assertEqual('Descuento para mayores de edad', mensaje6)
        self.assertEqual(1000.5, descuento6)
        
    def test_descuento_clientes(self):
        mensaje7, descuento7 = descuentos.calcular_descuento(28, 700, 5)
        self.assertEqual('Descuento para clientes', mensaje7)
        self.assertEqual(7, descuento7)

    def test_descuento_para_clientes(self):
        mensaje8, descuento8 = descuentos.calcular_descuento(66, 5000, 1)
        self.assertEqual('Descuento para clientes', mensaje8)
        self.assertEqual(100, descuento8)

    def test_no_valido(self):
        '''No valido'''
        mensaje9, descuento9 = descuentos.calcular_descuento(12, 700, 5)
        self.assertEqual('Descuento no valido', mensaje9)
        self.assertEqual(0, descuento9)

if __name__ == '__main__':
    unittest.main(testRunner=xmlrunner.XMLTestRunner(output='reporte-pruebas'))
