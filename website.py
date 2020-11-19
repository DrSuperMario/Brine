from flask import Flask, render_template, session, redirect, url_for

from forms import SignalForm

from models.data_reader import *
from models.test_connect import ConnectAndManage

app = Flask(__name__)
app.config['SECRET_KEY'] = "14cxTre7gHHou"
app.config['DEBUG'] = True

conn = ConnectAndManage()


@app.route('/', methods=['GET', 'POST'])
def home():

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
    with open('test.txt' ,'r') as r:
        pressed = r.read()
    print(pressed)    
    return render_template('home.html', pressed=pressed)


if __name__=="__main__":
    app.run()