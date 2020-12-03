import pandas as pd
from pandas import json_normalize as jsn

import requests as req

    
def json_to_dataframe(apiloc="127.0.0.1:5000",list_name="cryptolist"):
    payload = req.get(f"http://{apiloc}/{list_name}").json()
    return jsn(payload,('news' if list_name=="newslist" else 'Crypto'))   

def news_request(article_count=12, stream_sentiment_data=False):

    pressed = json_to_dataframe(list_name='newslist')

    def article_to_www(articles):
        for i in range(len(articles)):
            yield f"<a href=\"{articles['newsArticleWWW'][i]}\">{articles['newsArticle'][i]}</a>"

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
                                        justify='left',
                                        bold_rows=True,
                                        border=0,
                                        index_names=False,
                                        classes=['table table-sm','small-text'])

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


def crypto_request(index_count=12):

    crypt_list = json_to_dataframe(list_name='cryptolist')

    crypt_list.set_index(crypt_list['cryptoName'], inplace=True)
    crypt_list = crypt_list.drop(labels=['cryptoName','cryptoDate','cryptoId', 'cryptoCreationDate'], axis=1)
    crypt_list.columns = ['Price','PriceCap','Volume','Circulation']
    crypt_list = crypt_list[:index_count].to_html(render_links=True, 
                                        escape=False, 
                                        header=True,
                                        bold_rows=True,
                                        border=0,
                                        justify="left",
                                        index_names=False,
                                        classes=['table table-sm','small-text'])

    return crypt_list

def main():
    pass


if __name__=='__main__':
    main()