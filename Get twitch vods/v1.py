import os
from pynput.mouse import Button, Controller
from pynput.keyboard import Key, Controller as Keyboard
import time
import _thread
from urllib.request import urlopen as uReq
from selenium import webdriver
from bs4 import BeautifulSoup
import time
import cfscrape
import pyperclip

url = "https://www.twitch.tv/zwave69/videos?filter=archives&sort=time"

option = webdriver.ChromeOptions()
option.add_argument("headless")
driver = webdriver.Chrome(
    "Web scraping\\.ChromeDriver\\.chromedriver.exe", options=option
)

driver.get(url)

time.sleep(3)

soup = BeautifulSoup(driver.page_source, "html.parser")

driver.quit()

content_link = soup.findAll("div", {"class": "ScTransformWrapper-uo2e2v-1 eiQqOY"})
content_date = soup.findAll("div", {"class": "preview-card-thumbnail__image"})

mouse = Controller()
keyboard = Keyboard()

time.sleep(1)

keyboard.type("3")
keyboard.press(Key.enter)
keyboard.release(Key.enter)

content = {}

print(len(content_link))
print(len(content_date))
print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
for k in range(0, len(content_link)):
    line_link = content_link[k]
    line_link = str(line_link)
    line_link_splited = line_link.split("<")
    for split in line_link_splited:
        if split.count('href="/videos'):
            splited = split.split(" ")
            for split in splited:
                if split.count("href"):
                    link = split.split('"')
                    link = "https://www.twitch.tv" + link[1]
                    print(link)
    line_date = content_date[k]
    line_date = str(line_date)
    line_date_splited = line_date.split('title="')
    split = line_date_splited[1]
    splited = split.split('"')
    date = splited[0]
    print(date)
    content[date] = link
    print("----------------------------")


for key in content.keys():
    date = key
    if date.split(" ")[1] != "juin":
        pass
    else:
        link = content[date]
        print(date, link)

        keyboard.type(link)
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)

        time.sleep(20)

        keyboard.press(Key.shift)

        for k in range(0, 2):
            keyboard.press(Key.up)
            keyboard.release(Key.up)
        keyboard.release(Key.enter)

        keyboard.release(Key.shift)

        time.sleep(0.5)

        keyboard.press(Key.ctrl)
        keyboard.type("c")
        keyboard.release(Key.ctrl)

        time.sleep(0.5)

        text = pyperclip.paste()
        source_num = text.split("\n")[1][0]

        keyboard.type(source_num)
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)

        time.sleep(0.5)

        keyboard.press(Key.shift)

        for k in range(0, 4):
            keyboard.press(Key.up)
            keyboard.release(Key.up)
        keyboard.release(Key.enter)

        keyboard.release(Key.shift)

        time.sleep(0.5)

        keyboard.press(Key.ctrl)
        keyboard.type("c")
        keyboard.release(Key.ctrl)

        time.sleep(0.5)

        text = pyperclip.paste()
        m3u8_link = text.split("\n")[1][8:]
        print(m3u8_link)

        keyboard.type("y")
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)

        print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
