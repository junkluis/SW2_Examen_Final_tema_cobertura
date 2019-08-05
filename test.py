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

	def test_calcular_descuento_familias(self):
		mensaje, descuento = descuentos.calcular_descuento(35,1002,1)
		self.assertEqual(mensaje, 'Descuento para familias')
		self.assertEqual(descuento, 50.1)

	def test_calcular_descuento_familias_grandes(self):
		mensaje, descuento = descuentos.calcular_descuento(28,1002,6)
		self.assertEqual(mensaje, 'Descuento para familias')
		self.assertEqual(descuento, 601.2)

	def test_calcular_descuentos_especiales(self):
		mensaje, descuento = descuentos.calcular_descuento(51,1002,2)
		self.assertEqual(mensaje, 'Descuento especiales')
		self.assertEqual(descuento, 350.7)

	def test_calcular_descuento_mayores_edad(self):
		mensaje, descuento = descuentos.calcular_descuento(81,1002,2)
		self.assertEqual(mensaje, 'Descuento para mayores de edad')
		self.assertEqual(descuento, 250.5)

	def test_calcular_descuento_mayores_edad_grandes_valores(self):
		mensaje, descuento = descuentos.calcular_descuento(66,2502,0)
		self.assertEqual(mensaje, 'Descuento para mayores de edad')
		self.assertEqual(descuento, 1251.0)

	def test_calcular_descuento_clientes_generales(self):
		mensaje, descuento = descuentos.calcular_descuento(66,2502,3)
		self.assertEqual(mensaje, 'Descuento para clientes')
		self.assertEqual(descuento, 25.02)

	def test_calcular_descuento_clientes_generales_valor_mayor_a_500(self):
		mensaje, descuento = descuentos.calcular_descuento(66,5001,3)
		self.assertEqual(mensaje, 'Descuento para clientes')
		self.assertEqual(descuento, 100.02)

	def test_calcular_descuento_no_valido(self):
		mensaje, descuento = descuentos.calcular_descuento(0,0,0)
		self.assertEqual(mensaje, 'Descuento no valido')
		self.assertEqual(descuento, 0)



	


if __name__ == '__main__':
	unittest.main(testRunner=xmlrunner.XMLTestRunner(output='reporte-pruebas'))