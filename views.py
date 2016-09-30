# Views.py
#
from server import app
from flask import render_template, redirect, flash
from forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
    user = {'nickname': 'Miguel'}
    return render_template('index.html', user= user)

@app.route('/login', methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('login requested for OpenID="%s", remember_me=%s' %
            (form.openid.data, str(form.remember_me.data)))
        return redirect('/index')
    return render_template('login.html', title="Sign In", form = form,
                           providers=app.config['OPENID_PROVIDERS'])
