import cv2
import sys


lunched = True
cam = cv2.VideoCapture()

frame = cam.read()[1]

cv2.imshow("video", frame)

if cv2.waitKey(1) == ord("q"):
    sys.exit()

input("done")
