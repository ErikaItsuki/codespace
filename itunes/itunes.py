import requests
import sys

if len(sys.argv) != 2:
    sys.exit()

# requests.get(link) -> return sth from the server
response = requests.get("https://itunes.apple.com/search?entity=song&limit=1&term=" + sys.argv[1])
print(response.json()) #json() to format --> but only in python dictionary