import urllib.request, urllib.parse, urllib.error 
import json 
import ssl 

api_key=False 
if api_key is False:
    api_key=42
    serviceurl='http://py4e-data.dr-chuck.net/json?'
else:
    serviceurl='https://maps.googleapis.com/maps/api/geocode/json?' #? indicates enter the parameter 

#Ignore SSL certificate errors 

while True:
    address=str(input('Enter Address: '))
    #print(address)
    #Ann Arbor, MI-->not a valid non-string sequence or mapping object for url=serviceurl+urllib.parse.urlencode(address)
    if len(address)<1:break 
    dict={ }
    dict['address']=address
    if api_key is not False:
        dict['key']=api_key
    print(dict)
#{'address': 'Ann Arbor, MI', 'key': 42}
    url=serviceurl+urllib.parse.urlencode(dict)
    #url=serviceurl+urllib.parse.urlencode(address)
    #File "C:\Users\taralilk\AppData\Local\Programs\Python\Python311\Lib\urllib\parse.py", line 943, in urlencode
    #raise TypeError("not a valid non-string sequence "
#TypeError: not a valid non-string sequence or mapping object
    print(url)
    #http://py4e-data.dr-chuck.net/json?address=Ann+Arbor%2CMI&key=42  -->+-->space and %2C-->and 
    stringdata=urllib.request.urlopen(url).read().decode() #decode() as data is coming from the outside world converting UTF-8 to Unicode or Bytes to string #string data needs to be converted into object data 
    #print(stringdata) mentioned in the below 
    try:
        objectdata=json.loads(stringdata)
    #print('objectdata:',objectdata) --> object data inform of {[]} dict with list where as string data is same which was not in one line it's as shown below 
    #objectdata: {'results': [{'address_components': [{'long_name': 'Ann Arbor', 'short_name': 'Ann Arbor', 'types': ['locality', 'political']}, {'long_name': 'Washtenaw County', 'short_name': 'Washtenaw County', 'types': ['administrative_area_level_2', 'political']}, {'long_name': 'Michigan', 'short_name': 'MI', 'types': ['administrative_area_level_1', 'political']}, {'long_name': 'United States', 'short_name': 'US', 'types': ['country', 'political']}], 'formatted_address': 'Ann Arbor, MI, USA', 'geometry': {'bounds': {'northeast': {'lat': 42.3239728, 'lng': -83.6758069}, 'southwest': {'lat': 42.222668, 'lng': -83.799572}}, 'location': {'lat': 42.2808256, 'lng': -83.7430378}, 'location_type': 'APPROXIMATE', 'viewport': {'northeast': {'lat': 42.3239728, 'lng': -83.6758069}, 'southwest': {'lat': 42.222668, 'lng': -83.799572}}}, 'place_id': 'ChIJMx9D1A2wPIgR4rXIhkb5Cds', 'types': ['locality', 'political']}], 'status': 'OK'}
    except:
        objectdata=-None

    if not objectdata or 'status' not in objectdata or objectdata['status'] !='OK':  #objectdata['status']-->indicates we are looking for key-'status' and it's should be equal to value 'OK' in dictionary objectdata 
        print('===Failed to load==')
        continue 

    pid = objectdata['results'][0]['place_id']
    print('Place id ',pid)


    #print(json.dumps(objectdata, indent=4)) # to cross check 
    # Output below 

    #lat=dict['results'][0]-index value and getting array 
    #lat=objectdata['results'][0]['geometry']['location']['lat']  #It should be in order as like we are entering the maze 
    #print(lat)
    #42.2808256
#Traceback (most recent call last):
 # File "C:\Users\taralilk\OneDrive - Cisco\Documents\py4e\json14.py", line 48, in <module>
    #lat=objectdata['results'][0]['location']['lat']
#KeyError: 'location'  
    #lng=objectdata['results'][0]['geometry']['location']['lng']
    #print(lng)
    #-83.7430378
    #print('lattitude: ',lat,'longitude: ',lng)
    #lattitude:  42.2808256 longitude:  -83.7430378
    #location = objectdata['results'][0]['formatted_address']
    #print(location)
#lattitude:  12.9224695 longitude:  77.5743267
#816/i 16th Cross, Krishna Rajendra Rd, 7th Block, west block, Bengaluru, Karnataka 560082, India

#Enter Address: Hosahalli Gollarahatti
#{'address': 'Hosahalli Gollarahatti', 'key': 42}
#http://py4e-data.dr-chuck.net/json?address=Hosahalli+Gollarahatti&key=42
#lattitude:  12.9911586 longitude:  77.46230940000001
#Gollarahatti, Bengaluru, Karnataka 562130, India


    






































    #print(stringdata)  -->below informat {[]}
#    {
#   "results" : [
#      {
#         "address_components" : [
#            {
#              "long_name" : "Ann Arbor",
#               "short_name" : "Ann Arbor",
#               "types" : [ "locality", "political" ]
#           },
#            {
#               "long_name" : "Washtenaw County",
#               "short_name" : "Washtenaw County",
#               "types" : [ "administrative_area_level_2", "political" ]
#            },
#            {
#               "long_name" : "Michigan",
#               "short_name" : "MI",
#               "types" : [ "administrative_area_level_1", "political" ]
#            },
#            {
#               "long_name" : "United States",
#               "short_name" : "US",
#               "types" : [ "country", "political" ]
#            }
#         ],
#         "formatted_address" : "Ann Arbor, MI, USA",
#         "geometry" : {
#            "bounds" : {
#               "northeast" : {
#                  "lat" : 42.3239728,
#                  "lng" : -83.6758069
#               },
#               "southwest" : {
#                  "lat" : 42.222668,
#                  "lng" : -83.799572
#               }
#            },
#            "location" : {
#               "lat" : 42.2808256,
#               "lng" : -83.7430378
#            },
#            "location_type" : "APPROXIMATE",
#            "viewport" : {
#               "northeast" : {
#                  "lat" : 42.3239728,
#                  "lng" : -83.6758069
#               },
#               "southwest" : {
#                  "lat" : 42.222668,
#                  "lng" : -83.799572
#               }
#            }
#         },
#         "place_id" : "ChIJMx9D1A2wPIgR4rXIhkb5Cds",
#         "types" : [ "locality", "political" ]
#      }
#   ],
#   "status" : "OK"
#}
    




#print(json.dumps(objectdata, indent=4))
#{
#   "results": [
#        {
#            "address_components": [
#                {
#                    "long_name": "Ann Arbor",
#                    "short_name": "Ann Arbor",
#                    "types": [
#                        "locality",
#                        "political"
#                    ]
#                },
#                {
#                    "long_name": "Washtenaw County",
#                    "short_name": "Washtenaw County",
#                    "types": [
#                        "administrative_area_level_2",
#                        "political"
#                    ]
#                },
#                {
#                    "long_name": "Michigan",
#                    "short_name": "MI",
#                    "types": [
#                        "administrative_area_level_1",
#                        "political"
#                    ]
#                },
#                {
#                    "long_name": "United States",
#                    "short_name": "US",
#                    "types": [
#                        "country",
#                        "political"
#                    ]
#               }
#            ],
#            "formatted_address": "Ann Arbor, MI, USA",
#            "geometry": {
#                "bounds": {
#                    "northeast": {
#                        "lat": 42.3239728,
#                        "lng": -83.6758069
#                    },
#                    "southwest": {
#                        "lat": 42.222668,
#                        "lng": -83.799572
#                    }
#                },
#                "location": {
#                    "lat": 42.2808256,
#                    "lng": -83.7430378
#                },
#                "location_type": "APPROXIMATE",
#                "viewport": {
#                    "northeast": {
#                        "lat": 42.3239728,
#                        "lng": -83.6758069
#                    },
#                    "southwest": {
#                        "lat": 42.222668,
#                        "lng": -83.799572
#                    }
#                }
#            },
#            "place_id": "ChIJMx9D1A2wPIgR4rXIhkb5Cds",
#            "types": [
#                "locality",
#                "political"
#            ]
#        }
#    ],
#    "status": "OK"
#}