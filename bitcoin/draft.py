import json
import requests
import sys

def main():
    print(get_rate_USD())


def get_rate_USD():
    response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json").json()
    return json.dumps(response, indent = 2)

main()