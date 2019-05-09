#!/usr/bin/env python3
import urllib.request
import json
import yaml

majortom = 'http://api.open-notify.org/astros.json'
groundctrl = urllib.request.urlopen(majortom)
helmet = groundctrl.read()
helmetson = json.loads(helmet.decode('utf-8'))
#print("\n\nConverted python data")
#print(helmetson)
#print("\n\nPeople in Space: ",helmetson['number'])
people = helmetson['people']
#print(people)

def main():
    space = [{'first_name': 'Buster', 'last_name': 'Hymen', 'craft': 'ISS'}, {'first_name': 'Christina', 'last_name': 'Koch', 'craft': 'ISS'}]
    yamlstring = yaml.dump(space)
    print(yamlstring)
main()
