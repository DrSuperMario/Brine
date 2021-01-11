import pandas as pd
from pandas import json_normalize as jsn

#import os

import requests as req


def save_data_to_json(data, source):
    #check if data is there or empty then it would not ovserwrite full file
    if(len(str(data)) <= 15 or len(str(data)) > 50):
        data.to_json(f"temp/{source}.json")

    return None


def json_to_dataframe(apiloc="brinenewsapi.herokuapp.com",list_name="cryptolist"):

    def list_name_check(list_name):

        if(list_name=="newslist"): return "news"
        elif(list_name=="cryptolist"): return "Crypto"
        elif(list_name=="forexlist"): return "forex"
        elif(list_name=="stocklist"): return "stock"
        else: return "Error no List specified use (cryptolist , forexlist, newslist, stocklist)"
    
    try:    

        payload = req.get(f"http://{apiloc}/{list_name}").json()
        print(len(str(payload)))
        if(len(str(payload)) <=  15):
            return pd.read_json(f"temp/{list_name_check(list_name)}.json")
        
        return jsn(payload,list_name_check(list_name))
        

    except req.exceptions.ConnectionError:
        #breakpoint()
        return pd.read_json(f"temp/{list_name_check(list_name)}.json")


def news_request(article_count=12, stream_sentiment_data=False):
    
    pressed = json_to_dataframe(list_name='newslist')

    save_data_to_json(pressed, source="news")

    def article_to_www(articles):

        def shorten_link(link, lenght):
            if(len(link) > lenght):
                return link[:lenght] + "...."
            return link

        for i in range(len(articles)):
            yield f"<a href=\"{articles['newsArticleWWW'][i]}\" target=\"_blank\" title=\"{articles['newsArticle'][i]}\">{shorten_link(articles['newsArticle'][i], lenght=80)}</a>"

    if(stream_sentiment_data):

        df = pd.DataFrame(article_to_www(pressed))
        df = pd.concat([df,pressed['newsPolarityNeg'],
                           pressed['newsPolarityPos'],
                           pressed['newsPolarityNeu']], 
                       axis=1, ignore_index=True)
        df.columns = ['Article', 'Negative','Positive','Neutral']

        df.set_index(pressed['creationDate'], inplace=True)

        pressed = df[:article_count].to_html(render_links=True, 
                                        escape=False, 
                                        header=True,
                                        justify='right',
                                        bold_rows=True,
                                        border=0,
                                        index_names=False,
                                        classes=['table table-sm','small-text td-left'])

    else:   

        df = pd.DataFrame(article_to_www(pressed),index=pressed['creationDate'], columns=['newsArticle'])
    
        pressed = df[:article_count].to_html(render_links=True, 
                                            escape=False, 
                                            header=False,
                                            bold_rows=True,
                                            border=0,
                                            index_names=False,
                                            classes=['table table-sm','small-text'])

    return pressed


def crypto_request(index_count=13):

    crypt_list = json_to_dataframe(list_name='cryptolist')

    save_data_to_json(crypt_list, source="Crypto")

    crypt_list.set_index(crypt_list['cryptoName'], inplace=True)
    crypt_list = crypt_list.drop(labels=['cryptoName','cryptoDate','cryptoId', 'cryptoCreationDate'], axis=1)
    crypt_list.columns = ['Price','PriceCap','Volume','Circulation']
    crypt_list = crypt_list[:index_count].to_html(render_links=True, 
                                        escape=False, 
                                        header=True,
                                        bold_rows=True,
                                        border=0,
                                        justify="right",
                                        index_names=False,
                                        classes=['table table-sm','small-text'])

    return crypt_list

def forex_request():

    forex_list = json_to_dataframe(list_name='forexlist')

    save_data_to_json(forex_list, source="forex")

    forex_list.set_index(forex_list['forexTag'], inplace=True)
    forex_list = forex_list.drop(labels=['forexTag', 'forexId', 'forexDate'], axis=1)
    forex_list.columns = ['Name', 'Change', 'High', 'Bid', 'Low', 'Open']
    forex_list = forex_list.to_html(render_links=True, 
                                        escape=False, 
                                        header=True,
                                        bold_rows=True,
                                        border=0,
                                        justify="right",
                                        index_names=False,
                                        classes=['table table-sm','small-text'])
    return forex_list

def stock_request():

    stock_list = json_to_dataframe(list_name='stocklist')

    save_data_to_json(stock_list, source="stock")

    stock_list.set_index(stock_list['stockName'], inplace=True)
    stock_list = stock_list.drop(labels=['stockName','stockId', 'stockCreationDate'], axis=1)

    stock_list.columns = ['Low', 'Last', 'High', 'Change', 'Change%']
    stock_list = stock_list.to_html(render_links=True, 
                                        escape=False, 
                                        header=True,
                                        bold_rows=True,
                                        border=0,
                                        justify="right",
                                        index_names=False,
                                        classes=['table table-sm','small-text'])
    return stock_list


def main():
    pass


if __name__=='__main__':
    main()