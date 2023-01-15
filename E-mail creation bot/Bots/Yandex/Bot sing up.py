from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import random

s = time.sleep
t1 = time.time()


def r():
    s = random.sample(["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"], 4)
    s2 = ""
    for k in range(0, len(s)):
        s2 = s2 + s[k]
    return s2


s2 = r()
s3 = r()
username = "test" + s2
password = "Pass" + s3
firstname = "test" + s2
lastname = "test" + s2

url = "https://passport.yandex.com/registration/mail?from=mail&require_hint=1&origin=hostroot_homer_reg_com&retpath=https%3A%2F%2Fmail.yandex.com%2F&backpath=https%3A%2F%2Fmail.yandex.com%3Fnoretpath%3D1"

driver = webdriver.Chrome(
    "E-mail creation bot\\.ChromeDriver\\.chromedriver.exe"
)
driver.get(url)

driver.find_element_by_id("firstname").send_keys(firstname)

s(0.5)

driver.find_element_by_id("lastname").send_keys(lastname)

s(0.5)

driver.find_element_by_id("login").send_keys(username)

s(0.5)

driver.find_element_by_id("password").send_keys(password)

s(0.5)

driver.find_element_by_id("password_confirm").send_keys(password)


with open(
    "E-mail creation bot\\Bots\\Yandex\\.Identifiant (also Epic).txt",
    "a",
) as f:
    line = (
        "|     "
        + username
        + "@yandex.com       |         "
        + password
        + "      |"
        + "               False                 |"
        + "\n"
    )
    f.write(line)

t2 = time.time()
T = t2 - t1
print(T)

# feboy25790@whowlft.com

