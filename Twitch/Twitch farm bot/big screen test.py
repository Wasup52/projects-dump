import cv2
import time
import numpy as np
from PIL import ImageGrab, Image
from pynput.mouse import Button, Controller
import time
import desktopmagic.screengrab_win32 as screen_grab
import winsound

c = 0

mouse = Controller()
points = 0

t1 = time.time()
while True:
    available_gift = False

    mx = mouse.position[0]
    my = mouse.position[1]

    img_test = screen_grab.getRectAsImage(
        (mx + 100, my + 1500, mx + 100 + 200, my + 1500 + 200)
    )
    img_test_np = np.array(img_test)
    frame_test = cv2.cvtColor(img_test_np, cv2.COLOR_BGR2RGB)

    cv2.imshow("gift", frame_test)
    print(mx + 100, my + 1500)

    key = cv2.waitKey(1)

    if key == ord("q"):
        cv2.destroyAllWindows()
        break
