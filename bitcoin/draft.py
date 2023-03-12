import json
import requests
import sys

def main():
    o = get_rate_USD()
""" for key in o:
        print(key, end = "") # prints the whole dict :(..."""
    

def get_rate_USD():
    response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json").json()
    return json.dumps(response, indent = 2)

main()