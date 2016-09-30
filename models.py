from pymongo import MongoClient

client = MongoClient('mongodb://mongo:27017/sourcelair')

db = client.mega

import datetime

myrecord = {
        "nickname": "Boron",
        "name" : "Spyros",
        "email" : "sabbidis@gmail.com",
        "date" : datetime.datetime.utcnow()
        }

spyros = db.users.find_one({"name":"Spyros"})
print spyros

if spyros is None:
    db.users.insert(myrecord)

print db.users.find({})
