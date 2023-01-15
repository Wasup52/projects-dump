import csv

with open("Web scraping\\area_data.txt", "r") as f:
    lines = f.readlines()

dic = {}
for line in lines:
    area = line.split(">")[1].split("<")[0]
    area_id = line.split('"')[1]
    dic[area] = area_id

final = [["area", "area_id"]]
for key in dic.keys():
    final.append([key, dic[key]])

with open("Web scraping\\area_list.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(final)
