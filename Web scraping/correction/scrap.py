from urllib.request import urlopen as uReq
from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import time
import imaplib
import smtplib
import email
from email.message import EmailMessage

user = "mail@gmail.com"
password = "SECRET"
imap_url = "imap.gmail.com"

var = 33230
t = time.sleep
url = f"https://0100022v.moodle.monbureaunumerique.fr/pluginfile.php/{var}/mod_resource/content/1/TD7d.%20Toyota%20Moodle%20corrig%C3%A9%202020-2021.pdf"

option = webdriver.ChromeOptions()
option.add_argument("headless")
driver = webdriver.Chrome(
    "Web scraping\\.ChromeDriver\\.chromedriver.exe", options=option
)

driver.get(url)
soup = BeautifulSoup(driver.page_source, "html.parser")

driver.quit()

content = soup.findAll("head")

print(content)

print("done")
