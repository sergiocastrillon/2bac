i=float(input("Introduce la intensidad que circula por el circuito (en amperios): "))
r=float(input("Introduce el valor de la resistencia (en ohmios): "))
p=(r*i)*i # V = R*I y P = V * I
print("La potencia del circuito es de" , p , "W")