x=float(input("Introduce el número de metros de tela que requieres: " )) # Se pide al usuario que introduzca cuantos metros de tela quiere
p=x/0.0254 # Se hace la operación para realizar la conversión de metros a pulgadas
p=round(p,2) # Redondeo el resultado para que tenga dos cifras decimales
print(x,"metros son",p,"pulgadas") # Imprimo el resultado en pantalla

