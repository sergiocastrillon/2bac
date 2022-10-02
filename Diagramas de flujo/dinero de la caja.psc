Algoritmo sin_titulo
	Escribir "Introduce el número de billetes"
	Leer a
	Escribir "Introduce el número de monedas"
	Leer b
	c<-0
	d<-0
	Mientras c < a Hacer
		Escribir "Introduce el valor del billete"
		Leer billete
		c<-c + 1
		dinero<-dinero + billete
	Fin Mientras
	Mientras d < b Hacer
		Escribir "Introduce el valor de la moneda"
		Leer moneda
		d<-d+1
		dinero<-dinero + moneda
	Fin Mientras
	Escribir dinero
FinAlgoritmo
