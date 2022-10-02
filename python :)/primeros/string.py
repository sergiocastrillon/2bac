oracion=input("Dime una oración con más de seis caracteres: ")
letra=oracion[5]
print(letra)
if letra=="a" or letra =="e" or letra =="i" or letra =="o" or letra=="u":
    print("¡Por fin encuentro una vocal!")
else:
    print("Sigo buscando.")