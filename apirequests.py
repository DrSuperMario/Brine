import pandas as pd
from pandas import json_normalize as jsn

import requests as req


def json_to_dataframe(apiloc=None, location=None, json_key=None):
    payload = req.get(f"http://{apiloc}/{location}").json()
    return jsn(payload,json_key)
    


def cryotoData(apiloc=None):
    pass


def main():
    pass


if __name__=='__main__':
    main()