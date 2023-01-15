import cv2
import time
import numpy as np
from PIL import ImageGrab, Image
from pynput.mouse import Button, Controller
import time

try:
    mouse = Controller()
    points = 0

    t1 = time.time()
    while True:
        available_gift = False

        img_point_gift = ImageGrab.grab(bbox=(1665, 1014, 1670, 1020))
        img_point_gift_np = np.array(img_point_gift)
        frame_point_gift = cv2.cvtColor(img_point_gift_np, cv2.COLOR_BGR2RGB)

        cv2.imshow("gift", frame_point_gift)

        key = cv2.waitKey(1)

        for rows in frame_point_gift:
            for pixel in rows:
                pixel = str(pixel)
                # print(pixel)
                if pixel == "[118 196   0]":
                    available_gift = True
                    break
                else:
                    pass

        if available_gift:
            mouse.position = (1667, 1016)
            mouse.click(Button.left, 1)
            time.sleep(0.5)
            mouse.position = (1919, 330)
            points += 50
            print("+50")

        t2 = time.time()

        if t2 - t1 > 5 * 60:
            points += 10
            print("+10")
            t1 = t2

        time.sleep(30)

        if key == ord("q"):
            cv2.destroyAllWindows()
            break
except:
    print(f"Points gained = {points}")
