# -*- coding: utf-8 -*-
from __future__ import unicode_literals


def calcular_descuento(edad, valor_cotizado, dependientes):
	#Calcular el descuento considerando la edad, numero de dependientes y valor cotizado
	descuento = 0
	if(edad > 18 and valor_cotizado > 500 and dependientes >=0 ):
		
		mensaje = "Descuento valido"
		if((18<edad<27) or (750<valor_cotizado<1000) ):
			mensaje = "Descuento clientes iniciales"
			descuento = valor_cotizado*(0.2)

		elif( (valor_cotizado>1000) and (27<edad<=65)):

			if( (35<edad<50 and dependientes>0) or (dependientes>=4)  ):
				mensaje = "Descuento para familias"
				if dependientes>=6:
					descuento = valor_cotizado*(0.1*dependientes)
				else:
					descuento = valor_cotizado*(0.05*dependientes)

			elif( (50<=edad<=65) or (dependientes>=2 and valor_cotizado>2500) or (valor_cotizado>=5000) ):
				mensaje = "Descuento especiales"
				descuento = valor_cotizado*(0.35)

		elif( (edad>=80) or (edad>65 and dependientes==0) ):
			mensaje = "Descuento para mayores de edad"
			if(valor_cotizado >2000):
				descuento = valor_cotizado*(0.5)
			else:
				descuento = valor_cotizado*(0.25)

		else:
			mensaje = "Descuento para clientes"
			descuento = valor_cotizado*(0.01)

	else:
		mensaje = "Descuento no valido"
		descuento = 0

	return mensaje, descuento


if __name__ == "__main__":

	#Descuento clientes iniciales
	print(calcular_descuento(19,502,0))
	print(calcular_descuento(28,752,0))

	#Descento para familia
	print(calcular_descuento(36,1002,2))
	print(calcular_descuento(28,1002,4))

	#Descento especiales
	print(calcular_descuento(51,1002,2))
	print(calcular_descuento(34,2505,2))
	print(calcular_descuento(34,5001,0))
	
	#Descento mayores de edad
	print(calcular_descuento(81,1002,2))
	print(calcular_descuento(66,2502,0))

	#Descento cliente general
	print(calcular_descuento(66,2502,3))

	#Descento no validos
	print(calcular_descuento(0,0,0))



