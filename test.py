# -*- coding: utf-8 -*-
"""Archivo de pruebas."""
from __future__ import unicode_literals

import unittest
import xmlrunner
import src.descuento as descuentos


class TestDescuentos(unittest.TestCase):
    ''' Pruebas para calculo del descuento para clientes '''

    def test_menor_edad(self):
        ''' Caso de prueba '''
        edad, valor_cotizado, dependientes = 10, 500, 1
        mensaje, descuento = descuentos.calcular_descuento(edad, valor_cotizado, dependientes)
        self.assertEqual(mensaje, 'Descuento no valido')
        self.assertEqual(descuento, 0)

    def test_menos_500(self):
        ''' Caso de prueba '''
        edad, valor_cotizado, dependientes = 19, 400, 1
        mensaje, descuento = descuentos.calcular_descuento(edad, valor_cotizado, dependientes)
        self.assertEqual(mensaje, 'Descuento no valido')
        self.assertEqual(descuento, 0)

    def test_dependientes_negativos(self):
        ''' Caso de prueba '''
        edad, valor_cotizado, dependientes = 19, 600, -1
        mensaje, descuento = descuentos.calcular_descuento(edad, valor_cotizado, dependientes)
        self.assertEqual(mensaje, 'Descuento no valido')
        self.assertEqual(descuento, 0)

    def test_clientes_iniciales(self):
        ''' Caso de prueba '''
        edad, valor_cotizado, dependientes = 19, 600, 1
        mensaje, descuento = descuentos.calcular_descuento(edad, valor_cotizado, dependientes)
        self.assertEqual(mensaje, 'Descuento clientes iniciales')
        self.assertEqual(descuento, valor_cotizado*0.2)

    def test_familias_1(self):
        ''' Caso de prueba '''
        edad, valor_cotizado, dependientes = 35, 1600, 1
        mensaje, descuento = descuentos.calcular_descuento(edad, valor_cotizado, dependientes)
        self.assertEqual(mensaje, 'Descuento para familias')
        self.assertEqual(descuento, valor_cotizado*(0.05*dependientes))

    def test_familias_2(self):
        ''' Caso de prueba '''
        edad, valor_cotizado, dependientes = 28, 1600, 6
        mensaje, descuento = descuentos.calcular_descuento(edad, valor_cotizado, dependientes)
        self.assertEqual(mensaje, 'Descuento para familias')
        self.assertEqual(descuento, valor_cotizado*(0.1*dependientes))

    def test_especiales(self):
        ''' Caso de prueba '''
        edad, valor_cotizado, dependientes = 51, 1600, 1
        mensaje, descuento = descuentos.calcular_descuento(edad, valor_cotizado, dependientes)
        self.assertEqual(mensaje, 'Descuento especiales')
        self.assertEqual(descuento, valor_cotizado*0.35)

    def test_no_aplica(self):
        ''' Caso de prueba '''
        edad, valor_cotizado, dependientes = 28, 1600, 0
        mensaje, descuento = descuentos.calcular_descuento(edad, valor_cotizado, dependientes)
        self.assertEqual(mensaje, 'No aplica')
        self.assertEqual(descuento, 0)

    def test_mayor_edad_1(self):
        ''' Caso de prueba '''
        edad, valor_cotizado, dependientes = 82, 1600, 0
        mensaje, descuento = descuentos.calcular_descuento(edad, valor_cotizado, dependientes)
        self.assertEqual(mensaje, 'Descuento para mayores de edad')
        self.assertEqual(descuento, valor_cotizado*(0.25))

    def test_mayor_edad_2(self):
        ''' Caso de prueba '''
        edad, valor_cotizado, dependientes = 70, 2500, 0
        mensaje, descuento = descuentos.calcular_descuento(edad, valor_cotizado, dependientes)
        self.assertEqual(mensaje, 'Descuento para mayores de edad')
        self.assertEqual(descuento, valor_cotizado*0.5)

    def test_clientes_1(self):
        ''' Caso de prueba '''
        edad, valor_cotizado, dependientes = 27, 6000, 0
        mensaje, descuento = descuentos.calcular_descuento(edad, valor_cotizado, dependientes)
        self.assertEqual(mensaje, 'Descuento para clientes')
        self.assertEqual(descuento, valor_cotizado*0.02)

    def test_clientes_2(self):
        ''' Caso de prueba '''
        edad, valor_cotizado, dependientes = 27, 3000, 0
        mensaje, descuento = descuentos.calcular_descuento(edad, valor_cotizado, dependientes)
        self.assertEqual(mensaje, 'Descuento para clientes')
        self.assertEqual(descuento, valor_cotizado*0.01)


if __name__ == '__main__':
    unittest.main(testRunner=xmlrunner.XMLTestRunner(output='reporte-pruebas'))
