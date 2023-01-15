import imaplib
import email
import os


user = "mail@gmail.com"
password = "SECRET"
imap_url = "imap.gmail.com"
attachment_dir = "Gestion compte\\mail expensence administrator\\attachment_dir"


def auth(user, password, imap_url):
    con = imaplib.IMAP4_SSL(imap_url)
    con.login(user, password)
    return con


def get_body(msg):
    if msg.is_multipart():
        return get_body(msg.get_payload(0))
    else:
        body = str(msg.get_payload(None, True))
        body = body.replace("\\", "'")
        body = body.split("'")[1]
        return body.lower()


def get_attachments(msg):
    for part in msg.walk():
        if part.get_content_maintype() == "multipart":
            continue
        if part.get("Content-Disposition") is None:
            continue
        fileName = part.get_filename()

        if bool(fileName):
            filePath = os.path.join(attachment_dir, fileName)
            with open(filePath, "wb") as f:
                f.write(part.get_payload(decode=True))


def get_return_adress(msg):
    for part in msg.walk():
        if part.get_all("Return-Path") is None:
            pass
        else:
            return_adress = part.get_all("Return-Path")[0]
            return_adress = return_adress.strip("<>")
            return return_adress


# con = auth(user, password, imap_url)
# print(con.select("INBOX"))

# result, data = con.fetch(b"23", "(RFC822)")
# raw = email.message_from_bytes(data[0][1])
# # print(get_body(raw))
# get_attachments(raw)
