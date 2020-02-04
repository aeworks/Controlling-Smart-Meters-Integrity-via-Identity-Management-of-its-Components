#!/bin/bash

#Este codigo faz que nao fiquem espacos apos cada linha
#IMPORTANTE!! ele corta a primeira linha do texto, deve entao deixar uma linha vazia no inicio para
# nao apagar informacao do dateset
cat DumpBase_A_30 | while read line
do
cut -b -47 |tee hexBaseA_30.csv
done
rm DumpBase_A_30
