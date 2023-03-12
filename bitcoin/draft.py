import json
import requests
import sys

def main():
    o = get_rate_USD()
    for rate in o["bpi"]:
        for USD in rate["USD"]:
            print(USD["rate"])


def get_rate_USD():
    response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json").json()
    return json.dumps(response, indent = 2)

main()