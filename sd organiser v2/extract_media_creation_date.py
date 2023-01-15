import pytz
import datetime
import time
import os
import win32api
from win32com.propsys import propsys, pscon

file_path = "20210918_232855.mp4"
# file_path = "received_303994887680793.mp4"


try:
    properties = propsys.SHGetPropertyStoreFromParsingName(file_path)
    dt = properties.GetValue(pscon.PKEY_Media_DateEncoded).GetValue()
    dt_france = dt.astimezone(pytz.timezone("UTC"))
    print(dt_france, "first")

    dt_france = str(dt_france).split("+")[0]
    date = dt_france.split(" ")[0]
    time = dt_france.split(" ")[1]

    # dt = str(dt).split("+")[0]
    # date = dt.split(" ")[0]
    # time = dt.split(" ")[1]

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

    print(time_tuple)
except:
    dt = datetime.datetime.fromtimestamp(os.path.getmtime(file_path))
    dt_france = dt.astimezone(pytz.timezone("UTC"))
    print(dt_france, "second")

    dt_france = str(dt_france).split("+")[0]
    date = dt_france.split(" ")[0]
    time = dt_france.split(" ")[1]

    # dt = str(dt).split("+")[0]
    # date = dt.split(" ")[0]
    # time = dt.split(" ")[1]

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

    print(time_tuple)


def set_time(time_tuple):  # set windows clock time
    dayOfWeek = datetime.datetime(*time_tuple).isocalendar()[2]
    t = time_tuple[:2] + (dayOfWeek,) + time_tuple[2:]
    print(*t)
    win32api.SetSystemTime(*t)


set_time(time_tuple)
