import cv2
import time
import numpy as np
from PIL import ImageGrab, Image
from pynput.mouse import Button, Controller
import pytesseract
import csv
import random

mouse = Controller()

black_bg = cv2.imread(
    "cv2\\Color detector\\Black.jpg"
)

def ocr(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    thresh = cv2.threshold(gray, 220, 255, cv2.THRESH_BINARY_INV)[1]
    frame = Image.fromarray(thresh)
    string = pytesseract.image_to_string(
        frame, config="-c tessedit_char_whitelist=0123456789,."
    )
    return string

fieldnames = ["x_value", "balance"]
x_value = 0
balance = 5000.00
balance_list = ["5000.00"]
cooldown = 0
profit = 0

with open(
    "Black Jack bot\\output.csv", "w"
) as csv_file:
    csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    csv_writer.writeheader()

while True:

    double_bet = random.randint(0,20)

    if cooldown > 0:
        cooldown += 1
    if cooldown > 10:
        cooldown = 0

    time.sleep(.5)

    red_underline = False
    green_underline = False
    blue_underline = False
    yes = False
    bet = False

    img_red = ImageGrab.grab(bbox=(1160, 1005, 1165, 1010))
    img_red_np = np.array(img_red)
    frame_red = cv2.cvtColor(img_red_np, cv2.COLOR_BGR2RGB)

    img_green = ImageGrab.grab(bbox=(985, 1005, 990, 1010))
    img_green_np = np.array(img_green)
    frame_green = cv2.cvtColor(img_green_np, cv2.COLOR_BGR2RGB)

    img_blue = ImageGrab.grab(bbox=(910, 1005, 915, 1010))
    img_blue_np = np.array(img_blue)
    frame_blue = cv2.cvtColor(img_blue_np, cv2.COLOR_BGR2RGB)

    img_bet = ImageGrab.grab(bbox=(1035, 955, 1040, 960))
    img_bet_np = np.array(img_bet)
    frame_bet = cv2.cvtColor(img_bet_np, cv2.COLOR_BGR2RGB)

    # img_distribuer = ImageGrab.grab(bbox=(1045, 695, 1050, 700))
    # img_distribuer_np = np.array(img_distribuer)
    # frame_distribuer = cv2.cvtColor(img_distribuer_np, cv2.COLOR_BGR2RGB)

    img_balance = ImageGrab.grab(bbox=(470, 230, 605, 290))
    img_balance_np = np.array(img_balance)

    # cv2.imshow("red", frame_red)
    # cv2.imshow("green", frame_green)
    # cv2.imshow("blue", frame_blue)
    # cv2.imshow("bet", frame_bet)
    # cv2.imshow("distribuer", frame_distribuer)
    cv2.imshow("balance", img_balance_np)
    cv2.imshow("Quit", black_bg)

    key = cv2.waitKey(1)

    for rows in frame_red:
        for pixel in rows:
            pixel = str(pixel)
            # print(pixel)
            if pixel == "[ 12  12 198]" or pixel == "[ 16  16 255]":
                red_underline = True
            else:
                pass

    for rows in frame_green:
        for pixel in rows:
            pixel = str(pixel)
            # print(pixel)
            if pixel == "[  3 182  32]" or pixel == "[  4 237  42]":
                green_underline = True
            else:
                pass

    for rows in frame_blue:
        for pixel in rows:
            pixel = str(pixel)
            # print(pixel)
            if pixel == "[182 176   3]" or pixel == "[237 229   4]":
                blue_underline = True
            elif pixel == "[  3 182  32]" or pixel == "[  4 237  42]":
                yes = True
            else:
                pass

    for rows in frame_bet:
        for pixel in rows:
            pixel = str(pixel)
            # print(pixel)
            if pixel == "[182 176   3]" or pixel == "[237 229   4]":
                bet = True
            else:
                pass

    if red_underline:
        mouse.position = (1162, 1007)
        mouse.click(Button.left, 1)
    if green_underline:
        mouse.position = (987, 1007)
        mouse.click(Button.left, 1)
    if blue_underline or yes:
        mouse.position = (912, 1007)
        mouse.click(Button.left, 1)
    if bet and cooldown == 0:
        balance = ocr(img_balance_np)

        with open("Black Jack bot\\output.csv", "a") as csv_file:
            csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            info = {"x_value": x_value, "balance": float(balance.replace(",", "."))}
            csv_writer.writerow(info)

        x_value += 1
        cooldown = 1
        
        profit = float(balance.replace(",", ".")) - 5000
        print(profit)

        if double_bet == 15:
            #click on bet *2
            mouse.position = (1037, 957)
            mouse.click(Button.left, 1)
            #rebet only 1
            mouse.position = (740, 865) 
            mouse.click(Button.left, 1)
            mouse.position = (1055, 900)
            mouse.click(Button.left, 1)
            mouse.position = (1370, 865)
            mouse.click(Button.left, 1)
            mouse.position = (1055, 950)
            time.sleep(1)
            mouse.click(Button.left, 1)
        elif profit >= 100:
            break
        else:
            mouse.position = (1037, 957)
            mouse.click(Button.left, 1)
        

    if profit >= 150:
        break

    if key == ord("q"):
        cv2.destroyAllWindows()
        break

print("done")
print(balance_list)