import csv

top_path = "/root/Documents/Twitch Leak/Top gross earnings"

with open(top_path, "r") as f:
    lines = f.readlines()

for line in lines:
    infos = line.split()
    print(infos)

    rg = infos[0]
    name = infos[1]
    usr_id = infos[2]
    pay = infos[3]

    with open('/root/Documents/Twitch Leak/Top gross earnings.csv', 'a') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(infos)