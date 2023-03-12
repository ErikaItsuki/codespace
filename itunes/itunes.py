import requests
import sys
import json # more cleanl y format the python dict


if len(sys.argv) != 2:
    sys.exit()

# requests.get(link) -> return sth from the server
response = requests.get("https://itunes.apple.com/search?entity=song&limit=1&term=" + sys.argv[1])

# print 1 bunch only:
#1 the whole json code
# print(json.dumps(response.json(), indent=2)) #json() to format --> but only in python dictionary

#2 only the trackName in results (the only 1 dict in the list) # change limit=1 to 50 if need to find more songs
o = response.json()
for result in o["results"]: # documentation has key with dict values called results inside
    print(result["trackName"])


"""
for student in students:
    print(student, students['name']) => print key then the corresponding value

so here:
o["results"] access the R-value, i.e. the inner dictionary
with result, each meaning a bunch of data of that 1 search result, result["trackname"] gives the R of the song's name
"""
