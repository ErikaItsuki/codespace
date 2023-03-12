import json
import requests

def main():
    o = get_rate_USD()
    print(type(o)) # str cuz it is a multilayer dict


def get_rate_USD():
    response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json").json()
    print(type(response)) # type == dict
    return json.dumps(response, indent = 2)

main()

"""for key in o:
    print(key, end = "") # prints the whole dict # but not a prob"""