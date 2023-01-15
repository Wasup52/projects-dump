from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import random


t1 = time.time()
s = time.sleep


def r():
    s = random.sample(["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"], 4)
    s2 = ""
    for k in range(0, len(s)):
        s2 = s2 + s[k]
    return s2


s2 = r()
s3 = r()
s4 = r()
s5 = r()
username = "test" + s2
password = "pass" + s3
firstname = "test" + s4
lastname = "test" + s5

url = "https://signup.gmx.com/#.1559516-header-signup2-1"
driver = webdriver.Chrome(
    "E-mail creation bot\\.ChromeDriver\\.chromedriver.exe"
)
driver.get(url)
driver.delete_all_cookies()

s(5)

driver.find_element_by_class_name(
    "pos-form-element pos-text-input email-alias-input__alias-input ng-pristine ng-invalid ng-touched"
).send_keys(username)

s(0.5)

driver.find_element_by_id("password").send_keys(password)

s(0.5)

driver.find_element_by_id("passwordc").send_keys(password)

s(0.5)

driver.find_element_by_class_name("btn btn-submit").click()

with open(
    "E-mail creation bot\\Bots\\Yahoo\\.Identifiant.txt",
    "a",
) as f:
    line = (
        "|           "
        + username
        + "            |         "
        + password
        + "      |"
        + "\n"
    )
    f.write(line)

t2 = time.time()
T = t2 - t1
print(T)

s(15)

driver.quit()
