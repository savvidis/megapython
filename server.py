import os

from flask import Flask
app = Flask(__name__)
app.config.from_object('config')

from views import *
from models import *


if __name__ == '__main__':
    try:
        port = int(os.environ.get('PORT'))
    except ValueError:
        port = 5000
    app.run(debug=True, host='0.0.0.0', port=port)

