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
s4 = r()
s5 = r()
username = "test" + s2
password = "Pass" + s3
firstname = "test" + s4
lastname = "test" + s5

url = "https://signup.mail.com/#.1258-header-signup2-1"

driver = webdriver.Chrome(
    "E-mail creation bot\\.ChromeDriver\\.chromedriver.exe"
)
driver.get(url)

s(1)

# driver.find_element_by_class_name(
#     "pos-form-element pos-text-input email-alias-input__alias-input ng-pristine ng-invalid ng-touched"
# ).send_keys(username)

s(0.5)

driver.find_element_by_id("21fdc3df-1c22-4c94-a639-7ae006ff5e57").send_keys(firstname)

s(0.5)

driver.find_element_by_id("80d450b2-fd53-4343-94de-a1c2b5ed9691").send_keys(lastname)

s(0.5)

select = Select(driver.find_element_by_id("f54a4582-1c14-44a9-9599-943aeb3834ea"))
select.select_by_value("AL")

s(0.5)

driver.find_element_by_class_name("pos-dob pos-dob--mm").send_keys("02")

s(0.5)

driver.find_element_by_class_name("pos-dob pos-dob--dd").send_keys("75")

s(0.5)

driver.find_element_by_class_name("pos-dob pos-dob--yyyy").send_keys("2001")

s(0.5)

driver.find_element_by_id("password").send_keys(password)

s(0.5)

driver.find_element_by_id("confirm-password").send_keys(password)


with open(
    "E-mail creation bot\\Bots\\mail.com\\.Identifiant (also Epic).txt",
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
