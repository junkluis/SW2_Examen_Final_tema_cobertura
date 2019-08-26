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

    def test_edad_invalida(self):
        '''Prueba en caso de edad inválida'''
        edad = 15
        valor_cotizado = 500
        dependientes = 2
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

    def test_valido_cliente_inicial(self):
        '''Prueba en caso de dependientes inválidos'''
        edad = 22
        valor_cotizado = 600
        dependientes = 0
        retorno = descuentos.calcular_descuento(edad, valor_cotizado, dependientes)
        print(retorno)
        self.assertEqual(("Descuento clientes iniciales", valor_cotizado*(0.2)), retorno)

    def test_valido_cliente_incial_dos(self):
        '''Prueba en caso de dependientes inválidos'''
        edad = 20
        valor_cotizado = 800
        dependientes = 0
        retorno = descuentos.calcular_descuento(edad, valor_cotizado, dependientes)
        print(retorno)
        self.assertEqual(("Descuento clientes iniciales", valor_cotizado*(0.2)), retorno)

    def test_valido_familias(self):
        '''Prueba en caso de dependientes inválidos'''
        edad = 40
        valor_cotizado = 1100
        dependientes = 1
        retorno = descuentos.calcular_descuento(edad, valor_cotizado, dependientes)
        print(retorno)
        self.assertEqual(("Descuento para familias", valor_cotizado*(0.05*dependientes)), retorno)

    def test_valido_familia_dos(self):
        '''Prueba en caso de dependientes inválidos'''
        edad = 58
        valor_cotizado = 1100
        dependientes = 8
        retorno = descuentos.calcular_descuento(edad, valor_cotizado, dependientes)
        print(retorno)
        self.assertEqual(("Descuento para familias", valor_cotizado*(0.1*dependientes)), retorno)

    def test_valido_especiales(self):
        '''Prueba en caso de dependientes inválidos'''
        edad = 58
        valor_cotizado = 1100
        dependientes = 3
        retorno = descuentos.calcular_descuento(edad, valor_cotizado, dependientes)
        print(retorno)
        self.assertEqual(("Descuento especiales", valor_cotizado*(0.35)), retorno)

    def test_valido_no_aplica(self):
        '''Prueba en caso de dependientes inválidos'''
        edad = 31
        valor_cotizado = 1100
        dependientes = 3
        retorno = descuentos.calcular_descuento(edad, valor_cotizado, dependientes)
        print(retorno)
        self.assertEqual(("No aplica", 0), retorno)

    def test_valido_mayores_edad(self):
        '''Prueba en caso de dependientes inválidos'''
        edad = 85
        valor_cotizado = 2010
        dependientes = 3
        retorno = descuentos.calcular_descuento(edad, valor_cotizado, dependientes)
        print(retorno)
        self.assertEqual(("Descuento para mayores de edad", valor_cotizado*(0.5)), retorno)

    def test_valido_mayores_edad_dos(self):
        '''Prueba en caso de dependientes inválidos'''
        edad = 70
        valor_cotizado = 1990
        dependientes = 0
        retorno = descuentos.calcular_descuento(edad, valor_cotizado, dependientes)
        print(retorno)
        self.assertEqual(("Descuento para mayores de edad", valor_cotizado*(0.25)), retorno)

    def test_valido_descuento_clientes(self):
        '''Prueba en caso de dependientes inválidos'''
        edad = 70
        valor_cotizado = 5010
        dependientes = 1
        retorno = descuentos.calcular_descuento(edad, valor_cotizado, dependientes)
        print(retorno)
        self.assertEqual(("Descuento para clientes", valor_cotizado*(0.02)), retorno)

    def test_valido_descuento_clientes_dos(self):
        '''Prueba en caso de dependientes inválidos'''
        edad = 70
        valor_cotizado = 4990
        dependientes = 1
        retorno = descuentos.calcular_descuento(edad, valor_cotizado, dependientes)
        print(retorno)
        self.assertEqual(("Descuento para clientes", valor_cotizado*(0.01)), retorno)

if __name__ == '__main__':
    unittest.main(testRunner=xmlrunner.XMLTestRunner(output='reporte-pruebas'))
