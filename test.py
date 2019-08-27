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

    def test_descuento_no_valido(self):
        mensaje,descuento=descuentos.calcular_descuento(5, 100, 2)
        self.assertEqual('Descuento no valido',mensaje)
        
    def test_descuento_cliente_inicial(self):
        mensaje,descuento=descuentos.calcular_descuento(20, 800, 2)
        self.assertEqual("Descuento clientes iniciales",mensaje)

    def test_descuento_familia_pequena(self):
        mensaje,descuento=descuentos.calcular_descuento(45, 1100, 4)
        self.assertEqual(220,descuento)
    '''
    def test_descuento_familia_grande(self):
        mensaje,descuento=descuentos.calcular_descuento(45, 1100, 6)
        self.assertEqual(660,descuento)
    
    
    def test_descuento_especial(self):
        mensaje,descuento=descuentos.calcular_descuento(60, 1000, 6)
        self.assertEqual(350,descuento)
    '''
    
    def test_descuento_mayores_cotizado_bajo(self):
        mensaje,descuento=descuentos.calcular_descuento(85, 1000, 6)
        self.assertEqual(250,descuento)

    def test_descuento_mayores_cotizado_alto(self):
        mensaje,descuento=descuentos.calcular_descuento(85, 2500, 6)
        self.assertEqual(1250,descuento)

    def test_descuento_cliente_cotizado_bajo(self):
        mensaje,descuento=descuentos.calcular_descuento(70, 1000, 6)
        self.assertEqual(10,descuento)

    def test_descuento_cliente_cotizado_alto(self):
        mensaje,descuento=descuentos.calcular_descuento(70, 6000, 6)
        self.assertEqual(120,descuento)

if __name__ == '__main__':
    unittest.main(testRunner=xmlrunner.XMLTestRunner(output='reporte-pruebas'))
