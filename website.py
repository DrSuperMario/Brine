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

    pressed = json_to_dataframe(list_name='newslist')
    crypt_list = json_to_dataframe(list_name='cryptolist')

    crypt_list.set_index(crypt_list['cryptoName'], inplace=True)
    crypt_list = crypt_list.drop(labels=['cryptoName','cryptoDate','cryptoId', 'cryptoCreationDate'], axis=1)
    crypt_list.columns = ['Price','PriceCap','Volume','Circulation']
    crypt_list = crypt_list[:12].to_html(render_links=True, 
                                        escape=False, 
                                        header=True,
                                        bold_rows=True,
                                        border=0,
                                        justify="left",
                                        index_names=False,
                                        classes=['table table-sm','small-text'])

    def article_to_www(articles):
        for i in range(len(articles)):
            yield f"<a href=\"{articles['newsArticleWWW'][i]}\">{articles['newsArticle'][i]}</a>"
    
    df = pd.DataFrame(article_to_www(pressed),index=pressed['creationDate'], columns=['newsArticle'])
    pressed = df[:12].to_html(render_links=True, 
                                     escape=False, 
                                     header=False,
                                     bold_rows=True,
                                     border=0,
                                     index_names=False,
                                     classes=['table table-sm','small-text'])

    return render_template('home.html', pressed=pressed, crypt_list=crypt_list)


if __name__=="__main__":
    app.run(port=5050)