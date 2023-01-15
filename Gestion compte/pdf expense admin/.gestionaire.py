import os
from extract_debits import extract_debits
from extract_pdf_text import extract_pdf_text


path = "Relevé de compte"
file_list = os.listdir(path)


def str_sum(lines):
    L = []
    for line in lines:
        line = line.replace(",", ".")
        line = line.strip("\n")
        L += [float(line)]
    return sum(L)


def get_date(file_name):
    if file_name.count("RELEVES"):
        temp = file_name.split("_")[2]
        year = temp[0:4]
        month = temp[4:6]
    else:
        year = file_name.split("_")[1].split("-")[0]
        month = file_name.split("_")[1].split("-")[1]
    return f"{month}/{year}", (month, year)


everything = []
for file in file_list:
    with open(path + "\\" + file, "rb") as f:
        text = extract_pdf_text(f)
        # print(text)

    with open("Gestion compte\\..temp data.txt", "w") as f:
        f.write(text)

    with open("Gestion compte\\..temp data.txt", "r") as f:
        debits = extract_debits(f)

    date = get_date(file)[0]
    everything += [str_sum(debits)]

    print(f"-------{date}-------")
    print(debits)
    print(str_sum(debits))
    print("---------------------")

print(everything)
print(sum(everything))
