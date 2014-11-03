#-*- coding:utf-8 -*-

from flask_wtf import Form
from wtforms import TextField, BooleanField, SubmitField
from wtforms.validators import Required

class LoginForm(Form):
    user_name = TextField('user_name', validators=[Required()])
    remember_me = BooleanField('remember me', default=False)
    submit = SubmitField('Sign in')
