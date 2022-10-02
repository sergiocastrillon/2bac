h=float(input("Introduce el número de horas semanales trabajadas: "))
p=float(input("Introduce el precio de las horas base: "))
if h > 37.5:
    sueldo=37.5*p+(h-37.5)*2*p
else:
    sueldo= h*p
print("Tu sueldo es de" , sueldo , "euros")