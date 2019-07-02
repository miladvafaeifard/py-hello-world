import json
from datetime import timedelta
from urllib import request

def bootApplication():
    theJSON = __getData()
    if "title" in theJSON["metadata"]:
        print(theJSON["metadata"]["title"])

def __getData():
    weburl = request.urlopen("https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5_day.geojson")
    data = weburl.read()
    return json.loads(data)
