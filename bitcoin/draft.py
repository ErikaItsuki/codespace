import json
import requests

def main():
    o = get_rate_USD()
    for value in o.values():
        print(value)


def get_rate_USD():
    response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    return json.dumps(response.json(), indent = 2)

main()

"""for key in o:
    print(key, end = "") # prints the whole dict # but not a prob"""