'''
   ***Humming Code
   ***Eduardo Triana / ITS / FIME / UANL
'''
from random import *
import numpy as np

def encoding(msg):
	#Data bits vectors
	d1 = [1,0,0,0]
	d2 = [0,1,0,0]
	d3 = [0,0,1,0]
	d4 = [0,0,0,1]

	g = []
	G = []
	
	p1 = [] #Vector for parity bit 1
	p2 = [] #Vector for parity bit 2
	p3 = [] #Vector for parity bit 3
	'''
	p1 = d2 + d3 + d4
	p2 = d1 + d3 + d4
	p3 = d1 + d2 + d4
	'''
	#Para p1
	for i in range(4):
		p1.append((d2[i] ^ d3[i] ^ d4[i]))  
	
	#Para p2
	for i in range(4):
		p2.append((d1[i] ^ d3[i] ^ d4[i]))	

	#Para p3
	for i in range(4):
		p3.append((d1[i] ^ d2[i] ^ d4[i]))

	#Creating Generator matrix [G]
	'''
	p1 	p2 	p3 	d1 	d2 	d3 	d4
	................................................... 
  	0 	1 	1 	1 	0 	0 	0 
G =  	1 	0 	1 	0 	1 	0 	0 
  	1 	1 	0 	0 	0 	1 	0 
  	1 	1 	1 	0 	0 	0 	1  
	'''
	for i in range(len(d1)): #Bien podria ser cualquier databit
		g.append(p1[i])
		g.append(p2[i])
		g.append(p3[i]) # For parity		
		#Para los databits
		g.append(d1[i]) 
		g.append(d2[i])
		g.append(d3[i])
		g.append(d4[i]) # For databits 
		G.append(g)				
		g = []
	#cade = [1,0,1,0]
	matriz0 = np.matrix(msg)
	matriz1 = np.matrix(G)
	coding = matriz0 * matriz1

	print "G = ", G
	print  matriz1
	print "code = ", coding
def main(): 
	inp = raw_input('Get in your message >>> ')
	msg = []
	for i in inp:
		print i
		msg.append(int(i)) 
	print msg
	print len(msg)
	encoding(msg)


main()
	
	
