import os
from flask_login import (LoginManager)
from flask_openid import OpenID
from models import db, User

from config import basedir

from flask import Flask
app = Flask(__name__)
app.config.from_object('config')

from views import *
from models import *


lm = LoginManager()
lm.init_app(app)
lm.login_view = 'login'

@lm.user_loader
def load_user(username):
    return db.users.find_one({"_id": username})

oid = OpenID(app, os.path.join(basedir, 'tmp'))

if __name__ == '__main__':
    try:
        port = int(os.environ.get('PORT'))
    except ValueError:
        port = 5000
    app.run(debug=True, host='0.0.0.0', port=port)

