import json
import requests
import sys

def main():
    o = get_rate_USD()
    for key in o:
        print(key, end = "") # prints the whole dict # but not a prob



def get_rate_USD():
    response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    return json.dumps(response.json(), indent = 2)

main()