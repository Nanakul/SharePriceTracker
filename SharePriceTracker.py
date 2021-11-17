import json
import time
import pandas as pd
from alpha_vantage.timeseries import TimeSeries


# Grab API_KEY from json file
API_KEY = json.load(open('Secrets.json' ,'rb')) ['API_KEY']

# Variable for TimeSeries function in pandas data frame output
ts = TimeSeries(key=API_KEY, output_format='pandas')

# Get symbol from user of company they want to track
share = input('Please enter the symbol of the company you would like to track: ')

# Variable for intraday TimeSeries
data, meta_data = ts.get_intraday(symbol=share, interval='1min', outputsize='full')

def track_share(data):
    print(data)