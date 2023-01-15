from seleniumwire import webdriver
from stem import Signal
from stem.control import Controller
from tkinter import messagebox
import time
import temp_mail
import string
import random

def renew_connection():
    with Controller.from_port(port = 9051) as controller:
        controller.authenticate(password="16:872860B76453A77D60CA2BB8C1A7042072093276A3D701AD684053EC4C")
        controller.signal(Signal.NEWNYM)

def get_tor_driver(f_options=""):
    w_options = {
    'proxy': {
            'http':  'socks5://127.0.0.1:9050',
            'https': 'socks5://127.0.0.1:9050'
        }
    }
    if f_options != "":
        return webdriver.Firefox(seleniumwire_options = w_options, options = f_options)
    else:
        return webdriver.Firefox(seleniumwire_options = w_options)

def countdown(t):
    while t:
        mins, secs = divmod(t, 60)
        hours, mins = divmod(mins, 60)
        timer = '{:02d}:{:02d}:{:02d}'.format(hours, mins, secs)
        print(timer, " remaining", end="\r")
        time.sleep(1)
        t -= 1

invite_link = "https://e.pcloud.com/#page=register&invite=i8U5ZoybSK7"

tempMail = temp_mail.TempMail()

mail = tempMail.mail
password = "".join([random.choice(string.ascii_letters) for i in range(20)] + [random.choice("123456789") for i in range(5)])

f_options = webdriver.FirefoxOptions()
f_options.add_argument("--headless")

NUMBER_OF_ACCOUNTS = 13

MIN_TIME = 10*60 # 10 min in seconds
MAX_TIME = 45*60 # 45 min in seconds

WAIT = True

for k in range(NUMBER_OF_ACCOUNTS):
    try:
        if WAIT:
            wait_time = random.randint(MIN_TIME, MAX_TIME)
            mins, secs = divmod(wait_time, 60)
            hours, mins = divmod(mins, 60)
            print("Waiting for {:02d}:{:02d}:{:02d}...".format(hours, mins, secs))

            countdown(wait_time)

        try:
            print(f"Starting driver n°{k+1}...")
            driver = get_tor_driver(f_options)
        except:
            renew_connection()
            print("!!! Failed to start driver, trying with renewed connection...")
            driver = get_tor_driver(f_options)

        print("Getting ip of driver...")
        driver.get("https://httpbin.org/ip")
        ip = driver.page_source.split("\n")[1].split("\"")[3]

        print(f"Driver has ip : {ip}")

        print("Getting to sign up url...")
        driver.get(invite_link)

        time.sleep(5)

        print("Sending email...")
        driver.find_element_by_name("email").send_keys(mail)

        time.sleep(1)

        print("Sending password...")
        driver.find_element_by_name("password").send_keys(password)

        time.sleep(1)

        print("Checking terms...")
        driver.find_element_by_name("terms").click()

        time.sleep(1)

        print("Submiting...")
        driver.find_element_by_xpath("//button[@class='butt submitbut']").click()

        id = tempMail.get_last_message_id()

        if id != -1:
            print(f"Message with id : {id} received")
            messageTextBody = tempMail.get_message_textBody(id)
            verifUrl = tempMail.get_verif_url(messageTextBody)
            print(f"Verification url : {verifUrl}")

            print("Getting to verification url...")
            try:
                driver.get(verifUrl)
            except:
                print("!!! Failed")
                print(tempMail.textBody)
        else:
            print("!!! Failed to get message id")

        print("Adding account to database...")
        with open("accounts.txt", "a") as f:
            if id != -1:
                f.write(f"{mail}:{password}\tip:{ip}\n")
            else:
                f.write(f"{mail}:{password}\tip:{ip}\t!!! Failed\n")

        time.sleep(5)

        print("Clossing driver...")
        driver.close()
        driver.quit()

        renew_connection()
        tempMail.get_new_mail()

        mail = tempMail.mail
        password = "".join([random.choice(string.ascii_letters) for i in range(20)] + [random.choice("123456789") for i in range(5)])

        print("--- Connection renewed ---")
    except Exception as e:
        messagebox.showerror("Error", f"Error occured on itteration number {k+1}: \n{e.args[1]}")
        break
