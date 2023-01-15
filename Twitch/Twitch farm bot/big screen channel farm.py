import cv2
import time
import numpy as np
from PIL import ImageGrab, Image
from pynput.mouse import Button, Controller
import time
import desktopmagic.screengrab_win32 as screen_grab
import winsound

n = 0
c = 0
try:
    mouse = Controller()
    points = 0

    t1 = time.time()
    while True:
        available_gift = False

        # mx = mouse.position[0]
        # my = mouse.position[1]

        # img_test = screen_grab.getRectAsImage(
        #     (mx + 100, my + 1500, mx + 100 + 200, my + 1500 + 200)
        # )
        # img_test_np = np.array(img_test)
        # frame_test = cv2.cvtColor(img_test_np, cv2.COLOR_BGR2RGB)

        # cv2.imshow("gift", frame_test)
        # print(mx + 100, my + 1500)

        img_point_gift = screen_grab.getRectAsImage((2125, 995, 2130, 1000))
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
            mouse.position = (2150, 1030)
            mouse.click(Button.left, 1)
            time.sleep(0.5)
            mouse.position = (1176, 1079)
            points += 50
            print("+50")
            c = 0

        t2 = time.time()

        if t2 - t1 > 5 * 60:
            points += 10
            print("+10")
            t1 = t2
            c += 1
            n = 0

        if c > 3 and n <= 3:
            winsound.PlaySound("SystemHand", winsound.SND_ALIAS)
            n += 1

        if n > 3:
            c = 0
            n = 0

        time.sleep(30)

        if key == ord("q"):
            cv2.destroyAllWindows()
            break
except:
    print(f"Points gained = {points}")
