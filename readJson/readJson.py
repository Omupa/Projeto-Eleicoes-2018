import pyorient

client = pyorient.OrientDB("localhost", 2480)
session_id = client.connect("root","Pivic2018")
client.db_open("demodb", "root", "Pivic2018")

print(client.command("select from Castles"))

client.shutdown("root", "Pivic2018")