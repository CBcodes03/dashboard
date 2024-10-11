#get the database ready
import json
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://cb101:randompass1234@cluster0.ki7ti.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0" 
client = MongoClient(uri, server_api=ServerApi('1'))

#open the json file
with open('/home/chirag/Desktop/blackcoffer/jsondata.json', 'r') as file:
    jdata = json.load(file)
db=client['database'] #database name here
collection = db['data'] #cluster name 
collection.insert_many(jdata) #insert many documents into the cluster
documents = collection.find()
#for doc in documents:
#    print(doc)

#!!!!!already done!!!!!