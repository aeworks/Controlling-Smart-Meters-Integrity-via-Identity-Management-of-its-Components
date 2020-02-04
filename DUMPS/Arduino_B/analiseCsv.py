#!/usr/bin/env python
# coding=utf-8
import numpy as np
import csv


#===============================================================================
# Formato de arquivos a ser lidos
#===============================================================================
nomeTest = "binBf_1.csv"
#FORMATO ARQUIVOS A LER
nome = "binBf_"
ext = ".csv"

#===============================================================================
# Funcao que recupera o tamanho do csv, recive como parametro o nome do csv que 
# deseja ser conhecido
#===============================================================================
def tamanhoCSV(nomeDoCsv):
	nome = nomeDoCsv

	with open(nome, newline='') as File:
		reader= list(csv.reader(File))
		return int(len(reader))



#===============================================================================
# Lista de variaveis que vou usar para carregar csv na memoria
#===============================================================================

# # tempArquivos = np.array([ 'arq1', 'arq2', 'arq3', 'arq4', 'arq5', 'arq6', 'arq7', 'arq8', 'arq9', 'arq10', 'arq11', 'arq12', 'arq13', 'arq14', 'arq15', 'arq16', 'arq17', 'arq18', 'arq19', 'arq20', 'arq21', 'arq22', 'arq23', 'arq24', 'arq25', 'arq26', 'arq27', 'arq28', 'arq29', 'arq30' ])
# tempArquivos = np.array([ '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '' ])
# # arrayComCsv =np.empty([512, 128], dtype=int)
# arrayTotal = np.array([30])
# numeroArr = 0

# for arq in range(30):


# 	numeroArr+=1
# 	nomeCompletoArr = nome+str(numeroArr)+ext

# 	# arr = np.genfromtxt(nomeCompletoArr, delimiter=',')
# 	arrayTotal[arq] = np.genfromtxt(nomeCompletoArr, delimiter=',')


# print(arrayTotal)






				

# for lin in range(511):
# 	for col in range(127):
# 		numeroArr = 0
# 		for arr in tempArquivos:
# 			# print(arr.shape)
# 			numeroArr+=1
# 			linha = int(lin)
# 			coluna = int(col)
# 			print(numeroArr)
# 			print(arr)
# 			print(lin, col)
# 			valorAtual = arr[linha:coluna]
# 			print("Valor atual ", valorAtual)
# 			print("==================")

# for arr2 in tempArquivos:
# 	print("from second for")
# 	print(arr.shape)
# 	print(arr[0:0])




# arq1 = np.genfromtxt('binAf_1.csv', delimiter=',')
# arq2 = np.genfromtxt('binAf_2.csv', delimiter=',')
# arq3 = np.genfromtxt('binAf_3.csv', delimiter=',')
# arq4 = np.genfromtxt('binAf_4.csv', delimiter=',')
# arq5 = np.genfromtxt('binAf_5.csv', delimiter=',')
# arq6 = np.genfromtxt('binAf_6.csv', delimiter=',')
# arq7 = np.genfromtxt('binAf_7.csv', delimiter=',')
# arq8 = np.genfromtxt('binAf_8.csv', delimiter=',')
# arq9 = np.genfromtxt('binAf_9.csv', delimiter=',')
# arq10 = np.genfromtxt('binAf_10.csv', delimiter=',')
# arq11 = np.genfromtxt('binAf_11.csv', delimiter=',')
# arq12 = np.genfromtxt('binAf_12.csv', delimiter=',')
# arq13 = np.genfromtxt('binAf_13.csv', delimiter=',')
# arq14 = np.genfromtxt('binAf_14.csv', delimiter=',')
# arq15 = np.genfromtxt('binAf_15.csv', delimiter=',')
# arq16 = np.genfromtxt('binAf_16.csv', delimiter=',')
# arq17 = np.genfromtxt('binAf_17.csv', delimiter=',')
# arq18 = np.genfromtxt('binAf_18.csv', delimiter=',')
# arq19 = np.genfromtxt('binAf_19.csv', delimiter=',')
# arq20 = np.genfromtxt('binAf_20.csv', delimiter=',')
# arq21 = np.genfromtxt('binAf_21.csv', delimiter=',')
# arq22 = np.genfromtxt('binAf_22.csv', delimiter=',')
# arq23 = np.genfromtxt('binAf_23.csv', delimiter=',')
# arq24 = np.genfromtxt('binAf_24.csv', delimiter=',')
# arq25 = np.genfromtxt('binAf_25.csv', delimiter=',')
# arq26 = np.genfromtxt('binAf_26.csv', delimiter=',')
# arq27 = np.genfromtxt('binAf_27.csv', delimiter=',')
# arq28 = np.genfromtxt('binAf_28.csv', delimiter=',')
# arq29 = np.genfromtxt('binAf_29.csv', delimiter=',')
# arq30 = np.genfromtxt('binAf_30.csv', delimiter=',')

# tempArquivos[0] = np.genfromtxt('binAf_1.csv', delimiter=',')
# tempArquivos[1] = np.genfromtxt('binAf_2.csv', delimiter=',')
# tempArquivos[2] = np.genfromtxt('binAf_3.csv', delimiter=',')
# tempArquivos[3] = np.genfromtxt('binAf_4.csv', delimiter=',')
# tempArquivos[4]= np.genfromtxt('binAf_5.csv', delimiter=',')
# tempArquivos[5] = np.genfromtxt('binAf_6.csv', delimiter=',')
# tempArquivos[6] = np.genfromtxt('binAf_7.csv', delimiter=',')
# tempArquivos[7] = np.genfromtxt('binAf_8.csv', delimiter=',')
# tempArquivos[8] = np.genfromtxt('binAf_9.csv', delimiter=',')
# tempArquivos[9] = np.genfromtxt('binAf_10.csv', delimiter=',')
# tempArquivos[10] = np.genfromtxt('binAf_11.csv', delimiter=',')
# tempArquivos[11] = np.genfromtxt('binAf_12.csv', delimiter=',')
# tempArquivos[12] = np.genfromtxt('binAf_13.csv', delimiter=',')
# tempArquivos[13] = np.genfromtxt('binAf_14.csv', delimiter=',')
# tempArquivos[14] = np.genfromtxt('binAf_15.csv', delimiter=',')
# tempArquivos[15] = np.genfromtxt('binAf_16.csv', delimiter=',')
# tempArquivos[16] = np.genfromtxt('binAf_17.csv', delimiter=',')
# tempArquivos[17] = np.genfromtxt('binAf_18.csv', delimiter=',')
# tempArquivos[18] = np.genfromtxt('binAf_19.csv', delimiter=',')
# tempArquivos[19] = np.genfromtxt('binAf_20.csv', delimiter=',')
# tempArquivos[20] = np.genfromtxt('binAf_21.csv', delimiter=',')
# tempArquivos[21] = np.genfromtxt('binAf_22.csv', delimiter=',')
# tempArquivos[22] = np.genfromtxt('binAf_23.csv', delimiter=',')
# tempArquivos[23] = np.genfromtxt('binAf_24.csv', delimiter=',')
# tempArquivos[24] = np.genfromtxt('binAf_25.csv', delimiter=',')
# tempArquivos[25] = np.genfromtxt('binAf_26.csv', delimiter=',')
# tempArquivos[26] = np.genfromtxt('binAf_27.csv', delimiter=',')
# tempArquivos[27] = np.genfromtxt('binAf_28.csv', delimiter=',')
# tempArquivos[28] = np.genfromtxt('binAf_29.csv', delimiter=',')
# tempArquivos[29] = np.genfromtxt('binAf_30.csv', delimiter=',')




# ===============================================================================
# Formato arquivos dos bits estaveis
# ===============================================================================
#array que armazena os valores
arrayUnos_e_zeros = np.array([], dtype=int)


# ===============================================================================
# Formato arquivo porcentagem de bits
# ===============================================================================

#array que armazena os valores
arrayPromedios = np.array([], dtype=float)


# ===============================================================================
# Funcao para carregar os csv em memoria
# ===============================================================================


	




quantLinhas= tamanhoCSV(nomeTest) #coloquei um nome de um arquivo q vou usar para saber a quantida de linhas q tem
for linha in range(quantLinhas):
	print("to na linha ", linha)
	for elem in range(128):

		# Estableco as variaveis que vou usar para analisar os mesmos elementos de cada arquivo
		arrayLinha = np.array([], dtype=int)
		# print("tamahno array antes ", len(arrayLinha))
		unos = 0
		zeros = 0
		# print("total de unos ", unos, " total de zeros ", zeros)


		for arq in range(30): #aqui deve indicar a quantidade de arquivos que serao analizados
			num = str(arq+1)
			nomeCompleto = nome+num+ext
			# print("Processando arquivo ", nomeCompleto, " linha ", linha, " elemento ", elem)

			#for para abrir cada arquivo na mesma posicao
			with open(nomeCompleto, 'r') as arquivo:
				linhas = list(csv.reader(arquivo))

				
				elementoEspecifico = linhas[linha][elem] # primeiro é a linha e o segundo o a elemento
				# print("Processando arquivo ", nomeCompleto, " linha ", linha, " elemento ", elem)
				arrayLinha = np.append(arrayLinha, int(elementoEspecifico))
				# print(arrayLinha)

		#aqui deve colocar um elemento a cada 30 leituras
		# print("Tamanho atual do array uno e zeros ", len(arrayUnos_e_zeros))
		




			

		#===============================================================================
		# Aqui trato as informacoes dos valores obtidos na mesma posicao de cada arquivo
		#===============================================================================
		
		for elemArrayElem in arrayLinha: # for para separar quantos unos e zeros tenho e assim calcular probabilidades
			if(elemArrayElem == 1):
				unos+=1
			else:
				zeros+=1
			
		# print("total de unos ", unos, " total de zeros ", zeros)
	


		base = 30
		resultadoEstatistico = 0 

		if(unos > zeros):
			# print("Tendencia em 1")
			arrayUnos_e_zeros = np.append(arrayUnos_e_zeros, 1)

			resultadoEstatistico = unos/base
			arrayPromedios = np.append(arrayPromedios, resultadoEstatistico)

		elif(zeros > unos):
			# print("tendencia em 0")
			arrayUnos_e_zeros = np.append(arrayUnos_e_zeros, 0)

			resultadoEstatistico =  zeros/base
			arrayPromedios = np.append(arrayPromedios, resultadoEstatistico)
		else:
			# print("tendencia igual")
			arrayUnos_e_zeros = np.append(arrayUnos_e_zeros, 2)

			resultadoEstatistico = 15/30
			arrayPromedios = np.append(arrayPromedios, resultadoEstatistico)



		#fim for de ler os 30 arquivos

		
	#fim for dos elementos
#fim for da linhas

np.savetxt('mapaUnosZeros.csv', [arrayUnos_e_zeros], fmt="%d", delimiter =', ')
np.savetxt('mapaEstatistico.csv', [arrayPromedios], fmt="%.4f", delimiter =', ')




