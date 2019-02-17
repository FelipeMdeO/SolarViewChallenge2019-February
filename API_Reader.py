# This script have functions to find brazil coords and mount database
# with sun irradiation value for each coord

import requests
import mysql.connector
import time
import geopip
import numpy

startTime = time.time()

print("Running")

URL = "https://power.larc.nasa.gov/cgi-bin/v1/DataAccess.py?request=execute&" \
      "identifier=SinglePoint&parameters=ALLSKY_SFC_SW_DWN&startDate=1981&" \
      "endDate=2017&userCommunity=SSE&tempAverage=INTERANNUAL&" \
      "outputList=ASCII&user=anonymous"

connection = mysql.connector.connect(host='localhost',
                                     database='nasadata',
                                     user='root',
                                     passwd='felipe3211')

mycursor = connection.cursor()


def request_data_from_api(lat, lng):
    """
    This function receive a valid coords and send request to NASA API to inform
    solar irradiance in time
    When receive results call function to inset data in MySQL database
    :param lat: latitude to request solar irradiance information
    :param lng: longitude to request solar irradiance information
    :return:
    """
    PARAMS = {'lat': lat, 'lon': lng}

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
            #format data to database
            latitude = lat
            longitude = lng
            splited_line = s.split(':')
            irradiation_value = float(splited_line[1].replace(",", ""))
            aux = str(splited_line[0].replace(" ", ""))
            month = aux[5:]
            year = aux[:5]
            print("\tData Insert in DB: " + str(latitude) + ", " + str(longitude) + ", " + str(year)
                  + ", " + str(month) + ", " + str(irradiation_value))
            sql = "INSERT INTO irradiation2 (latitude, longitude, year, month, incidence) VALUES (%s, %s, %s, %s, %s)"
            year = int(''.join(filter(lambda x: x.isdigit(), year)))
            month = int(''.join(filter(lambda x: x.isdigit(), month)))
            if month == 13:
                continue  # 13 position is year mean, I no need this
            val = (latitude, longitude, year, month, irradiation_value)
            mycursor.execute(sql, val)
            #print(mycursor.rowcount, "record inserted.")
            connection.commit()


def fill_DB():
    """
    function to show all Brazil coords with offset of 0.2 degrees in each coords.
    0.2 degrees result in maximum of 11 km of erro offset. (1 degree is 111 km)
    To do it, the function receveid extremy coords of Brazil and use loop
    verifying in library imported for how country this coords are.
    If coords from Brazil, this function request to other function to 
    get data from NASA API
    :return: 
    """

    # TODO Alter this method to method using shape file
    # TODO Do method to visualize in DB last line insert and work after ir
    # use to it SELECT * FROM irradiation ORDER BY id DESC LIMIT 1; and catch last lat and lng
    # TODO Use threads to acelerate this process

    lat_max =   4.5
    lat_min = -34.0
    lng_dir = -33.0
    lng_esq = -74.0


    for lat in numpy.arange(lat_min, lat_max, 0.2):
        for lng in numpy.arange(lng_esq, lng_dir, 0.2):
            try:
                response = geopip.search(lat=lat, lng=lng)
                country = response.get('NAME')
                if country == 'Brazil':
                    print("Working at latitude= " + str(lat) + " longitude= " + str(lng))
                    request_data_from_api(lat=lat, lng=lng)
            except:
                continue


fill_DB()

endTime = time.time()
totalTime = endTime - startTime

print("The total time to catch data was " + str(totalTime))
