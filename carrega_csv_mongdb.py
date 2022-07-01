'''

Arquivo: carrega_csv_mongdb
Objetivo: carrega os arquivos csv original e tratado no MongoDB Atlas, um de cada vez, para isso devemos retirar o comentário nas linhas 25, 32 e 36

Autor: Carlos Bahia

'''
import csv
import matplotlib.pyplot as plt
import pandas as pd
from modules.connector_mongodb import connector
from pymongo import MongoClient
import pymongo
from bson.json_util import dumps, loads



connection_DB= pymongo.MongoClient(f"mongodb+srv://soulcode:a1b2c3@cluster0.xweww.mongodb.net/atividade_individual?retryWrites=true&w=majority")

print("teste de conexão: ")
print(connection_DB)

print("teste de leitura do arquivo csv")
#df_dados = pd.read_csv("C:\\Users\\Dalva\\Downloads\\Soulcode\\Projeto Individual\\marketing_campaign_original.csv", sep  =';')
df_dados = pd.read_csv("C:\\Users\\Dalva\\Downloads\\Soulcode\\Projeto Individual\\marketing_campaign_tratado_final.csv", sep  =';')
print(df_dados)
# Converte de DF para Dicionário
data_dict = df_dados.to_dict(orient='records')

# Conecta ao banco de dados
#db = connection_DB.marketing_campaign_original
db = connection_DB.marketing_campaign_tratado

#  insere dados no MongoDB Atlas
#db.marketing_campaign_original.insert_many(data_dict)
db.marketing_campaign_tratado.insert_many(data_dict)

print('-------------------------------------------------------------')
print('Dados inseridos com sucesso  !!')
print(db)
print('-------------------------------------------------------------')
