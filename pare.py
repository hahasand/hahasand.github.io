
import json, os

jsonpaths = [i for i in os.listdir() if i.endswith('.json')]

#with open('HA4.json') as f:
#    j = json.load(f)

jssets = [] # list of sets for JavaScript to use

for jsonpath in jsonpaths:
    with open(jsonpath) as file:
        d = json.load(file)['data']
        print(d['releaseDate'], d['name'], len(d['cards']), d['type'], jsonpath)
        for card in d['cards']:
            print('', card['number'], card['name'])
        # Make simplified data for js
        jsset = {}
        for k in ['name','releaseDate','type','code']: jsset[k] = d[k]
        jsset['cards'] = []
        for card in d['cards']:
            jscard = {}
            for k in ['number','name']: jscard[k] = card[k]
            jsset['cards'].append(jscard)
        jssets.append(jsset)


with open('jssets.js','w') as file:
    file.write('SETS=' + json.dumps(jssets,indent=1))


#
