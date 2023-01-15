from pynput.mouse import Button, Controller
from pynput.keyboard import Key, Controller as Keyboard
import time
import numpy as np
from PIL import ImageGrab, Image
import cv2
import pytesseract

mouse = Controller()
keyboard = Keyboard()
t = time.sleep


def ocr(img):
    frame = Image.fromarray(img)
    string = pytesseract.image_to_string(
        frame, config="-c tessedit_char_whitelist=0123456789,."
    )
    return string


while True:
    nb_people = ImageGrab.grab(bbox=(1660, 1015, 1685, 1035))
    nb_people_np = np.array(nb_people)
    gray = cv2.cvtColor(nb_people_np, cv2.COLOR_BGR2GRAY)
    resized = cv2.resize(gray, (nb_people.size[0] * 5, nb_people.size[1] * 5))
    blur = cv2.medianBlur(resized, 5)
    thresh = cv2.threshold(blur, 160, 255, cv2.THRESH_BINARY_INV)[1]

    cv2.imshow("nb", thresh)
    key = cv2.waitKey(1)

    if key == ord("q"):
        cv2.destroyAllWindows()
        break

    nb_people_str = ocr(thresh)
    people = int(nb_people_str)
    # print(people)

    if people <= 12:
        mouse.position = (1890, 1010)
        t(0.5)
        mouse.click(Button.left, 1)
        t(2)
        mouse.position = (897, 1008)
        t(0.5)
        mouse.click(Button.left, 1)
        t(0.5)
        mouse.position = (1002, 801)
        t(0.5)
        mouse.click(Button.left, 1)
        t(0.5)
        mouse.position = (1106, 766)
        t(0.5)
        mouse.click(Button.left, 1)

        print("moved")

        break
