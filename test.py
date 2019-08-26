# -*- coding: utf-8 -*-
"""Archivo de pruebas."""
from __future__ import unicode_literals

import unittest
import xmlrunner
import src.descuento as descuentos



class TestDescuentos(unittest.TestCase):
    ''' Pruebas para calculo del descuento para clientes '''

    def test_descuento_valido(self):
        ''' Caso de prueba '''

        msj, desc = descuentos.calcular_descuento(19, 800, 1)
        self.assertEqual('Descuento clientes iniciales', msj)
        self.assertEqual(800*0.2, desc)
    
    def test_descuento_invalido(self):
        ''' Caso de prueba invalido'''

        msj, desc = descuentos.calcular_descuento(11,0,0)
        self.assertEqual('Descuento no valido',msj)
        self.assertEqual(0,0)
    
    def test_descuento_clientes_bajo(self):
        ''' Caso de prueba '''
        msj, desc = descuentos.calcular_descuento(29, 749, 1)
        self.assertEqual('Descuento para clientes', msj)
        self.assertEqual(749*0.01, desc)
    
    def test_descuento_clientes_alto(self):
        ''' Caso de prueba '''
        msj, desc = descuentos.calcular_descuento(66, 5001, 1)
        self.assertEqual('Descuento para clientes', msj)
        self.assertEqual(5001*0.02, desc)
    
    def test_descuento_familias1(self):
        ''' Caso de prueba '''
        msj, desc = descuentos.calcular_descuento(36, 5001, 1)
        self.assertEqual('Descuento para familias', msj)
        self.assertEqual(5001*(0.05*1), desc)

    def test_descuento_familias2(self):
        ''' Caso de prueba '''
        msj, desc = descuentos.calcular_descuento(36, 5001, 7)
        self.assertEqual('Descuento para familias', msj)
        self.assertEqual(5001*(0.1*7), desc)
    
    def test_descuento_especial(self):
        ''' Caso de prueba '''
        msj, desc = descuentos.calcular_descuento(55, 5001, 1)
        self.assertEqual('Descuento especiales', msj)
        self.assertEqual(5001*0.35, desc)

    def test_descuento_noaplica(self):
        ''' Caso de prueba '''
        msj, desc = descuentos.calcular_descuento(40, 5001, 0)
        self.assertEqual('No aplica', msj)
        self.assertEqual(0, desc)

    def test_descuento_mayores_edad1(self):
        ''' Caso de prueba '''
        msj, desc = descuentos.calcular_descuento(90, 5001, 1)
        self.assertEqual('Descuento para mayores de edad', msj)
        self.assertEqual(5001*0.5, desc)

    def test_descuento_mayores_edad2(self):
        ''' Caso de prueba '''
        msj, desc = descuentos.calcular_descuento(90, 1002, 1)
        self.assertEqual('Descuento para mayores de edad', msj)
        self.assertEqual(1002*0.25, desc)


if __name__ == '__main__':
    unittest.main(testRunner=xmlrunner.XMLTestRunner(output='reporte-pruebas'))
