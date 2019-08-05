# -*- coding: utf-8 -*-
"""Archivo de descuentos."""

from __future__ import unicode_literals


def calcular_descuento(edad, valor_cotizado, dependientes):
    #Calcular el descuento considerando la edad, numero de dependientes y valor cotizado
    mensaje = ""
    descuento = 0

    if(edad > 18 and valor_cotizado > 500 and dependientes >= 0):

        if((18 < edad < 27) or (750 < valor_cotizado < 1000)):
            mensaje = "Descuento clientes iniciales"
            descuento = valor_cotizado*(0.2)

        elif((valor_cotizado > 1000) and (27 < edad <= 65)):

            if((35 <= edad < 50 and dependientes > 0) or (dependientes >= 4)):
                mensaje = "Descuento para familias"
                if dependientes >= 6:
                    descuento = valor_cotizado*(0.1*dependientes)
                else:
                    descuento = valor_cotizado*(0.05*dependientes)

            elif 50 <= edad <= 65:
                mensaje = "Descuento especiales"
                descuento = valor_cotizado*(0.35)

            else:
                mensaje = "No aplica"
                descuento = 0                

        elif( (edad >= 80) or (edad > 65 and dependientes == 0)):
            mensaje = "Descuento para mayores de edad"
            if(valor_cotizado > 2000):
                descuento = valor_cotizado*(0.5)
            else:
                descuento = valor_cotizado*(0.25)

        else:
            mensaje = "Descuento para clientes"
            if(valor_cotizado >= 5000):
                descuento = valor_cotizado*(0.02)
            else:
                descuento = valor_cotizado*(0.01)
            

    else:
        mensaje = "Descuento no valido"
        descuento = 0
        descuento = 0

    return mensaje, descuento



