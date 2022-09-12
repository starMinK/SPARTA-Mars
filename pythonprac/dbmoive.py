from pymongo import MongoClient
client = MongoClient('mongodb+srv://idvalue:passwordvalue@Cluster0.vlj5yqv.mongodb.net/?retryWrites=true&w=majority')
db = client.dbsparta

db.movies.update_one({'title': '가버나움'},{'$set':{'star': "0"}})