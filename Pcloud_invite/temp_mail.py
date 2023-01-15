import time
import requests

MAILSAC_KEY = "k_tKXGAoWjjefZ4kToWwUnI7lMc289quWkFb9re"

class TempMail():
    def __init__(self) -> None:
        mail_r = requests.get("https://www.1secmail.com/api/v1/?action=genRandomMailbox&count=1")
        mail = mail_r.json()[0]

        self.mail = mail
        self.login = self.mail.split("@")[0]
        self.domain = self.mail.split("@")[1]
        
        while self.is_in_db(mail):
            mail_r = requests.get("https://www.1secmail.com/api/v1/?action=genRandomMailbox&count=1")
            mail = mail_r.json()[0]

            self.mail = mail
            self.login = self.mail.split("@")[0]
            self.domain = self.mail.split("@")[1]

        while self.has_mail():
            mail_r = requests.get("https://www.1secmail.com/api/v1/?action=genRandomMailbox&count=1")
            mail = mail_r.json()[0]

            self.mail = mail
            self.login = self.mail.split("@")[0]
            self.domain = self.mail.split("@")[1]

    def get_new_mail(self):
        mail_r = requests.get("https://www.1secmail.com/api/v1/?action=genRandomMailbox&count=1")
        mail = mail_r.json()[0]

        self.mail = mail
        self.login = self.mail.split("@")[0]
        self.domain = self.mail.split("@")[1]

        while self.is_in_db(mail):
            mail_r = requests.get("https://www.1secmail.com/api/v1/?action=genRandomMailbox&count=1")
            mail = mail_r.json()[0]

            self.mail = mail
            self.login = self.mail.split("@")[0]
            self.domain = self.mail.split("@")[1]

        while self.has_mail():
            mail_r = requests.get("https://www.1secmail.com/api/v1/?action=genRandomMailbox&count=1")
            mail = mail_r.json()[0]

            self.mail = mail
            self.login = self.mail.split("@")[0]
            self.domain = self.mail.split("@")[1]

    def get_last_message_id(self):

        boxe_r = requests.get(f"https://www.1secmail.com/api/v1/?action=getMessages&login={self.login}&domain={self.domain}") 
        boxe = boxe_r.json()
        
        t1 = time.time()
        while boxe == []:
            boxe_r = requests.get(f"https://www.1secmail.com/api/v1/?action=getMessages&login={self.login}&domain={self.domain}") 
            boxe = boxe_r.json()

            t2 = time.time()
            runningTime = t2 - t1

            if runningTime > 5*60:
                return None
        
        id = boxe[0]["id"]

        return id

    def get_message_textBody(self, id):
        message_r = requests.get(f"https://www.1secmail.com/api/v1/?action=readMessage&login={self.login}&domain={self.domain}&id={id}") 

        # print(message_r.text)
        # print("----------")

        self.textBody = message_r.json()["textBody"]

        # print(textBody)

        return self.textBody

    # Check if account exists in db "accounts.txt"
    def is_in_db(self, mail):
        with open("accounts.txt", "r") as f:
            for line in f.readlines():
                if mail in line:
                    print("!!! Account already exists in bd, trying again...")
                    return True
        return False

    # Check if the mail boxe already as a mail in it
    def has_mail(self):
        boxe_r = requests.get(f"https://www.1secmail.com/api/v1/?action=getMessages&login={self.login}&domain={self.domain}") 
        boxe = boxe_r.json()

        if boxe == []:
            return False
        else:
            print("!!! Account already has a mail in mail boxe, trying again...")
            return True

    def get_verif_url(self, textBody):
        return textBody.split("\n")[6].replace("\\", "")