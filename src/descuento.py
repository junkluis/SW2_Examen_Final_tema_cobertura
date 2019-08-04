# -*- coding: utf-8 -*-
from __future__ import unicode_literals


def calcular_descuento(edad, dependientes, valor_cotizado):
	#Calcular el descuento considerando la edad, numero de dependientes y valor cotizado

	if(edad > 18 and valor_cotizado > 500 and dependientes >=0 ):
		mensaje = "Descuento valido"
		if( (18 > edad >27) or ( 500 > valor_cotizado > 1000) ):
			mensaje = "Descuento clientes iniciales"
			descuento = valor_cotizado*(0.2)

		if( (28 > edad > 50 and dependientes > 0) or (dependientes>2) ):
			mensaje = "Descuento para familias"
			descuento = valor_cotizado*(0.05*dependientes)

		if( (50 > edad > 75) or (dependientes > 4 and valor_cotizado>1000) or (valor_cotizado > 50000) ):
			mensaje = "Descuento especiales"
			descuento = valor_cotizado*(0.35)

		if( ( edad > 50) and (valor_cotizado >1000 ) or (dependientes == 1 and valor_cotizado > 1000)):
			mensaje = "Descuento para socios"
			if( valor_cotizado > 50000):
				descuento = valor_cotizado*(0.05) +1000
			else:
				descuento = valor_cotizado*(0.05) +500
			
		if( (edad > 75) or (edad > 50 and valor_cotizado>1000 and dependientes>=2)):
			mensaje = "Descuento para mayores de edad"
			descuento = valor_cotizado*(0.05)			

		else:
			mensaje = "Descuento para clientes"
			descuento = valor_cotizado*(0.01)

	else:
		mensaje = "Descuento no valido"
		descuento = 0

	return mensaje, descuento
