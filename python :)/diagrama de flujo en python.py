a=0
total=0
n=int(input("Introduce el número de artículos que vas a comprar: "))
while a<n:
    a=a+1
    p=float(input("Introduce el precio del artículo: "))
    if p>200 or p==200:
        pfinal=p-(p*0.15)
        print("El descuento del artículo es del 15% y cuesta " ,pfinal ," euros")
    if p>100 and p<200:
        pfinal=p-(p*0.12)
        print("El descuento del artículo es del 12% y cuesta " ,pfinal , " euros")
    if p<100 or p==100:
        pfinal=p-(p*0.10)
        print("El descuento del artículo es del 10% y cuesta " ,pfinal , " euros")
    total=total+pfinal
print("El precio final es de ",total , " euros")
    