# -*- coding: utf-8 -*-
"""
Created on Sun Jan 19 21:53:37 2020

@author: paulo
"""

#Imports
import os
import pandas as pd

#Coletando dados dos arquivos ja tratados
caminho = u"C:\\Users\\paulo\\Documents\\CamaraDeputados\\Dados\\arquivos_simplificados\\"
arquivos = [open(caminho + arq).read().splitlines() for arq in os.listdir(caminho)]
headers = arquivos[0][0]

#Unindo dados de todos os arquivos
votacoes = []
for arq in arquivos:
	for voto in arq[1:]:
		votacoes.append(voto)
		
#Arquivo completo de votos para visualizacao apenas
fileopen = open(caminho + "dados.csv","w")
fileopen.write(headers + "\n")
fileopen.writelines([voto.strip() + "\n" for voto in votacoes[:-1]])
fileopen.close()

#Dataframe de votos
df = pd.DataFrame([voto.split(";") for voto in votacoes],columns = headers.split(";"))