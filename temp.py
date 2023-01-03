# APIs
# application programming interface
# many live on the Net
# HOW? -> the requests lib

# pip install requests

# javascript object notation (JSON) -> to exchange data bwn CPs
import requests # for http request
import sys # for sys.argv

if len(sys.argv) != 2:
    sys.exit()

response = requests.get("https://itunes.apple.com/search?entity=song&limit=1&term="+ sys.argv[1])
print(response.json())

