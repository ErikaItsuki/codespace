import requests

def main():
    o = get_rate_USD()
    rate = o["bpi"]["USD"]["rate_float"]
    print(rate)


def get_rate_USD():
    response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json").json()
    return response # type == dict


main()

"""for key in o:
    print(key, end = "") # prints the whole dict # but not a prob"""