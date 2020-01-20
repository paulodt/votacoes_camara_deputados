# -*- coding: utf-8 -*-
"""
Created on Sun Jan 19 16:02:49 2020

@author: paulo
"""

"""Dados extraidos de 
https://www2.camara.leg.br/atividade-legislativa/plenario/resultadoVotacao"""

#Imports
import os

#Diretorio de arquivos de votacao
caminho = u"C:\\Users\\paulo\\Documents\\CamaraDeputados\\Dados\\"

#Arquivos com detalhes de votacao
arquivos_votacao = [arq for arq in os.listdir(caminho) if arq[0:2] == "LV"]
conteudo_arquivos_votacao = [open(caminho + arq).read() for arq in arquivos_votacao]

#Dados votacao
arquivos_detalhes_votacoes = [open(caminho + "HE" + arq[2:]).read() for arq in arquivos_votacao]
detalhes_votacoes = [arq.splitlines() for arq in arquivos_detalhes_votacoes]
datas_votacoes = [detalhes[2] for detalhes in detalhes_votacoes]

#Layout do arquivo
tamanhos_partes = [10,7,40,10,10,25,3]
codigo_partes = ["data","header", "votacao","nome_parlamentar","voto","sigla_partido","UF","codigo_parlamentar"]

#Tabulando linhas
arquivos_quebrados = [f.splitlines() for f in conteudo_arquivos_votacao]
arquivos_tabulados = []

for n in range(len(arquivos_quebrados)):
    arq = arquivos_quebrados[n]
    linhas_tabuladas = []
    for linha in arq:
        linha_tabulada = [datas_votacoes[n]]
        pos = 0
        for tam in tamanhos_partes:
            linha_tabulada.append(linha[pos:pos+tam].strip())
            pos += tam
        linhas_tabuladas.append(linha_tabulada)
    arquivos_tabulados.append(linhas_tabuladas)
    
#Arquivos simplificados de votacao
for arq in arquivos_tabulados:
	if(arq[0][1][0] == "C"):
	    fileopen = open(caminho + "arquivos_simplificados\\" + arq[0][1] + arq[0][2] + ".txt","w")
	    fileopen.write(";".join(codigo_partes) + "\n")
	    fileopen.writelines([";".join(linha) + "\n" for linha in arq[:-1]])
	    fileopen.write(";".join(arq[-1])) #evitar quebra de linha na última linha
	    fileopen.close()