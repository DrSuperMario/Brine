from datetime import datetime


import matplotlib.pyplot as plt
import mplfinance as mpf

import mpld3
import pandas as pd
import pandas_datareader as pdr


start = datetime(2020,11,11)
end = datetime.now()


class MakePlots():
    
    def search_ticker(ticker_to_search, time_start, time_end):
        try:
            data = pdr.DataReader(ticker_to_search, 'yahoo', start=time_start, end=time_end) 
            
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
        return data 


    
    def plot_data_to_html(self):

        list_of_tickers = {'AAPL':'Apple',
                            'HPQ':'HP',
                            'MSFT':'Microsoft',
                            'TSLA':'Tesla',
                            'GOOGL':'Google',
                            'AMZN':'Amazon'}

        
        def make_multiple_plots(plot_dimensions=(2,3) , **list_of_tickers):
            
            fig, axs= plt.subplots(*plot_dimensions, figsize=(10,6))
            axs = axs.flatten()
            fig.subplots_adjust(hspace = 0.4)

            dimensions = plot_dimensions[0] * plot_dimensions[1]
            
            for i in range(dimensions):
                for k, v in list_of_tickers.items():
                    axs[i].plot(self.search_ticker(ticker_to_search=k))
                    axs[i].set_title(v)
                    i+=1
                if i==dimensions:
                    return mpld3.fig_to_html(fig, figid="plotly")
    
                
        return make_multiple_plots(**list_of_tickers)

    @classmethod
    def make_single_plot(cls, ticker_name, start_t, end_t):
        
        data_to_plot = cls.search_ticker(ticker_to_search=ticker_name, 
                                   time_start=start_t, 
                                   time_end=end_t)

        if(isinstance(data_to_plot,str)):
            return None       

        mpf.figure()
        fig, axs= plt.subplots(figsize=(12,3))
        #axs = axs.flatten()
        fig.subplots_adjust(hspace = 0.4)

        axs.plot(data_to_plot['Adj Close'], label='Adj Close')
        axs.plot(data_to_plot['Open'], label='Open', alpha=0.8)
        axs.plot(data_to_plot['Low'], label='Low', alpha=0.6)
        axs.plot(data_to_plot['High'], label='High', alpha=0.5)
        axs.legend()
        axs.set_title(ticker_name)

        return mpld3.fig_to_html(fig, figid="plotly")