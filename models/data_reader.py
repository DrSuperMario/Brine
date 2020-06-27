import pandas as pd
from models.connect import connect_to_database as cnc



def get_all_data():
    df = cnc()
    return df.to_html(index=True)

def get_group_data():
    df = cnc()
    get_groups = df.groupby(['market_id','date','signal_name','opinion','change']).count()
    return get_groups.to_html()


def find_data_by_group(market_id):
    df = cnc()
    get_groups = df.groupby('market_id')
    get_groups = get_groups.get_group(market_id)
    return get_groups.to_html()

def find_data_by_ticker(ticker):
    df = cnc()
    ticker_data = df.loc[df['signal_name'] == ticker]
    return ticker_data.to_html()


if __name__=="__main__":
    pass
