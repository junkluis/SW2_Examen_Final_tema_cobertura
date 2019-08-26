# -*- coding: utf-8 -*-
"""Archivo de pruebas."""
from __future__ import unicode_literals

import unittest
import xmlrunner
import src.descuento as descuentos


class TestDescuentos(unittest.TestCase):
    ''' Pruebas para calculo del descuento para clientes '''

    def test_no_valido_edad(self):
        ''' Caso de prueba '''
        mensaje, descuento = descuentos.calcular_descuento(17, 600, 0)
        self.assertEqual(mensaje, 'Descuento no valido')
        self.assertEqual(descuento, 0)

    def test_no_valido_valor_cotizado(self):
        ''' Caso de prueba '''
        mensaje, descuento = descuentos.calcular_descuento(19, 300, 0)
        self.assertEqual(mensaje, 'Descuento no valido')
        self.assertEqual(descuento, 0)

    def test_no_valido_dependientes(self):
        ''' Caso de prueba '''
        mensaje, descuento = descuentos.calcular_descuento(19, 800, -5)
        self.assertEqual(mensaje, 'Descuento no valido')
        self.assertEqual(descuento, 0)

    def test_valido_clientes_iniciales_edad(self):
        ''' Caso de prueba '''
        valor_cotizado = 600
        mensaje, descuento = descuentos.calcular_descuento(
            20, valor_cotizado, 0)
        self.assertEqual(mensaje, 'Descuento clientes iniciales')
        self.assertEqual(descuento, valor_cotizado*0.2)

    def test_valido_clientes_iniciales_valor(self):
        ''' Caso de prueba '''
        valor_cotizado = 800
        mensaje, descuento = descuentos.calcular_descuento(
            19, valor_cotizado, 0)
        self.assertEqual(mensaje, 'Descuento clientes iniciales')
        self.assertEqual(descuento, valor_cotizado*0.2)

    def test_valido_familias_1(self):
        ''' Caso de prueba '''
        valor_cotizado = 1200
        dependientes = 5
        mensaje, descuento = descuentos.calcular_descuento(
            30, valor_cotizado, dependientes)
        self.assertEqual(mensaje, 'Descuento para familias')
        self.assertEqual(descuento, valor_cotizado*0.05*dependientes)

    def test_valido_familias_2(self):
        ''' Caso de prueba '''
        valor_cotizado = 1200
        dependientes = 7
        mensaje, descuento = descuentos.calcular_descuento(
            45, valor_cotizado, dependientes)
        self.assertEqual(mensaje, 'Descuento para familias')
        self.assertEqual(descuento, valor_cotizado*(0.1*dependientes))

    def test_valido_especiales(self):
        ''' Caso de prueba '''
        valor_cotizado = 1200
        dependientes = 0
        mensaje, descuento = descuentos.calcular_descuento(
            55, valor_cotizado, dependientes)
        self.assertEqual(mensaje, 'Descuento especiales')
        self.assertEqual(descuento, valor_cotizado*0.35)

    def test_no_aplica(self):
        ''' Caso de prueba '''
        valor_cotizado = 1200
        dependientes = 0
        mensaje, descuento = descuentos.calcular_descuento(
            30, valor_cotizado, dependientes)
        self.assertEqual(mensaje, 'No aplica')
        self.assertEqual(descuento, 0)


if __name__ == '__main__':
    unittest.main(testRunner=xmlrunner.XMLTestRunner(output='reporte-pruebas'))
