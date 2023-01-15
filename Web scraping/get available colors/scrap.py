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

t = time.sleep
url = "https://www.wegobuy.com/en/page/buy?from=search-input&url=https%3A%2F%2Fitem.taobao.com%2Fitem.htm%3Fid%3D614687794037&partnercode=w949NG"

# option = webdriver.ChromeOptions()
# option.add_argument("headless")
# driver = webdriver.Chrome(
#     "Web scraping\\.ChromeDriver\\.chromedriver.exe", options=option
# )
option = webdriver.FirefoxOptions()
option.add_argument("headless")
driver = webdriver.Firefox(options=option)

driver.get(url)
driver.find_element_by_xpath(
    '//*[@id="container"]/div/div[1]/div[2]/div/div[2]/div/footer/a'
).click()
t(0.5)
driver.find_element_by_xpath(
    '//*[@id="container"]/div/div[1]/div[2]/div/div[1]/div[2]/div[2]/div[2]/div[5]/div[2]/dl[1]/dd/ul/li[5]/span'
).click()

soup = BeautifulSoup(driver.page_source, "html.parser")

driver.quit()

content = soup.findAll("ul", {"class": "goods-options-tags"})[1]

colors = {}
for tag in content:
    ok = str(tag).split('"')[1]
    if ok == "disabled":
        colors[tag.span.text] = "OOS"
    else:
        colors[tag.span.text] = "in stock"

string = ""
for color in colors:
    string += f"{color} is {colors[color]} \n"

subject = "Ambition nmini swoosh hoodie"
body = string
msg = f"Subject: {subject}\n\n{body}"

# if colors[Earthy] != "OOS" or colors[black] != "OOS":
#     mail.sendmail(user, "mail@hotmail.fr", msg)
#     mail = smtplib.SMTP("smtp.gmail.com", 587)
#     mail.ehlo()  # start
#     mail.starttls()
#     mail.login(user, password)
#     mail.send_message(msg)
#     mail.close()  # stop

with open("Web scraping\\get available colors\\colors.txt", "w") as f:
    f.writelines(string)

print("done")
