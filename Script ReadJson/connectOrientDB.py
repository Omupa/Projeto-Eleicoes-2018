import pyorient, sys

client = pyorient.OrientDB("localhost", 2480)
session_id = client.connect("root", "Pivic2018")
db_name = "eleicoes"
db_username = "root"
db_password = "Pivic2018"


#if client.db_exists( db_name, pyorient.STORAGE_TYPE_MEMORY ):
#    client.db_open( db_name, db_username, db_password )
#    print (db_name + " opened successfully")
#else:
#    print ("database [" + db_name + "] does not exist! session ending...")
#    sys.exit()