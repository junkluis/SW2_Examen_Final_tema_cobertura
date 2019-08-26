# -*- coding: utf-8 -*-
"""Archivo de pruebas."""
from __future__ import unicode_literals

import unittest
import xmlrunner
import src.descuento as descuentos



class TestDescuentos(unittest.TestCase):
    ''' Pruebas para calculo del descuento para clientes '''

    def primer_caso(self):
        ''' Caso de prueba sd'''
        mensaje_esperado= "Descuento no valido"
        descuento_esperado = 0
        mensaje, descuento= descuentos.calcular_descuento(17,400,0)
       
        self.assertEqual(mensaje,"Descuento no valido")
        self.assertEqual(descuento_esperado,descuento)

    def segundo_caso(self):
        ''' Caso de prueba sd'''
        mensaje_esperado= "Descuento clientes iniciales"
        descuento_esperado = 120
        mensaje,descuento= descuentos.calcular_descuento(19,600,1)
       
        self.assertEqual(mensaje_esperado,mensaje)
        self.assertEqual(descuento_esperado,descuento)

    def segundo_caso_a(self):
        ''' Caso de prueba sd'''
        mensaje_esperado= "Descuento para familias"
        descuento_esperado = 120
        mensaje,descuento= descuentos.calcular_descuento(40,1200,8)
       
        self.assertEqual(mensaje_esperado,mensaje)
        self.assertEqual(descuento_esperado,descuento)

    def segundo_caso_b(self):
        ''' Caso de prueba sd'''
        mensaje_esperado= "Descuento para familias"
        descuento_esperado = 60
        mensaje,descuento= descuentos.calcular_descuento(40,1200,4)
       
        self.assertEqual(mensaje_esperado,mensaje)
        self.assertEqual(descuento_esperado,descuento)
        

    def tercer_caso(self):
        ''' Caso de prueba sd'''
        mensaje_esperado= "Descuento especiales"
        descuento_esperado = 420
        mensaje,descuento= descuentos.calcular_descuento(60,1200,2)
       
        self.assertEqual(mensaje_esperado,mensaje)
        self.assertEqual(descuento_esperado,descuento)

    def cuarto_caso(self):
        ''' Caso de prueba sd'''
        mensaje_esperado= "No aplica"
        descuento_esperado = 0
        mensaje,descuento= descuentos.calcular_descuento(30,1200,2)
       
        self.assertEqual(mensaje_esperado,mensaje)
        self.assertEqual(descuento_esperado,descuento)




if __name__ == '__main__':
    unittest.main(testRunner=xmlrunner.XMLTestRunner(output='reporte-pruebas'))
