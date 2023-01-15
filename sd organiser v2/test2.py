from time import time
import os
import progress.bar

file_name = "Screenshot_20200831-230305.jpg"
# file_name = "Screenshot_2016-01-01-23-37-37.png"

if file_name.split(".")[1] == "jpg":
    file_name = file_name.split(".")[0]
    file_date = file_name.split("_")[1]
    date = file_date.split("-")[0]
    time = file_date.split("-")[1]

    year = date[0:4]
    month = date[4:6]
    day = date[6 : len(date)]

    hour = time[0:2]
    minute = time[2:4]
    second = time[4 : len(time)]

if file_name.split(".")[1] == "png":
    file_name = file_name.split(".")[0]
    file_date = file_name.split("_")[1]

    year, month, day, hour, minute, second = file_date.split("-")

print(year, month, day, hour, minute, second)
