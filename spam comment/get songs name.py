from typing_extensions import final
from bs4 import BeautifulSoup
import time

with open("spam comment\\top 100.html", "r", encoding="utf8") as f:
    html = f.read()


soup = BeautifulSoup(html, "html.parser")

content_list = soup.findAll(
    "h3",
    {
        "class": "card-title xs-text-charcoal title--compressed xs-text-2 xs-line-height-2 xs-mb2"
    },
)[0:100]

for content in content_list:
    title = str(content.get_text())
    title = title.split(" ")
    final = ""
    for char in title:
        if char == "":
            pass
        elif char == "by":
            pass
        else:
            final += char + " "
    final = final.strip("\n ").split("\xa0")[1]

    print(final)
