from pymongo import MongoClient
client = MongoClient("mongodb+srv://<id>:<password>!@cluster0.a6bcg.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")

db = client.test
doc = {
    'name':'bob',
    'age':27
}

db.users.insert_one(doc)