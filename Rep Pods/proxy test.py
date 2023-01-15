# from selenium import webdriver
import time
import seleniumwire
from send_mail import mail
from bs4 import BeautifulSoup
from selenium.webdriver.common.proxy import Proxy, ProxyType
from seleniumwire import webdriver

with open("Rep Pods/.Proxys.txt", "r") as f:
    lines = f.readlines()


for line in lines:
    PROXY_HOST = line.split("\t")[0].strip(" ")
    PROXY_PORT = line.split("\t")[1].strip(" ")
    # print(f"{PROXY_HOST}, {PROXY_PORT}")

    username = "kphcrcwz"
    pswd = "a7u18c3pogne"

    url = "https://zelien.me/tracking.php?id=211202083443"

    w_options = {
    'proxy': {
            'http': f'socks5://{username}:{pswd}@{PROXY_HOST}:{PROXY_PORT}',
            'https': f'socks5://{username}:{pswd}@{PROXY_HOST}:{PROXY_PORT}',
            'no_proxy': 'localhost,127.0.0.1'
        }
    }
    f_options = webdriver.FirefoxOptions()
    f_options.add_argument("--headless")
    driver = webdriver.Firefox(seleniumwire_options=w_options, options=f_options)

    driver.get(url)

    soup = BeautifulSoup(driver.page_source, "html.parser")
    title = soup.findAll("title")[0].text
    print(f"{title}, {PROXY_HOST}, {PROXY_PORT}")

    driver.quit()