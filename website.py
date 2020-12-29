from flask import Flask, render_template, session, redirect, url_for, request
from datetime import datetime

from forms import SignalForm
from models.search import search_ticker

from apirequests import news_request, crypto_request, forex_request
import models.plotly as mlpt





app = Flask(__name__)
app.config['SECRET_KEY'] = "14cxTre7gHHou"
app.config['DEBUG'] = True

def search_data(search_start="", search_end=""):

    form = SignalForm(request.form)
    search_field_start = request.form.get('search_field_start')
    search_field_end = request.form.get('search_field_end')
   
    return search_ticker(form.search_field.data, 
                        search_start=("" if search_start is None else search_field_start), 
                        search_field_end=("" if search_end is None else search_field_end),
                        )

@app.route('/search', methods=['GET','POST']) 
def search():

    if request.method == 'POST':
        search_field = request.form.get('search_field')

        return render_template('search.html',
                            date=datetime.now(), 
                            form=search_data(),
                            search_field = search_field)

    return render_template('search.html')

@app.route('/', methods=['GET', 'POST'])
def home():

    if request.method == 'POST':
        return render_template('search.html',date=datetime.now(), form=search_data())

    return render_template('home.html', home=True, pressed = news_request(article_count=14), crypt_list = crypto_request())

@app.route('/news', methods=['GET','POST'])
def news():

    if request.method == 'POST':
        return render_template('search.html',date=datetime.now(), form=search_data())

    return render_template('news.html',news_list=news_request(article_count=89, stream_sentiment_data=True),news=True)

@app.route('/crypto', methods=['GET','POST'])
def crypto():

    if request.method == 'POST':
        return render_template('search.html',date=datetime.now(), form=search_data())

    return render_template('crypto.html',crypto_list=crypto_request(index_count=89),crypto=True)

@app.route('/forex', methods=['GET','POST'])
def forex():

    if request.method == 'POST':
        return render_template('search.html',date=datetime.now(), form=search_data())

    return render_template('forex.html', forex_list = forex_request(), forex=True)

@app.route('/stock', methods=['GET','POST'])
def stock():

    if request.method == 'POST':
        return render_template('search.html', form=search_data())

    return render_template('stock.html', chart_data=mlpt.plot_data_to_html(), stock=True)

@app.route('/api', methods=['GET','POST'])
def api():

    if request.method == 'POST':
        return render_template('search.html',date=datetime.now(), form=search_data())

    return render_template('api.html')

@app.route('/about', methods=['GET','POST'])
def about():

    if request.method == 'POST':
        return render_template('search.html',date=datetime.now(), form=search_data())

    return render_template('about.html')


if __name__=="__main__":
    app.run()
