# -*- coding: utf-8 -*-
"""Archivo de pruebas."""
from __future__ import unicode_literals

import unittest
import xmlrunner
import src.descuento as descuentos



class TestDescuentos(unittest.TestCase):
    ''' Pruebas para calculo del descuento para clientes '''

    def test_edad_invalida(self):
        '''Prueba en caso de edad inválida'''
        edad = 15
        valor_cotizado = 600
        dependientes = 0
        retorno = descuentos.calcular_descuento(edad, valor_cotizado, dependientes)
        print(retorno)
        self.assertEqual(("Descuento no valido", 0), retorno)

    def test_valor_invalido(self):
        '''Prueba en caso de valor inválido'''
        edad = 19
        valor_cotizado = 400
        dependientes = 0
        retorno = descuentos.calcular_descuento(edad, valor_cotizado, dependientes)
        print(retorno)
        self.assertEqual(("Descuento no valido", 0), retorno)

    def test_dependientes_invalidos(self):
        '''Prueba en caso de dependientes inválidos'''
        edad = 19
        valor_cotizado = 600
        dependientes = -1
        retorno = descuentos.calcular_descuento(edad, valor_cotizado, dependientes)
        print(retorno)
        self.assertEqual(("Descuento no valido", 0), retorno)

    def test_validos_uno_uno(self):
        '''Prueba en caso de dependientes inválidos'''
        edad = 19
        valor_cotizado = 600
        dependientes = 0
        retorno = descuentos.calcular_descuento(edad, valor_cotizado, dependientes)
        print(retorno)
        self.assertEqual(("Descuento clientes iniciales", valor_cotizado*(0.2)), retorno)

    def test_validos_uno_dos(self):
        '''Prueba en caso de dependientes inválidos'''
        edad = 28
        valor_cotizado = 780
        dependientes = 0
        retorno = descuentos.calcular_descuento(edad, valor_cotizado, dependientes)
        print(retorno)
        self.assertEqual(("Descuento clientes iniciales", valor_cotizado*(0.2)), retorno)

    def test_validos_dos_uno_dos(self):
        '''Prueba en caso de dependientes inválidos'''
        edad = 35
        valor_cotizado = 1200
        dependientes = 1
        retorno = descuentos.calcular_descuento(edad, valor_cotizado, dependientes)
        print(retorno)
        self.assertEqual(("Descuento para familias", valor_cotizado*(0.05*dependientes)), retorno)

    def test_validos_dos_uno_uno(self):
        '''Prueba en caso de dependientes inválidos'''
        edad = 55
        valor_cotizado = 1200
        dependientes = 8
        retorno = descuentos.calcular_descuento(edad, valor_cotizado, dependientes)
        print(retorno)
        self.assertEqual(("Descuento para familias", valor_cotizado*(0.1*dependientes)), retorno)

    def test_validos_dos_dos(self):
        '''Prueba en caso de dependientes inválidos'''
        edad = 55
        valor_cotizado = 1200
        dependientes = 3
        retorno = descuentos.calcular_descuento(edad, valor_cotizado, dependientes)
        print(retorno)
        self.assertEqual(("Descuento especiales", valor_cotizado*(0.35)), retorno)

    def test_validos_dos_tres(self):
        '''Prueba en caso de dependientes inválidos'''
        edad = 28
        valor_cotizado = 1200
        dependientes = 3
        retorno = descuentos.calcular_descuento(edad, valor_cotizado, dependientes)
        print(retorno)
        self.assertEqual(("No aplica", 0), retorno)

    def test_validos_tres_uno_uno(self):
        '''Prueba en caso de dependientes inválidos'''
        edad = 80
        valor_cotizado = 2001
        dependientes = 3
        retorno = descuentos.calcular_descuento(edad, valor_cotizado, dependientes)
        print(retorno)
        self.assertEqual(("Descuento para mayores de edad", valor_cotizado*(0.5)), retorno)

    def test_validos_tres_dos_dos(self):
        '''Prueba en caso de dependientes inválidos'''
        edad = 66
        valor_cotizado = 1999
        dependientes = 0
        retorno = descuentos.calcular_descuento(edad, valor_cotizado, dependientes)
        print(retorno)
        self.assertEqual(("Descuento para mayores de edad", valor_cotizado*(0.25)), retorno)

    def test_validos_cuatro_uno(self):
        '''Prueba en caso de dependientes inválidos'''
        edad = 70
        valor_cotizado = 5001
        dependientes = 1
        retorno = descuentos.calcular_descuento(edad, valor_cotizado, dependientes)
        print(retorno)
        self.assertEqual(( "Descuento para clientes", valor_cotizado*(0.02)), retorno)

    def test_validos_cuatro_dos(self):
        '''Prueba en caso de dependientes inválidos'''
        edad = 70
        valor_cotizado = 4999
        dependientes = 1
        retorno = descuentos.calcular_descuento(edad, valor_cotizado, dependientes)
        print(retorno)
        self.assertEqual(( "Descuento para clientes", valor_cotizado*(0.01)), retorno)

if __name__ == '__main__':
    unittest.main(testRunner=xmlrunner.XMLTestRunner(output='reporte-pruebas'))
