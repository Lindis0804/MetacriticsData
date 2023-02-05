from pymongo import MongoClient
client = MongoClient('localhost',27017)
database = client['admin']
collection = database['films']
rec = {
}
rec['film'] = 'Black Panther 2'
rec['author'] = ["Ryan Coogler","Marvel"]
collection.insert_one(rec)

