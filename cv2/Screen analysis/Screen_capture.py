import cv2
import numpy as np
from PIL import ImageGrab


while True:
    img = ImageGrab.grab(bbox=(701, 1005, 1197, 988))
    img_np = np.array(img)
    frame = cv2.cvtColor(img_np, cv2.COLOR_BGR2GRAY)

    cv2.imshow("screen", frame)

    key = cv2.waitKey(1)

    if key == ord("q"):
        cv2.destroyAllWindows()
        break

