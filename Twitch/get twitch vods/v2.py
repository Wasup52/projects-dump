from bs4 import BeautifulSoup
from numpy.core.numeric import full
import get_vod_link
import requests

streamer_names = ["zwave69", "aminematue"]

for k, streamer_name in enumerate(streamer_names):
    with open(f"Twitch\get twitch vods\.{streamer_name}.html", "r") as f:
        content = f.read()

    soup = BeautifulSoup(content, "lxml")

    content_link = soup.findAll("a")

    link_dict = {}

    for link in content_link:
        href = str(link.get("href"))
        if href.count(f"{streamer_name}/streams/"):
            date = str(link.get_text()).strip("\n").strip(" ")

            link_dict[date] = href

    start_date = "16/06/2021"
    end_date = ""

    # print(link_dict)

    started = False
    for key in link_dict.keys():
        full_date = key
        date = full_date.split(" ")[0].split("-")
        date = f"{date[2]}/{date[1]}/{date[0]}"

        if date == start_date:
            started = True
        if date == end_date:
            started = False

        if started:
            link = link_dict[full_date]

            print(f"---------------------------{date}---------------------------")
            print(get_vod_link.get(link, full_date), full_date + "\n")

    if k != len(streamer_names) - 1:
        print(
            "\n"
            + "!--------------------------Aminematue--------------------------!"
            + "\n\n"
        )
