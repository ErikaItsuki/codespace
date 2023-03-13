import requests
import sys

def main():
    while True:
        try:
            if len(sys.argv) < 2:
                sys.exit("Missing command-line argument")
            else:
                n = (float(sys.argv[1]))
                break
        except (ValueError, requests.RequestException):
            sys.exit("Command-line argument is not a number")

    o = get_rate_USD()
    print(f'${(o["bpi"]["USD"]["rate_float"] * n):.4f}')


def get_rate_USD():
    response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json").json()
    return response # type == dict


if __name__ == "__main__":
    main()