import json, os, pandas

data_dir = "../data_new_2_turno/"
resultado = "resultados_2_turno"
candidato = {}

for folder in os.listdir(data_dir):
    print(folder)
    data = data_dir + folder + "/"
    count = 0

    for file in os.listdir(data):
        with open(data+file, 'r') as g:
            for line in g.readlines():
                #data = json.loads(line)
                count = count +1
    
    candidato[folder] = count

dataframe = pandas.DataFrame(candidato.items(), columns=['candidato', 'twitters'])
dataframe.to_csv("../" + resultado + "/Soma_twitter_por_candidato.csv", index=False)

