n1=input("Introduce el nombre de la primera persona: ")
e1=int(input("Introduce su edad: "))
n2=input("Introduce el nombre de la segunda persona: ")
e2=int(input("Introduce su edad: "))
n3=input("Introduce el nombre de la tercera persona: ")
e3=int(input("Introduce su edad: "))
if e1<e2 and e1<e3:
    print("La persona de menor edad es", n1 , "y tiene", e1 , "años.")
if e2<e1 and e2<e3:
    print("La persona de menor edad es", n2 , "y tiene", e2 , "años.")
if e3<e1 and e3<e2:
    print("La persona de menor edad es", n3 , "y tiene", e3 , "años.")
if e3==e2==e1:
    print("Las tres personas tienen la misma edad")
    