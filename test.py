# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import unittest
import src.descuento as descuentos
import xmlrunner


class Test(unittest.TestCase):

	#Incluya una pequeña descripción de lo que se prueba.
	def test_nombre_casos_prueba(self):
		self.assertEqual('','')

	def test_calcular_descuento_cliente_jovenes(self):
		mensaje, descuento = descuentos.calcular_descuento(19,502,0)
		self.assertEqual(mensaje, 'Descuento clientes iniciales')
		self.assertEqual(descuento, 100.4)




	


if __name__ == '__main__':
	unittest.main(testRunner=xmlrunner.XMLTestRunner(output='reporte-pruebas'))