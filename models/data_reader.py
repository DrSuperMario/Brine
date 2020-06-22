import pandas as pd
from models.connect import connect_to_database as cnc

def get_all_data(): 

    df = cnc()

    return df.to_html(index=True)

def get_group_data():

    df = cnc()
    df = df.groupby(['market_id','date','signal_name','opinion','change']).count()

    return df.to_html()
    

def find_data_by_group(market_id):

    df = self.get_all_data()
    dfgroups = df.groupby('market_id')

    return dfgroups.get_group(market_id)
    

if __name__=="__main__":
    print(get_group_data())
