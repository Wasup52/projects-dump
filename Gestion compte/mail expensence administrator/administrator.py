import pytesseract
import cv2
import numpy as np
from PIL import Image


def ocr(img):
    frame = Image.open(img)
    im = np.array(frame)
    gray = cv2.cvtColor(im, cv2.COLOR_RGB2GRAY)
    thresh = cv2.threshold(gray, 220, 255, cv2.THRESH_BINARY)[1]

    string = pytesseract.image_to_string(thresh)
    return string


def cuntable(img_path):
    lines = ocr(img_path)
    lines = lines.split("\n")

    expenses = []
    for line in lines:
        if line.count("+") or line.count("-"):
            expenses += [line]
        else:
            pass

    transactions = []
    for expense1 in expenses:
        expense1 = expense1.split()
        for expense in expense1:
            # print(expense)
            if expense.count(","):
                expense = expense.split(",")
                decimal = expense[1][:2]
                number = expense[0] + "." + decimal
                transactions += [float(number)]
    print(transactions, len(transactions))

    transactions_name = []
    name = ""
    for line in lines:
        print(line)
        if (
            line.count("FACT")
            or line.count("VIR")
            or line.count("*")
            or line.count("CHEQUES")
            or line.count("VIREMENT")
        ):
            if line.count("+") or line.count("-"):
                line = line.split(" ")
                for char_l in line:
                    if char_l.count("+") or char_l.count("-"):
                        n_line = line[: line.index(char_l)]
                line = ""
                for char in n_line:
                    line += char + " "
                line = line.strip(" ")
            if line.count("FACT"):
                line = line.split(" ")
                line = line[: len(line) - 2]
                for i in range(0, len(line)):
                    name += line[i] + " "
                name = name.strip(" ")
                transactions_name += [name]
                name = ""
            elif line.count("CHEQUES"):
                line = line.split(" ")
                line = line[: len(line) - 2]
                for i in range(0, len(line)):
                    name += line[i] + " "
                name = name.strip(" ")
                transactions_name += [name]
                name = ""
            else:
                transactions_name += [line]
    print(transactions_name, len(transactions_name))

    both = {}
    for i in range(0, len(transactions)):
        if transactions_name[i] in both.keys():
            both[transactions_name[i]] += transactions[i]
        else:
            both[transactions_name[i]] = transactions[i]

    total_spent = 0
    total_gained = 0
    for transaction in transactions:
        if transaction < 0:
            total_spent += abs(transaction)
        else:
            total_gained += transaction

    conclusion_str = ""
    for key in both.keys():
        conclusion_str += f"{key} : {both[key]}" + "\n"

    total_str = f"\ntotal spent : -{total_spent}\ntotal gained : {total_gained}\ntotal : {sum(transactions)}"
    final_str = conclusion_str + total_str

    return final_str


# print(
#     cuntable(
#         "Gestion compte\mail expensence administrator\\attachment_dir\Screenshot_20201112-084542.jpg"
#     )
# )
# print(
#     cuntable(
#         "Gestion compte\\mail expensence administrator\\attachment_dir\\Screenshot_20200204-232443.jpg"
#     )
# )

