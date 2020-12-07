from flask_wtf import FlaskForm
from wtforms import StringField, RadioField, SubmitField, TextField


class SignalForm(FlaskForm):

    search_field = StringField('Search Signal by Name')
    search_field_button = SubmitField('Search Signal')
