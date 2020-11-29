from flask import Flask, render_template, session, redirect, url_for

#from forms import SignalForm

from models.data_reader import *
from models.test_connect import ConnectAndManage
from apirequests import json_to_dataframe

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
    with open('crypt_list.txt','r') as f:
        crypt_list = f.read()

    pressed = json_to_dataframe(apiloc='127.0.0.1:5000', location='newslist', json_key='news')

    pressed.set_index(pressed['creationDate'], inplace=True)
    df=pressed.drop(['newsArticleWWW', 
            'articleDate', 
            'newsPolarityNeg', 
            'newsPolarityPos', 
            'newsPolarityNeu', 
            'creationDate',
            'newsArticleId'], axis=1)
    pressed = df[:14].to_html()

    return render_template('home.html', pressed=pressed, crypt_list=crypt_list)


if __name__=="__main__":
    app.run(port=5050)