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

    def test_clientes_iniciales_edad(self):
        ''' Caso de prueba '''
        returned = descuentos.calcular_descuento(19, 750, 0)
        self.assertEqual(returned, ('Descuento clientes iniciales', 150))

    def test_clientes_iniciales_cotizacion(self):
        ''' Caso de prueba '''
        returned = descuentos.calcular_descuento(100, 800, 0)
        self.assertEqual(returned, ('Descuento clientes iniciales', 160))

    def test_familias_dependientes_mayor_6(self):
    	''' Caso de prueba '''
    	returned = descuentos.calcular_descuento(28, 1200, 6)
    	self.assertEqual(returned, ('Descuento para familias', 720.0000000000001))

    def test_familias_dependientes_menor_6(self):
    	''' Caso de prueba '''
    	returned = descuentos.calcular_descuento(28, 1200, 5)
    	self.assertEqual(returned, ('Descuento para familias', 300))

    def test_familias_edad(self):
    	''' Caso de prueba '''
    	returned = descuentos.calcular_descuento(35, 1200, 1)
    	self.assertEqual(returned, ('Descuento para familias', 60))

    def test_especiales(self):
    	''' Caso de prueba '''
    	returned = descuentos.calcular_descuento(50, 1200, 1)
    	self.assertEqual(returned, ('Descuento especiales', 420))

    def test_no_aplica(self):
    	''' Caso de prueba '''
    	returned = descuentos.calcular_descuento(28, 1100, 1)
    	self.assertEqual(returned, ('No aplica', 0))

    def test_no_aplica1(self):
    	''' Caso de prueba '''
    	returned = descuentos.calcular_descuento(34, 1100, 1)
    	self.assertEqual(returned, ('No aplica', 0))

    def test_mayores_edad_mayor_80(self):
    	''' Caso de prueba '''
    	returned = descuentos.calcular_descuento(80, 1100, 1)
    	self.assertEqual(returned, ('Descuento para mayores de edad', 275))

    def test_mayores_edad_mayor_80_1(self):
    	''' Caso de prueba '''
    	returned = descuentos.calcular_descuento(80, 3000, 1)
    	self.assertEqual(returned, ('Descuento para mayores de edad', 1500))

    def test_mayores_edad_dependientes(self):
    	''' Caso de prueba '''
    	returned = descuentos.calcular_descuento(70, 2000, 0)
    	self.assertEqual(returned, ('Descuento para mayores de edad', 500))

    def test_mayores_edad_dependientes1(self):
    	''' Caso de prueba '''
    	returned = descuentos.calcular_descuento(70, 3000, 0)
    	self.assertEqual(returned, ('Descuento para mayores de edad', 1500))



if __name__ == '__main__':
    unittest.main(testRunner=xmlrunner.XMLTestRunner(output='reporte-pruebas'))
