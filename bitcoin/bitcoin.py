import requests
import sys

def main():
    while True:
        try:
            if sys.argv < 2:
                sys.exit("Missing command-line argument")
            else:
                requests.get(float(sys.argv[1]))
        except (ValueError, requests.RequestException): # ambiguous exception that occured while handling your request
            sys.exit("")

if __name__ == "__main__":
    main()