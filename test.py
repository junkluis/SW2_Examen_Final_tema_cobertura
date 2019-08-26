# -*- coding: utf-8 -*-
"""Archivo de pruebas."""
from __future__ import unicode_literals
import unittest
import xmlrunner
#import src.descuento as descuentos
from src.descuento import *


class TestDescuentos(unittest.TestCase):
    ''' Pruebas para calculo del descuento para clientes '''
    

    def test_comprobar_variables(self): 
        mensaje, descuento = calcular_descuento(19,501,0)
        msj_esperado = 'Descuento clientes iniciales'
        self.assertEqual(msj_esperado, mensaje)

    def test_comprobar_variables2(self): 
        mensaje, descuento = calcular_descuento(16,400,0)
        msj_esperado = 'Descuento no valido'
        self.assertEqual(msj_esperado, mensaje)

    def test_comprobar_variables3(self): 
        mensaje, descuento = calcular_descuento(36,2,5)
        msj_esperado = 'Descuento no valido'
        self.assertEqual(msj_esperado, mensaje)

    def test_comprobar_variables4(self): 
        mensaje, descuento = calcular_descuento(52,2,5)
        msj_esperado = 'Descuento no valido'
        self.assertEqual(msj_esperado, mensaje)

    def test_comprobar_variables5(self): 
        mensaje, descuento = calcular_descuento(40,10000,100)
        msj_esperado = 'Descuento para familias'
        descuento_esperado=100000.0
        self.assertEqual(msj_esperado, mensaje)
        self.assertEqual(descuento_esperado,descuento)

    def test_comprobar_variables6(self): 
        mensaje, descuento = calcular_descuento(40,10000,3)
        msj_esperado = 'Descuento para familias'
        descuento_esperado=1500.0000000000002
        self.assertEqual(msj_esperado, mensaje)
        self.assertEqual(descuento_esperado,descuento)

if __name__ == '__main__':
    unittest.main(testRunner=xmlrunner.XMLTestRunner(output='reporte-pruebas'))


