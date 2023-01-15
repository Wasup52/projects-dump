with open("Twitch\get twitch vods\\_vod links.txt") as f:
    lines = f.readlines()

to_test = """---------------------------18/06/2021---------------------------
https://dgeft87wbj63p.cloudfront.net/4fd806bd4648b677d405_zwave69_42388091372_1624048644/chunked/index-dvr.m3u8

---------------------------19/06/2021---------------------------
https://dgeft87wbj63p.cloudfront.net/eb3a85c9cdc9df8ff52a_zwave69_42397138780_1624137214/chunked/index-dvr.m3u8

---------------------------24/06/2021---------------------------
https://dgeft87wbj63p.cloudfront.net/007e4f1e9779376b16a0_zwave69_42440153084_1624563856/chunked/index-dvr.m3u8

---------------------------25/06/2021---------------------------
https://dgeft87wbj63p.cloudfront.net/2813d2be6cd36d1fc384_zwave69_42449735932_1624651274/chunked/index-dvr.m3u8

---------------------------26/06/2021---------------------------
https://dgeft87wbj63p.cloudfront.net/ffe4cd3910a565e872eb_zwave69_42459383228_1624740793/chunked/index-dvr.m3u8

---------------------------27/06/2021---------------------------
https://dgeft87wbj63p.cloudfront.net/7f3d730b59e832646cf9_zwave69_42468752012_1624827719/chunked/index-dvr.m3u8

---------------------------28/06/2021---------------------------
https://dgeft87wbj63p.cloudfront.net/3aaecca17dc4dc7e0fd5_zwave69_42478178284_1624919207/chunked/index-dvr.m3u8

---------------------------29/06/2021---------------------------
https://dgeft87wbj63p.cloudfront.net/03e051a8fbad096b8597_zwave69_42486376524_1624993084/chunked/index-dvr.m3u8

"""

to_test = to_test.split("\n")

# print(to_test)
# print(lines)

sure_dict = {}
for k in range(0, len(lines) - 1, 3):
    date = lines[k].strip("\n").strip("---------------------------")
    link = lines[k + 1].strip("\n")

    # print(link, date)

    sure_dict[date] = link

# print("------------------------------------------------")

to_test_dict = {}
for k in range(0, len(to_test) - 1, 3):
    date = to_test[k].strip("\n").strip("---------------------------")
    link = to_test[k + 1]

    # print(link, date)

    to_test_dict[date] = link


for key in to_test_dict.keys():
    to_test_link = to_test_dict[key]
    sure_link = to_test_dict[key]

    if to_test_link == sure_link:
        print(key, "GOOD")
    else:
        print(key, "BAD")
