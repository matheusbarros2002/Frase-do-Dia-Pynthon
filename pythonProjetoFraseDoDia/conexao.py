#conexão com banco de dados

from pymongo import MongoClient

client= MongoClient("mongodb://localhost:27017/")

#print(client.list_database_names())

meu_banco = client['famosos']
colecao = meu_banco['cadastro']
for item in colecao.find({'_id':0}, {'nome':1}):
    print(item)
