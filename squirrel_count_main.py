# TODO - Create a CSV called "squirrel_count"
# TODO - Create tabel with "Primary Fur Color" row.
# TODO - How many of each color listed beside each color.
# Fur Color, Count
# grey, 2473
# red, 392
# black, 103


import pandas

#####################################################
# MY VERSION
# # Load the data from the CSV file
# data = pandas.read_csv("squirrel_data.csv")
# primary_fur_color = data['Primary Fur Color']
# counts = data['Primary Fur Color'].value_counts()
# print(counts)
# counts.to_csv("squirrel_count.csv")
#####################################################

#################################################################################
# CLASS VERSION
data = pandas.read_csv("squirrel_data.csv")
grey_squirrels = data[data["Primary Fur Color"] == "Gray"]
# print(grey_squirrels)
red_squirrels = data[data["Primary Fur Color"] == "Cinnamon"]
black_squirrels = data[data["Primary Fur Color"] == "Black"]

grey_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
red_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])
print(grey_squirrels_count)
print(red_squirrels_count)
print(black_squirrels_count)

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [grey_squirrels_count, red_squirrels_count, black_squirrels_count]
}

df = pandas.DataFrame(data_dict)
df.to_csv("class_squirrel_count")

#################################################################################
