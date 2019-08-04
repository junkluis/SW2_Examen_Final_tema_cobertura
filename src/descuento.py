# -*- coding: utf-8 -*-
from __future__ import unicode_literals


def calcular_descuento(edad, dependientes, valor_cotizado):
	if(valor_cotizado > 500 and edad >= 18):
		if(edad > 75 and dependientes == 1):
			descuento = valor_cotizado*0.50

		else:
			if(dependientes > 0 or valor_cotizado > 1000):
				descuento = valor_cotizado*(0.05*(dependientes+1))
			elif(valor_cotizado > 700 and (dependientes == 1 or edad > 50)):
				descuento = valor_cotizado*0.25
			else:
				descuento = 0
	else:
		descuento = 0

	return descuento


if __name__ == "__main__":
    print(calcular_descuento(19,5,499))