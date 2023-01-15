import sys
import datetime
import win32api
import os
import time
import tkinter as tk
from tkinter import filedialog, Text
import shutil


def get_file_time(file_path):
    date = time.ctime(os.path.getmtime(file_path))

    if date.split()[1] == "Jan":
        month = 1
    if date.split()[1] == "Feb":
        month = 2
    if date.split()[1] == "Mar":
        month = 3
    if date.split()[1] == "Apr":
        month = 4
    if date.split()[1] == "May":
        month = 5
    if date.split()[1] == "Jun":
        month = 6
    if date.split()[1] == "Jul":
        month = 7
    if date.split()[1] == "Aug":
        month = 8
    if date.split()[1] == "Sep":
        month = 9
    if date.split()[1] == "Oct":
        month = 10
    if date.split()[1] == "Nov":
        month = 11
    if date.split()[1] == "Dec":
        month = 12

    day = int(date.split()[2])

    hour = int(date.split()[3].split(":")[0])
    minute = int(date.split()[3].split(":")[1])
    second = 0
    millisecond = 0

    year = int(date.split()[4])

    # adjust hour
    if 1 <= month <= 3 or 11 <= month <= 12:
        if hour == 0:
            if day == 1:
                month -= 1
                if month == 0:
                    month = 12
                    year -= 1
                day = 31
            else:
                day -= 1
            hour = 23
        else:
            hour -= 1
    elif 4 <= month <= 10:
        if hour == 0:
            day -= 1
            hour = 22
        elif hour == 1:
            day -= 1
            hour = 23
        else:
            hour -= 2

    time_tuple = (year, month, day, hour, minute, second, millisecond)

    # print(time_tuple)

    return time_tuple


test = "D:\Robin\Galerie\carte sd 2\A trier\Screenshot_20180709-024612.jpg"

print(get_file_time(test))
