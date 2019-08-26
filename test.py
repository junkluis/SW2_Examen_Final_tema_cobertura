# -*- coding: utf-8 -*-
"""Archivo de pruebas."""
from __future__ import unicode_literals

import unittest
import xmlrunner
import src.descuento as descuentos


class TestDescuentos(unittest.TestCase):
    ''' Pruebas para calculo del descuento para clientes '''

    def test_descuento_no_valido(self):
        ''' Descuento no valido '''
        edad = 19
        valor = 499
        dependientes = 1
        msj, desc = descuentos.calcular_descuento(edad, valor, dependientes)

        self.assertEqual("Descuento no valido", msj)
        self.assertEqual(0, desc)

    def test_descuento_clientes_iniciales_por_edad(self):
        ''' Descuento para clientes iniciales por edad '''
        edad = 19
        valor = 751
        dependientes = 0
        msj, desc = descuentos.calcular_descuento(edad, valor, dependientes)

        self.assertEqual("Descuento clientes iniciales", msj)
        self.assertEqual(valor * 0.2, desc)

    def test_descuento_clientes_iniciales_por_valor(self):
        ''' Descuento para clientes iniciales por valor '''
        edad = 28
        valor = 999
        dependientes = 0
        msj, desc = descuentos.calcular_descuento(edad, valor, dependientes)

        self.assertEqual("Descuento clientes iniciales", msj)
        self.assertEqual(valor * 0.2, desc)

    def test_descuento_familias_pocos_dependientes(self):
        ''' Descuento para familias con < 4 dependients '''
        edad = 35
        valor = 1001
        dependientes = 1
        msj, desc = descuentos.calcular_descuento(edad, valor, dependientes)

        self.assertEqual("Descuento para familias", msj)
        self.assertEqual(valor * (0.05 * dependientes), desc)

    def test_descuento_familias_muchos_dependientes(self):
        ''' Descuento para familias con >= 6 dependients '''
        edad = 65
        valor = 2000
        dependientes = 7
        msj, desc = descuentos.calcular_descuento(edad, valor, dependientes)

        self.assertEqual("Descuento para familias", msj)
        self.assertEqual(float(1400.0000000000002), float(desc))

    def test_descuento_especial(self):
        ''' Descuentos especiales'''
        edad = 65
        valor = 2000
        dependientes = 0
        msj, desc = descuentos.calcular_descuento(edad, valor, dependientes)

        self.assertEqual("Descuento especiales", msj)
        self.assertEqual(valor * 0.35, desc)

    def test_descuento_no_aplica(self):
        ''' Descuento no valido'''
        edad = 38
        valor = 2000
        dependientes = 0
        msj, desc = descuentos.calcular_descuento(edad, valor, dependientes)

        self.assertEqual("No aplica", msj)
        self.assertEqual(0, desc)

    def test_descuento_mayores_de_edad_mayor_valor(self):
        ''' Descuento para mayores de edad con cotizacion > 2000'''
        edad = 66
        valor = 2001
        dependientes = 0
        msj, desc = descuentos.calcular_descuento(edad, valor, dependientes)

        self.assertEqual("Descuento para mayores de edad", msj)
        self.assertEqual(valor * 0.5, desc)

    def test_descuento_mayores_de_edad_menor_valor(self):
        ''' Descuento para mayores de edad con cotizacion <= 2000'''
        edad = 66
        valor = 2000
        dependientes = 0
        msj, desc = descuentos.calcular_descuento(edad, valor, dependientes)

        self.assertEqual("Descuento para mayores de edad", msj)
        self.assertEqual(valor * 0.25, desc)

    def test_descuento_clientes_mayor_valor(self):
        ''' Descuento para clientes con valor cotizado >= 5000'''
        edad = 66
        valor = 5000
        dependientes = 1
        msj, desc = descuentos.calcular_descuento(edad, valor, dependientes)

        self.assertEqual("Descuento para clientes", msj)
        self.assertEqual(valor * 0.02, desc)

    def test_descuento_clientes_menor_valor(self):
        ''' Descuento para clientes con valor cotizado < 5000'''
        edad = 66
        valor = 4999
        dependientes = 1
        msj, desc = descuentos.calcular_descuento(edad, valor, dependientes)

        self.assertEqual("Descuento para clientes", msj)
        self.assertEqual(valor * 0.01, desc)


if __name__ == '__main__':
    unittest.main(testRunner=xmlrunner.XMLTestRunner(output='reporte-pruebas'))
