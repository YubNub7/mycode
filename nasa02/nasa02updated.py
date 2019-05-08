#!/usr/bin/env python3

import requests ## 3rdparty URL lookup

## Define the main function
def main():
    neourl = 'https://api.nasa.gov/neo/rest/v1/feed?' 
    startdate = "start_date={}".format(input("Enter Start Date as yyyy-mm-dd: "))
    enddate = '&end_date=END_DATE'
    mykey = '&api_key=DEMO_KEY'
    neourl = neourl + startdate + mykey
    neojson = (requests.get(neourl)).json()
    print(neojson)

def moon_lengths(missdistance):
    m_length = 238900

    print(missdistance/m_length)
main()
#moon_lengths(1000000)
