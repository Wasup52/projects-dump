import time
import cv2

s = time.sleep

while 1:
    w = cv2.VideoCapture(0)
    w.read()
    s(0.1)
    w.release()
