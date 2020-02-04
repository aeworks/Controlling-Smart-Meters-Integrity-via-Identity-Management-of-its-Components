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
Funcao que toma um arquivo em hexadecimal e transforma em binario
"""	

def compareBinaryLevel():

	fila =0
	nome = 'hexBaseC_30.csv' # esse aqui é o aquivo dump em hexadecimal
	# nome2 = 'hexD7.csv'
# Abro o primeiro arquivo csv a ser usado
	with open(nome, newline='') as File:  
			    reader = list(csv.reader(File, delimiter=' '))
			    for i in range(tamanhoCSV(nome)):
			    	filaHexDump =  hex(*reader[i])
			    
			    	print("{0:08b}".format(int(str(filaHexDump.el0),16)), "{0:08b}".format(int(str(filaHexDump.el1),16)), "{0:08b}".format(int(str(filaHexDump.el2),16)), 
			    		"{0:08b}".format(int(str(filaHexDump.el3),16)), "{0:08b}".format(int(str(filaHexDump.el4),16)), "{0:08b}".format(int(str(filaHexDump.el5),16)), 
			    		"{0:08b}".format(int(str(filaHexDump.el6),16)), "{0:08b}".format(int(str(filaHexDump.el7),16)), "{0:08b}".format(int(str(filaHexDump.el8),16)), 
			    		"{0:08b}".format(int(str(filaHexDump.el9),16)), "{0:08b}".format(int(str(filaHexDump.el10),16)), "{0:08b}".format(int(str(filaHexDump.el11),16)), 
			    		"{0:08b}".format(int(str(filaHexDump.el12),16)), "{0:08b}".format(int(str(filaHexDump.el13),16)), "{0:08b}".format(int(str(filaHexDump.el14),16)), 
			    		"{0:08b}".format(int(str(filaHexDump.el15),16)))

compareBinaryLevel()


