# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import unittest
import src.descuento as descuentos
import xmlrunner


class Test(unittest.TestCase):

	#Incluya una pequeña descripción de lo que se prueba.
	def test_nombre_casos_prueba(self):
		self.assertEqual('','')

	#opcion 5
	def test_descuento_no_valido(self):
		mensaje, resultado = descuentos.calcular_descuento(0,0,0)
		self.assertEqual(resultado, 0)
		self.assertEqual(mensaje, "Descuento no valido")


if __name__ == '__main__':
	unittest.main(testRunner=xmlrunner.XMLTestRunner(output='reporte-pruebas'))