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

    def test_primer_caso(self):
        '''Primer caso'''
        mensaje, descuento = descuentos.calcular_descuento(17, 1000, 0)
        self.assertEqual('Descuento no valido', mensaje)
        self.assertEqual(0, descuento)

    def test_sexto_caso(self):
        '''Sexto caso'''
        mensaje, descuento = descuentos.calcular_descuento(19, 5000, 1)
        self.assertEqual('Descuento clientes iniciales', mensaje)
        self.assertEqual(1000, descuento)

    def test_cuarto_caso(self):
        '''Caso cuatro'''
        mensaje, descuento = descuentos.calcular_descuento(30, 4000, 2)
        self.assertEqual('No aplica', mensaje)
        self.assertEqual(0, descuento)

    def test_segundo_caso_a(self):
        '''Caso dos a'''
        mensaje, descuento = descuentos.calcular_descuento(40, 4000, 2)
        self.assertEqual('Descuento para familias', mensaje)
        self.assertEqual(400.0, descuento)

    def test_caso_dos_c(self):
        '''Caso dos c'''
        mensaje, descuento = descuentos.calcular_descuento(40, 4000, 6)
        self.assertEqual('Descuento para familias', mensaje)
        self.assertEqual(2400.0000000000005, descuento)

    def test_caso_tres(self):
        '''Caso tres'''
        mensaje, descuento = descuentos.calcular_descuento(60, 4000, 1)
        self.assertEqual('Descuento especiales', mensaje)
        self.assertEqual(1400.0, descuento)

    def test_caso_cinco_a(self):
        '''Caso 5 a '''
        mensaje, descuento = descuentos.calcular_descuento(80, 3000, 1)
        self.assertEqual('Descuento para mayores de edad', mensaje)
        self.assertEqual(1500.0, descuento)

       
    def test_caso_cinco_b(self):
        '''Caso 5 b'''
        mensaje, descuento = descuentos.calcular_descuento(68, 3000, 0)
        self.assertEqual('Descuento para mayores de edad', mensaje)
        self.assertEqual(1500, descuento)

    def test_caso_seis_a(self):
        '''Caso 6 a'''
        mensaje, descuento = descuentos.calcular_descuento(68, 2000, 1)
        self.assertEqual('Descuento para clientes', mensaje)
        self.assertEqual(20, descuento)

    def test_caso_seis_b(self):
        '''Caso 6 b'''
        mensaje, descuento = descuentos.calcular_descuento(68, 8000, 1)
        self.assertEqual('Descuento para clientes', mensaje)
        self.assertEqual(160.0, descuento)




if __name__ == '__main__':
    unittest.main(testRunner=xmlrunner.XMLTestRunner(output='reporte-pruebas'))
