# -*- coding: utf-8 -*-
"""Archivo de pruebas."""
from __future__ import unicode_literals

import unittest
import xmlrunner
import src.descuento as descuentos



class TestDescuentos(unittest.TestCase):
    ''' Pruebas para calculo del descuento para clientes '''

    def test_descuento_clientes_iniciales(self):
        mensajeesperado = "Descuento clientes iniciales"
        descuentoesperado = 800*0.2
        mensaje, descuento = descuentos.calcular_descuento(20,800,2)
        self.assertEqual(descuentoesperado, descuento)
        self.assertEqual(mensajeesperado, mensaje)

    def test_descuento_para_familias_con_5_dependientes(self):
        mensajeesperado = "Descuento para familias"
        descuentoesperado = 1100*0.05*5
        mensaje, descuento = descuentos.calcular_descuento(37,1100,5)
        self.assertEqual(descuentoesperado, descuento)
        self.assertEqual(mensajeesperado, mensaje)

    def test_descuento_para_familias_con_6_dependientes(self):
        mensajeesperado = "Descuento para familias"
        descuentoesperado = 1100*(0.1*6)
        mensaje, descuento = descuentos.calcular_descuento(37,1100,6)
        self.assertEqual(descuentoesperado, descuento)
        self.assertEqual(mensajeesperado, mensaje)

    def test_descuento_especial(self):
        mensajeesperado = "Descuento especiales"
        descuentoesperado = 1100 * (0.35)
        mensaje, descuento = descuentos.calcular_descuento(50, 1100, 2)
        self.assertEqual(descuentoesperado, descuento)
        self.assertEqual(mensajeesperado, mensaje)

    def test_no_tiene_descuento(self):
        mensajeesperado = "No aplica"
        descuentoesperado = 0
        mensaje, descuento = descuentos.calcular_descuento(32, 1100, 0)
        self.assertEqual(descuentoesperado, descuento)
        self.assertEqual(mensajeesperado, mensaje)

    def test_descuento_mayores_edad_valor_2100(self):
        mensajeesperado = "Descuento para mayores de edad"
        descuentoesperado = 2100*0.5
        mensaje, descuento = descuentos.calcular_descuento(80, 2100, 0)
        self.assertEqual(descuentoesperado, descuento)
        self.assertEqual(mensajeesperado, mensaje)

    def test_descuento_mayores_edad_valor_1900(self):
        mensajeesperado = "Descuento para mayores de edad"
        descuentoesperado = 1900*0.25
        mensaje, descuento = descuentos.calcular_descuento(70, 1900, 0)
        self.assertEqual(descuentoesperado, descuento)
        self.assertEqual(mensajeesperado, mensaje)

    def test_descuento_para_clientes_menor_5000(self):
        mensajeesperado = "Descuento para clientes"
        descuentoesperado = 600*(0.01)
        mensaje, descuento = descuentos.calcular_descuento(30, 600, 0)
        self.assertEqual(descuentoesperado, descuento)
        self.assertEqual(mensajeesperado, mensaje)

    def test_descuento_para_clientes_igual_5000(self):
        mensajeesperado = "Descuento para clientes"
        descuentoesperado = 5000*(0.02)
        mensaje, descuento = descuentos.calcular_descuento(70, 5000, 1)
        self.assertEqual(descuentoesperado, descuento)
        self.assertEqual(mensajeesperado, mensaje)

    def test_descuento_no_valido(self):
        mensajeesperado = "Descuento no valido"
        descuentoesperado = 0
        mensaje, descuento = descuentos.calcular_descuento(18, 1000, 1)
        self.assertEqual(descuentoesperado, descuento)
        self.assertEqual(mensajeesperado, mensaje)




if __name__ == '__main__':
    unittest.main(testRunner=xmlrunner.XMLTestRunner(output='reporte-pruebas'))
