from urllib.request import urlopen as uReq
from selenium import webdriver
from bs4 import BeautifulSoup
import time
import cfscrape

scraper = cfscrape.CloudflareScraper()

url = "https://twitchtracker.com/aminematue/games/32982"

soup = scraper.get(url).content

# time.sleep(3)

# soup = BeautifulSoup(driver.page_source, "html.parser")

# driver.quit()

# content = soup.findAll("tbody")

# with open("Web scraping\Get remaining stream time\data.html", "w") as f:
#     f.write(soup.prettify())

print(soup)
