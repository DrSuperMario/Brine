import requests
from datetime import datetime as dt
import pandas as pd
from pandas import json_normalize as jsn
import time


url_to_API = 'http://64.225.65.21/markets'

def connect_to_database():
    
    end_connect = False
    
    while True:

        try:
            
            time.sleep(1)
            data = requests.get(url_to_API)
            
            if data != None:
                jsonify = data.json()
                df = pd.concat([jsn(jsonify['markets'][x]['Signals']) for x in range(len(jsonify['markets']))])   
                df = df.set_index(pd.to_datetime(df['date'])).sort_index(ascending=False)
                df.index = df.index.to_series().apply(lambda x: dt.strftime(x, '%H:%M:%S - %m.%d.%Y'))
                df = df.drop('date', axis=1)
                end_connect
                return df
            
        except:
            
            time.sleep(1)
            print(f'Connection not made to : {url_to_API}')



if __name__=="__main__":
    connect_to_database()
