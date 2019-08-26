# -*- coding: utf-8 -*-
"""Archivo de pruebas."""
from __future__ import unicode_literals

import unittest
import xmlrunner
import src.descuento as descuentos

'''
caso 1, entre 18 y 27 mayor a 500
'''

class TestDescuentos(unittest.TestCase):
    ''' Pruebas para calculo del descuento para clientes '''

    def test_descuento1(self):
        edad =20
        valor_cotizado = 600
        dependientes = 0
        mensaje_obtenido, descuento_obtenido=descuentos.calcular_descuento(edad, valor_cotizado, dependientes)
        mensaje_esperado= "Descuento clientes iniciales"
        descuento_esperado = valor_cotizado*0.2
        self.assertEqual([mensaje_obtenido,descuento_obtenido],[mensaje_esperado,descuento_esperado])

    def test_descuento2(self):
        edad =35
        valor_cotizado = 800
        dependientes = 0
        mensaje_obtenido, descuento_obtenido=descuentos.calcular_descuento(edad, valor_cotizado, dependientes)
        mensaje_esperado= "Descuento clientes iniciales"
        descuento_esperado = valor_cotizado*0.2
        self.assertEqual([mensaje_obtenido,descuento_obtenido],[mensaje_esperado,descuento_esperado])

    def test_descuento_familias1(self):
        edad =35
        valor_cotizado = 1200
        dependientes = 1
        mensaje_obtenido, descuento_obtenido=descuentos.calcular_descuento(edad, valor_cotizado, dependientes)
        mensaje_esperado= "Descuento para familias"
        descuento_esperado = valor_cotizado*0.05*dependientes
        self.assertEqual([mensaje_obtenido,descuento_obtenido],[mensaje_esperado,descuento_esperado])

    def test_descuento_familias2(self):
        edad =35
        valor_cotizado = 1200
        dependientes = 6
        mensaje_obtenido, descuento_obtenido=descuentos.calcular_descuento(edad, valor_cotizado, dependientes)
        mensaje_esperado= "Descuento para familias"
        #720.0000001
        #descuento_esperado = valor_cotizado*0.1*dependientes
        descuento_esperado = 720.0000000000001
        self.assertEqual([mensaje_obtenido,descuento_obtenido],[mensaje_esperado,descuento_esperado])

    def test_descuento_especiales(self):
        edad =50
        valor_cotizado = 1200
        dependientes = 1
        mensaje_obtenido, descuento_obtenido=descuentos.calcular_descuento(edad, valor_cotizado, dependientes)
        mensaje_esperado= "Descuento especiales"
        descuento_esperado = valor_cotizado*0.35
        self.assertEqual([mensaje_obtenido,descuento_obtenido],[mensaje_esperado,descuento_esperado])

    def test_descuento_no_aplica(self):
        edad =45
        valor_cotizado = 1200
        dependientes = 0
        mensaje_obtenido, descuento_obtenido=descuentos.calcular_descuento(edad, valor_cotizado, dependientes)
        mensaje_esperado= "No aplica"
        descuento_esperado = valor_cotizado*0
        self.assertEqual([mensaje_obtenido,descuento_obtenido],[mensaje_esperado,descuento_esperado])

    def test_descuento_mayores_edad1(self):
        edad =75
        valor_cotizado = 2500
        dependientes = 0
        mensaje_obtenido, descuento_obtenido=descuentos.calcular_descuento(edad, valor_cotizado, dependientes)
        mensaje_esperado= "Descuento para mayores de edad"
        descuento_esperado = valor_cotizado*0.5
        self.assertEqual([mensaje_obtenido,descuento_obtenido],[mensaje_esperado,descuento_esperado])

    def test_descuento_mayores_edad2(self):
        edad =80
        valor_cotizado = 1800
        dependientes = 0
        mensaje_obtenido, descuento_obtenido=descuentos.calcular_descuento(edad, valor_cotizado, dependientes)
        mensaje_esperado= "Descuento para mayores de edad"
        descuento_esperado = valor_cotizado*0.25
        self.assertEqual([mensaje_obtenido,descuento_obtenido],[mensaje_esperado,descuento_esperado])

    def test_descuento_clientes1(self):
        edad =70
        valor_cotizado = 6000
        dependientes = 1
        mensaje_obtenido, descuento_obtenido=descuentos.calcular_descuento(edad, valor_cotizado, dependientes)
        mensaje_esperado= "Descuento para clientes"
        descuento_esperado = valor_cotizado*0.02
        self.assertEqual([mensaje_obtenido,descuento_obtenido],[mensaje_esperado,descuento_esperado])

    def test_descuento_clientes1(self):
        edad =70
        valor_cotizado = 4000
        dependientes = 1
        mensaje_obtenido, descuento_obtenido=descuentos.calcular_descuento(edad, valor_cotizado, dependientes)
        mensaje_esperado= "Descuento para clientes"
        descuento_esperado = valor_cotizado*0.01
        self.assertEqual([mensaje_obtenido,descuento_obtenido],[mensaje_esperado,descuento_esperado])

    def test_descuento_no_valido1(self):
        edad =18
        valor_cotizado = 600
        dependientes = 0
        mensaje_obtenido, descuento_obtenido=descuentos.calcular_descuento(edad, valor_cotizado, dependientes)
        mensaje_esperado= "Descuento no valido"
        descuento_esperado = valor_cotizado*0
        self.assertEqual([mensaje_obtenido,descuento_obtenido],[mensaje_esperado,descuento_esperado])

    def test_descuento_no_valido2(self):
        edad =35
        valor_cotizado = 400
        dependientes = 0
        mensaje_obtenido, descuento_obtenido=descuentos.calcular_descuento(edad, valor_cotizado, dependientes)
        mensaje_esperado= "Descuento no valido"
        descuento_esperado = valor_cotizado*0
        self.assertEqual([mensaje_obtenido,descuento_obtenido],[mensaje_esperado,descuento_esperado])

    def test_descuento_no_valido3(self):
        edad =35
        valor_cotizado = 400
        dependientes = -1
        mensaje_obtenido, descuento_obtenido=descuentos.calcular_descuento(edad, valor_cotizado, dependientes)
        mensaje_esperado= "Descuento no valido"
        descuento_esperado = valor_cotizado*0
        self.assertEqual([mensaje_obtenido,descuento_obtenido],[mensaje_esperado,descuento_esperado])

if __name__ == '__main__':
    unittest.main(testRunner=xmlrunner.XMLTestRunner(output='reporte-pruebas'))
