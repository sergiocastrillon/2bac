h=float(input("Introduce el número de horas que has estado aparcado: "))
if h<2 or h==2:
    coste=h*3
if h>2 and h<5 or h==5:
    coste=5+(h-2)*2
if h>5 and h<10 or h==10:
    coste=11+(h-5)
if h>10:
    coste=16+(h-10)*0.5
print("El coste final es de", coste, "euros")