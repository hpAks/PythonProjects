import csv
import pandas
data_lines = []
with open("weather_data.csv") as file:
    for line in file:
        data_lines.append(line)

with open("weather_data.csv") as csv_file:
    data = csv.reader(csv_file)
    temp = []
    for row in data:
        if row[1] != "temp":
            temp.append(int(row[1]))
    print(temp)

data = pandas.read_csv("weather_data.csv")
data_dict = data.to_dict()
print(data_dict)
avg = sum(data["temp"])/len(data["temp"])
temp_list = data["temp"]
print(f"Average temperature: {temp_list.mean()}")
print(f"Max temperature: {temp_list.max()}")
print(f"Min temperature:{temp_list.min()}")
print(data.condition[0])
print(data[data.day == "Monday"])
print(data[data.temp == data.temp.max()])
monday = data[data.day == "Monday"]
monday_temp = monday.temp * 1.8 +32
print(f"Mondays temp in F:{monday_temp}")


# Squirrel fur count
squirrel_data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
fur_col = squirrel_data["Primary Fur Color"]

fur_dict = {}
for col in fur_col:
    if col in fur_dict:
        count = fur_dict[col]
        fur_dict.update({col: count+1})
    else:
        fur_dict.update({col:1})
data_dict = {
    "Fur Color":[fur_dict.keys()],
    "Count":[fur_dict.values()]
}
data_frame = pandas.DataFrame(data_dict)
print(data_frame.to_csv("squirrel_count.csv"))


