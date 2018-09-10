# project/users/forms.py

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired, Length, EqualTo, Email


class RegisterForm(FlaskForm):
    email = StringField('Email', validator=[
                        DataRequired(), Email(), Length(min=6, max=40)])
    password = PasswordField('Password', validator=[
        DataRequired(), Length(min=6, max=40)])
    confirm = PasswordField('Repeat Password', validator=[
                            DataRequired(), EqualTo('password')])
