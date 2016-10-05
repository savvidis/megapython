from pymongo import MongoClient
from pymongo.errors import DuplicateKeyError
from mongokat import Collection, Document
from werkzeug.security import check_password_hash
from werkzeug.security import generate_password_hash
from flask.ext.login import UserMixin


client = MongoClient('mongodb://mongo:27017/sourcelair')

db = client.mega
def populate():
    collection = db.users
     # Ask for data to store
    user = raw_input("Enter your username: ")
    password = raw_input("Enter your password: ")
    pass_hash = generate_password_hash(password, method='pbkdf2:sha256')

     # Insert the user in the DB
    try:
        collection.insert({"_id": user, "password": pass_hash})
        print "User created."
    except DuplicateKeyError:
        print "User already present in DB."





class User():

    def __init__(self, username):
        self.username = username
        self.is_authenticated = true


    def get_id(self):
        return unicode(self.username)

    @staticmethod
    def validate_login(password_hash, password):
        return check_password_hash(password_hash, password)


