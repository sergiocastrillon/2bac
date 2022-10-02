precio=float(input("Introduce el precio del traje: "))
if precio>150:
    descuento=20
else:
    descuento=15
preciof=precio-(precio*(descuento/100))
print("El precio final es de", preciof, "euros con un descuento del",descuento,"%")
