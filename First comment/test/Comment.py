from selenium import webdriver
import getpass
import time
import pickle


url = "https://www.youtube.com/watch?v=wjRgs9N_zUs"


def save_cookies(driver, location):
    pickle.dump(driver.get_cookies(), open(location, "wb"))


def load_cookies(driver, location):
    cookies = pickle.load(open(location, "rb"))
    driver.delete_all_cookies()
    url = "https://www.google.com"
    driver.get(url)
    for cookie in cookies:
        driver.add_cookie(cookie)


chrome = webdriver.Chrome(
    ".ChromeDriver\\.chromedriver.exe"
)
chrome.get(url)
time.sleep(2)
chrome.find_element_by_xpath("//*[@id='buttons']/ytd-button-renderer").click()
time.sleep(1)
chrome.find_element_by_xpath("//*[@id='identifierId']").send_keys("mail@hotmail.fr")
time.sleep(0.5)
chrome.find_element_by_xpath("//*[@id='identifierNext']").click()
time.sleep(0.5)
chrome.find_element_by_xpath("//*[@id='password']/div[1]/div/div[1]/input").send_keys(
    "dragon91"
)
time.sleep(0.5)
chrome.find_element_by_xpath("//*[@id='passwordNext']").click()
save_cookies(
    chrome,
    "cookies\\cookies.txt",
)
time.sleep(10)
chrome.quit()

# chrome = webdriver.Chrome(
#     ".ChromeDriver\\.chromedriver.exe"
# )
# load_cookies(
#     chrome,
#     "cookies\\cookies.txt",
# )
# chrome.get(url)
