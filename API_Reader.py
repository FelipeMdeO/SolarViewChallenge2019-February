# This script have how function access python API and download global sun irradiation
import requests
import mysql.connector
from mysql.connector import Error
from mysql.connector import errorcode
import time
import geopip
import numpy

startTime = time.time()

##write your code or functions calls

print("Running")

URL = "https://power.larc.nasa.gov/cgi-bin/v1/DataAccess.py?request=execute&" \
      "identifier=SinglePoint&parameters=ALLSKY_SFC_SW_DWN&startDate=1981&" \
      "endDate=2017&userCommunity=SSE&tempAverage=INTERANNUAL&" \
      "outputList=ASCII&user=anonymous"

connection = mysql.connector.connect(host='localhost',
                                     database='cadastro',
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
            print("\tData Insert in DB: " + str(latitude) + "," + str(longitude) + "," + str(year)
                  + "," + str(month) + "," + str(irradiation_value))
            sql = "INSERT INTO data (latitude, longitude, year, month, irradiation) VALUES (%s, %s, %s, %s, %s)"
            year = int(''.join(filter(lambda x: x.isdigit(), year)))
            month = int(''.join(filter(lambda x: x.isdigit(), month)))
            if month == 13:
                continue  # 13 position is year mean, i no need this
            val = (latitude, longitude, year, month, irradiation_value)
            mycursor.execute(sql, val)
            #print(mycursor.rowcount, "record inserted.")
            connection.commit()


def find_brazil_coords():
    """
    function to show all Brazil coords with offset of 1/2" in each coords
    To do it, the function receveid extremy coords of Brazil and use loop
    verifyng in library imported for how country this coords are.
    If coords from Brazil, this function request to other function to 
    obtein data from NASA API
    :return: 
    """

    lat_max =   4.3475
    lat_min = -33.9060
    lng_dir = -33.8555
    lng_esq = -73.9336

    for lat in numpy.arange(lat_min, lat_max, 0.5):
        for lng in numpy.arange(lng_esq, lng_dir, 0.5):
            try:
                response = geopip.search(lat=lat, lng=lng)
                country = response.get('NAME')
                if country == 'Brazil':
                    print("Working at latitude= " + str(lat) + " longitude= " + str(lng))
                    request_data_from_api(lat=lat, lng=lng)
            except:
                continue


find_brazil_coords()

endTime = time.time()
totalTime = endTime - startTime
