import sys
import datetime
# import win32api
import os
import time
import tkinter as tk
from tkinter import filedialog, Text
import shutil


def set_time(time_tuple):
    dayOfWeek = datetime.datetime(*time_tuple).isocalendar()[2]
    t = time_tuple[:2] + (dayOfWeek,) + time_tuple[2:]
    print(*t)
    win32api.SetSystemTime(*t)


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

    print(time_tuple)

    return time_tuple


# ----- get the dir to transfer path -----
root = tk.Tk()


def img_path():
    global initial_dir
    initial_dir = tk.filedialog.askdirectory(
        initialdir="D:\Robin\Galerie", title="Choose Dir To Transfert To Sd Card"
    )
    root.destroy()
    root.quit()


canvas = tk.Canvas(root, height=80, width=340, bg="#263D42")
canvas.pack()

frame = tk.Frame(root, bg="white")
frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

button = tk.Button(
    frame,
    text="Choose Dir To Transfert To Sd Card",
    padx=10,
    pady=5,
    fg="black",
    command=img_path,
)
button.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

button2 = tk.Button

root.mainloop()
# ----------------------------------------

# ----- get the dir to transfer to path -----
root = tk.Tk()


def img_path():
    global destintion_dir
    destintion_dir = tk.filedialog.askdirectory(
        initialdir="F:", title="Choose Dir To Transfert On To Sd Card"
    )
    root.destroy()
    root.quit()


canvas = tk.Canvas(root, height=80, width=340, bg="#263D42")
canvas.pack()

frame = tk.Frame(root, bg="white")
frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

button = tk.Button(
    frame,
    text="Choose Dir To Transfert On To Sd Card",
    padx=10,
    pady=5,
    fg="black",
    command=img_path,
)
button.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

button2 = tk.Button

root.mainloop()
# -------------------------------------------

files = os.listdir(initial_dir)

for file_name in files:
    time_tuple = get_file_time(initial_dir + "\\" + file_name)
    time.sleep(0.5)
    set_time(time_tuple)
    time.sleep(0.5)
    shutil.copy(initial_dir + "\\" + file_name, destintion_dir + "\\" + file_name)

print("done")
