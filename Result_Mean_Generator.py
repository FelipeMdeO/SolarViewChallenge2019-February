# This script will be receive a value of latitude and longitude, will connect in database
# process result obtained and generate a graph

import mysql.connector
import time
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

# input data
#latitude = input("Digite a latitude desejada: ")
#longitude = input("Digite a longitude desejada: ")

# connect to database
from mpl_toolkits.mplot3d.proj3d import transform

startTime = time.time()

connection = mysql.connector.connect(host='localhost',
                                     database='nasadata',
                                     user='root',
                                     passwd='felipe3211')

mycursor = connection.cursor()

sql = "SELECT * from irradiation WHERE latitude =%s AND longitude =%s"
latitude = -33.2
longitude= -53
val = (latitude, longitude)
mycursor.execute(sql, val)

records = mycursor.fetchall()

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

# todo plot area
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
