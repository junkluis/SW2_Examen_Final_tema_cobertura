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

    def descuento_inicial(self):
        mensajeesperado = "Descuento clientes iniciales"
        descuentoesperado = 800*0.2
        mensaje, descuento = descuentos.calcular_descuento(20,800,2)
        self.assertEqual(mensajeesperado, mensaje)
        self.assertEqual(descuentoesperado, descuento)



if __name__ == '__main__':
    unittest.main(testRunner=xmlrunner.XMLTestRunner(output='reporte-pruebas'))
