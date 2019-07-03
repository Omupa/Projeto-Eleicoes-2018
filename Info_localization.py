import json, os
import pandas as pd

data_dir = "../data_new_2_turno/"
resultado = "resultados_2_turno"
saoRetweets = {
    "geo": 0,
    "place": 0,
    "coordinates": 0,
    "none": 0
}

for folder in os.listdir(data_dir):
    print(folder)
    data = data_dir + folder + "/"

    if not os.path.exists("../" + resultado):
        break
    #    os.makedirs("./data_HistFreqUser/" + folder

    for file in os.listdir(data):
        with open(data+file, 'r') as g:
            for line in g.readlines():
                linha = json.loads(line)

                if linha.get('geo') != None:
                    soma = saoRetweets["geo"]
                    soma = soma + 1
                    saoRetweets["geo"] = soma

                if linha.get('place') != None:
                    soma = saoRetweets["place"]
                    soma = soma + 1
                    saoRetweets["place"] = soma

                if linha.get('coordinates') != None:
                    soma = saoRetweets["coordinates"]
                    soma = soma + 1
                    saoRetweets["coordinates"] = soma

                if linha.get('coordinates') == None and linha.get('place') == None and linha.get('geo') == None:
                    soma = saoRetweets["none"]
                    soma = soma + 1
                    saoRetweets["none"] = soma

dataframe = pd.DataFrame(saoRetweets.items(), columns=['type', 'count'])
dataframe.to_csv("../" + resultado + "/Info_localization.csv", index=False)
