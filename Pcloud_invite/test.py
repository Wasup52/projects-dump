# textBody = "You're one step away from getting complete and functional access to your pCloud account\n\nHi, welcome to your personal Cloud..\nBefore we start, we need you to verify your email address so you can take advantage of pCloud's full functionality.\n\nCLICK TO VERIFY EMAIL\nhttps:\/\/e.pcloud.com\/track?url=aHR0cHM6Ly9lLnBjbG91ZC5jb20vPyNwYWdlPXZlcmlmeW1haWwmY29kZT1QNnZ6WnJya01ycWxpWUp6NnBmeFljbXJ4NnlLVjVGQzc=&token=j7yZP6vzZ7ZkZyk2UtFlt1aV0eLJHITUbR4S1Eyok\n\nThank you for trusting pCloud with your files!\nBest wishes,\nThe pCloud team\n\nP.S. Have a question? Reply to this e-mail and get more info\n\nTo ensure delivery to your inbox, please add [team@pcloud.com] to your address book.\n2022 \u00a9 pCloud AG, 74 Zugerstrasse Str, 6340 Baar, Switzerland."

# print(textBody.split("\n")[6].replace("\\", ""))

# import temp_mail
# import string
# import random

# tempMail = temp_mail.TempMail()

# print("".join([random.choice(string.ascii_letters) for i in range(20)] + [random.choice("123456789") for i in range(5)]))

# import requests

# r = requests.get("https://httpbin.org/ip")
# print(r.json()["origin"])

from seleniumwire import webdriver

f_options = webdriver.FirefoxOptions()
f_options.add_argument("--headless")

driver = webdriver.Firefox(options = f_options)
driver.get("https://httpbin.org/ip")
print(driver.page_source.split("\n")[1].split("\"")[3])