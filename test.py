# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import unittest
import src.descuento as descuentos

class Test(unittest.TestCase):
	#Incluya una pequeña descripción de lo que se prueba.
	def test_nombre_casos_prueba(self):
		self.assertEqual('','')


	def test_descuento_no_valido(self):
		resultado = descuentos.calcular_descuento(0,0,0)
		self.assertEqual(resultado, 0)




if __name__ == '__main__':
	unittest.main()