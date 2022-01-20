import requests
import json
from datetime import datetime

AV_ENDPOINT = 'https://www.alphavantage.co/query'
AV_KEY = json.load(open('Secrets.json', 'rb'))['AV_API_KEY']


def get_closing_price():
    querystring = {'function': 'TIME_SERIES_DAILY',
                   'symbol': 'MS',
                   'apikey': AV_KEY}

    response = requests.get(AV_ENDPOINT, params=querystring)
    data = response.json()['Time Series (Daily)']
    data_list = [value for (key, value) in data.items()]

    for i in range(len(data_list)):
        data_list[i] = {
            'Close': data_list[i]['4. close']
        }

        print(data_list[i])

    # Get yesterday's close price
    yday_cp = data_list[0]['Close']
    print(yday_cp)

    # Get day before yesterday's close price
    dby_cp = data_list[1]['Close']
    print(dby_cp)

    # Get absolute difference between the two days
    difference = abs(float(yday_cp) - float(dby_cp))
    print(difference)
    diff_percent = (difference / float(yday_cp)) * 100
    print(diff_percent)

    # Check if difference is greater than 5%
    if diff_percent > 5:
        pass


if __name__ == '__main__':
    get_closing_price()
