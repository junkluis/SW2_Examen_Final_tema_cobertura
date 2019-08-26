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

    def test_calcular_descuento_1_1(self):
        """
        condicional edad entre 18 y 27 y valor entre 750 y 1000 verdadera
        """
        mensaje, descuento = descuentos.calcular_descuento(20, 800, 1)
        self.assertEqual(mensaje, "Descuento clientes iniciales")
        self.assertEqual(descuento, 160) #800*0.2

    def test_calcular_descuento_1_2(self):
        """
        condicional edad entre 18 y 27 y valor entre 750 y 1000 falsa
        """
        mensaje, descuento = descuentos.calcular_descuento(15, 800, 1)
        self.assertEqual(mensaje, "Descuento no valido")
        self.assertEqual(descuento, 0)

    def test_calcular_descuento_1_3(self):
        """
        condicional edad entre 18 y 27 y valor entre 750 y 1000 falsa
        """
        mensaje, descuento = descuentos.calcular_descuento(15, 700, 1)
        self.assertEqual(mensaje, "Descuento no valido")
        self.assertEqual(descuento, 0)

    def test_calcular_descuento_1_4(self):
        """
        condicional edad entre 18 y 27 y valor entre 750 y 1000 falsa
        """
        mensaje, descuento = descuentos.calcular_descuento(15, 700, -1)
        self.assertEqual(mensaje, "Descuento no valido")
        self.assertEqual(descuento, 0)

    def test_calcular_descuento_1_5(self):
        """
        condicional edad entre 18 y 27 y valor entre 750 y 1000 verdadera
        """
        mensaje, descuento = descuentos.calcular_descuento(20, 700, 1)
        self.assertEqual(mensaje, "Descuento clientes iniciales")
        self.assertEqual(descuento, 140) #700*0.2

    def test_calcular_descuento_1_6(self):
        """
        condicional edad entre 18 y 27 y valor entre 750 y 1000 falsa
        """
        mensaje, descuento = descuentos.calcular_descuento(20, 780, -1)
        self.assertEqual(mensaje, "Descuento no valido")
        self.assertEqual(descuento, 0)

    def test_calcular_descuento_2_1(self):
        """
        condicional verdadera
        """
        mensaje, descuento = descuentos.calcular_descuento(35, 1200, 1)
        self.assertEqual(mensaje, "Descuento para familias")
        self.assertEqual(descuento, 1200*0.05*1)

    def test_calcular_descuento_2_2(self):
        """
        condicional verdadera
        """
        mensaje, descuento = descuentos.calcular_descuento(35, 1200, 6)
        self.assertEqual(mensaje, "Descuento para familias")
        self.assertAlmostEqual(descuento, 1200*0.1*6)

    def test_calcular_descuento_3(self):
        """
        condicional verdadera
        """
        mensaje, descuento = descuentos.calcular_descuento(55, 1200, 2)
        self.assertEqual(mensaje, "Descuento especiales")
        self.assertAlmostEqual(descuento, 1200*0.35)

    def test_calcular_descuento_4(self):
        """
        condicional falsa
        """
        mensaje, descuento = descuentos.calcular_descuento(30, 1200, 2)
        self.assertEqual(mensaje, "No aplica")
        self.assertAlmostEqual(descuento, 0)

    def test_calcular_descuento_5_1(self):
        """
        condicional verdadera
        """
        mensaje, descuento = descuentos.calcular_descuento(70, 1200, 0)
        self.assertEqual(mensaje, "Descuento para mayores de edad")
        self.assertAlmostEqual(descuento, 1200*0.25)

    def test_calcular_descuento_5_2(self):
        """
        condicional verdadera
        """
        mensaje, descuento = descuentos.calcular_descuento(80, 2100, 2)
        self.assertEqual(mensaje, "Descuento para mayores de edad")
        self.assertAlmostEqual(descuento, 2100*0.5)

    def test_calcular_descuento_6_1(self):
        """
        condicional verdadera
        """
        mensaje, descuento = descuentos.calcular_descuento(70, 5000, 2)
        self.assertEqual(mensaje, "Descuento para clientes")
        self.assertAlmostEqual(descuento, 5000*0.02)

    def test_calcular_descuento_6_2(self):
        """
        condicional verdadera
        """
        mensaje, descuento = descuentos.calcular_descuento(70, 4500, 2)
        self.assertEqual(mensaje, "Descuento para clientes")
        self.assertAlmostEqual(descuento, 4500*0.01)

if __name__ == '__main__':
    unittest.main(testRunner=xmlrunner.XMLTestRunner(output='reporte-pruebas'))
