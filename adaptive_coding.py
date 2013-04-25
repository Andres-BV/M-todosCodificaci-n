'''
  Adaptive coding
	Eduardo Triana - ITS - FIME - UANL
'''


def start():
	
	cadena = str(raw_input('Text input >>>'))

	# ENCODER **************************************************************************************

	string = {"a":1, "b":2, "c":3, "d":4, "e":5, "f":6, "g":7, "h":8, "i":9, "j":10, "k":11, "l":12, 
	"m":13, "n":14, "o":15, "p":16, "q":17, "r":18, "s":19, "t":20, "u":21, "v":22, "w":23, "x":24, "y":25, "z":26, " ":27}

	cad = list(cadena)
	compressed = [] #Lista donde guardo todos los outputs
	bandera = 0 #Para indicar si "s+c" ya existe en el diccionario
	todecoder = [] #Para poder decodificar
	#print cad
	#s = []
	i = 0	
	
	largo = len(cad)
	s = cad[i]
	while i != largo-1:
		c = cad[i+1]
		if (s+c) in string:
			s = s + c
		else:
			output = string[s]
			maximo = max(string.values())
			string[s+c] = maximo+1
			#todecoder.append(output)
			#todecoder.append(s+c)
			s = c
			compressed.append(output)

		i = i + 1
	output = string[s]
	compressed.append(output)
	
	print "comprimido = ", compressed	
	#print "string = ", string
	#print "junto = ", todecoder

	# DECODER***************************************************************************************************************

	string2 = {1:"a", 2:"b", 3:"c", 4:"d", 5:"e", 6:"f", 7:"g", 8:"h", 9:"i", 10:"j", 11:"k", 12:"l", 13:"m", 14:"n", 15:"o"
		,16:"p", 17:"q", 18:"r", 19:"s", 20:"t", 21:"u", 22:"v", 23:"w", 24:"x", 25:"y", 26:"z", 27:" "} #Este va a la inversa

	s2 = 0
	largo2 = len(compressed)
	#print largo2
	j = 0
	
	recuperado = [] # Para meter todo mi mensaje original

	while j != (largo2):
		k = compressed[j]
		#print "k = ", k
		entry = string2[k]
		recuperado.append(entry)
		if s2 != 0:
			maximo2 = max(string2.keys())
			string2[maximo2+1] = s2+entry[0]
		s2 = entry
		j = j + 1

	

	print "\nrecuperado = "
	print "".join(recuperado) 

if __name__ == '__main__':
	start()
