import simplejson as json #import simplejson
#import json

#Dict(Json)선언

data = {}
data['people'] = []
data['people'].append({
    'name':'Kim',
    'website':'naver.com',
    'from':'Seoul'
})
data['people'].append({
    'name':'Park',
    'website':'google.com',
    'from':'Busan'
})

data['people'].append({
    'name':'Jeong',
    'website':'daum.netm',
    'from':'Jennam'
})

#print(data)

#Dict(Json) -> str
e = json.dumps(data, indent=4)

d = json.loads(e)

with open('c:/Coding/python/4_XML/member.json','w') as outfile:
    outfile.write(e)

with open('c:/Coding/python/4_XML/member.json','r') as infile:
    r = json.loads(infile.read())
    print("======")
    #print(type(r))
    #print(r)
    for p in r['people']:
        print('Name: ' + p['name'])
        print('website: ' + p['website'])
        print('From: ' + p['from'])
        print(' ')
