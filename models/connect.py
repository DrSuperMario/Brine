import requests
from datetime import datetime as dt
import pandas as pd
from pandas import json_normalize as jsn

data = requests.get("http://127.0.0.1:5000/markets")
jsonify = data.json()

def connect_to_database():

    df = pd.concat([jsn(jsonify['markets'][x]['Signals']) for x in range(len(jsonify['markets']))])   
    df = df.set_index(pd.to_datetime(df['date'])).sort_index(ascending=True)
    df.index = df.index.to_series().apply(lambda x: dt.strftime(x, '%H.%M.%S - %m.%d.%Y'))
    df = df.drop('date', axis=1)

    return df
