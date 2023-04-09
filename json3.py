import urllib.request, urllib.parse, urllib.error 
import json 

serviceurl='http://maps.googleapis.com/maps/api/geocode/json?'

while True:
    address=input('Enter Address: ')
    if len(address)<1:break #breaking infinte loop we could use if address=='done'
    url=serviceurl+urllib.parse.urlencode({'address:'address})
     #TypeError: not a valid non-string sequence or mapping object
    print('Retrieving',url)
    stringdata=urllib.request.urlopen(url).read().decode() #string dtata
    print(stringdata)
    try:
        objectdata=json.loads(stringdata)
    except:
        objectdata=None
    print(objectdata)


