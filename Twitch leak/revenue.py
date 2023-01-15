import csv
import os
import gzip

path = "/root/Documents/Twitch Leak/twitch-payouts/all_revenues/"
test_file = "/root/Documents/Twitch Leak/twitch-payouts/all_revenues/2019/08/28/all_revenues.csv.gz"

CriticalRole_id = "229729353"

berlu_id = "96324761"
berlu_lines = []

year_dir = os.listdir(path)

for year in year_dir:
    # print(year)
    month_list = os.listdir(path+year)
    for month in month_list:
        # print(f"\t{month}")
        sub_dir_list = os.listdir(path+year+"/"+month)
        for sub_dir in sub_dir_list:
            # print(f"\t\t{sub_dir}")
            file_list = os.listdir(path+year+"/"+month+"/"+sub_dir)
            for file in file_list:
                # print(f"\t\t\t{file}")
                with gzip.open(path+year+"/"+month+"/"+sub_dir+"/"+file, 'rt', encoding="utf8") as f:
                    csvFile = csv.reader(f)
                    # lines = [line for line in csvFile]
                    for line in csvFile:
                        # print(line)
                        if CriticalRole_id in line:
                            print(line)
                        #     berlu_lines.append(line)
