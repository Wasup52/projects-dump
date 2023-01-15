import smtplib

# sender = "mail@hotmail.com"

def mail(sender, password, receiver_mail, subject, body):
    try:
        msg = f"Subject: {subject}\n\n{body}"

        mail = smtplib.SMTP("smtp-mail.outlook.com", 587)

        mail.ehlo()  # start
        mail.starttls()
        mail.login(sender, password)
        mail.sendmail(sender, receiver_mail, msg)
        mail.close()  # stop

        return True
    except:
        return False

