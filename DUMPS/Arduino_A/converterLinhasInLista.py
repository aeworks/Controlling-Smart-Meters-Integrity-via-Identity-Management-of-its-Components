#!/usr/bin/env python
# coding=utf-8


def converterEmList():

	totalArquivos = 30
	

	#fomato dos arquivos a formatar
	nomeCsv = "bin"
	nomeArduino = "A_"
	extensao = ".csv"
	
	
	#formato do arquivo que vou criar
	nomeArduinoFormatado = "Af_"

	
	#percorro cada arquivo
	for i in range(totalArquivos):

		num = i+1;
		numCsvInt = str(num)
		nomeCompleto = nomeCsv+nomeArduino+numCsvInt+extensao
		nomeCompletoFormatado = nomeCsv+nomeArduinoFormatado+numCsvInt+extensao
		
		# abro cada arquivo
		arquivo = open(nomeCompleto,"r")
		for linha in arquivo:
			a = ""
			# print(list(linha))
			arquivo2 = open(nomeCompletoFormatado, "a")

			#formatando a linha para que fique como um csv
			linhaAtual = str(list(linha.rstrip('\n')))
			linhaAtual = linhaAtual.replace(" ", "")
			linhaAtual = linhaAtual.replace("'", "")
			linhaAtual = linhaAtual.replace("[", "")
			linhaAtual = linhaAtual.replace("]", "")
			linhaAtual = linhaAtual.replace(",,", ",")


			#armazeno o valor no arquivo
			arquivo2.write(linhaAtual)
			arquivo2.write("\n")
			arquivo2.close()

	arquivo.close()



converterEmList()