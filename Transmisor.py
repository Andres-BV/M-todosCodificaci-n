#Generador y transmisor de palabras
#Esto se ejecuta desde un bash

import random 
from sys import argv

def generador(): #Generador de palabras
  #z = 1
	#for a in range(9):
	
	length = int(argv[1])
	freqzero = float(argv[2])
	zerocorrect = float(argv[3])
	onecorrect = float(argv[4])
	repet = int(argv[5])

	conteo0 = 0
	conteo1 = 0

	freqzero = freqzero*length
	listaG = []

	for i in range(length):
		bit = int(random.randint(0,1))
		if bit == 0:		
			if freqzero > conteo0:
				listaG.append(0)
				conteo0 = conteo0 + 1
			else:
				listaG.append(1)
		else:
			listaG.append(1)
	print "Generated:  " ,listaG
	
	#Transmision de palabras
	
	zerocorrect = zerocorrect*length
	onecorrect = onecorrect*length
	exitos = 0.0
	#print "zerocorrect:", zerocorrect
	#print "onecorrect: ", onecorrect, "\n"

	for j in range(repet):
		conteo0 = 0
		contCorr0 = 0
		contCorr1 = 0
		listaT = []
		for k in range(length):
			bitransmited = int(random.randint(0,1))
			if bitransmited == 0:		
				if freqzero > conteo0:
					if zerocorrect > contCorr0:
						listaT.append(0)
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
					contCorr1 = contCorr1 + 1
				else:
					listaT.append(0)
					contCorr0 = contCorr0 + 1
		if listaT == listaG:
			exitos = exitos + 1
		print "Transmited: ", listaT
	porcent = (exitos/repet)*100	
	print "\n", repet
	print exitos	
	print porcent

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
	
def transmisor():	#transmitir muchas veces
	'''
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
	generador()
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
