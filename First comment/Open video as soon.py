import urllib, json
import urllib.request
import requests
from selenium import webdriver
import time


def look_for_new_video():
    api_key = "SECRET" # google api key
    channel_id = "channel id" # the channel id of the channel you want to look for new videos

    base_video_url = "https://www.youtube.com/watch?v="
    base_search_url = "https://www.googleapis.com/youtube/v3/search?"

    url = (
        base_search_url
        + f"key={api_key}&channelId={channel_id}&part=snippet,id&order=date&maxResults=1"
    )
    print(url)
    inp = urllib.request.urlopen(url)

    resp = json.load(inp)
    vidID = resp["items"][0]["id"]["videoId"]
    print(vidID)

    video_exists = False

    with open(
        "videoid.json", "r"
    ) as json_file:
        data = json.load(json_file)
        if data["videoId"] != vidID:
            driver = webdriver.Chrome(
                ".ChromeDriver\\.chromedriver.exe"
            )
            driver.get(base_video_url + vidID)
            video_exists = True

    if video_exists:
        with open(
            "videoid.json",
            "w",
        ) as json_file:
            data = {"videoId": vidID}
            json.dump(data, json_file)


try:
    while True:
        look_for_new_video()
        time.sleep(10)
except KeyboardInterrupt:
    print("stopping")

