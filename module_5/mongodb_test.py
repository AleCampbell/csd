
from pymongo import MongoClient

url = "mongodb+srv://admin:admin@cluster0.fk51n.mongodb.net/pytech"

# connect to the MongoDB cluster 
client = MongoClient(url)


db = client.pytech
 
print("\n -- Pytech Collection List --")
print(db.list_collection_names())

input("\n\n  End of program, press any key to exit... ")