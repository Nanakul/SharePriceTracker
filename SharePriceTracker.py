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

# Function to track the share
def track_share() -> None:
    """This function will print the data of the company specified by the user.
    """
    print(data)

# Function that checks the last change in volatility of the stock
def volitility_check():
    """This function will check the last change in volatility of the given stock.
    """
    closing_data = data['4. close']
    percent_change = closing_data.pct_change()
    print(percent_change)
    
    last_change = percent_change[-1]
    print('The last change was: {}'.format(last_change))

# Function to move panda frame data to excel
def output_excel() -> None:
    """This function will take the data and store it in an excel file every minute for 1 hour. 
    """
    i = 0
    while i != 60:
        data, meta_data = ts.get_intraday(symbol=share, interval='1min', outputsize='full')
        data.to_excel('SharePrice.xlsx')
        time.sleep(60)
        i += 1
        print('{} minute(s) has passed.'.format(i))    

if __name__ == '__main__':
    track_share()
    volitility_check()
    output_excel()