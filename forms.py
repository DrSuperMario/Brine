from flask_wtf import FlaskForm
from wtforms import StringField, RadioField, SubmitField, TextField


class SignalForm(FlaskForm):
    #group_data = SubmitField('Get Data by Group')
    all_data = SubmitField('Get All Data')
    search_field = TextField('Search Signal by Name')
    search_field_button = SubmitField('Search Signal')

