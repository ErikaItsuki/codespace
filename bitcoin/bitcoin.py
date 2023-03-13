import requests
import sys

def main():
    while True:
        try:
            if len(sys.argv) < 2:
                sys.exit("Missing command-line argument")
            else:
                n = (float(sys.argv[1]))
        except (ValueError, requests.RequestException): # ambiguous exception that occured while handling your request
            sys.exit("Command-line argument is not a number")
        else:
            o = get_rate_USD()
            print(o["bpi"]["USD"]["rate_float"] * n)


def get_rate_USD():
    response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json").json()
    return response # type == dict


if __name__ == "__main__":
    main()