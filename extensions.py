import requests
import json
from config import APIkey


class APIException(Exception):
    pass


class Convertor:
    @staticmethod
    def get_price(base, sym, amount):
        url = f"https://api.apilayer.com/exchangerates_data/convert?to={sym}&from={base}&amount={amount}"
        payload = {}
        headers = {
            "apikey": APIkey
        }

        response = requests.request("GET", url, headers=headers, data=payload)

        result = response.text
        data = json.loads(result)
        return round(data['result'], 2)