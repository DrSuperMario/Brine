from datetime import datetime


import matplotlib.pyplot as plt
import mpld3
import pandas as pd
import pandas_datareader as pdr


start = datetime(2020,11,11)
end = datetime.now()


def search_ticker(ticker_name='TSLA'):
    return pdr.DataReader(ticker_name, 'yahoo', start=start, end=end)



def plot_data_to_html():

    list_of_tickers = {'AAPL':'Apple',
                        'HPQ':'HP',
                        'MSFT':'Microsoft',
                        'TSLA':'Tesla',
                        'GOOGL':'Google',
                        'AMZN':'Amazon'}

    
    def make_plots(plot_dimensions=(2,3) , **list_of_tickers):
        
        fig, axs= plt.subplots(*plot_dimensions, figsize=(10,6))
        axs = axs.flatten()
        fig.subplots_adjust(hspace = 0.4)

        dimensions = plot_dimensions[0] * plot_dimensions[1]
        
        for i in range(dimensions):
            for k, v in list_of_tickers.items():
                axs[i].plot(search_ticker(ticker_name=k))
                axs[i].set_title(v)
                i+=1
            if i==dimensions:
                return mpld3.fig_to_html(fig, figid="plotly")
            
    return make_plots(**list_of_tickers)