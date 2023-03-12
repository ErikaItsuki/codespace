import json
import requests
import sys

def main():
    o = get_rate_USD()
    # print(o) # OK
    print(o[2])


def get_rate_USD():
    response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json").json()
    return json.dumps(response, indent = 2)

main()