# This script will be receive a value of latitude and longitude, will connect in database
# process result obtained and generate a graph

import mysql.connector
import time
import geopip
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

# input data
latitude = input("Digite a latitude desejada: ")
longitude = input("Digite a longitude desejada: ")

startTime = time.time()

connection = mysql.connector.connect(host='localhost',
                                     database='nasadata',
                                     user='root',
                                     passwd='felipe3211')

mycursor = connection.cursor()

sql = "SELECT * from irradiation WHERE latitude =%s AND longitude =%s"
#latitude = -30.0301
#longitude= -52.1367

try:
    response = geopip.search(lat=latitude, lng=longitude)
    country = response.get('NAME')
    if country != 'Brazil':
        exit("Coords do not belong to Brazil!")
except:
    exit("Coords do not belong to Brazil!")

# Process latitude and longitude to do reguest to database
rounded_lat = round(latitude, 1)
rounded_lng = round(longitude, 1)

# Bellow I Have decimal parte of earch number
decimal_part_of_lat = round(rounded_lat-int(rounded_lat), 1)
decimal_part_of_lng = round(rounded_lng-int(rounded_lng), 1)

# Verify if I have the latitude in DB
increment_lat = 0
increment_lng = 0
if decimal_part_of_lat*10 % 2 == 0:
    pass
else:
    increment_lat = 0.1

if decimal_part_of_lng*10 % 2 == 0:
    pass
else:
    increment_lng = 0.1

lat_query = round(rounded_lat+increment_lat, 1)
lng_query = round(rounded_lng+increment_lng, 1)

val = (lat_query, lng_query)
mycursor.execute(sql, val)

#sql_lat_verify = "SELECT id, COUNT(*) from irradiation WHERE latitude =%s"
#sql_lng_verify  = "SELECT id, COUNT(*) irradiation WHERE longitude =%s"


records = mycursor.fetchall()
# todo insert here tratment to case record are empty


list_of_months = [[], [], [], [], [], [], [], [], [], [], [], []]  # List 12 X N
for row in records:
    identify, lat, lng, year, month, value = row
    if value == -999.0:  # append only valid values
        continue
    list_of_months[int(month)-1].append(float(value))

month_averages = []
for i in range(12):
    average = sum(list_of_months[i])/len(list_of_months[i])
    month_averages.append((float(average)))
    print("Para o mes {} a media foi {}".format(i+1, average))


endTime = time.time()
totalTime = endTime - startTime

# plot area
fix, ax = plt.subplots(1, 1)

# Set the locator
locator = mdates.MonthLocator
# Specify the format - %b gives up Jan, Feb...
fmt = mdates.DateFormatter('%b')
month_list = ['January', 'February', 'March', 'April', 'May', 'June', 'July',
              'August', 'September', 'October', 'November', 'December']


ax.plot(month_list, month_averages, 'o-')
plt.xticks(rotation=-45)
plt.ylabel('kW-hr/m^2/day')


font1 = {
    'weight': 'bold'
}
# todo parametrise values of x and y with base of max and min value of irradiation
plt.text(x=0, y=3, s="Latitude: ", fontdict=font1)
plt.text(x=2, y=3, s=str(latitude))
plt.text(x=0, y=2.5, s="Longitude: ", fontdict=font1)
plt.text(x=2, y=2.5, s=str(longitude))
plt.grid(True)

plt.title('All Sky Insolation Average per Month')
plt.text(0,0,"teste")
plt.show()

print('-'*20)
print("The total time to catch data was " + str(totalTime))
