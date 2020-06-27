import requests
from datetime import datetime as dt
import pandas as pd
from pandas import json_normalize as jsn
import time



def connect_to_database():
    
    end_connect = False
    
    while True:

        try:
            
            time.sleep(1)
            data = requests.get("http://127.0.0.1:5000/markets")
            
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
            print('Connection not made')



if __name__=="__main__":
    connect_to_database()
