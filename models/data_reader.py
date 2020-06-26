import pandas as pd
from models.connect import connect_to_database as cnc


df = cnc()

def get_all_data(): 

    return df.to_html(index=True)

def get_group_data():

    get_groups = df.groupby(['market_id','date','signal_name','opinion','change']).count()

    return get_groups.to_html()
    

def find_data_by_group(market_id):

    get_groups = df.groupby('market_id')
    get_groups = get_groups.get_group(market_id)

    return get_groups.to_html()

def find_data_by_ticker(ticker):

    ticker_data = df.loc[df['signal_name'] == ticker]

    return ticker_data.to_html()
    

if __name__=="__main__":
    get_all_data()
