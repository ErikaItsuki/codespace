import json
import requests
import sys

def main():
    o = get_rate_USD().json()
    print(o)

def get_rate_USD():
    response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    return json.dumps(response, indent = 2)

main()