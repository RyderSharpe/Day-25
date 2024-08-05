import pandas

# Load the data from the CSV file
data = pandas.read_csv("weather_data.csv")

#################################################################
# Output: <class 'pandas.core.frame.DataFrame'>
# Dataframe is equivalent to your entire table.
# print(type(data))

# Output: <class 'pandas.core.series.Series'>
# Series is essentially a column.
# print(type(data["temp"]))

# data_dict = data.to_dict()
# print(data_dict)
# #################################################################
#
# # Convert the "temp" column to a list
# temp_list = data["temp"].to_list()
# # print(temp_list)
#
# len_list = (len(temp_list))
# # print(len_list)
#
# #################################################################
# # Calculate the sum of the list using a for loop
# total_sum = 0
# for x in len_list:
#     total_sum += x
#
# # Calculate the sum of the list using the built-in sum() function
# total_sum = sum(temp_list)
# average = total_sum / len_list
# print(average)
#
# # Calculate the sum of the list using the built-in mean/median/mode() function
# print(data.temp.mean())
# print(data.temp.median())
# print(data.temp.mode())
# print(data.temp.max())
# #################################################################
#
# # GET DATA IN COLUMNS
# print(data["condition"])
print(data.condition)
#
# # GET DATA IN ROW
# print(data[data.day == "Monday"])
# # Print row with max temperature
# print(data[data.temp == data.temp.max()])
# #################################################################
#
# # My version #
# monday = data[data.day == "Monday"]
# # print(monday.condition)
# print(monday.temp)
# temp_fahrenheit = ((monday.temp) * 9/5) + 32
# print(temp_fahrenheit)
#
# # Class version #
# monday = data[data.day == "Monday"]
# monday_temp = monday.temp[0]
# monday_temp_f = monday_temp * 9/5 + 32
# print(monday_temp_f)
# ##################################################################
#
# ## CREATE A DATAFRAME FROM SCRATCH
# data_dict = {
#     "students" : ["Amy", "James", "Angela"],
#     "scores" : [76, 56, 65]
# }
# data = pandas.DataFrame(data_dict)
# # print(data)
# data.to_csv("new_data.csv")