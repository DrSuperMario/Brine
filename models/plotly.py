from datetime import datetime


import matplotlib.pyplot as plt
import mpld3
import pandas as pd
import pandas_datareader as pdr


start = datetime(2020,11,11)
end = datetime.now()


class MakePlots():
    
    def search_ticker(ticker_to_search, time_start, time_end):
        return pdr.DataReader(ticker_to_search, 'yahoo', start=time_start, end=time_end)


    
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
    
        fig, axs= plt.subplots(figsize=(12,3))
        #axs = axs.flatten()
        fig.subplots_adjust(hspace = 0.4)

        axs.plot(cls.search_ticker(ticker_to_search=ticker_name, 
                                time_start=start_t, 
                                time_end=end_t))
        axs.set_title(ticker_name)
     

        return mpld3.fig_to_html(fig, figid="plotly")