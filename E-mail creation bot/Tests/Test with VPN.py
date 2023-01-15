from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
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

url = "https://signup.live.com/signup?lcid=1033&wa=wsignin1.0&rpsnv=13&ct=1571687962&rver=7.0.6737.0&wp=MBI_SSL&wreply=https%3a%2f%2foutlook.live.com%2fowa%2f%3fnlp%3d1%26signup%3d1%26RpsCsrfState%3dc37c21ae-1167-0002-6e33-01bcba34c2a7&id=292841&CBCXT=out&lw=1&fl=dob%2cflname%2cwld&cobrandid=90015&lic=1&uaid=814317ead6c24bea8e6e33eee6c5f151"

chop = webdriver.ChromeOptions()
chop.add_extension(
    "E-mail creation bot\\ChromeDriver\\Touch VPN.crx"
)
driver = webdriver.Chrome(
    "E-mail creation bot\\ChromeDriver\\.chromedriver.exe",
    options=chop,
)

# driver = webdriver.Chrome(
#    "E-mail creation bot\\ChromeDriver\\.chromedriver.exe",
#    options=Options.add_extension(
#        "E-mail creation bot\\ChromeDriver\\extension_3_8_0_0.crx"
#    ),
# )
#

driver.get(url)
driver.delete_all_cookies()

s(20)

driver.find_element_by_id("MemberName").send_keys(username)

time.sleep(0.5)

driver.find_element_by_id("iSignupAction").click()

time.sleep(2)

driver.find_element_by_id("PasswordInput").send_keys(password)

time.sleep(0.5)

driver.find_element_by_id("iSignupAction").click()

time.sleep(2)

driver.find_element_by_id("FirstName").send_keys(firstname)

time.sleep(0.5)

driver.find_element_by_id("LastName").send_keys(lastname)

time.sleep(0.5)

driver.find_element_by_id("iSignupAction").click()

time.sleep(2)

select = Select(driver.find_element_by_id("BirthDay"))
select.select_by_value("1")

time.sleep(0.5)

select = Select(driver.find_element_by_id("BirthMonth"))
select.select_by_value("1")

time.sleep(0.5)

select = Select(driver.find_element_by_id("BirthYear"))
select.select_by_value("2000")

time.sleep(0.5)

driver.find_element_by_id("iSignupAction").click()

with open(
    "E-mail creation bot\\Identifiant.txt",
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
