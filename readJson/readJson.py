import pyorient

client = pyorient.OrientDB("localhost", 2480)
session_id = client.connect("root","Pivic2018")
client.db_open("eleicoesbrasil2018", "root", "Pivic2018")