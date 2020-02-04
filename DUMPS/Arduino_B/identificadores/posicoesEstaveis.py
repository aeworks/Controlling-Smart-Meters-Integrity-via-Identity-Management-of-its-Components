#!/usr/bin/env python
# coding=utf-8

import csv
import numpy as np

nome = "mapaEstatistico.csv"
arquivoBits = "mapaUnosZeros.csv"


arrayPosicoes = np.array([], dtype=int)
novoArray = np.array([], dtype=float)
arrayBits = np.array([], dtype=int)
arrayBitsEstaveis = np.array([], dtype=int)


limiar = 0.9


#==================================================
# Recuperar arquivos
#==================================================

arquivo = np.genfromtxt(nome, delimiter=',')
arqBits = np.genfromtxt(arquivoBits, delimiter=',', dtype=int)


#==================================================
# saber posicoes estaveis
#==================================================


for i in arquivo:
	novoArray = np.append(novoArray, float(i))

for j in range(len(novoArray)):
	num = float(str(novoArray[j]))

	if(num >= limiar):
		arrayPosicoes = np.append(arrayPosicoes, j)
		


# print(len(arrayPosicoes))
np.savetxt('posicoes.csv', arrayPosicoes, delimiter=',', fmt="%d")




#==================================================
# Recuperar bits desde las posiciones
#==================================================


for b in arqBits:
	arrayBits = np.append(arrayBits, b)

for posi in arrayPosicoes:
	# print(arrayBits[posi])
	arrayBitsEstaveis = np.append(arrayBitsEstaveis, arrayBits[posi])

print(len(arrayBitsEstaveis))

np.savetxt('bitsEstaveis.csv', arrayBitsEstaveis , fmt="%d", delimiter=',')


#recuperar array como valores 1 e 0

