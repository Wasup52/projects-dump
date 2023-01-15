import os
import time
import datetime
import win32con
import win32api
from list_dir import list_dir
from win32_setctime import setctime


dir_path = "D:\Robin\Galerie\dossier sd pas ok\Louise"


def safe_modif(dir_path, no_modif, copied):
    file_changed_count = 0

    file_names = list_dir(dir_path)

    for file_name in file_names:

        special_file = False

        if file_name.count("Instagram"):
            date = file_name.split("_")[1].split(".")[0]
            date = date.split("-")
            year = int(date[0])
            month = int(date[1])
            day = int(date[2])
            hour = int(date[3])
            minute = int(date[4])
            second = int(date[5])
            time_tuple = (year, month, day, hour, minute, second)
        elif file_name.count("Screenshot") and file_name.count(".png"):
            date = file_name.split("_")[1].split(".")[0]
            date = date.split("-")
            year = int(date[0])
            month = int(date[1])
            day = int(date[2])
            hour = int(date[3])
            minute = int(date[4])
            second = int(date[5])
            time_tuple = (year, month, day, hour, minute, second)
        elif file_name.count("Screenshot") and file_name.count(".jpg"):
            date = file_name.split("_")[1].split(".")[0]
            year = int(date[:4])
            date = date[4:]
            month = int(date[:2])
            date = date[2:]
            day = int(date[:2])
            date = date[2:].strip("-")
            hour = int(date[:2])
            date = date[2:]
            minute = int(date[:2])
            date = date[2:]
            second = int(date[:2])
            time_tuple = (year, month, day, hour, minute, second)
        elif file_name.count("Snapchat") and file_name.count("_"):
            date = file_name.split("_")[1].split(".")[0]
            date = date.split("-")
            year = int(date[0])
            month = int(date[1])
            day = int(date[2])
            hour = int(date[3])
            minute = int(date[4])
            second = int(date[5])
            time_tuple = (year, month, day, hour, minute, second)
        elif file_name.count("IMG_"):
            date = file_name.split("_")[1] + "_" + file_name.split("_")[2]
            year = int(date[:4])
            date = date[4:]
            month = int(date[:2])
            date = date[2:]
            day = int(date[:2])
            date = date[2:].strip("_")
            hour = int(date[:2])
            date = date[2:]
            minute = int(date[:2])
            date = date[2:]
            second = int(date[:2])
            time_tuple = (year, month, day, hour, minute, second)
        elif file_name.count("_") and file_name.count("-") == 0:
            ok = 0
            for part in file_name.split(".")[0].split("_"):
                if part.isdigit():
                    ok += 1
                if ok == len(file_name.split("_")):
                    date = file_name
                    year = int(date[:4])
                    date = date[4:]
                    month = int(date[:2])
                    date = date[2:]
                    day = int(date[:2])
                    date = date[2:].strip("_")
                    hour = int(date[:2])
                    date = date[2:]
                    minute = int(date[:2])
                    date = date[2:]
                    second = int(date[:2])
                    special_file = True
                    time_tuple = (year, month, day, hour, minute, second)

        file_location = dir_path + "\\" + file_name

        if (
            file_name.count("Instagram")
            or file_name.count("Screenshot")
            and file_name.count(".png")
            or file_name.count("Screenshot")
            and file_name.count(".jpg")
            or file_name.count("Snapchat")
            and file_name.count("_")
            or special_file
            or file_name.count("IMG_")
        ):
            if copied:
                pass
            else:
                date = (
                    str(time_tuple[2])
                    + "/"
                    + str(time_tuple[1])
                    + "/"
                    + str(time_tuple[0])
                    + " "
                    + str(time_tuple[3])
                    + ":"
                    + str(time_tuple[4])
                    + ":"
                    + str(time_tuple[5])
                )
                print(file_location, date)
            date = datetime.datetime(*time_tuple)
            modTime = time.mktime(date.timetuple())

            if no_modif:
                pass
            else:
                setctime(file_location, modTime)
                os.utime(file_location, (modTime, modTime))

            win32api.SetFileAttributes(file_location, win32con.FILE_ATTRIBUTE_HIDDEN)

            file_changed_count += 1

    return file_changed_count


# safe_modif(dir_path, True)
