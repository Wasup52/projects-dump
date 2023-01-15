from os import truncate
import time
from typing import Counter


amine = False

with open("Twitch\\wath time remaining\\t.txt", "r") as f:
    lines = f.readlines()

time_in_min_a = []
time_in_min_z = []
for line in lines:
    if line == "--------------------------Amine--------------------------\n":
        amine = True
    if line.count("h") == 1:
        line_split = line.split("\t")
        # print(line_split)
        for split in line_split:
            if split.count("h") == 1:
                t = split.strip("m\n").split("h")

                if t[1] == "":
                    h = int(t[0]) * 60
                    m = 0
                else:
                    h = int(t[0]) * 60
                    m = int(t[1])

                if amine == True:
                    time_in_min_a.append((h + m) / 1.5)
                else:
                    time_in_min_z.append((h + m) / 2)

time_in_min = time_in_min_a + time_in_min_z

s_a = sum(time_in_min_a)
time_a = s_a / 60
str_time_a = str(time_a).split(".")
str_minute_a = "0." + str_time_a[1][:2]

s_z = sum(time_in_min_z)
time_z = s_z / 60
str_time_z = str(time_z).split(".")
str_minute_z = "0." + str_time_z[1][:2]

s = sum(time_in_min)
time = s / 60
str_time = str(time).split(".")
str_minute = "0." + str_time[1][:2]


print(
    f"il reste {int(str_time_a[0])}h{round(float(str_minute_a)*60)}m a visioner chez Amine"
)
print(
    f"il reste {int(str_time_z[0])}h{round(float(str_minute_z)*60)}m a visioner chez Zwave"
)
print(
    f"il reste {int(str_time[0])}h{round(float(str_minute)*60)}m a visioner ~ {round(time/10)} jours"
)
