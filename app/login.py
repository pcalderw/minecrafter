from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, IntegerField, ValidationError
from wtforms.validators import DataRequired
from datetime import datetime


def is18(form, field):
    secs = field.data
    years = (datetime.now() - datetime.fromtimestamp(secs)).days/365.2425
    if years < 21:
        raise ValidationError(f'You must be 21 years old to use this cool server, you\'r only {years} years old')
    if years >=50:
        raise ValidationError(f'Liar anyone over 50 can\'t use a computer.')
    if years >=30:
        raise ValidationError(f'You\'re {years} years old, too old. Go away.')


class LoginForm(FlaskForm):
    age = IntegerField('How Many Seconds Have You Been Alive?', validators=[DataRequired(), is18])
    submit = SubmitField('Make me real')

