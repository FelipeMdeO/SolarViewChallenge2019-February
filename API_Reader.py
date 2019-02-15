# This script have how function access python API and download global sun irradiation
import requests
import time
import json
from urllib.request import urlopen

print("Running")

# api-endpoint
#https://power.larc.nasa.gov/cgi-bin/v1/DataAccess.py?request=execute&identifier=SinglePoint&
# parameters=ALLSKY_SFC_SW_DWN&startDate=1981&endDate=2017&userCommunity=SSE&
# tempAverage=INTERANNUAL&outputList=ASCII&lat=-8.275&lon=-49.851&user=anonymous

URL = "https://power.larc.nasa.gov/cgi-bin/v1/DataAccess.py?request=execute&" \
      "identifier=SinglePoint&parameters=ALLSKY_SFC_SW_DWN&startDate=1981&" \
      "endDate=2017&userCommunity=SSE&tempAverage=INTERANNUAL&" \
      "outputList=ASCII&user=anonymous"

# defining a params dict for the parameters to be sent to the API
lat = -8.2756
lon = -49.8516

PARAMS = {'lat': lat, 'lon': lon}


# sending get request and saving the response as response object
r = requests.get(url=URL, params=PARAMS)

# Convert bytes to string type and string type to dict
data = r.content
data = data.decode('utf-8')

list_of_strings = []
for string in data.splitlines():
    list_of_strings.append(string)

flag = False
for s in list_of_strings:
    if not flag and 'ALLSKY_SFC_SW_DWN' in s:   #start detected
        flag = True
        continue
    if '}' in s and flag:
        break   #end detected
    if flag:
        print(s)
        #format data to database
        latitude = lat
        longitude = lon
        splited_line = s.split(':')
        irradiation_value = float(splited_line[1].replace(",", ""))
        aux = str(splited_line[0].replace(" ", ""))
        month = aux[5:]
        year = aux[:5]
        # this information below more lat and long have what I need to db
        output = str(irradiation_value) + ' ' + year + '  ' + month
        print(output)
        print('-'*20)
        # Now write data in database


