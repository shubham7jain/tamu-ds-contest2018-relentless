import json

with open('test.json') as f:
    data = json.load(f)

for feature in data['features']:
    print(feature['geometry']['type'])
    print(feature['geometry']['coordinates'])
