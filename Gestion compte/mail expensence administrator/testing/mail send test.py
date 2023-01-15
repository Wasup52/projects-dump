import imaplib
import smtplib
import email
import time
import os
from mail_extract import auth, get_body, get_attachments, get_return_adress
from administrator import ocr, cuntable
from email.message import EmailMessage
user = "mail@gmail.com"
password = "SECRET"
imap_url = "imap.gmail.com"
attachment_dir = "Gestion compte\\mail expensence administrator\\attachment_dir"

return_adress = "mail@hotmail.com"

base = """
<!DOCTYPE html>

<style>
    body {
        font-family: Calibri;
        font-size: large;
        font-weight: 400;
    }

    ul {
        padding: 0;
        margin: 0;
        list-style: none;
        display: flex;
    }
</style>
"""

transactions = [
    -200.0,
    512.1,
    6.9,
    -100.0,
    -2.74,
    -10.63,
    15.1,
    -23.0,
    100.0,
    -320.0,
    120.0,
    200.0,
    -13.7,
    -7.3,
    -5.6,
    -7.37,
    8.7,
    -10.9,
    -2.0,
    -12.0,
    -9.6,
    100.0,
    -320.0,
    120.0,
    -5.6,
    -5.6,
    -10.0,
    -9.9,
    -7.55,
    8.7,
    -10.9,
    -5.6,
    -5.6,
    -3.5,
    -9.9,
    100.0,
    -320.0,
    -5.6,
    100.0,
    -100.0,
    120.0,
    150.0,
    -8.01,
    8.7,
    -10.9,
]

transactions_name = [
    "VIR SEPA M PERRET ROBIN",
    "VIR SEPA DDFIP DE LA MARNE",
    "VIR SEPA PRO BTP PRESTATIONS FR",
    "CB GROUPEMENT PARI FACT",
    "CB INTERMARCHE",
    "CB PAYPAL",
    "VIR SEPA C.P.A.M. CHAUMONT",
    "CB CBT G BONNAY",
    "VIR SEPA MR PERRET LUDOVIC OU",
    "VIR SEPA LOYER COLLOC ROBIN",
    "VIR SEPA MLLE DE PAUW AURORE",
    "VIR SEPA M PERRET ROBIN",
    "CB MC DONALD'S",
    "CB ECRANS CHAUMONT",
    "CB SNCF INTERNET",
    "CB INTERMARCHE",
    "* REMISE SERVICES BOUQUET LIBE",
    "* COTISATION BOUQUET LIBERTE",
    "CB MC DONALD'S",
    "CB DEL ARTE CHMT",
    "CB BURGER KING",
    "VIR SEPA MR PERRET LUDOVIC OU",
    "VIR SEPA LOYER COLLOC ROBIN",
    "VIR SEPA MLLE DE PAUW AURORE",
    "CB SNCF INTERNET",
    "CB SNCF INTERNET",
    "VIREMENT VERS COMPTE N26",
    "CB MC DONALD'S",
    "CB INTERMARCHE",
    "* REMISE SERVICES BOUQUET LIBE",
    "* COTISATION BOUQUET LIBERTE",
    "CB SNCF INTERNET",
    "CB SNCF INTERNET",
    "CB MC DONALD'S",
    "CB MC DONALD'S",
    "VIR SEPA MR PERRET LUDOVIC OU",
    "VIR SEPA LOYER COLLOC ROBIN",
    "CB SNCF INTERNET",
    "VIR SEPA WINAMAX",
    "CB WINAMAX FR",
    "VIR SEPA MLLE DE PAUW AURORE",
    "VIR SEPA MLLE DE PAUW AURORE",
    "CB GEANT CG804",
    "* REMISE SERVICES BOUQUET LIBE",
    "* COTISATION BOUQUET LIBERTE",
]


total_spent = 0
total_gained = 0
for transaction in transactions:
    if transaction < 0:
        total_spent += abs(transaction)
    else:
        total_gained += transaction


both = {}
for i in range(0, len(transactions)):
    if transactions_name[i] in both.keys():
        both[transactions_name[i]] += transactions[i]
    else:
        both[transactions_name[i]] = transactions[i]

conclusion_str = "<body>"
for key in both.keys():
    if both[key] < 0:
        conclusion_str += f"""{key} : <a style="color: rgb(255,0,0);font-weight: 600;">{both[key]}</a><br>"""
    elif both[key] > 0:
        conclusion_str += f"""{key} : <a style="color: rgb(0,255,0);font-weight: 600;">+{both[key]}</a><br>"""
    else:
        conclusion_str += (
            f"""{key} : <a style="font-weight: 600;">{both[key]}</a><br>"""
        )

total_str = f"""<br>total spent : -{total_spent}<br>total gained : {total_gained}<br>"""
if sum(transactions) < 0:
    total_str += f"""<a style="font-weight: 700;">TOTAL : </a><a style="color: rgb(255,0,0);font-weight: 700;">{sum(transactions)}</a><br>"""
elif sum(transactions) > 0:
    total_str += f"""<a style="font-weight: 700;">TOTAL : </a><a style="color: rgb(0,255,0);font-weight: 700;">+{sum(transactions)}</a><br>"""
else:
    total_str += f"""<a style="font-weight: 700;">TOTAL : </a><a style="font-weight: 700;">{sum(transactions)}</a><br>"""

final_html = base + conclusion_str + total_str + "</body>"

con = auth(user, password, imap_url)
print(con.select("INBOX"))

msg = EmailMessage()
msg["Subject"] = "Expenses"
msg["From"] = user
msg["To"] = return_adress
msg.add_alternative(final_html, subtype="html")

mail = smtplib.SMTP("smtp.gmail.com", 587)

mail.ehlo()  # start
mail.starttls()
mail.login(user, password)
mail.send_message(msg)
mail.close()  # stop
