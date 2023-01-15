import os
import cv2
import time
import datetime
import win32con
import win32api
import pytesseract
import numpy as np
import tkinter as tk
from tkinter import filedialog
from win32_setctime import setctime
from PIL import Image, ImageGrab
from list_dir import list_dir
from date_modifier_v2 import safe_modif

test_mode = True

with open("sd organiser\\temp data.txt", "r") as f:
    lines = f.readlines()
    line = lines[0].split(",")
    dir_path = line[0].split("=")[1]
    copied_dir_path = line[1].split("=")[1]


def ocr_date(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    thresh = cv2.threshold(gray, 200, 255, cv2.THRESH_BINARY)[1]
    scale_percent = 120  # percent of original size
    width = int(date_thresh.shape[1] * scale_percent / 100)
    height = int(date_thresh.shape[0] * scale_percent / 100)
    resized = cv2.resize(date_thresh, (width, height), interpolation=cv2.INTER_AREA)

    frame = Image.fromarray(resized)
    string = pytesseract.image_to_string(
        frame, config="-c tessedit_char_whitelist=0123456789./"
    )
    return string


file_names = list_dir(dir_path)

file_changed_count = safe_modif(dir_path, test_mode, False)
safe_modif(copied_dir_path, True, True)  # to hide cpoied dir files

file_names = file_names[file_changed_count:]

time.sleep(3)

img_date = ImageGrab.grab(bbox=(1285, 205, 1385, 1015))
date_np = np.array(img_date)
date_gray = cv2.cvtColor(date_np, cv2.COLOR_BGR2GRAY)
date_thresh = cv2.threshold(date_gray, 200, 255, cv2.THRESH_BINARY)[1]


scale_percent = 120  # percent of original size
width = int(date_thresh.shape[1] * scale_percent / 100)
height = int(date_thresh.shape[0] * scale_percent / 100)
resized = cv2.resize(date_thresh, (width, height), interpolation=cv2.INTER_AREA)

cv2.imshow("date", date_thresh)
cv2.imshow("resized", resized)

cv2.waitKey(0)

date = ocr_date(date_np)
dates = date.split("\n")

i = 0
for date in dates:
    date = date.strip("\n")
    day = int(date[:2])
    date = date[2:]

    if date[0] == "7" or date[0] == "/":
        date = date[1:]
    month = int(date[:2])
    date = date[2:]

    if date[0] == "7" or date[0] == "/":
        date = date[1:]
    year = int(date[:4])
    date = date[4:]

    if date[0] == "7" or date[0] == "/":
        date = date[1:]
    date = date.replace(".", "")

    hour = int(date[:2])
    minute = int(date[len(date) - 2 :])
    second = 0

    time_tuple = (year, month, day, hour, minute, second)

    file_location = dir_path + "\\" + file_names[i]

    with open("sd organiser\\temp data.txt", "a") as f:
        f.writelines(file_location, time_tuple)

    print(file_location, time_tuple)
    date = datetime.datetime(*time_tuple)
    modTime = time.mktime(date.timetuple())

    if test_mode:
        pass
    else:
        setctime(file_location, modTime)
        os.utime(file_location, (modTime, modTime))

    i += 1

# ---- Unhide previously hidden files ----
file_names = list_dir(dir_path)

for file_name in file_names:
    file_location = dir_path + "\\" + file_name
    win32api.SetFileAttributes(file_location, win32con.FILE_ATTRIBUTE_NORMAL)

file_names = list_dir(copied_dir_path)

for file_name in file_names:
    file_location = copied_dir_path + "\\" + file_name
    win32api.SetFileAttributes(file_location, win32con.FILE_ATTRIBUTE_NORMAL)
# ----------------------------------------


with open("sd organiser\\temp data.txt", "r") as f:
    result = f.readlines()

root = tk.Tk()

root.geometry("400x800")

result_label = tk.Label(root, text=result)
result_label.place(x=10, y=10)

root.mainloop()
