#!/usr/bin/env python3
import json
import yaml
import urllib.request
# Get JSON Data
majortom = ' http://api.open-notify.org/astros.json'
groundctrl = urllib.request.urlopen(majortom)
quiz = groundctrl.read()
quizson = json.loads(quiz.decode('utf-8'))

peeps = []

for person in quizson ['people']:
    dict1 = {}
    dict1["first_name"] = person['name'].split()[0]
    dict1["last_name"] = person['name'].split()[1]
    dict1["craft"] = person['craft']
    peeps.append(dict1)

zfile = open("astros.yaml", "w")
yaml.dump(peeps, zfile)
zfile.close()
