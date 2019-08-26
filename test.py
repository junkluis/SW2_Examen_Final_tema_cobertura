# -*- coding: utf-8 -*-
"""Archivo de pruebas."""
from __future__ import unicode_literals

import unittest
import xmlrunner
import src.descuento as descuentos



class TestDescuentos(unittest.TestCase):
    ''' Pruebas para calculo del descuento para clientes '''

    def prueba_edad_invalida(self):
        '''Prueba en caso de edad inválida'''
        edad = 15
        valor_cotizado = 600
        dependientes = 0
        retorno = descuentos.calcular_descuento(edad, valor_cotizado, dependientes)
        self.assertEqual(("Descuento no valido", 0), retorno)

    def prueba_valor_invalido(self):
        '''Prueba en caso de valor inválido'''
        edad = 19
        valor_cotizado = 400
        dependientes = 0
        retorno = descuentos.calcular_descuento(edad, valor_cotizado, dependientes)
        self.assertEqual(("Descuento no valido", 0), retorno)

    def pruena_dependientes_invalidos(self):
        '''Prueba en caso de dependientes inválidos'''
        edad = 19
        valor_cotizado = 600
        dependientes = -1
        retorno = descuentos.calcular_descuento(edad, valor_cotizado, dependientes)
        self.assertEqual(("Descuento no valido", 0), retorno)

if __name__ == '__main__':
    unittest.main(testRunner=xmlrunner.XMLTestRunner(output='reporte-pruebas'))
