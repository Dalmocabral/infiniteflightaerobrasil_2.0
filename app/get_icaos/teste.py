import json 

with open('Planilha1.json') as json_file:
    dados = json.loads(json_file)

print(dados)    