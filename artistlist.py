# CodeBar session with Nills & Kaoruko Kawanishi <3

apikey = "5b97c38c59e3edf289c47d714095291a"
url = "https://ws.audioscrobbler.com/2.0/?method=artist.getsimilar&artist="
artist = "miles+davis"
url+=artist
url+="&api_key=5b97c38c59e3edf289c47d714095291a&format=json"
print(url)
print(f"https://ws.audioscrobbler.com/2.0/?method=artist.getsimilar&artist={artist}&api_key={apikey}&format=json")

import urllib.request
with urllib.request.urlopen(url) as response:
    rawdata = response.read()

import json
data = json.loads(rawdata)
print(data["similarartists"]["artist"][1]["name"])

artists = data["similarartists"]["artist"]
for i, artist in enumerate(artists):
    print(f"{i+1}: {artist['name']} - {artist['match']}")
