# Views.py
#
from server import app
from flask import render_template, flash, redirect, session, url_for, request, g
from flask.ext.login import login_user, logout_user, login_required, current_user
from forms import LoginForm
from models import db, User, populate



@app.route('/')
def index2():
    user = {}
    return render_template('base.html', user= user)

@app.route('/index')
def index():
    user = g.user
    user['nickname'] = g.user['_id']
    print user
    return render_template('index.html', user= user)

@app.route('/login', methods=["GET", "POST"])
def login():
    print "My g user:", g.user
    if g.user is not None:
        return redirect(url_for('index'))
    form = LoginForm()
    if request.method == 'POST' and form.validate_on_submit():
        user = db.users.find_one({"_id": form.username.data})
        print "User:", user
        if user and User.validate_login(user['password'], form.password.data):
            print "MY ID IS : " , user['_id']
            user_obj = User(user['_id'])
            print "MY Class IS : ", user_obj.is_authenticated
            login_user(user_obj)
            flash("Logged in successfully!", category='success')
            current_user =  user_obj
            return redirect(request.args.get("next") or url_for("index"))
        else:
            print "Error Cannot validate"
            flash("Error Cannot validate", category='success')
    else:
        flash("cannot validate form", category='success')
    return render_template('login.html', title="Sign In", form = form,
                           providers=app.config['OPENID_PROVIDERS'])


@app.before_request
def before_request():
    g.user = current_user

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))





