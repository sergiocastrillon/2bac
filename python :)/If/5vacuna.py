edad=int(input("Introduce la edad del paciente: "))
sexo=input("Introduce su sexo: ")
if edad>69:#edad>70 or edad==70:
    print("Al paciente se le debe poner la vacuna C")
if edad<70 and edad>15:
    if sexo.lower()=="mujer":
        print("Al paciente se le debe poner la vacuna B")
    if sexo.lower()=="hombre":
        print("Al paciente se le debe poner la vacuna A")
if edad<16:
    print("Al paciente se le debe poner la vacuna A")
    