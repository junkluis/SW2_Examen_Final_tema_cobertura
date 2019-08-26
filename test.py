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

    def test_edad_invalido(self):
        ''' Caso de prueba '''
        returned = descuentos.calcular_descuento(17, 500, 0)
        self.assertEqual(returned, ('Descuento no valido', 0))

    def test_valor_cotizado_invalido(self):
        ''' Caso de prueba '''
        returned = descuentos.calcular_descuento(19, 500, 0)
        self.assertEqual(returned, ('Descuento no valido', 0))

    def test_valor_dependientes_invalido(self):
        ''' Caso de prueba '''
        returned = descuentos.calcular_descuento(19, 600, -1)
        self.assertEqual(returned, ('Descuento no valido', 0))


#-----------------------------------------------------------------------
    def test_clientes_menor_5000_1(self):
        ''' Caso de prueba '''
        returned = descuentos.calcular_descuento(27, 600, 0)
        self.assertEqual(returned, ('Descuento para clientes', 6))

    def test_clientes_menor_5000_2(self):
        ''' Caso de prueba '''
        returned = descuentos.calcular_descuento(27, 750, 0)
        self.assertEqual(returned, ('Descuento para clientes', 7.5))

    def test_clientes_mayor_5000_1(self):
        ''' Caso de prueba '''
        returned = descuentos.calcular_descuento(27, 6000, 0)
        self.assertEqual(returned, ('Descuento para clientes', 120))

#-----------------------------------------------------------------------


    def test_clientes_iniciales(self):
        ''' Caso de prueba '''
        returned = descuentos.calcular_descuento(19, 800, 0)
        self.assertEqual(returned, ('Descuento clientes iniciales', 160))


if __name__ == '__main__':
    unittest.main(testRunner=xmlrunner.XMLTestRunner(output='reporte-pruebas'))
