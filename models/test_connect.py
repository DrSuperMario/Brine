import requests
from datetime import datetime as dt
import pandas as pd
from pandas import json_normalize as jsn
import time


url_to_API = 'http://46.101.204.81:5000/'


class ConnectAndManage:
    
    end_connect = True


    def connect_to_database(self, destination='markets', username=None, password=None):
        while True:
            try:
                time.sleep(1)
                if destination == 'login':
                    #payload = "{\n\t\"username\": \"user\",\n\t\"password\": \"passwd\"\n}"
                    payload_2 = """
                                    {{
	                                    "username": "{user}",
                                    	"password": "{passwd}"
                                    }}
                    """.format(user=username, passwd=password)

                    headers = {
                                'Content-Type': 'application/json'
                               }

                    response = requests.request("POST", url_to_API + destination, headers=headers, data = payload_2)
                    enc_connect = False
                    return response.text.encode('utf8')

                data = requests.get(url_to_API + destination)

                if data != None:
                    end_connect = False
                    return data
            except:
                time.sleep(1)
                print(f'Connection not made to : {url_to_API}')

    def login_to_api(self, username, password):
        return self.connect_to_database('login', username, password)

    def get_json_data(self):
        data = self.connect_to_database('markets')
        jsonify = data.json()
        df = pd.concat([jsn(jsonify['markets'][x]['Signals']) for x in range(len(jsonify['markets']))])   
        df = df.set_index(pd.to_datetime(df['date'])).sort_index(ascending=False)
        df.index = df.index.to_series().apply(lambda x: dt.strftime(x, '%H:%M:%S - %m.%d.%Y'))
        df = df.drop('date', axis=1)
        return df



if __name__=="__main__":
    makemehappy = ConnectAndManage()
    print(makemehappy.login_to_api('mario','kuum'))
    print(makemehappy.get_json_data())