from django.shortcuts import render

# Funcion para calcular el descuento, solicitando edad,
# cantidad de dependientes (hijos o esposa) y # el valos
# que ha sido previamente cotizado
def calcular_descuento(edad, dependientes, valor_cotizado):
 
  if(edad > 75 and dependientes = 1):
    #Descuento del 50% a tercera edad
    descuento = valor_cotizado*0.50
 
  else:
    if(dependientes > 0 or valor_cotizado > 1000):
      #Descuento del 5% por cada dependiente
      descuento = valor_cotizado*(0.05*dependientes)
 
    elif(valor_cotizado > 700 and (dependientes = 1 or edad > 50)):
      descuento = valor_cotizado*0.25
 
    else:
      descuento = 0
 
  return descuento
