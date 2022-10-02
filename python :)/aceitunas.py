sueldo=float(input("Introduce tu sueldo: "))
cajas=int(input("Introduce las cajas que has vendido: "))
if cajas == 20 or cajas > 20:
    sobresueldo=sueldo * 0.15
    total = sueldo + sobresueldo
else:
    total = sueldo
    sobresueldo = 0
print("Tu sueldo final es de " ,total, "euros y tienes " ,sobresueldo, "euros de sobresueldo")