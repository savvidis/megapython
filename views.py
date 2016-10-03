# Views.py
#
from server import app, oid
from flask import render_template, flash, redirect, session, url_for, request, g
from flask.ext.login import login_user, logout_user, current_user, login_required
from forms import LoginForm
from models import UserCollection, db

@app.route('/')
def index2():
    user = g.user
    return render_template('base.html', user= user)

@app.route('/index')
@login_required
def index():
    user = g.user
    return render_template('index.html', user= user)

@app.route('/login', methods=["GET", "POST"])
@oid.loginhandler
def login():
    if g.user is not None and g.user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        session['remember_me'] = form.remember_me.data
        flash('login requested for OpenID="%s", remember_me=%s' %
        (form.openid.data, str(form.remember_me.data)))
        return oid.try_login(form.openid.data, ask_for=['nickname', 'email'])
    return render_template('login.html', title="Sign In", form = form,
                           providers=app.config['OPENID_PROVIDERS'])


@app.before_request
def before_request():
    g.user = current_user

@oid.after_login
def after_login(resp):
    if resp.email is None or resp.email == "":
        flash('Invalid login. Please try again')
        return redirect(url_for('login'))
    user = db.users.find_one({'email':resp.email})
    if user is None:
        nickname = resp.nickname
        if nickname is None or nickname == "":
            nickname = resp.email.split('@')[0]

        user = {"email": resp.email, "nickname": resp.nickname}
        db.users.insert(user)
    remember_me = False
    if 'remember_me' in session:
        remember_me = session['remember_me']
        session.pop('remember_me', None)
    login_user(user, remember  = remember_me)
    return redirect(request.args.get('next') or url_for('index'))

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

