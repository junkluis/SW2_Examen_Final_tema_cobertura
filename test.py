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



if __name__ == '__main__':
    unittest.main(testRunner=xmlrunner.XMLTestRunner(output='reporte-pruebas'))


