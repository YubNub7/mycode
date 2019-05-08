#!/usr/bin/env python3
import urllib.request
import json

##Define NEOapi
neourl = 'https://api.nasa.gov/neo/rest/v1/feed?'
startdate = 'start_date=2019-05-08'
enddate = '&end_date=END_DATE'
mykey = '&api_key=DEMO_KEY'  ## your key goes in place of DEMO_KEY

neourl = neourl + startdate + mykey

## Call the webservice
neourlobj = urllib.request.urlopen(neourl)

## Read the file-like object
neoread = neourlobj.read()

## Decode json to python data structure
decodeneo = json.loads(neoread.decode('utf-8'))

## Display our pythonic data
print("\n\nConverted python data")
print(decodeneo)
