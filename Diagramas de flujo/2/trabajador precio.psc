Algoritmo sin_titulo
	Escribir "Introduce el número de horas trabajadas"
	Leer horas
	Escribir "Introduce el precio por hora"
	Leer precio
	Si horas > 37.5 Entonces
		hextra = horas - 37.5
		dinero<-(37.5 * precio) + (hextra * (precio * 2))
	SiNo
		dinero<-horas * precio
	Fin Si
	Escribir "El trabajador ha ganado", dinero "euros"
FinAlgoritmo
