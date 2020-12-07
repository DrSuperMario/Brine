from flask import Flask, render_template, session, redirect, url_for, request

from forms import SignalForm
from models.search import search_ticker

from apirequests import news_request, crypto_request
import models.plotly as mlpt

app = Flask(__name__)
app.config['SECRET_KEY'] = "14cxTre7gHHou"
app.config['DEBUG'] = True


@app.route('/', methods=['GET', 'POST'])
def home():

    form = SignalForm(request.form)

    if request.method == 'POST':
        search = search_ticker(form.search_field.data)
        return render_template('search.html', form=search)

    return render_template('home.html', home=True, pressed = news_request(article_count=13), crypt_list = crypto_request())

@app.route('/news', methods=['GET'])
def news():
    return render_template('news.html',news_list=news_request(article_count=89, stream_sentiment_data=True),news=True)

@app.route('/crypto', methods=['GET'])
def crypto():
    return render_template('crypto.html',crypto_list=crypto_request(index_count=89),crypto=True)

@app.route('/forex', methods=['GET'])
def forex():
    return render_template('forex.html', forex=True)

@app.route('/stock', methods=['GET','POST'])
def stock():
    return render_template('stock.html', chart_data=mlpt.plot_data_to_html(), stock=True)

if __name__=="__main__":
    app.run(port=5050)