import os
from flask.ext.login import (LoginManager)
from flask.ext.openid import OpenID

from config import basedir

from flask import Flask
app = Flask(__name__)
app.config.from_object('config')

from views import *
from models import *


lm = LoginManager()
lm.init_app(app)
lm.login_view = 'login'

oid = OpenID(app, os.path.join(basedir, 'tmp'))

if __name__ == '__main__':
    try:
        port = int(os.environ.get('PORT'))
    except ValueError:
        port = 5000
    app.run(debug=True, host='0.0.0.0', port=port)

