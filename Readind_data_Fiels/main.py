# import csv
# import pandas as pd
#
# #
# # with open("2.1 weather_data.csv") as weather_data:
# #     data = csv.reader(weather_data)
# #     temperature = []
# #     for row in data:
# #         temp = row[1]
# #         if row[1] != "temp":
# #             temp = int(temp)
# #         temperature.append(temp)
# #
# #     print(temperature)
#
# data = pd.read_csv("2.1 weather_data.csv")
# # print(data["temp"].mean())
# #
# # print(data[data.temp == data.temp.max()])
#
# monday = data[data.day == "Monday"]
# print(monday.temp+270)

#  create a csv called score_coount that has a smalltable
# containg fur colors

# figure out how many of each color exist
import pandas as pd

data = pd.read_csv("4.1 2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
primary_fur = data["Primary Fur Color"].value_counts()
df = pd.DataFrame(primary_fur)
df.to_csv("score_count.csv")