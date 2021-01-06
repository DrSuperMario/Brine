from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DateField


class SignalForm(FlaskForm):

    search_field = StringField('Search Signal by Name')
    search_field_button = SubmitField('Search Signal')
    search_field_start = DateField('start')
    search_field_end = DateField('end')
    search_ticker_button = SubmitField('Search Button')
