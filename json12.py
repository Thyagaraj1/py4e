import urllib.request, urllib.parse, urllib.error
import json
import ssl

api_key=False
if api_key is False:
    api_key=42
    serviceurl='http://py4e-data.dr-chuck.net/json?'
else:
    serviceurl='https://maps.googleapis.com/maps/api/geocode/json?'

#Ignore SSL certification Errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    address=input('Enter address: ')
    if len(address)<1:break
    dict={}
    dict['address']=address
    if api_key is not False:dict['key']=api_key
    #print(dict)
    #{'address': 'Magadi', 'key': 42}
    #Enter location: Magadi
#Retrieving http://py4e-data.dr-chuck.net/json?address=Magadi&key=42
#Retrieved 3427 characters
#{
    #"results": [
      #  {
        #    "address_components": [
          #      {
              #      "long_name": "Magadi",
                #    "short_name": "Magadi",
                #    "types": [
                  #      "locality",
                  #      "political"
                  #  ]
               # },
                #{
                 #   "long_name": "Ramanagara",
                 #   "short_name": "Ramanagara",
                  #  "types": [
                  #      "administrative_area_level_3",
                   #     "political"
                  #  ]
                #},
                #{
                 #   "long_name": "Bangalore Division",
                  #  "short_name": "Bangalore Division",
                  #  "types": [
                   #     "administrative_area_level_2",
                   #     "political"
                   # ]
               # },
                #{
                  #  "long_name": "Karnataka",
                   # "short_name": "KA",
                   # "types": [
                    #    "administrative_area_level_1",
                    #    "political"
                  #  ]
               # },
                #{
                   # "long_name": "India",
                   # "short_name": "IN",
                   # "types": [
                    #    "country",
                    #    "political"
                  #  ]
                #}
            #],
            #"formatted_address": "Magadi, Karnataka, India",
           # "geometry": {
                #"bounds": {
                   # "northeast": {
                   #     "lat": 12.9652398,
                   #     "lng": 77.2459811
                   # },
                    #"southwest": {
                     #   "lat": 12.9486655,
                    #    "lng": 77.2058801
                    #}
               # },
               # "location": {
                #    "lat": 12.9576756,
                #    "lng": 77.22614519999999
                #},
                #"location_type": "APPROXIMATE",
               # "viewport": {
                #    "northeast": {
                   #     "lat": 12.9652398,
                   #     "lng": 77.2459811
                    #},
                    #"southwest": {
                    #    "lat": 12.9486655,
                   #     "lng": 77.2058801
                   # }
                #}
            #},
            #"place_id": "ChIJN4F8-V8zrjsRuxV1h5saCIQ",
            #"types": [
             #   "locality",
              #  "political"
           # ]
        #},
       # {
           # "address_components": [
               # {
                #    "long_name": "Magadi",
                #    "short_name": "Magadi",
                 #   "types": [
                 #       "locality",
                 #       "political"
                  #  ]
                #},
               # {
                 #   "long_name": "Kajiado County",
                  #  "short_name": "Kajiado County",
                  #  "types": [
                  #      "administrative_area_level_1",
                   #     "political"
                   # ]
                #},
                #{
                  #  "long_name": "Kenya",
                  #  "short_name": "KE",
                   # "types": [
                   #     "country",
                    #    "political"
                   # ]
               # }
           # ],
            #"formatted_address": "Magadi, Kenya",
            #"geometry": {
               # "bounds": {
                #    "northeast": {
               #         "lat": -1.8866467,
                #        "lng": 36.3114452
                #    },
                #    "southwest": {
                 #       "lat": -1.9150411,
                 #       "lng": 36.292305
                 #   }
              #  },
               # "location": {
                  #  "lat": -1.8996701,
                  #  "lng": 36.301039
                #},
                #"location_type": "APPROXIMATE",
                #"viewport": {
                #    "northeast": {
                  #      "lat": -1.8866467,
                  #      "lng": 36.3114452
                  #  },
                  #  "southwest": {
                    #    "lat": -1.9150411,
                   #     "lng": 36.292305
                    #}
                #}
            #},
            #"place_id": "ChIJCVvjp0IiLhgRx4c32zOpjO8",
           # "types": [
            #    "locality",
            #    "political"
            #]
        #}
    #],
    #"status": "OK"
#}
#lat 12.9576756 lng 77.22614519999999
#Magadi, Karnataka, India
    url=serviceurl+urllib.parse.urlencode(dict)
    #print('Retrieving: ',url)
    #Retrieving: http://py4e-data.dr-chuck.net/json?address=Magadi&key=42
    uh=urllib.request.urlopen(url,context=ctx)
    data=uh.read().decode()
    #print(data)
    ##Enter address: Ann arbor
#{
   #"results" : [
     # {
      #   "address_components" : [
        #    {
         #      "long_name" : "Ann Arbor",
           #    "short_name" : "Ann Arbor",
           #    "types" : [ "locality", "political" ]
            #},
            #{
            #   "long_name" : "Washtenaw County",
             #  "short_name" : "Washtenaw County",
              # "types" : [ "administrative_area_level_2", "political" ]
            #},
            #{
             #  "long_name" : "Michigan",
             #  "short_name" : "MI",
              # "types" : [ "administrative_area_level_1", "political" ]
            #},
            #{
             #  "long_name" : "United States",
              # "short_name" : "US",
               #"types" : [ "country", "political" ]
            #}
         #],
         #"formatted_address" : "Ann Arbor, MI, USA",
         #"geometry" : {
          #  "bounds" : {
             #  "northeast" : {
              #    "lat" : 42.3239728,
               #   "lng" : -83.6758069
               #},
              # "southwest" : {
              #    "lat" : 42.222668,
               #   "lng" : -83.799572
               #}
            #},
            #"location" : {
              # "lat" : 42.2808256,
               #"lng" : -83.7430378
           # },
            #"location_type" : "APPROXIMATE",
            #"viewport" : {
              # "northeast" : {
               #   "lat" : 42.3239728,
                #  "lng" : -83.6758069
               #},
               #"southwest" : {
               #   "lat" : 42.222668,
                 # "lng" : -83.799572
               #}
            #}
        # },
         #"place_id" : "ChIJMx9D1A2wPIgR4rXIhkb5Cds",
         #"types" : [ "locality", "political" ]
      #}
   #],
   #"status" : "OK"
#}

    #print('Retrieved',len(data),'character')
    #Retrieved 1736 character
    #Converting string data into object data
    try:
        objd=json.loads(data)
    except:
        objd=None
    #print(objd)
#Enter address: Ann arbor
#{'results': [{'address_components': [{'long_name': 'Ann Arbor', 'short_name': 'Ann Arbor', 'types': ['locality', 'political']}, {'long_name': 'Washtenaw County', 'short_name': 'Washtenaw County', 'types': ['administrative_area_level_2', 'political']}, {'long_name': 'Michigan', 'short_name': 'MI', 'types': ['administrative_area_level_1', 'political']}, {'long_name': 'United States', 'short_name': 'US', 'types': ['country', 'political']}], 'formatted_address': 'Ann Arbor, MI, USA', 'geometry': #{'bounds': {'northeast': {'lat': 42.3239728, 'lng': -83.6758069}, 'southwest': {'lat': 42.222668, 'lng': -83.799572}}, 'location': {'lat': 42.2808256, 'lng': -83.7430378}, 'location_type': 'APPROXIMATE', 'viewport': {'northeast': {'lat': 42.3239728, 'lng': -83.6758069}, 'southwest': {'lat': 42.222668, 'lng': -83.799572}}}, 'place_id': 'ChIJMx9D1A2wPIgR4rXIhkb5Cds', 'types': ['locality', 'political']}], 'status': 'OK'}
    if not objd or 'status' not in objd or objd['status'] !='OK':
        print("==Failure to load data==")
        continue

    #print(json.dumps(objd,indent=4))
#"geometry": {
            #    "bounds": {
            #        "northeast": {
            #            "lat": 42.3239728,
            #            "lng": -83.6758069
            #        },
            #        "southwest": {
            #            "lat": 42.222668,
            #            "lng": -83.799572
            #        }
            #    },
            #    "location": {
            #        "lat": 42.2808256,
            #        "lng": -83.7430378
    lat=objd['results'][0]['geometry']['location']['lat']
    lng=objd['results'][0]['geometry']['location']['lng']
    print('lattitude',lat,'longitude',lng)
    #lattitude 42.2808256 longitude -83.7430378


#output from print(json.dumps(objd,indent=4))
#{
    #"results": [
    #    {
        #    "address_components": [
        #        {
            #        "long_name": "Ann Arbor",
            #        "short_name": "Ann Arbor",
            #        "types": [
            #            "locality",
            #            "political"
            #        ]
            #    },
            #    {
            #        "long_name": "Washtenaw County",
            #        "short_name": "Washtenaw County",
            #        "types": [
            #            "administrative_area_level_2",
            #            "political"
            #        ]
            #    },
            #    {
            #        "long_name": "Michigan",
            #        "short_name": "MI",
            #        "types": [
            #            "administrative_area_level_1",
            #            "political"
            #        ]
            #    },
            #    {
            #        "long_name": "United States",
            #        "short_name": "US",
            #        "types": [
            #            "country",
            #            "political"
            #        ]
            #    }
            #],
            #"formatted_address": "Ann Arbor, MI, USA",
            #"geometry": {
            #    "bounds": {
            #        "northeast": {
                #        "lat": 42.3239728,
                    #    "lng": -83.6758069
                    #},
                #    "southwest": {
                #        "lat": 42.222668,
                #        "lng": -83.799572
                #    }
                #},
                #"location": {
                #    "lat": 42.2808256,
                #    "lng": -83.7430378
                #},
            #    "location_type": "APPROXIMATE",
            #    "viewport": {
                #    "northeast": {
                #        "lat": 42.3239728,
                #        "lng": -83.6758069
                #    },
                #    "southwest": {
                    #    "lat": 42.222668,
                #        "lng": -83.799572
                #    }
            #    }
        #    },
            #"place_id": "ChIJMx9D1A2wPIgR4rXIhkb5Cds",
            #"types": [
            #    "locality",
                #"political"
            #]
        #}
    #],
    #"status": "OK"
#}
