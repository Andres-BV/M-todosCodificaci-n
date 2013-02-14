#Generador y transmisor de palabras
#Autor: Eduardo Triana
#FIME - ITS

import random 
from sys import argv

def generador(l, cer): #Generador y transmisor de palabras
  
	freqzero = 0
	if cer == 0: #Esto lo hago para saber que frecuencia de ceros usare, con valores validos desde 0.1 hasta 0.9
		freqzero = 0.1
	elif cer == 1:
		freqzero = 0.2
	elif cer == 2:
		freqzero = 0.3
	elif cer == 3:
		freqzero = 0.4
	elif cer == 4:
		freqzero = 0.5
	elif cer == 5:
		freqzero = 0.6
	elif cer == 6:
		freqzero = 0.7
	elif cer == 7:
		freqzero = 0.8
	elif cer == 8:
		freqzero = 0.9			
	
	#z = 1
	#for a in range(9):
	archi=open('canalTriana.dat','a') #Abro el archivo donde se almacenaran todas las probabilidades de exito, junto con los largos y frecuencias
	#length = int(argv[1])
	length = pow(2,l) #El largo del archivo lo elevamos a la "l", necesito l para generar el dat
	
	#freqzero = float(argv[1]) Esto ya va arriba, y ya no es con parametro
	zerocorrect = float(argv[1])
	onecorrect = float(argv[2])	# El orden de parametros por consola es: 1) Porcentaje de ceros correctos. 2) Porcentaje de unos correctos. 3) Repeticiones
	repet = int(argv[3])

	conteo0 = 0
	conteo1 = 0

	freqzeroProduct = freqzero*length
	listaG = []
		
	for i in range(length):	#Todo esto es para generar cada una de las palabras
		bit = int(random.randint(0,1))
		if bit == 0:		
			if freqzeroProduct > conteo0: #Agregando los bits para formar las cadenas de palabras
				listaG.append(0)
				conteo0 = conteo0 + 1
			else:
				listaG.append(1)
		else:
			listaG.append(1)
	print "Generated:  " ,listaG  #Imprimiendo la palabra generada
	
	#Transmision de palabras
	
	zerocorrect = zerocorrect*length  
	onecorrect = onecorrect*length    
	exitos = 0.0
	#print "zerocorrect:", zerocorrect
	#print "onecorrect: ", onecorrect, "\n"

	# Todo lo que sigue corresponde a la transmision de las palabras

	for j in range(repet):
		conteo0 = 0
		contCorr0 = 0
		contCorr1 = 0
		listaT = []
		for k in range(length):
			bitransmited = int(random.randint(0,1))
			if bitransmited == 0:		
				if freqzeroProduct > conteo0:
					if zerocorrect > contCorr0:
						listaT.append(0)		#Esto es para que la frecuencia de ceros corresponda a la que indicamos
						conteo0 = conteo0 + 1
						contCorr0 = contCorr0 + 1
					else:
						listaT.append(1)
						contCorr1 = contCorr1 + 1
				else:
						listaT.append(1)
			else:
				if onecorrect > contCorr1:
					listaT.append(1)
					contCorr1 = contCorr1 + 1		#Si ya rebasamos el limite de ceros creados, ahora ponemos unos
				else:
					listaT.append(0)
					contCorr0 = contCorr0 + 1
		if listaT == listaG:		#Comparamos el contenido de las listas de palabras transmitidas con las generadas
			exitos = exitos + 1	#Elevamos en 1 el exito obtenido
		print "Transmited: ", listaT
	porcent = (exitos/repet)	#Creamos el porcentaje de exito, esto sera la columna 3 de nuestro archivo dat, es lo mero mero
	print "\n", repet
	print exitos	
	print porcent
	
	newl = str(l)				#
	newfreqzero = str(freqzero)		# Convirtiendo a string todos los datos para poder escribirlos en nuestro dat
	newporcent = str(porcent)		#
			
	if cer != 8:				# Cuando la frecuencia de ceros ya sea 0.9, saltamos 2 lineas en el dat
		archi.write(newl)
		archi.write(' ')
		archi.write(newfreqzero)	# Escribiendo en el dat 
		archi.write(' ')
		archi.write(newporcent)
		archi.write('\n')

	else:
		archi.write(newl)
		archi.write(' ')
		archi.write(newfreqzero)
		archi.write(' ')		#Escribiendo en el dat
		archi.write(newporcent)
		archi.write('\n\n')
	
	archi.close() 		# Cerrando el archivo, se abre cada vez que se ejecuta esta subrutina


	'''
	f = open("palabras.txt", "w")
	
	for j in range(20):
		for i in range(30):
			y = str(random.randint(0,1))		
			if (i != 29):			
				f.write(y)
			else:
				f.write(y+ "\n")	
	f.close()
	transmisor()
	'''
	
def transmisor():	#Esta subrutina la omiti ya que la transmision la hice junto con el generador de palabras
	'''
	for i in range(9):
		print "Transmitiend con largo = ", i
		generador(i)
	
	archivo = open("palabras.txt", "r")
	print "Ingresa la linea que quieres enviar: "
	linea = int(raw_input())
	counter = 0	
	for i in archivo.xreadlines():	
		if counter == linea:		
			print i.strip()			
		counter = counter + 1
	archivo.close() 			
	'''
def main():

	for i in range(10):		#Para poder correr el transmisor con potencias desde 0 hasta la 9
		for j in range(9):	#Para poder correr el transmisor con frecuencias de zero desde 0.1 hasta 0.9		
			print "\nTransmitiendo con largo = ", i, "y con freqzero = ", j      # Meramente informativo para el programador
			generador(i, j) #Correr el generador/transmisor con largos y frecuencias distintas

	#i = 1
	#while i <= 512:
		#generador(i)
	#	i = i*2

if __name__ == "__main__":
	main()

'''
LARGO	FRECUENCIAS_ZERO	PEZ	PEU	%

genera

//GRAFICAR EN BASE A LAS POTENCIAS Y AL LARGO DE LAS PALABRAS	
'''
