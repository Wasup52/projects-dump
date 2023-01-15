import smtplib
import time


sender = "mail@hotmail.com"

with open("E-mail sending\sender.txt", "r") as f:
    line = f.readlines()[0]
    sender, password = line.split(" ")

with open("E-mail sending\e-mail list.txt", "r") as f:
    lines = f.readlines()
    for line in lines:
        name, mail = line.split(" ")
        receiver_name = name
        receiver_mail = mail

        t1 = time.time()

        subject = "Just a test"
        body = "https://www.cdiscount.com/high-tech/casques-baladeur-hifi/bose-quietcomfort-35-ii-casque-avec-micro-pleine-t/f-1065420-bos0017817770613.html?idOffre=233747188"
        msg = f"Subject: {subject}\n\n{body}"

        mail = smtplib.SMTP("smtp-mail.outlook.com", 587)

        mail.ehlo()  # start
        mail.starttls()
        mail.login(sender, password)
        mail.sendmail(sender, receiver_mail, msg)
        mail.close()  # stop

        t2 = time.time()

        print(t2 - t1)
