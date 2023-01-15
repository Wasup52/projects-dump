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

# test_mode = True
dir_path = "D:/Robin/Galerie/dossier sd ok/Anniv Hiver"
copied_dir_path = "D:/Robin/Galerie/dossier sd ok/Anniv Hiver"


root = tk.Tk()

yes = tk.IntVar()
root.title("Date modifier")
root.geometry("640x300")


def choose_sd_dir():
    global dir_path
    dir_path = tk.filedialog.askdirectory(initialdir="F:", title="Select dir")
    sd_dir_path["text"] = dir_path


def choose_copied_dir():
    global copied_dir_path
    copied_dir_path = tk.filedialog.askdirectory(
        initialdir="D:\Robin\Galerie", title="Select dir"
    )
    copy_to_sd_dir_path["text"] = copied_dir_path


def launch():
    root.destroy()
    root.quit()


sd_dir_path_label = tk.Label(root, text="Sd dir path :", font=("bold", 14))
sd_dir_path_label.place(x=0, y=10)
sd_dir_path_button = tk.Button(root, text="choose", width=10, command=choose_sd_dir)
sd_dir_path_button.place(x=550, y=40)
sd_dir_path = tk.Label(root, text=dir_path, font=14)
sd_dir_path.place(x=0, y=40)

copy_to_sd_dir_path_label = tk.Label(root, text="Copied dir path :", font=("bold", 14))
copy_to_sd_dir_path_label.place(x=0, y=80)
copy_to_sd_dir_path_button = tk.Button(
    root, text="choose", width=10, command=choose_copied_dir
)
copy_to_sd_dir_path_button.place(x=550, y=110)
copy_to_sd_dir_path = tk.Label(root, text=copied_dir_path, font=14)
copy_to_sd_dir_path.place(x=0, y=110)

test_mode_label = tk.Label(root, text="Test mode ?", font=("bold", 14))
test_mode_label.place(x=0, y=160)
test_mode_box_yes = tk.Checkbutton(root, variable=yes)
test_mode_box_yes.place(x=150, y=160)

launch_button = tk.Button(root, text="Launch", font=("bold", 14), command=launch)
launch_button.place(x=280, y=220)

root.mainloop()
if yes.get() == 1:
    test_mode = True
else:
    test_mode = False

print(dir_path, copied_dir_path, test_mode)

is_ok = False
if test_mode:
    root = tk.Tk()

    root.title("Date modifier")
    root.geometry("440x200")

    def yes():
        global is_ok
        is_ok = True
        root.destroy()
        root.quit()

    def no():
        global is_ok
        is_ok = False
        root.destroy()
        root.quit()

    succesfull_label = tk.Label(root, text="Was test successfull ?", font=("bold", 14))
    succesfull_label.place(x=150, y=50)
    yes_button = tk.Button(root, text="Yes", font=14, width=10, command=yes)
    yes_button.place(x=100, y=120)
    no_button = tk.Button(root, text="No", font=14, width=10, command=no)
    no_button.place(x=250, y=120)

    root.mainloop()

    if is_ok:
        data = f"dir_path={dir_path}, copied_dir_path={copied_dir_path}"
        with open("sd organiser\\temp data.txt", "w") as f:
            f.writelines(data)

        print("Launched for real")
        os.startfile("sd organiser\\no_test.py")


"""
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
"""
