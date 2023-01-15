from selenium import webdriver
from bs4 import BeautifulSoup
import time
from send_mail import mail

"""
https://xwtk.cloud/Checkout/payman.php?redirect_when_succeeded=https%3A%2F%2Fzelien.me%2Fcheckout.php%3Fsuccess%3Fproduct%3D4.5%26orderid%3D109642&redirect_when_failed=https%3A%2F%2Fzelien.me%2Fcancelled.php%3Fcheckoutidentifier%3D109642&successful_order_code_page=https%3A%2F%2Fzelien.me%2Fpaypalnotifier.php&currency=USD&default_price=42&quantity=1&paypal_email=419068697@qq.com&checkout_identifier=109642&product_name=Zeware Pro Order 211202083443
https://www.paypal.com/webapps/hermes?token=88E9979132736450K&useraction=commit&rm=1&mfid=1638463143350_af3771d96a103
""" 

vpn_path = "/root/.mozilla/firefox/w3msmnsu.default-esr/extensions/touch-vpn@anchorfree.com.xpi"
vpn_name = "touch-vpn"

# url = "https://zelien.me/tracking.php?id=211202083443"
url = "https://kasen.digital/tracking.php?id=220308055736"

option = webdriver.FirefoxOptions()
option.add_argument("--headless")
driver = webdriver.Firefox(options=option)

# ---- Use vpn ----
# driver.install_addon(vpn_path, temporary=False)

# print("getting extension id")
# driver.get("about:memory")

# driver.find_element_by_id("measureButton").click()

# soup = BeautifulSoup(driver.page_source, "html.parser")
# extensions_id = soup.findAll("span", {"class" : "mrName", "title" : "WebExtensions that are active in this session"})

# for ext_id_str in extensions_id:
#     if ext_id_str.text.count(vpn_name):
#         ext_id = ext_id_str.text.split(",")[2].split("/")[2]
        
# extension_pop_up_url = f"moz-extension://{ext_id}/panel/index.html"

# driver.get(extension_pop_up_url)
# print("going to extension page")

# time.sleep(1)

# driver.find_element_by_xpath("//*[@class='button button--red data-consent__accept-button']").click()

# time.sleep(1)

# driver.find_element_by_id("ConnectionButton").click()
# print("starting vpn")

# time.sleep(5)
# -----------------

print("going to tracking page")
try:
    driver.get(url)
except:
    print("error")
    driver.quit()

soup = BeautifulSoup(driver.page_source, "html.parser")
status_h4 = soup.findAll("h4", {"class" : "mbr-text mbr-fonts-style display-7 text-white"})
status = str(status_h4[1]).split("<br/>")[1].split("<")[0]

print(status)

print("quit")
driver.quit()

# sender = "mail@hotmail.com"
# pswd = "Dragon91"
# receiver = "perret.robin@hotmail.com"
# mail(sender, pswd, receiver, f"Pods Order Status is {status}", "")