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

    def test_descuento_menor_edad(self):
        ''' Caso cliente es menor de edad'''
        self.assertEqual(descuentos.calcular_descuento(17, 800, 1), ('Descuento no valido', 0))

    def test_valor_cotizado_menor(self):
        ''' Caso valor cotizado es menor de 500 '''
        self.assertEqual(descuentos.calcular_descuento(20, 400, 1), ('Descuento no valido', 0))

    def test_dependientes_menor_cero(self):
        ''' Caso dependientes es menor de 0 '''
        self.assertEqual(descuentos.calcular_descuento(20, 800, -1), ('Descuento no valido', 0))

    def test_todos_valores_no_validos(self):
        ''' Caso cliente es menor de edad, valor cotizado es menor de 500 y dependientes es menor de 0 '''
        self.assertEqual(descuentos.calcular_descuento(17, 400, -1), ('Descuento no valido', 0))

    def test_todos_valores_validos(self):
        ''' Caso cliente es mayor de edad, valor cotizado es mayor de 500 y dependientes es mayor o igual a 0 '''
        self.assertEqual(descuentos.calcular_descuento(20, 800, 1), ('Descuento clientes iniciales', 160))

    def test_descuento_familias(self):
        ''' Caso para familias '''
        self.assertEqual(descuentos.calcular_descuento(37, 1500, 3), ('Descuento para familias', 225.00000000000003))

    def test_descuento_especial_no_aplica(self):
        ''' Caso especial para cliente de entre 28 y 34 anios '''
        self.assertEqual(descuentos.calcular_descuento(30, 1500, 3), ('No aplica', 0))

    def test_descuento_mayores_edad(self):
        ''' Caso clientes mayores a 80 anios '''
        self.assertEqual(descuentos.calcular_descuento(85, 1500, 3), ('Descuento para mayores de edad', 375))

    def test_descuento_clientes(self):
        ''' Caso clientes mayores a 65 anios con dependientes '''
        self.assertEqual(descuentos.calcular_descuento(75, 1500, 3), ('Descuento para clientes', 15))

if __name__ == '__main__':
    unittest.main(testRunner=xmlrunner.XMLTestRunner(output='reporte-pruebas'))
