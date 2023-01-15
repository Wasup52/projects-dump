import imaplib
import smtplib
import email
import time
import os
from mail_extract import auth, get_body, get_attachments, get_return_adress
from administrator import ocr, cuntable
from relaunch import relaunch


user = "mail@gmail.com"
password = "SECRET"
imap_url = "imap.gmail.com"
attachment_dir = "attachment_dir"

con = auth(user, password, imap_url)

while True:
    try:
        num_of_mail_1 = con.select("INBOX")[1][0]
        time.sleep(60)
        num_of_mail_2 = con.select("INBOX")[1][0]
        if num_of_mail_2 != num_of_mail_1:
            _, data = con.fetch(num_of_mail_2, "(RFC822)")
            raw = email.message_from_bytes(data[0][1])
            return_adress = get_return_adress(raw)

            if get_body(raw) == "break":
                break

            get_attachments(raw)
            if len(os.listdir(attachment_dir)) != 0:

                attachment = os.listdir(attachment_dir)[0]
                attachment_path = attachment_dir + "/" + attachment
                expenses = cuntable(attachment_path)
                return_adress = get_return_adress(raw)

                # ---- write an send mail ----
                subject = "Expenses"
                body = expenses
                msg = f"Subject: {subject}\n\n{body}"

                mail = smtplib.SMTP("smtp.gmail.com", 587)

                mail.ehlo()  # start
                mail.starttls()
                mail.login(user, password)
                mail.sendmail(user, return_adress, msg)
                mail.close()  # stop
                # ----------------------------

                os.remove(attachment_path)
    except:
        print("anking relaunched")
        relaunch()

# ---- write an send mail ----
subject = "Consol response"
body = "Script stoped successfully"
msg = f"Subject: {subject}\n\n{body}"

mail = smtplib.SMTP("smtp.gmail.com", 587)

mail.ehlo()  # start
mail.starttls()
mail.login(user, password)
mail.sendmail(user, return_adress, msg)
mail.close()  # stop
# ----------------------------
