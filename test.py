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

    def test_calcular_descuento_rama_1(self):
        """ caso de prueba 1: Descuento clientes iniciales """
        edad = 19
        valor_cotizado = 501
        dependientes = 1
        mensaje, descuento = descuentos.calcular_descuento(edad, valor_cotizado, dependientes)
        mensaje_esperado = "Descuento clientes iniciales"
        descuento_esperado = valor_cotizado*(0.2)
        self.assertEqual(mensaje, mensaje_esperado)
        self.assertEqual(descuento, descuento_esperado)

    def test_calcular_descuento_rama_2(self):
        """ caso de prueba 2: Descuento para familias con 6 dependientes o mas"""
        edad = 35
        valor_cotizado = 1001
        dependientes = 6
        mensaje, descuento = descuentos.calcular_descuento(edad, valor_cotizado, dependientes)
        mensaje_esperado = "Descuento para familias"
        descuento_esperado = valor_cotizado*(0.1*dependientes)
        self.assertEqual(mensaje, mensaje_esperado)
        self.assertEqual(descuento, descuento_esperado)

    def test_calcular_descuento_rama_3(self):
        """ caso de prueba 3: Descuento para familias con menos de 6 dependientes"""
        edad = 49
        valor_cotizado = 1001
        dependientes = 1
        mensaje, descuento = descuentos.calcular_descuento(edad, valor_cotizado, dependientes)
        mensaje_esperado = "Descuento para familias"
        descuento_esperado = valor_cotizado*(0.05*dependientes)
        self.assertEqual(mensaje, mensaje_esperado)
        self.assertEqual(descuento, descuento_esperado)

    def test_calcular_descuento_rama_4(self):
        """ caso de prueba 4: Descuento especiales """
        edad = 50
        valor_cotizado = 1001
        dependientes = 1
        mensaje, descuento = descuentos.calcular_descuento(edad, valor_cotizado, dependientes)
        mensaje_esperado = "Descuento especiales"
        descuento_esperado = valor_cotizado*(0.35)
        self.assertEqual(mensaje, mensaje_esperado)
        self.assertEqual(descuento, descuento_esperado)

    def test_calcular_descuento_rama_5(self):
        """ caso de prueba 5: No aplica """
        edad = 28
        valor_cotizado = 1001
        dependientes = 1
        mensaje, descuento = descuentos.calcular_descuento(edad, valor_cotizado, dependientes)
        mensaje_esperado = "No aplica"
        descuento_esperado = 0
        self.assertEqual(mensaje, mensaje_esperado)
        self.assertEqual(descuento, descuento_esperado)

    def test_calcular_descuento_rama_6(self):
        """ caso de prueba 6: Descuento para mayores de edad con valor cotizado mayor a 2000 """
        edad = 80
        valor_cotizado = 2001
        dependientes = 1
        mensaje, descuento = descuentos.calcular_descuento(edad, valor_cotizado, dependientes)
        mensaje_esperado = "Descuento para mayores de edad"
        descuento_esperado = valor_cotizado*(0.5)
        self.assertEqual(mensaje, mensaje_esperado)
        self.assertEqual(descuento, descuento_esperado)

    def test_calcular_descuento_rama_7(self):
        """ caso de prueba 7: Descuento para mayores de edad con valor cotizado menor o igual a 2000 """
        edad = 66
        valor_cotizado = 2000
        dependientes = 0
        mensaje, descuento = descuentos.calcular_descuento(edad, valor_cotizado, dependientes)
        mensaje_esperado = "Descuento para mayores de edad"
        descuento_esperado = valor_cotizado*(0.25)
        self.assertEqual(mensaje, mensaje_esperado)
        self.assertEqual(descuento, descuento_esperado)

    def test_calcular_descuento_rama_8(self):
        """ caso de prueba 8: Descuento para clientes  con valor cotizado mayor o igual a 5000 """
        edad = 27
        valor_cotizado = 5000
        dependientes = 1
        mensaje, descuento = descuentos.calcular_descuento(edad, valor_cotizado, dependientes)
        mensaje_esperado = "Descuento para clientes"
        descuento_esperado = valor_cotizado*(0.02)
        self.assertEqual(mensaje, mensaje_esperado)
        self.assertEqual(descuento, descuento_esperado)

    def test_calcular_descuento_rama_9(self):
        """ caso de prueba 9: Descuento para clientes  con valor cotizado menor a 5000 """
        edad = 28
        valor_cotizado = 750
        dependientes = 1
        mensaje, descuento = descuentos.calcular_descuento(edad, valor_cotizado, dependientes)
        mensaje_esperado = "Descuento para clientes"
        descuento_esperado = valor_cotizado*(0.01)
        self.assertEqual(mensaje, mensaje_esperado)
        self.assertEqual(descuento, descuento_esperado)

    def test_calcular_descuento_rama_final(self):
        """ caso de prueba 1: Descuento no valido """
        edad = 18
        valor_cotizado = 500
        dependientes = 0 #cualquier valor mayor a 0 funciona
        mensaje, descuento = descuentos.calcular_descuento(edad, valor_cotizado, dependientes)
        mensaje_esperado = "Descuento no valido"
        descuento_esperado = 0
        self.assertEqual(mensaje,mensaje_esperado)
        self.assertEqual(descuento, descuento_esperado)





if __name__ == '__main__':
    unittest.main(testRunner=xmlrunner.XMLTestRunner(output='reporte-pruebas'))
