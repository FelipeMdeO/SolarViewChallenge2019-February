# This script will be connect in database
# and download irradiation data to Brazil of informated year

import mysql.connector
import time

startTime = time.time()

connection = mysql.connector.connect(host='localhost',
                                     database='nasadata',
                                     user='root',
                                     passwd='felipe3211')

mycursor = connection.cursor()

file = open('output.txt', 'w')
year = input("Digite o ano a ser avaliado: ")

sql = "SELECT latitude, longitude, incidence  from irradiation WHERE year = %s"
val = (2017, )
mycursor.execute(sql, val)
records = mycursor.fetchall()


i = 0
incidence_average = 0
for row in records:
    latitude, longitude, incidence = row
    incidence_average = incidence_average + incidence
    if i >= 11:
        incidence_average = incidence_average/12
        line_to_file = str(latitude) + ';' + str(round(longitude, 1)) + ';' + str(incidence_average) + '\n'
        file.write(line_to_file)
        incidence_average = 0
        i = 0
    i = i + 1


file.close()

endTime = time.time()
totalTime = endTime - startTime

print("The total time to catch data was " + str(totalTime))
