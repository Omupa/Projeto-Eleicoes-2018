import json, os
import pandas as pd

data_dir = "../data_new_2_turno/"
resultado = "resultados_2_turno"
userFreq = {}
inicio = 1

for folder in os.listdir(data_dir):
    print(folder)
    data = data_dir + folder + "/"

    #if not os.path.exists("./data_HistFreqUser/" + folder):
    #    os.makedirs("./data_HistFreqUser/" + folder)

    for file in os.listdir(data):
        with open(data+file, 'r') as g:
            for line in g.readlines():
                linha = json.loads(line)
                chave = linha.get('user').get('id')
                if chave in userFreq:
                    soma = userFreq[linha.get('user').get('id')]
                    soma = soma + 1
                    userFreq[linha.get('user').get('id')] = soma
                else:
                    userFreq[linha.get('user').get('id')] = inicio

dataframe = pd.DataFrame(userFreq.items(), columns=['id', 'twitters'])
dataframe.to_csv("../" + resultado + "/Frequencia_por_usuario.csv", index=False)
