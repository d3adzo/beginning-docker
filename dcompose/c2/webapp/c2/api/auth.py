from flask import request
from flask import render_template
from flask import redirect, url_for
from flask import session

from c2 import app
from c2.app import get_db
from c2.database import auth


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        conn = get_db()
        auth_status, user_name = auth.authenticate_user(conn, request.form['username'], request.form['password'])
        if auth_status:
            session['username'] = user_name
            return redirect(url_for('index'))
        return redirect(url_for('login'))
    else:
        return render_template('login.html')


@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('index'))


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        conn = get_db()
        if auth.add_user(conn, request.form['email'], request.form['username'], request.form['password']):
            return redirect(url_for('login'))
        else:
            return "Error creating user. Make sure to fill out all details."
    else:
        if session.get("username") is None:
            return render_template('signup.html')
        else:
            return redirect(url_for('index'))
