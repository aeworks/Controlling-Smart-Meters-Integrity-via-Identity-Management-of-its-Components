#!/usr/bin/env python
# coding=utf-8

import numpy as np
import matplotlib.pyplot as plt
import csv
import binascii




"""
Esta clase é usada para recuperar elementos todos os elementos de um arquivo
"""
class hex:
	def __init__ (self, el0, el1, el2, el3, el4, el5, el6, el7, el8, el9, el10, el11, el12, el13, el14, el15):
		self.el0 = el0
		self.el1 = el1
		self.el2 = el2
		self.el3 = el3
		self.el4 = el4
		self.el5 = el5
		self.el6 = el6
		self.el7 = el7
		self.el8 = el8
		self.el9 = el9
		self.el10= el10
		self.el11 = el11
		self.el12 = el12
		self.el13 = el13
		self.el14 = el14
		self.el15 = el15


"""
Funcao que recupera o tamanho do csv, recive como parametro o nome do csv que deseja ser conhecido
"""
def tamanhoCSV(nomeDoCsv):
	nome = nomeDoCsv

	with open(nome, newline='') as File:
		reader= list(csv.reader(File))
		return int(len(reader))

"""
Funcao que toma dois arquivos em hexadecimal, transforma eles em binario e realiza um XOR entre os elementos
"""	

# def compareBinaryLevel():

# 	fila =0
# 	nome = 'hexD19.csv' # esse aqui é o dump de referencia (hexD4), comecou desde o hexD4
# 	nome2 = 'hexD7.csv'
# # Abro o primeiro arquivo csv a ser usado
# 	with open(nome, newline='') as File:  
# 			    reader = list(csv.reader(File, delimiter=' '))
# # 				Abro o segundo arquivo csv a ser usado para a comparacao
# 			    with open(nome2, newline='') as File2:  
# 			    		    reader2 = list(csv.reader(File2, delimiter=' '))
# 			    		    for i in range(tamanhoCSV(nome2)):
# 			    		    	filaHexDump =  hex(*reader[i])
# 			    		    	filaHexDump2 =  hex(*reader2[i])
			    		   
# 			    		    	print("{0:08b}".format(int(str(filaHexDump.el0),16)), "{0:08b}".format(int(str(filaHexDump.el1),16)), "{0:08b}".format(int(str(filaHexDump.el2),16)), 
# 			    		    		"{0:08b}".format(int(str(filaHexDump.el3),16)), "{0:08b}".format(int(str(filaHexDump.el4),16)), "{0:08b}".format(int(str(filaHexDump.el5),16)), 
# 			    		    		"{0:08b}".format(int(str(filaHexDump.el6),16)), "{0:08b}".format(int(str(filaHexDump.el7),16)), "{0:08b}".format(int(str(filaHexDump.el8),16)), 
# 			    		    		"{0:08b}".format(int(str(filaHexDump.el9),16)), "{0:08b}".format(int(str(filaHexDump.el10),16)), "{0:08b}".format(int(str(filaHexDump.el11),16)), 
# 			    		    		"{0:08b}".format(int(str(filaHexDump.el12),16)), "{0:08b}".format(int(str(filaHexDump.el13),16)), "{0:08b}".format(int(str(filaHexDump.el14),16)), 
# 			    		    		"{0:08b}".format(int(str(filaHexDump.el15),16)))

# 			    		    	# # Elementos que pertencem ao primeiro arquivo do hexDump pra transformarlos em hexa
# 			    		    	# element0Dump1, element1Dump1, element2Dump1, element3Dump1, element4Dump1, element5Dump1, element6Dump1, element7Dump1 =  "{0:08b}".format(int(str(filaHexDump.el0),16)), "{0:08b}".format(int(str(filaHexDump.el1),16)), "{0:08b}".format(int(str(filaHexDump.el2),16)), "{0:08b}".format(int(str(filaHexDump.el3),16)), "{0:08b}".format(int(str(filaHexDump.el4),16)), "{0:08b}".format(int(str(filaHexDump.el5),16)), "{0:08b}".format(int(str(filaHexDump.el6),16)), "{0:08b}".format(int(str(filaHexDump.el7),16))
# 			    		    	# element8Dump1, element9Dump1, element10Dump1, element11Dump1, element12Dump1, element13Dump1, element14Dump1, element15Dump1 = "{0:08b}".format(int(str(filaHexDump.el8),16)), "{0:08b}".format(int(str(filaHexDump.el9),16)), "{0:08b}".format(int(str(filaHexDump.el10),16)), "{0:08b}".format(int(str(filaHexDump.el11),16)), "{0:08b}".format(int(str(filaHexDump.el12),16)), "{0:08b}".format(int(str(filaHexDump.el13),16)), "{0:08b}".format(int(str(filaHexDump.el14),16)), "{0:08b}".format(int(str(filaHexDump.el15),16))


# 			    		    	# # Elementos que pertencem ao segundo arquivo do hexDump para transformarlos a hexa
# 			    		    	# element0Dump2, element1Dump2, element2Dump2, element3Dump2, element4Dump2, element5Dump2, element6Dump2, element7Dump2 = "{0:08b}".format(int(str(filaHexDump2.el0),16)), "{0:08b}".format(int(str(filaHexDump2.el1),16)), "{0:08b}".format(int(str(filaHexDump2.el2),16)), "{0:08b}".format(int(str(filaHexDump2.el3),16)), "{0:08b}".format(int(str(filaHexDump2.el4),16)), "{0:08b}".format(int(str(filaHexDump2.el5),16)), "{0:08b}".format(int(str(filaHexDump2.el6),16)), "{0:08b}".format(int(str(filaHexDump2.el7),16))
# 			    		    	# element8Dump2, element9Dump2, element10Dump2, element11Dump2, element12Dump2, element13Dump2, element14Dump2, element15Dump2 = "{0:08b}".format(int(str(filaHexDump2.el8),16)), "{0:08b}".format(int(str(filaHexDump2.el9),16)), "{0:08b}".format(int(str(filaHexDump2.el10),16)), "{0:08b}".format(int(str(filaHexDump2.el11),16)), "{0:08b}".format(int(str(filaHexDump2.el12),16)), "{0:08b}".format(int(str(filaHexDump2.el13),16)), "{0:08b}".format(int(str(filaHexDump2.el14),16)), "{0:08b}".format(int(str(filaHexDump2.el15),16))


# 			    		    	# #conversao de elementos para Binarios do hexDump1
			    		    
# 			    		    	# element0Dump1_bin, element1Dump1_bin, element2Dump1_bin, element3Dump1_bin, element4Dump1_bin, element5Dump1_bin, element6Dump1_bin, element7Dump1_bin = bin(int(element0Dump1,2)), bin(int(element1Dump1,2)), bin(int(element2Dump1,2)), bin(int(element3Dump1,2)), bin(int(element4Dump1,2)), bin(int(element5Dump1,2)), bin(int(element6Dump1,2)), bin(int(element7Dump1,2))
# 			    		    	# element8Dump1_bin, element9Dump1_bin, element10Dump1_bin, element11Dump1_bin, element12Dump1_bin, element13Dump1_bin, element14Dump1_bin, element15Dump1_bin = bin(int(element8Dump1,2)), bin(int(element9Dump1,2)), bin(int(element10Dump1,2)), bin(int(element11Dump1,2)), bin(int(element12Dump1,2)), bin(int(element13Dump1,2)), bin(int(element14Dump1,2)), bin(int(element15Dump1,2))


# 			    		    	# #conversao de elementos para Binarios do hexDump2
# 			    		    	# element0Dump2_bin, element1Dump2_bin, element2Dump2_bin, element3Dump2_bin, element4Dump2_bin, element5Dump2_bin, element6Dump2_bin, element7Dump2_bin =bin(int(element0Dump2,2)), bin(int(element1Dump2,2)), bin(int(element2Dump2,2)), bin(int(element3Dump2,2)), bin(int(element4Dump2,2)), bin(int(element5Dump2,2)), bin(int(element6Dump2,2)), bin(int(element7Dump2,2))
# 			    		    	# element8Dump2_bin, element9Dump2_bin, element10Dump2_bin, element11Dump2_bin, element12Dump2_bin, element13Dump2_bin, element14Dump2_bin, element15Dump2_bin = bin(int(element8Dump2,2)), bin(int(element9Dump2,2)), bin(int(element10Dump2,2)), bin(int(element11Dump2,2)), bin(int(element12Dump2,2)), bin(int(element13Dump2,2)), bin(int(element14Dump2,2)), bin(int(element15Dump2,2))


# 			    		    	# xor0, xor1, xor2, xor3, xor4, xor5, xor6, xor7 = int(element0Dump1_bin,2) ^ int(element0Dump2_bin,2), int(element1Dump1_bin,2) ^ int(element1Dump2_bin,2), int(element2Dump1_bin,2) ^ int(element2Dump2_bin,2), int(element3Dump1_bin,2) ^ int(element3Dump2_bin,2), int(element4Dump1_bin,2) ^ int(element4Dump2_bin,2), int(element5Dump1_bin,2) ^ int(element5Dump2_bin,2), int(element6Dump1_bin,2) ^ int(element6Dump2_bin,2), int(element7Dump1_bin,2) ^ int(element7Dump2_bin,2)
# 			    		    	# xor8, xor9, xor10, xor11, xor12, xor13, xor14, xor15 = int(element8Dump1_bin,2) ^ int(element8Dump2_bin,2), int(element9Dump1_bin,2) ^ int(element9Dump2_bin,2), int(element10Dump1_bin,2) ^ int(element10Dump2_bin,2), int(element11Dump1_bin,2) ^ int(element11Dump2_bin,2), int(element12Dump1_bin,2) ^ int(element12Dump2_bin,2), int(element13Dump1_bin,2) ^ int(element13Dump2_bin,2), int(element14Dump1_bin,2) ^ int(element14Dump2_bin,2), int(element15Dump1_bin,2) ^ int(element15Dump2_bin,2)


# 			    		    	# print("0b{0:08b}".format(xor0), "0b{0:08b}".format(xor1), "0b{0:08b}".format(xor2), "0b{0:08b}".format(xor3), "0b{0:08b}".format(xor4), "0b{0:08b}".format(xor5), "0b{0:08b}".format(xor6), "0b{0:08b}".format(xor7), "0b{0:08b}".format(xor8), "0b{0:08b}".format(xor9), "0b{0:08b}".format(xor10), "0b{0:08b}".format(xor11), "0b{0:08b}".format(xor12), "0b{0:08b}".format(xor13), "0b{0:08b}".format(xor14), "0b{0:08b}".format(xor15))

			    		    	




def convertoHexToBinary():

	nome ='hexA_'
	num = 1
	ext = '.csv'
	nomeHex = nome+str(num)+ext

	inte =0
	with open(nomeHex, newline='') as File:  
			    reader = list(csv.reader(File, delimiter=' '))

			    for i in reader:
			    	for t in range(16):
			    		print(i[t])
			    	# for j in i:
			    		
			    		# if(inte == 15):
			    		# 	inte = 0
			    		# else:
			    		# 	print("valor de inte ", inte, " valor de j ", j)
			    		# =======
			    			# for k in repr(j):
			    			# 	num = k.isdigit()
			    			# 	if(k.isdigit()):
			    			# 		print(k)
			    			# 		if(int(k) == 0):
			    			# 			zeros+=1
			    			# 		elif(int(k) == 1):
			    			# 			unos+=1
			    		
			    			
			    			
			    		



"""
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


				AQUI ENCONTRA-SE FUNCOES QUE FORAM UTILIZADAS COMO TESTES PARA O CODIGO FINAL


++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


"""



# def compareBinValeus():
# 	fila =0
# 	nome = 'hexDump1.csv'

# 	with open(nome, newline='') as File:  
# 			    reader = list(csv.reader(File, delimiter=' '))
# 			    # print("Reader:", reader)
# 			    filaHexDump =  hex(*reader[fila])
# 			    filaHexDump2 =  hex(*reader[100])
# 			    a = "{0:08b}".format(int(str(filaHexDump.el15),16))
# 			    b = "{0:08b}".format(int(str(filaHexDump2.el0),16))
# 			    b = "{0:08b}".format(int(str(filaHexDump.el15),16))

# 			    print("==========================================")
# 			    print("==========================================")

# 			    # print("tipo variavel a ", type(a))
# 			    # print("tipo variavel b ", type(b))
# 			    print("Valor de a: ", a)
# 			    print("Valor de b: ", b)

# 			    a2 = bin(int(a,2))
# 			    b2 = bin(int(b,2))

# 			    # a3 = bin(int(a2,2))
# 			    # b3 = bin(int(b2,2))



# 			    print("Valor de a2: ", a2)
# 			    print("Valor de b2: ", b2)

# 			    xor = int(a2,2) ^ int(b2,2)
# 			    # re = int(z3,2) ^ int(w3,2)


# 			    print("XOR: ", xor)
# 			    print("Resultado do XOR re : ", "0b{0:08b}".format(xor))




# 			    # x = bin(int(filaHexDump.el15, 16))
# 			    # y = filaHexDump2.el10
# 			    # # z = bin(int(x,16)) ^ bin(int(y,16))
# 			    # print("tipo variavel x ", type(x))
# 			    # print("tipo variavel y ", type(y))
# 			    # print("Valor do x: ", x)
# 			    # print("Valor do x: ", y)



# 			    # # c = bin(int(str(a))) ^ bin(int(str(b)))

# 			    # print("Valor de a: ", x, " Valor de b: ", y)
# 			    # print("==========================================")
# 			    # # print("a ^ b = ", c)
# 			    # print(x) 

# 			    print("==========================================")
			


# def testBinConvert():


# 	A = int('00000101',16)
# 	B = int('00101101',16)

# 	print("tipo variavel A ", type(A))

# 	print(bin(A))    
# 	print(bin(B))
# 	print("Resp0:") 
# 	print(bin(A ^ B))

# 	print("==========================================")

# 	z= 'A0'
# 	w = "A0"
# 	z2= "{0:08b}".format(int(z,16)) # bin(int(z,16)) #"{0:08b}".format(int(z,16))
# 	# z2 = bin(int(z,16))
# 	w2 = "{0:08b}".format(int(w,16))
# 	# w2 = bin(int(w,16))

# 	print("Valor z2: ", z2)
# 	print("Valor w2: ", w2)



# 	z3 = bin(int(z2,2))
# 	w3 = bin(int(w2,2))


# 	print("Valor de z em bianiro: ", z3)
# 	print("Valor de w em bianiro: ", w3)
# 	re = int(z3,2) ^ int(w3,2)
# 	re2 = int(z2,2) ^ int(w2,2)
# 	re3 = "0b{0:08b}".format(re2)
# 	print("Resultado do XOR re : ", "0b{0:08b}".format(re))
# 	print("Resultado do XOR re2 : ", "0b{0:08b}".format(re2))
# 	print("Resultado re3: ", re3)

# 	a = "11011111"
# 	b = "11001011"
# 	print(a)
# 	print(b)
# 	y = int(a,2) ^ int(b,2)
# 	print("Resp1: ")
# 	print('{0:08b}'.format(y,2))  #{0:b}'.format(y))

# 	y = int(a, 2)^int(b,2)
# 	print("Resp2: ")
# 	print(bin(y)[2:].zfill(len(a)))



"""
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
												FIM FUNCOES DE TESTE

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


"""
convertoHexToBinary()


# if(tamanhoCSV('hexdump1.csv') == tamanhoCSV('hexdump2.csv')):

# 	# print("Arquivos a comparar sao iguais!!! \nPode continuar...")
# 	compareBinaryLevel()
# 	# compareBinValeus()



	




