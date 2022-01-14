import requests
import json
from datetime import datetime

AV_ENDPOINT = 'https://www.alphavantage.co/query'
AV_KEY = json.load(open('Secrets.json', 'rb'))['AV_API_KEY']



