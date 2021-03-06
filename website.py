from flask import (
                    Flask, 
                    render_template, 
                    session, 
                    redirect, 
                    url_for, 
                    request, 
                    send_file
)

from datetime import datetime
from dateutil import parser

from forms import SignalForm
from models.search import SearchData

from apirequests import (
                         news_request, 
                         crypto_request, 
                         forex_request, 
                         stock_request
)    
from models.plotly import MakePlots

MP = MakePlots()


app = Flask(__name__)
app.config['SECRET_KEY'] = "14cxTre7gHHou"
app.config['DEBUG'] = True

def search_data(search_start=None, search_end=None):


    form = SignalForm(request.form)
    search_field_start = request.form.get('search_field_start')
    search_field_end = request.form.get('search_field_end') 
   
    #stupid but fast, replace in the future
    def check_date(date, date_type):
        if(date == '' or date == None):
            if(date_type == 'start'.lower()):
                return datetime(2020,11,11)
            elif(date_type== 'end'.lower()):
                return datetime.now()
        else:
            return parser.parse(date)
     
         

    plot = MP.make_single_plot(ticker_name=str(
                                               request.form.get('search_field')).upper(),
                                               start_t=check_date(search_field_start,'start'),
                                               end_t=check_date(search_field_end,'end')
            )    
    

    find_ticker = SearchData(form.search_field.data, 
                        search_start=check_date(search_field_start,'start'), 
                        search_field_end=check_date(search_field_end,'end'))
    
    #breakpoint()
    return plot,find_ticker.search_ticker(), find_ticker.search_info()


@app.route('/search', methods=['GET','POST']) 
def search():

    if request.method == 'POST':
        if request.form.get('download_button'):
            return send_file('static/temp/temp.csv',attachment_filename=f"{request.form.get('search_field')}.csv")

        search_field = request.form.get('search_field')
        plot, form, info = search_data()
      
        return render_template('search.html',
                                date_f="2020-11-11",
                                date_e=datetime.strftime(datetime.now(), '%Y-%m-%d'), 
                                form=form,
                                plot=plot,
                                info=info,
                                download_button_s = True,
                                search_field = search_field)

    return render_template('search.html')

@app.route('/', methods=['GET', 'POST'])
def home(): 

    if request.method == 'POST':
        plot, form, info = search_data()
        return render_template('search.html',date=datetime.now(),form=form, plot=plot, info=info)

    return render_template('home.html', home=True, pressed = news_request(article_count=14), crypt_list = crypto_request())

@app.route('/news', methods=['GET','POST'])
def news():

    if request.method == 'POST':
        plot, form ,info = search_data()
        return render_template('search.html',date=datetime.now(),form=form, plot=plot, info=info)

    return render_template('news.html',news_list=news_request(article_count=89, stream_sentiment_data=True),news=True)

@app.route('/crypto', methods=['GET','POST'])
def crypto():

    if request.method == 'POST':
        plot, form, info = search_data()
        return render_template('search.html',date=datetime.now(),form=form, plot=plot, info=info)

    return render_template('crypto.html',crypto_list=crypto_request(index_count=89),crypto=True)

@app.route('/forex', methods=['GET','POST'])
def forex():

    if request.method == 'POST':
        plot, form, info = search_data()
        return render_template('search.html',date=datetime.now(),form=form, plot=plot, info=info)

    return render_template('forex.html', forex_list = forex_request(), forex=True)

@app.route('/stock', methods=['GET','POST'])
def stock():

    if request.method == 'POST':
        plot, form, info = search_data()
        return render_template('search.html',date=datetime.now(),form=form, plot=plot, info=info)

    return render_template('stock.html', chart_data=stock_request(), stock=True)

@app.route('/api', methods=['GET','POST'])
def api():

    if request.method == 'POST':
        plot, form, info = search_data()
        return render_template('search.html',date=datetime.now(),form=form, plot=plot, info=info)

    return render_template('api.html')

@app.route('/about', methods=['GET','POST'])
def about():

    if request.method == 'POST':
        plot, form, info = search_data()
        return render_template('search.html',date=datetime.now(),form=form, plot=plot, info=info)

    return render_template('about.html')

@app.route('/signals', methods=['GET','POST'])
def signals():
    return render_template('signals.html')


if __name__=="__main__":
    app.run()
