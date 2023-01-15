import sys
import shutil
import datetime
import win32api
import os
import time
import pytz
import progress.bar
from win32com.propsys import propsys, pscon
from win32_setctime import setctime


def set_time(file_path, time_tuple):  # set windows clock time
    dt = datetime.datetime(*time_tuple)
    epoch_time = dt.timestamp()
    setctime(file_path, epoch_time)
    os.utime(file_path, (epoch_time, epoch_time))


def get_file_time(file_path, file_name):
    try:
        properties = propsys.SHGetPropertyStoreFromParsingName(file_path)
        dt = properties.GetValue(pscon.PKEY_Media_DateEncoded).GetValue()
        dt_france = dt.astimezone(pytz.timezone("CET"))
    except:
        dt = datetime.datetime.fromtimestamp(os.path.getmtime(file_path))
        dt_france = dt.astimezone(pytz.timezone("CET"))

    if file_name.count("("):
        ext = file_name.split(".")[1]
        file_name = file_name.split("(")[0]
        file_name = file_name + "." + ext

    if file_name.count("Resized"):
        dt_france = str(dt_france).split("+")[0]
        date = dt_france.split(" ")[0]
        time = dt_france.split(" ")[1]

        year, month, day = date.split("-")
        hour, minute, second = time.split(":")
    elif file_name.count("Screenshot"):
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
        elif file_name.split(".")[1] == "png":
            file_name = file_name.split(".")[0]
            file_date = file_name.split("_")[1]

            year, month, day, hour, minute, second = file_date.split("-")
    elif file_name.count("_"):
        try:
            int(file_name.split("_")[0])
            file_name = file_name.split(".")[0]
            file_date = file_name.split("_")
            date = file_date[0]
            time = file_date[1]

            year = date[0:4]
            month = date[4:6]
            day = date[6 : len(date)]

            hour = time[0:2]
            minute = time[2:4]
            second = time[4 : len(time)]
        except:
            dt_france = str(dt_france).split("+")[0]
            date = dt_france.split(" ")[0]
            time = dt_france.split(" ")[1]

            # dt = str(dt).split("+")[0]
            # date = dt.split(" ")[0]
            # time = dt.split(" ")[1]

            year, month, day = date.split("-")
            hour, minute, second = time.split(":")
    else:
        dt_france = str(dt_france).split("+")[0]
        date = dt_france.split(" ")[0]
        time = dt_france.split(" ")[1]

        year, month, day = date.split("-")
        hour, minute, second = time.split(":")

    time_tuple = (
        int(year),
        int(month),
        int(day),
        int(hour),
        int(minute),
        int(second),
        0,
    )

    return time_tuple


t1 = time.time()

parent_dir = "F:"

dirs_list = os.listdir(parent_dir)

for dir_name in dirs_list:
    print(dir_name)
    files_names = os.listdir(parent_dir + "\\" + dir_name)

    if (
        dir_name == "System Volume Information"
        or dir_name == "Android"
        or dir_name == "DCIM"
        or dir_name == "document"
        or dir_name == "Fiches_cours"
        or dir_name == "Pictures"
        or dir_name == "SleepBot"
        or dir_name == "Transfert"
    ):
        pass
    else:
        bar = progress.bar.IncrementalBar("\tProcessing", max=len(files_names))
        for file_name in files_names:
            file_path = parent_dir + "\\" + dir_name + "\\" + file_name
            time_tuple = get_file_time(file_path, file_name)
            set_time(file_path, time_tuple)
            bar.next()
        bar.finish()

t2 = time.time()

print("done", t1, t2, t2 - t1)
