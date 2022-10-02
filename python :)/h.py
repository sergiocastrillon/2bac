nota = float(input("Introduce tu nota media: "))
beca = float(input("Introduce el valor inicial de la beca"))
if nota > 7:
    becaf = beca + beca * 0.25
    print("Beca 25")
if nota < 7 and nota > 5 or nota==5 or nota==7:
    becaf = beca + beca * 0.1
    print("Beca 10")
if nota < 5:
    print("No tienes beca")