#!/usr/bin/env python
import requests
import os
import flask
from flask import Flask, flash, redirect, render_template, request, session, abort,url_for
import sqlalchemy
from sqlalchemy import *
from sqlalchemy.orm.session import sessionmaker
#os.chdir("/app")
db=create_engine('sqlite:///userlogin.db',connect_args={'check_same_thread': False})
appnew = Flask(__name__)
metadata=MetaData()
metadata.bind=db
conn=db.connect()
Newusers=Table('userdata',metadata,autoload=True,autoload_with=db)
@appnew.route('/login')
def login():
    return render_template('login.html')
@appnew.route('/login', methods=['POST'])
def do_login():
    #return render_template('login.html')
    POST_USERNAME = str(request.form['username'])
    POST_PASSWORD = str(request.form['password'])
    Session=sessionmaker(bind=db)
    s=Session()
    query=s.query(Newusers).filter(Newusers.c.username.in_([POST_USERNAME]),Newusers.c.password.in_([POST_PASSWORD]))
    result=query.first()
    if(result):
        session['logged_in']=True
        session['username']=request.form['username']
        #return redirect(url_for('Orgunits_list'))
        return  "Logged in successfully" + "<br>" +"<br>" +"<b><a href = '/logout'>click here to log out</a></b>"
        #return  redirect(url_for('details1'))
        #return redirect(url_for('displaycsvfile'))
        #return redirect(url_for('home'))
    else:
        return "Invalid Attempt <br><a href = '/login'></b>" + \
        "click here to log in</b></a>"
@appnew.route('/logout')
def logout():
    session['logged_in']=False
    session.pop('username', None)
    return redirect(url_for('login'))
if __name__ == '__main__':
    appnew.secret_key = os.urandom(12)
    appnew.run(debug=True)
    application=appnew





    
