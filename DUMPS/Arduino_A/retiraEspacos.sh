#!/bin/bash

#este codigo retira os espacos que existem entre as colunas
cat binA_1.csv | sed 's/ //g' >> testeSemEspaco.csv