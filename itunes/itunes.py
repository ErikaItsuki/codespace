import requests
import sys
import json # more cleanly format the python dict


if len(sys.argv) != 2:
    sys.exit()

# requests.get(link) -> return sth from the server
response = requests.get("https://itunes.apple.com/search?entity=song&limit=1&term=" + sys.argv[1])
print(json.dumps(response.json(), indent=2)) #json() to format --> but only in python dictionary
