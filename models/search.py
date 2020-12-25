from datetime import datetime
from dateutil import parser

import pandas as pd
import pandas_datareader as pdr



def search_ticker(ticker, search_start, search_field_end, download_button):

    if ticker:
        
        try:
            
            df = pdr.DataReader(ticker.upper(), 'yahoo', 
            start=(parser.parse(search_start) if search_start else datetime(2020,11,11)), 
            end=(parser.parse(search_field_end) if search_field_end else datetime.now()))
            stock = df.to_html(render_links=True, 
                                escape=False, 
                                header=True,
                                justify='left',
                                bold_rows=True,
                                border=0,
                                index_names=False,
                                classes=['table table-sm','small-text'])
            if download_button:
                print("Hwlllooo oasdas sa da \n\n\n")

            return stock
            
        except pdr._utils.RemoteDataError:
            return """
            </div> 
            <div class="center-text">
                <h1 class="lead">Error connecting server </h1> 
            </div>    
            """
        except KeyError:
            return """
            </div> 
            <div class="center-text">
                <h1 class="lead">Ticker Not found</h1> 
            </div>    
            """
    return False

        
    

