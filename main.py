# with open('weather_data.csv', 'r') as data_file:
#     # data = data_file.readlines()
#     # print(data)
#     for line in data_file:
#         print(line.strip())

import csv
with open('weather_data.csv', 'r') as data_file:
    data = csv.reader(data_file)
    temperatures = []

    for row in data:
        print(row)
