from flask_wtf import FlaskForm
from wtforms import StringField, RadioField, SubmitField, TextField


class SignalForm(FlaskForm):
    #group_data = SubmitField('Get Data by Group')
    all_data = SubmitField('Get All Data')
    search_field = TextField('Search Signal by Name')
    search_field_button = SubmitField('Search Signal')


    """
    form = SignalForm()

    if form.validate_on_submit():
        if form.all_data.data:
            passed = get_all_data()
            return render_template('result.html', pressed=passed)
        elif form.search_field_button.data:
            session['search_field'] = form.search_field.data
            pressed = find_data_by_ticker(session['search_field'])
            return render_template('result.html', pressed = pressed)
    """