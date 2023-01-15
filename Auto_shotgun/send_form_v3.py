import random
import re
import requests
import bs4
from requests_html import HTMLSession
import time
from http import HTTPStatus


# print every key and value of the dictionary
def print_dict(dict):
    for key, value in dict.items():
        print(f"{key}: {value}")


def print_data(data):
    for key, value in data.items():
        print(f"{get_key(ids_and_questions, key)} : {value}")


def get_key(dict, val):
    for key, value in dict.items():
        if val == value:
            return key

        if type(value) is list and val == value[0]:
            return key + "_sentinel"
        
        if type(value) is list and val == value[0].split("_")[0] + ".other_option_response":
            return key + ".other_option_response"

        if type(value) is list and val == value[0].split("_")[0]:
            return key

def get_full_link(formLink):
    r = requests.get(formLink)
    return r.url


def get_entries_id_and_question_dict(formLink):
    # get the page content of the formLink
    print(f"Getting the page content of {formLink}...")
    t1 = time.time()
    session = HTMLSession()
    r = session.get(formLink)
    r.html.render(sleep=.1, keep_page=True)
    print("Got the page content of the formLink in {:.2f} seconds".format(time.time() - t1))

    print("Extracting the data...")
    t1 = time.time()
    soup = bs4.BeautifulSoup(r.html.html, "html.parser")

    # get the question from the data-params value of html elements with jsmodel attribute
    entries_data_params = [entry["data-params"] for entry in soup.select("[jsmodel]") if "data-params" in entry.attrs]

    entries_id_and_question_dict = {}
    for data_params in entries_data_params:
        if len(data_params.split("[[")) > 2: # means that it is a multiple choice question
            entries_id_and_question_dict[data_params.split('"')[1]] = [None, None]

            mcq = [response.split('"')[1] for response in data_params.split("[[")[2].split("]]")[0].split("],[")]

            entries_id_and_question_dict[data_params.split('"')[1]][0] = "entry." + data_params.split("[[")[1].split(",")[0] + "_sentinel"
            entries_id_and_question_dict[data_params.split('"')[1]][1] = mcq
        else:
            entries_id_and_question_dict[data_params.split('"')[1]] = "entry." + data_params.split("[[")[1].split(",")[0]
    print("Extracted the data in {:.2f} seconds".format(time.time() - t1))
    

    return entries_id_and_question_dict


def get_data_exte(entries_id_and_question_dict, prenom, nom, facebook, mail, tel, garant, ville_etu, commentaire):
    data = {}

    for key, value in entries_id_and_question_dict.items():
        # key is the question
        # value is either the entry id or a list containing the entry id at index 0 and the mcq responses at index 1

        matched = False;
        key = key.lower().replace("é", "e").replace("è", "e")
        # use regex to get the words of the key
        key_for_test = re.findall(r"[\w']+", key)

        if key_for_test.count("nom"):
            data[value] = nom
            matched = True
        if key_for_test.count("prenom"):
            data[value] = prenom
            matched = True
        if key_for_test.count("nom") and key_for_test.count("prenom"):
            data[value] = nom + " " + prenom
            matched = True
        if key_for_test.count("facebook"):
            data[value] = facebook
            matched = True
        if key_for_test.count("mail") or key.__contains__("mail"): # because the question can be "mail", "email", "e-mail", "e mail"
            data[value] = mail
            matched = True
        if key_for_test.count("telephone"):
            data[value] = tel
            matched = True
        if key_for_test.count("garant") or key_for_test.count("exte"):
            resp = ""
            if key_for_test.count("prenom"):
                resp += garant.split(" ")[0] + " "
            if key_for_test.count("nom"):
                resp += garant.split(" ")[1] + " "
            if key_for_test.count("promo"):
                resp += garant.split(" ")[2] + " "
            
            if resp != "":
                data[value] = resp
            else:
                data[value] = garant
            matched = True
        if key_for_test.count("commentaire"):
            data[value] = commentaire
            matched = True
        if key_for_test.count("ville") and type(value) is not list:
            data[value] = ville_etu
            matched = True

        # all the folowing if are for entries with a list of choices so .split("_")[0] is used to remove "_sentinel" end data[value] = "" is required to send the form
        if key_for_test.count("promo") and type(value) is list:
            for response in value[1]:
                response_for_test = response.lower().replace("é", "e").replace("è", "e")
                if response_for_test.__contains__("autre") or response_for_test.__contains__("exte"):
                    data[value[0].split("_")[0]] = response
                    data[value[0]] = ""
                    matched = True
        if key_for_test.count("ville") and type(value) is list:
            if (ville_etu != "Dijon"):
                for response in value[1]:
                    response_for_test = response.lower().replace("é", "e").replace("è", "e")
                    if response_for_test == "":
                        data[value[0].split("_")[0] + ".other_option_response"] = ville_etu
                        data[value[0].split("_")[0]] = "__other_option__"
                        data[value[0]] = ""
                        matched = True
            else:
                for response in value[1]:
                    response_for_test = response.lower().replace("é", "e").replace("è", "e")
                    if response_for_test.__contains__("dijon"):
                        data[value[0].split("_")[0]] = response
                        data[value[0]] = ""
                        matched = True

        if key_for_test.count("breuvage") or key_for_test.count("boisson") and type(value) is list:
            for response in value[1]:
                response_for_test = response.lower().replace("é", "e").replace("è", "e")
                if response_for_test.__contains__("oh"):
                    data[value[0].split("_")[0]] = response
                    data[value[0]] = ""
                    matched = True

        # if the entry is not matched, fill it with a random value
        if not matched:
            if type(value) is list :
                data[value[0].split("_")[0]] = value[1][random.randint(0, len(value[1]) - 1)]
                data[value[0]] = ""
            else:
                data[value] = " "

    return data

def get_data(entries_id_and_question_dict, prenom, nom, facebook, mail, tel, promo, commentaire):
    data = {}

    for key, value in entries_id_and_question_dict.items():
        matched = False;
        key = key.lower().replace("é", "e").replace("è", "e")
        # use regex to get the words of the key
        key_for_test = re.findall(r"[\w']+", key)

        if key_for_test.count("nom"):
            data[value] = nom
            matched = True
        if key_for_test.count("prenom"):
            data[value] = prenom
            matched = True
        if key_for_test.count("nom") and key_for_test.count("prenom"):
            data[value] = nom + " " + prenom
            matched = True
        if key_for_test.count("facebook"):
            data[value] = facebook
            matched = True
        if key_for_test.count("mail") or key.__contains__("mail"): # because the question can be "mail", "email", "e-mail", "e mail"
            data[value] = mail
            matched = True
        if key_for_test.count("telephone"):
            data[value] = tel
            matched = True
        if key_for_test.count("garant") or key_for_test.count("exte"):
            data[value] = " "
            matched = True
        if key_for_test.count("commentaire"):
            data[value] = commentaire
            matched = True
        if key_for_test.count("ville") and type(value) is not list:
            data[value] = "Dijon"
            matched = True

        # all the folowing if are for entries with a list of choices so .split("_")[0] is used to remove "_sentinel" end data[value] = "" is required to send the form
        if key_for_test.count("promo") and type(value) is list:
            for response in value[1]:
                response_for_test = response.lower().replace("é", "e").replace("è", "e")
                if response_for_test.__contains__(promo):
                    data[value[0].split("_")[0]] = response
                    data[value[0]] = ""
                    matched = True
        if key_for_test.count("ville") and type(value) is list:
            for response in value[1]:
                response_for_test = response.lower().replace("é", "e").replace("è", "e")
                if response_for_test.__contains__("dijon"):
                    data[value[0].split("_")[0]] = response
                    data[value[0]] = ""
                    matched = True
        if key_for_test.count("breuvage") or key_for_test.count("boisson") and type(value) is list:
            for response in value[1]:
                response_for_test = response.lower().replace("é", "e").replace("è", "e")
                if response_for_test.__contains__("oh"):
                    data[value[0].split("_")[0]] = response
                    data[value[0]] = ""
                    matched = True

        # if the entry is not matched, fill it with a random value
        if not matched:
            if type(value) is list :
                data[value[0].split("_")[0]] = value[1][random.randint(0, len(value[1]) - 1)]
                data[value[0]] = ""
            else:
                data[value] = " "

    return data

def get_data1(entries_id_and_question_dict):
    return get_data_exte(entries_id_and_question_dict, "prenom", "nom", "facebook", "mail", "num_tel", "garant",  "ville_etu", "commentaire")

def get_data2(entries_id_and_question_dict):
    return get_data(entries_id_and_question_dict, "prenom", "nom", "facebook", "mail", "num_tel", "garant",  "ville_etu", "commentaire")

def send_form(formLink, data):
    # get the form response link
    splitedFormLink = formLink.split("/")
    formResponseLink = "/".join(splitedFormLink[:-1]) + "/formResponse"

    # send the form
    r = requests.post(formResponseLink, data=data)

    # check if the form is sent successfully
    if r.status_code == 200:
        return True
    else:
        print(f"!!! {r.status_code} {HTTPStatus(r.status_code).phrase}: Error sending form")
        return False

formLink = input("Enter the form link: ")
print()

succed = True
errorMessage = ""
nbOfFormToSend = 0
nbOfFormSent = 0

t0 = time.time()
if formLink.startswith("https://forms.gle"):
    print("Google form short link detected")

    print("Getting full link...")
    t1 = time.time()
    formLink = get_full_link(formLink)
    print("Got full link in {:.2f} seconds".format(time.time() - t1))


print("Getting entries infos...")
t1 = time.time()
ids_and_questions = get_entries_id_and_question_dict(formLink)
print("Got entries infos in {:.2f} seconds\n".format(time.time() - t1))


print("\n----------- Name -----------\n")
nbOfFormToSend += 1

print("Getting Name's data...")
t1 = time.time()
data = get_data2(ids_and_questions)
print("Got Name's data in {:.2f} seconds".format(time.time() - t1))

print("Sending form for Name...")
t1 = time.time()
if send_form(formLink, data):
    print("Form sent successfully in {:.2f} seconds after {:.2f}".format(time.time() - t1, t1 - t0))
    nbOfFormSent += 1
else:
    print("!!! Failed")
    succed = False
    errorMessage += "Name, "

print("------ Sent data ------")
# print_dict(data)
print_data(data)

# ------------------------------ Send form Name2 ------------------------------
print("\n----------- Name2 -----------\n")
nbOfFormToSend += 1

print("Getting Name2's data...")
t1 = time.time()
data = get_data1(ids_and_questions)
print("Got Name2's data in {:.2f} seconds".format(time.time() - t1))

print("Sending form for Name2...")
t1 = time.time()
if send_form(formLink, data):
    print("Form sent successfully in {:.2f} seconds after {:.2f}".format(time.time() - t1, t1 - t0))
    nbOfFormSent += 1
else:
    print("!!! Failed")
    succed = False
    errorMessage += "Name2, "

print("------ Sent data ------")
# print_dict(data)
print_data(data)