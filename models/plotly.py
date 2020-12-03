from datetime import datetime


import matplotlib.pyplot as plt
import mpld3
import pandas as pd
import pandas_datareader as pdr


start = datetime(2019,1,1)
end = datetime.now()

def search_ticker(ticker_name='TSLA'):
    return pdr.DataReader(ticker_name, 'yahoo', start=start, end=end)

def plot_data_to_html():
    fig = plt.figure()
    plt.plot(search_ticker())
    tooltip = mpld3.plugins.PointHTMLTooltip(fig,css="align-content-center")
    mpld3.plugins.connect(fig, tooltip)

    return mpld3.fig_to_html(fig)

def main():
    return plot_data_to_html()

if __name__=='__main__':
    main()