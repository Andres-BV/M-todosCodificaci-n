import random 
from sys import argv
import string
import time

def boyer(largoM, largoN):

  #Para m = largo de texto, n = largo de patron
	archi=open('BM.dat','a') #Abro el archivo
	#largoM = int(argv[1]) 
	#largoN = int(argv[2])
	newporcent = 0.0
	M = []
	N = []
	com = []
	# Llenando listas ------------------------------------
	for i in range(largoM):
		let = random.choice(string.ascii_lowercase)
		M.append(let) #Rellenando la cadena de texto
		
	for j in range(largoN):
		let = random.choice(string.ascii_lowercase)
		N.append(let) #Rellenando el patron
	#print M
	#print N, "\n\n"

	# Algoritmo Boyer-Moore -------------------------------
	tiempoInicial = time.time()

	for x in range(largoM):
		if x >= largoN:
			if M[x] == N[-1]:
				miLargo = (x)-(largoN-1)
				com = M[miLargo:x+1]
				#print "i = ",x,  "  -  M[x] = ", M[x], " - com = ", com 				
				print com
				if com == N:
					print "match: com = ", com, " - N = ", N	
					
				else:
					print "No exito :("

	tiempoFinal = time.time()
	d = tiempoFinal - tiempoInicial
	diferencia = round(d, 6) 
	
	newlargoM = str(largoM)
	newlargoN = str(largoN)			#Para poder meter los datos al dat
	newdiferencia = str(diferencia)
   
	if largoN != 10:		# Cuando el largo del patron es 9, saltamos 2 lineas en el dat
		archi.write(newlargoM)	#Escribe largo de texto
		archi.write(' ')
		archi.write(newlargoN)	# Escribiendo largo del patron 
		archi.write(' ')
		archi.write(newdiferencia) #Escribiendo los promedios de tiempo
		archi.write('\n')

	else:
		archi.write(newlargoM)	#Lo mismo que arriba
		archi.write(' ')
		archi.write(newlargoN)
		archi.write(' ')		
		archi.write(newdiferencia)
		archi.write('\n\n')
	
	archi.close() 		# Cerrando el archivo, se abre cada vez que se ejecuta esta subrutina

	
def main():
		for i in range(10):	#Correr distintos tipos de largo de texto
			for j in range(10):	#Correr distintos tipos de largo de patron		
				print "\nTransmitiendo con largo de texto = ", i+1, "y con patron = ", j+1      # Meramente informativo para el programador
				boyer(i+1, j+1) 
		

if __name__ == "__main__":
	main()	
