import requests
import bs4
from requests_html import HTMLSession
from websockets import client
import time


def print_dict(dict):
    for key, value in dict.items():
        print(f"{key}: {value}")

def get_full_link(formLink):
    r = requests.get(formLink)
    return r.url

def get_entries_id(formLink):
    # get the page content of the formLink
    session = HTMLSession()
    r = session.get(formLink)
    r.html.render(sleep=.5, keep_page=True)

    soup = bs4.BeautifulSoup(r.html.html, "html.parser")

    # get the html element with name start with "entry"
    entries = soup.select("[name^=entry]")
    # get the id of the html element
    entries_id = [entry["name"] for entry in entries]

    return entries_id

def get_entries_dict(entries_id):
    entries = {}

    if (len(entries_id) == 10):
        entries["nom"] = entries_id[0]
        entries["prenom"] = entries_id[1]
        entries["nom_facebook"] = entries_id[2]
        entries["adresse_mail"] = entries_id[3]
        entries["num_tel"] = entries_id[4]
        entries["referant"] = entries_id[5]
        entries["commentaire"] = entries_id[6]
        entries["promo"] = entries_id[7].split("_")[0]
        entries["ville_etude"] = entries_id[8].split("_")[0]
        entries["breuvage"] = entries_id[9].split("_")[0]
    elif (len(entries_id) == 8):
        entries["nom"] = entries_id[0]
        entries["prenom"] = entries_id[1]
        entries["adresse_mail"] = entries_id[2]
        entries["num_tel"] = entries_id[3]
        entries["referant"] = entries_id[4]
        entries["promo"] = entries_id[5].split("_")[0]
        entries["ville_etude"] = entries_id[6].split("_")[0]
        entries["breuvage"] = entries_id[7].split("_")[0]
    else:
        print("!!! Error: number of entries is not 8 or 10")
        exit() # exit the program if the number of entries is not 8 or 10 (because the program is not made to handle this case)

    return entries

def get_data(entries):
    data = {}

    if (len(entries) == 10):
        data[entries["nom"]] = "Robin"
        data[entries["prenom"]] = "PERRET"
        data[entries["nom_facebook"]] = "Robin PERRET"
        data[entries["adresse_mail"]] = "perret.robin@hotmail.com"
        data[entries["num_tel"]] = "0664685406"
        data[entries["referant"]] = "Jean Estran"
        data[entries["commentaire"]] = "Super OB"
        data[entries["promo"]] = "autre / exte (une question supplémentaire après)"
        data[entries["ville_etude"] + ".other_option_response"] = "Nancy"
        data[entries["ville_etude"]] = "__other_option__"
        data[entries["breuvage"]] = "OH"
        data[entries["promo"] + "_sentinel"] = ''
        data[entries["ville_etude"] + "_sentinel"] = ''
        data[entries["breuvage"] + "_sentinel"] = ''
    elif (len(entries) == 8):
        data[entries["nom"]] = "Robin"
        data[entries["prenom"]] = "PERRET"
        data[entries["adresse_mail"]] = "perret.robin@hotmail.com"
        data[entries["num_tel"]] = "0664685406"
        data[entries["referant"]] = "Jean Estran"
        data[entries["promo"]] = "autre / exte (une question supplémentaire après)"
        data[entries["ville_etude"] + ".other_option_response"] = "Nancy"
        data[entries["ville_etude"]] = "__other_option__"
        data[entries["breuvage"]] = "OH"
        data[entries["promo"] + "_sentinel"] = ''
        data[entries["ville_etude"] + "_sentinel"] = ''
        data[entries["breuvage"] + "_sentinel"] = ''

    # data["ffv"] = 1
    # data["partialResponse"] = "[null,null,'6517647741696831976']"
    # data["pageHistory"] = 0
    # data["fbzx"] = 6517647741696831976

    return data


def send_form(formLink, data):
    # get the form response link
    splitedFormLink = formLink.split("/")
    formResponseLink = "/".join(splitedFormLink[:-1]) + "/formResponse"

    # create a dictionary of the form data to be sent
    # data = {}
    # for entry_id in entries_id:
    #     data[entry_id] = "test"

    # send the form
    r = requests.post(formResponseLink, data=data)

    # check if the form is sent successfully
    if r.status_code == 200:
        print("Form sent successfully")
        return True
    else:
        print(f"!!! {r.status_code}: Error sending form")
        return False

formLink = input("Enter the form link: ")
print()

t0 = time.time()
if formLink.startswith("https://forms.gle"):
    print("Google form short link detected")

    print("Getting full link...")
    t1 = time.time()
    formLink = get_full_link(formLink)
    print("Got full link in {:.2f} seconds".format(time.time() - t1))

print("Getting entries id...")
t1 = time.time()
entries_id = get_entries_id(formLink)
print("Got entries id in {:.2f} seconds".format(time.time() - t1))

print("-------------")
for entry_id in entries_id:
    print(entry_id)
print("-------------")

print("Getting entries dict...")
t1 = time.time()
entries = get_entries_dict(entries_id)
print("Got entries dict in {:.2f} seconds".format(time.time() - t1))

print("-------------")
print_dict(entries)
print("-------------")

print("Getting data...")
t1 = time.time()
data = get_data(entries)
print("Got data in {:.2f} seconds".format(time.time() - t1))

print("-------------")
print_dict(data)
print("-------------")

exit()

print("Sending form...")
t1 = time.time()
if send_form(formLink, data):
    print("Form sent in {:.2f} seconds".format(time.time() - t1))
else:
    pass

print("\nFinished in {:.2f} seconds".format(time.time() - t0))

