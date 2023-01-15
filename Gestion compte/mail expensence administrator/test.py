import imaplib
import smtplib
import email
import time
import os
from mail_extract import auth, get_body, get_attachments, get_return_adress
from email.message import EmailMessage

user = "mail@gmail.com"
password = "SECRET"
imap_url = "imap.gmail.com"
attachment_dir = "Gestion compte\\mail expensence administrator\\attachment_dir"

return_adress = "mail@hotmail.com"

con = auth(user, password, imap_url)
print(con.select("INBOX"))

expenses = """
<!DOCTYPE html>
<html lang="en-US">

<body>
    <img src="https://quickchart.io/chart/render/zf-aad84b22-a302-49a6-b5ff-30b56fa70277">
</body>

</html>
"""

# ---- write an send mail ----
msg = EmailMessage()
msg["Subject"] = "Expenses"
msg["From"] = user
msg["To"] = return_adress
msg.add_alternative(expenses, subtype="html")

mail = smtplib.SMTP("smtp.gmail.com", 587)

mail.ehlo()  # start
mail.starttls()
mail.login(user, password)
mail.send_message(msg)
mail.close()  # stop
# ----------------------------

print("done")
