from datetime import datetime

import pandas as pd
import pandas_datareader as pdr

start = datetime(2020,11,11)
end = datetime.now()


def search_ticker(ticker=str):
    try:
        df = pdr.DataReader(ticker.upper(), 'yahoo', start=start, end=end)
        stock = df.to_html(render_links=True, 
                            escape=False, 
                            header=True,
                            justify='left',
                            bold_rows=True,
                            border=0,
                            index_names=False,
                            classes=['table table-sm','small-text'])
    except:
        return """
        </div> 
        <div class="center-text">
            <h1 class="lead">Ticker not found </h1> 
        </div>    
        """

    return stock