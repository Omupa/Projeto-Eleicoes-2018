
import json, os

data_dir = "./data_new/"

for folder in os.listdir(data_dir):
    data = data_dir + folder + "/"

    if not os.path.exists("./data_id/" + folder):
        os.makedirs("./data_id/" + folder)

    data_id = open("./data_id/" + folder + "/data_id.txt", 'w')

    for file in os.listdir(data):
        with open(data+file, 'r') as g:
            tweets = g.readlines()
            for line in tweets:
                data = json.loads(line)
                data_id.write(data.get('user').get('id_str')+"\n")
data_id.close()
