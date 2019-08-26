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
        self.assertEqual('Descuento para familias', mensaje4)
        self.assertEqual(0, descuento4)
        
if __name__ == '__main__':
    unittest.main(testRunner=xmlrunner.XMLTestRunner(output='reporte-pruebas'))
