import requests
from bs4 import BeautifulSoup
from requests.models import parse_url

search_url = "https://search.azlyrics.com/suggest.php?q="

with open("spam comment\\songs.txt", "r", encoding="utf8") as f:
    lines = f.readlines()

for line in lines:
    url = search_url + line
    r = requests.get(url)
    content = str(r.content)
    print(content)
    print(content.split("[")[1].split('"')[1])
    if content.split("[")[1].split('"')[1] == "url":
        url = content.split("[")[1].split('"')[3]
        splited = url.split("\\")
        request_url = ""
        for char in splited:
            if char != "":
                request_url += char
        html = requests.get(request_url).text
        soup = BeautifulSoup(html, "html.parser")
        lyrics = soup.get_text()
        # print("-------------------", line, "-------------------")
        print(lyrics)
        # print("--------------------------------------------------------")
