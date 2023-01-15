import cv2
import numpy as np

# cam = cv2.VideoCapture(
#     "cv2\\Video test\\vtest.avi"
# )
cam = cv2.VideoCapture(1)

while cam.isOpened():
    frame = cam.read()[1]
    out = frame

    print(frame)

    for x in range(1, len(frame) + 1):
        for y in range(1, len(x) + 1):
            V = []
            s = 0
            for x_ in range(x - 1,x + 2):
                for y_ in range(y - 1,y + 2):
                    if x_ == x and y_ == y:
                        pass
                    else:
                        V += frame[x][y]
            
            for v in V:
                s += 

            if 
            out[x][y] =

    cv2.imshow("video", frame1)

    frame1 = frame2
    frame2 = cam.read()

    key = cv2.waitKey(1)

    if key == ord("q"):
        cam.release()
        cv2.destroyAllWindows()

def diff(rgb1, rgb2):
    return rgb1[0]