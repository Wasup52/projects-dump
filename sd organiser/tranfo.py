import os


dir_path = "F:\Découpage vidéo"
names = os.listdir(dir_path)

file_names = []
for name in names:
    name = name + "\n"
    file_names += name

with open("sd organiser\\temp data.txt", "w") as f:
    f.writelines(file_names)
with open("sd organiser\\temp data.txt", "r") as f:
    lines = f.readlines()

for line in lines:
    line = line.strip("\n")
    line = '"' + line + '"' + ","
    print(line)
