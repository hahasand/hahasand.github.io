
import json, os

jsonpaths = ['jsons/'+i for i in os.listdir('jsons') if i.endswith('.json')]

#with open('HA4.json') as f:
#    j = json.load(f)

jssets = [] # list of sets for JavaScript to use

for jsonpath in jsonpaths:
    with open(jsonpath) as file:
        d = json.load(file)['data']
        #print(d['releaseDate'], d['name'], len(d['cards']), d['type'], jsonpath)
        # Make simplified data for js
        jsset = {}
        for k in ['name','releaseDate','type','code','isOnlineOnly']: jsset[k] = d[k]
        jsset['cards'] = []
        for card in d['cards']:
            if card.get('hasContentWarning'): continue
            if 'scryfallCardBackId' in card['identifiers'] and card['identifiers']['scryfallCardBackId'][0] != '0':
                print(card['name'], card['identifiers']['scryfallCardBackId'])
            jscard = {}
            for k in ['number','name','types','colors']: jscard[k] = card[k]
            jscard['scryfallId'] = card['identifiers']['scryfallId']
            if 'scryfallCardBackId' in card['identifiers'] and card['identifiers']['scryfallCardBackId'] != '0aeebaf5-8c7d-4636-9e82-8c27447861f7':
                jscard['scryfallCardBackId'] = card['identifiers']['scryfallCardBackId']
            jsset['cards'].append(jscard)
        jssets.append(jsset)

def sortkey(jsset):
    return jsset['releaseDate']

jssets.sort(key=sortkey)

with open('jssets.js','w') as file:
    file.write('SETS=' + json.dumps(jssets,indent=1))


#
