import json, os
import pandas as pd

data_dir = "../data_new_1_turno/"
resultado = "resultados_1_turno"
saoRetweets = {
    "yes": 0,
    "no": 0
}

for folder in os.listdir(data_dir):
    print(folder)
    data = data_dir + folder + "/"

    #if not os.path.exists("./data_HistFreqUser/" + folder):
    #    os.makedirs("./data_HistFreqUser/" + folder)

    for file in os.listdir(data):
        with open(data+file, 'r') as g:
            for line in g.readlines():
                linha = json.loads(line)
                chave = linha.get('retweeted_status')
                if linha.get('retweeted_status') != None:
                    soma = saoRetweets["yes"]
                    soma = soma + 1
                    saoRetweets["yes"] = soma
                else:
                    soma = saoRetweets["no"]
                    soma = soma + 1
                    saoRetweets["no"] = soma

dataframe = pd.DataFrame(saoRetweets.items(), columns=['boolean', 'count'])
dataframe.to_csv("../" + resultado + "/Sao_retweets.csv", index=False)
