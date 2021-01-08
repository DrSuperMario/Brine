import requests as req
from bs4 import BeautifulSoup as BS
import os

import pandas_datareader as pdr



class SearchData():

    def __init__(self, ticker, search_start, search_field_end):
        self.ticker = ticker
        self.search_start = search_start
        self.search_field_end = search_field_end    
    
    
    def search_ticker(self):
            

        if(self.ticker):
            
            try:
                global df
                global stock
                #breakpoint()
                df = pdr.DataReader(self.ticker.upper(), 'yahoo', 
                                    start=self.search_start, 
                                    end=self.search_field_end)
                stock = df.to_html(render_links=True, 
                                    escape=False, 
                                    header=True,
                                    justify='right',
                                    bold_rows=True,
                                    border=0,
                                    index_names=False,
                                    classes=['table table-sm','small-text'])

                if(os.path.exists('static/temp/temp.csv')):
                    os.remove('static/temp/temp.csv')

                df.to_csv('static/temp/temp.csv')

                
            except pdr._utils.RemoteDataError:
                return """
                </div> 
                <div class="center-text">
                    <h1 class="lead">Sorry No data to Show :(  </h1> 
                </div>    
                """
            except KeyError:
                return """
                </div> 
                <div class="center-text">
                    <h1 class="lead">Ticker Not found</h1> 
                </div>    
                """
            
        return stock


    def search_info(self):
        S = req.Session()
        URL = f"https://www.marketwatch.com/investing/stock/{self.ticker.lower()}"
        R = S.get(url=URL,headers={'agent_desktop':
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
        'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 '
        'Safari/537.36',}).content
        try:
            descp = BS(R, features="lxml").find_all('p',{"class","description__text"})[0].get_text()
        except IndexError:
            descp = """ </div> 
                <div class="center-text">
                    <h2 class="lead">Nothing Found</h1> 
                </div>   """ 

        return descp

            
        

