#Algoritmo de Huffman
#Carlos Triana - FIME, ITS

def main():
  frec = [] #Para poner las frecuencias de los caracteres
	newtext = []
	corleone = [] 
	'''
		El formato de las frecuencias es la frecuencia, seguido del caracter correspondiente
	'''
	texto = raw_input('Ingresar cadena: ')
	print texto

	miLista = list(texto)
	newtext = miLista[:]
	
	for car in newtext:
		#frec.append(car)
		c = newtext.count(car)
		if c == 1:
			frec.append(car)
			frec.append(c)
		elif c > 1:
			if car not in corleone: 
				corleone.append(car)
				corleone.append(c)
	
	santino = [] #Para guardas las listas
	
	corleone2 = corleone[:]
	corleone2.reverse()
	largo = len(corleone)

	for bla in range(largo):
		if bla%2 == 0:
			li = [corleone2[bla], corleone2[bla+1]]
			santino.append(li)

	santino.sort()
	
	largo2 = len(santino)
	fredo = [] #Esta la la extenderemos a la lista "frec"

	for w in range(largo2):
		fredo.append(santino[w][0])
		fredo.append(santino[w][1])

	print frec
	frec.reverse()
	suma = frec + fredo

	print frec
	print corleone
	#print corleone2
	#print santino
	#print largo2
	print fredo
	print suma
main()
