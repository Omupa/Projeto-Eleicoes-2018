import json, os
import pandas as pd

data_dir = "../data_new_teste/"
resultado = "resultados_teste"

model = {
    "tweet": [],
    "user": [],
    "alvaro": [],
    "amoedo": [],
    "bolsonaro": [],
    "boulos": [],
    "cirogomes": [],
    "daciolo": [],
    "eymael": [],
    "geraldo": [],
    "haddad": [],
    "henrique": [],
    "marina": []
}

dataframe = pd.DataFrame(model)

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

                row = {
                    "tweet": 0,
                    "user": 0,
                    "alvaro": 0,
                    "amoedo": 0,
                    "bolsonaro": 0,
                    "boulos": 0,
                    "cirogomes": 0,
                    "daciolo": 0,
                    "eymael": 0,
                    "geraldo": 0,
                    "haddad": 0,
                    "henrique": 0,
                    "marina": 0
                }
                
                row["tweet"] = linha.get('id_str')
                row["user"] = linha.get('user').get('id_str')

                for mention in linha.get('entities').get('user_mentions'):

                    if mention.get("id") == 73745956:
                        row["alvaro"] = 1

                    if mention.get("id") == 256730310:
                        row["amoedo"] = 1

                    if mention.get("id") == 128372940:
                        row["bolsonaro"] = 1

                    if mention.get("id") == 762402774260875265:
                        row["boulos"] = 1

                    if mention.get("id") == 33374761:
                        row["cirogomes"] = 1

                    if mention.get("id") == 989899804200325121:
                        row["daciolo"] = 1

                    if mention.get("id") == 73889361:
                        row["eymael"] = 1

                    if mention.get("id") == 74215006:
                        row["geraldo"] = 1

                    if mention.get("id") == 354095556:
                        row["haddad"] = 1

                    if mention.get("id") == 870030409890910210:
                        row["henrique"] = 1

                    if mention.get("id") == 105155795:
                        row["marina"] = 1

                dataframe = dataframe.append(row, ignore_index=True)

#dataframe = pd.DataFrame(saoRetweets.items(), columns=['type', 'count'])
dataframe.to_csv("../" + resultado + "/Correlacao_candidatos.csv", index=False)
