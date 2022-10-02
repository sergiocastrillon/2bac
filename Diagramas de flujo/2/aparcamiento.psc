Algoritmo sin_titulo
	Escribir "Introduce las horas aparcadas"
	Leer t
	Si t <= 2 Entonces
		p<-t * 3
	SiNo
		
	Fin Si
	Si t > 2 y t <= 5 Entonces
		p<-6 + (t-2)*2
	SiNo
		
	Fin Si
	Si t > 5 y t <= 10 Entonces
		p<-12 + (t-5)
	SiNo
		
	Fin Si
	Si t > 10 Entonces
		p<-17 + (t-10) * 0.5
	SiNo
		
	Fin Si
	Escribir "El precio por el tiempo total de aparcamiento es de", p "euros"
FinAlgoritmo
