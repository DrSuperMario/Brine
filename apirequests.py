import pandas as pd
from pandas import json_normalize as jsn

import requests as req

    
def json_to_dataframe(apiloc="127.0.0.1:5000",list_name="cryptolist"):
    payload = req.get(f"http://{apiloc}/{list_name}").json()
    return jsn(payload,('news' if list_name=="newslist" else 'Crypto'))    


def cryotoData(apiloc=None):
    pass


def main():
    pass


if __name__=='__main__':
    main()