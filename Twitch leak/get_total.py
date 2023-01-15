with open("berlu", "r") as f:
    lines = f.readlines()

dic_2019 = {}
dic_2020 = {}
dic_2021 = {}
stuff_in_dic = ['ad_share_gross', 'sub_share_gross', 'bits_share_gross', 'bits_developer_share_gross', 'bits_extension_share_gross', 'prime_sub_share_gross', 'bit_share_ad_gross', 'fuel_rev_gross', 'bb_rev_gross']

for line in lines:
    if line == "['user_id', 'payout_entity_id', 'ad_share_gross', 'sub_share_gross', 'bits_share_gross', 'bits_developer_share_gross', 'bits_extension_share_gross', 'prime_sub_share_gross', 'bit_share_ad_gross', 'fuel_rev_gross', 'bb_rev_gross', 'report_date', 'experimental_rev_gross']\n":
        pass
    else:
        infos = line.strip("['").strip("']\n").split("', '")
        ad_share_gross = infos[2]
        sub_share_gross = infos[3]
        bits_share_gross = infos[4]
        bits_developer_share_gross = infos[5]
        bits_extension_share_gross = infos[6]
        prime_sub_share_gross = infos[7]
        bit_share_ad_gross = infos[8]
        fuel_rev_gross = infos[9]
        bb_rev_gross = infos[10]
        date_split = infos[11].split("/")
        date = f"{date_split[1]}/{date_split[0]}/{date_split[2]}"
        year = date_split[2]
        if year == "2019":
            if date in dic_2019.keys():
                pass
            else:
                # dic_2019[date] = {stuff_in_dic[k-2]:float(infos[k]) for k in range(2,11)}
                dic_2019[date] = [float(infos[k]) for k in range(2,11)]
        if year == "2020":
            if date in dic_2020.keys():
                pass
            else:
                # dic_2020[date] = {stuff_in_dic[k-2]:float(infos[k]) for k in range(2,11)}
                dic_2020[date] = [float(infos[k]) for k in range(2,11)]
        if year == "2021":
            if date in dic_2021.keys():
                pass
            else:
                # dic_2021[date] = {stuff_in_dic[k-2]:float(infos[k]) for k in range(2,11)}
                dic_2021[date] = [float(infos[k]) for k in range(2,11)]

dic = {"2019":dic_2019,"2020":dic_2020,"2021":dic_2021}

month_total_list = []

print(stuff_in_dic)
for key in dic.keys():
    print(key)
    for key2 in sorted(dic[key].keys()):
        month_total = sum(dic[key][key2])
        print(f"\t{key2}, {dic[key][key2]}, {month_total}")
        month_total_list.append(month_total)

print(f"total : {sum(month_total_list)}")
# print(f"difference from online liste : {sum(month_total_list) - 9626712.16}")