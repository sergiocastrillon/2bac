Algoritmo sin_titulo
	Escribir "Introduce el n�mero de art�culos que vas a comprar"
	Leer n
	a<-0
	total<-0
	Mientras a < n  Hacer
		a<-a+1
		Escribir "Introduce el precio del art�culo"
		Leer p
		Si p >= 200 Entonces
			pfinal<-p - (p*0.15)
			Escribir "El descuento del art�culo es del 15% y cuesta " ,pfinal ," euros"
		SiNo
			
		Fin Si
		Si p > 100 y p < 200 Entonces
			pfinal<-p - (p * 0.12)
			Escribir "El descuento del art�culo es del 12% y cuesta " ,pfinal , " euros"
		SiNo
			
		Fin Si
		Si p <= 100 Entonces
			pfinal<-p - (p * 0.10)
			Escribir "El descuento del art�culo es del 10% y cuesta " ,pfinal , " euros"
		SiNo
			
		Fin Si
		total<-total + pfinal
	Fin Mientras
	Escribir "El precio final es de " ,total , " euros"
FinAlgoritmo
