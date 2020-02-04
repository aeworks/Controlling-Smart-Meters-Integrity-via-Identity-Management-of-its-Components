#!/usr/bin/env python
# coding=utf-8
import numpy as np


nomeArquivo = 'bitsEstaveis.csv'

arrayBits = np.array([], dtype=int)

arqBits = np.genfromtxt(nomeArquivo, delimiter=',', dtype=int)


# for valor in arqBits:
# 	# print(valor)
# 	arrayBits = np.append(arrayBits, valor)

# print(len(arrayBits))
# print(len(arrayBits))


for i in range(2048):
	arrayBits = np.append(arrayBits, arqBits[i])


np.savetxt('janelaBits.csv', arrayBits, delimiter=',', fmt="%d")



