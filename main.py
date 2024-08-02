import pandas
import numpy as np

# Load the data from the CSV file
data = pandas.read_csv("weather_data.csv")
df = pandas.DataFrame(np.random.randn(5,3),columns=['Monday','temp','condition'])

##################################################################
# # Output: <class 'pandas.core.frame.DataFrame'>
# # Dataframe is equivalent to your entire table.
# print(type(data))
#
# # Output: <class 'pandas.core.series.Series'>
# # Series is essentially a column.
# print(type(data["temp"]))

# data_dict = data.to_dict()
# print(data_dict)
##################################################################

# # Convert the "temp" column to a list
# temp_list = data["temp"].to_list()
# # print(temp_list)
#
# len_list = (len(temp_list))
# # print(len_list)

##################################################################
# # Calculate the sum of the list using a for loop
# total_sum = 0
# for x in len_list:
#     total_sum += x

# # Calculate the sum of the list using the built-in sum() function
# total_sum = sum(temp_list)
# average = total_sum / len_list
# print(average)

# # Calculate the sum of the list using the built-in mean/median/mode() function
# print(data.temp.mean())
# print(data.temp.median())
# print(data.temp.mode())
# print(data.temp.max())
##################################################################

# # Get data in columns
# print(data["condition"])
# print(data.condition)

# # Get data in row
# print(data[data.day == "Monday"])

# Print row with max temperature
print(data[data.temp == data.temp.max()])
