from app import app
from app.registration import RegistrationForm
from app.login import LoginForm
from flask import render_template, redirect

@app.route('/')
@app.route('/index')
@app.route('/registration')
@app.route('/register', methods=['GET','POST'])
def try_register():
    validation = app.config['registration_secret']
    regForm = RegistrationForm()
    if regForm.validate_on_submit():
        if regForm.password.data != app.config['registration_secret']:
            return registration(regForm.username.data, False)
        tryWhitelist(regForm.username.data)
        return registration(regForm.username.data, True)
    return registration()
    
def registration(uname=None, isAdded=False):
    regForm = RegistrationForm()
    return render_template('registration.html', title='Registration', form=regForm, whitelisted_username=uname, valid=isAdded)

@app.route('/admin')
def admin():
    return render_template('admin.html')

def tryWhitelist(uname):
    uname = ''.join(c for c in uname if c.isalnum() or c == '-' or c == '_')
    whitelist = f"whitelist add {uname}"
    runMinecraftCommand(whitelist)

import os
def runMinecraftCommand(cmd):
    cmd = f"screen -r minecraft -p 0 -X stuff \"{cmd}$(printf '\r')\""
    result = os.system(cmd)
    return result


@app.route('/login', methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        return render_template('login.html', form=form)
    return render_template('login.html', form=form)