from pymongo import MongoClient
from mongokat import Collection, Document

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



class User(Document):

    @property
    def is_authenticated(self):
        return True

    @property
    def is_active(self):
        return True

    @property
    def is_anonymous(self):
        return False

class UserCollection:
    document_class = User
