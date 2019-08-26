# -*- coding: utf-8 -*-
"""Archivo de pruebas."""
from __future__ import unicode_literals

import unittest
import xmlrunner
import src.descuento as descuentos



class TestDescuentos(unittest.TestCase):
    ''' Pruebas para calculo del descuento para clientes '''

    def test_mayor_edad(self):
        ''' Caso de prueba '''
        edad = 19
        valor_cotizado = 501
        dependientes = 0
        mjs_esperado = ("Descuento clientes iniciales", 100.2)
        mjs = descuentos.calcular_descuento(edad, valor_cotizado, dependientes)
        self.assertEqual(mjs, mjs_esperado)

    def test_mayor_dependiente_7(self):
        ''' Caso de prueba '''
        edad = 35
        valor_cotizado = 1001
        dependientes = 7
        mjs_esperado = ("Descuento para familias", 700.7)
        mjs = descuentos.calcular_descuento(edad, valor_cotizado, dependientes)
        self.assertEqual(mjs, mjs_esperado)

    def test_mayor_edad_2(self):
        ''' Caso de prueba '''
        edad = 51
        valor_cotizado = 1001
        dependientes = 4
        mjs_esperado = ("Descuento para familias", 200.20000000000002)
        mjs = descuentos.calcular_descuento(edad, valor_cotizado, dependientes)
        self.assertEqual(mjs, mjs_esperado)

    def test_mayor_dependiente_3(self):
        ''' Caso de prueba '''
        edad = 65
        valor_cotizado = 1001
        dependientes = 3
        mjs_esperado = ('Descuento especiales', 350.34999999999997)
        mjs = descuentos.calcular_descuento(edad, valor_cotizado, dependientes)
        self.assertEqual(mjs, mjs_esperado)

    def test_mayor_dependiente_0(self):
        ''' Caso de prueba '''
        edad = 49
        valor_cotizado = 1001
        dependientes = 0
        mjs_esperado = ('No aplica', 0)
        mjs = descuentos.calcular_descuento(edad, valor_cotizado, dependientes)
        self.assertEqual(mjs, mjs_esperado)

    def test_edad_80(self):
        ''' Caso de prueba '''
        edad = 80
        valor_cotizado = 2001
        dependientes = 0
        mjs_esperado = ("Descuento para mayores de edad", 1000.5)
        mjs = descuentos.calcular_descuento(edad, valor_cotizado, dependientes)
        self.assertEqual(mjs, mjs_esperado)

    def test_edad_80_dependiente_0(self):
        ''' Caso de prueba '''
        edad = 80
        valor_cotizado = 1001
        dependientes = 0
        mjs_esperado = ("Descuento para mayores de edad", 250.25)
        mjs = descuentos.calcular_descuento(edad, valor_cotizado, dependientes)
        self.assertEqual(mjs, mjs_esperado)

    def test_edad_69_dependiente_1(self):
        ''' Caso de prueba '''
        edad = 69
        valor_cotizado = 5000
        dependientes = 1
        mjs_esperado = ("Descuento para clientes", 100.0)
        mjs = descuentos.calcular_descuento(edad, valor_cotizado, dependientes)
        self.assertEqual(mjs, mjs_esperado)

    def test_edad_69_dependiente_1_valor_4000(self):
        ''' Caso de prueba '''
        edad = 69
        valor_cotizado = 4001
        dependientes = 1
        mjs_esperado = ("Descuento para clientes", 40.01)
        mjs = descuentos.calcular_descuento(edad, valor_cotizado, dependientes)
        self.assertEqual(mjs, mjs_esperado)

    def test_menor_edad(self):
        ''' Caso de prueba '''
        edad = 17
        valor_cotizado = 4001
        dependientes = 1
        mjs_esperado = ("Descuento no valido", 0)
        mjs = descuentos.calcular_descuento(edad, valor_cotizado, dependientes)
        self.assertEqual(mjs, mjs_esperado)



if __name__ == '__main__':
    unittest.main(testRunner=xmlrunner.XMLTestRunner(output='reporte-pruebas'))
