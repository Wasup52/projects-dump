import cv2
import numpy as np


video_capture = cv2.VideoCapture(1)


def color_reco(color):

    while True:
        if color == "blue":
            low = np.array([100, 50, 100])
            hight = np.array([140, 255, 255])
        if color == "red":
            low = np.array([0, 100, 40])
            hight = np.array([10, 255, 255])
        if color == "green":
            low = np.array([80, 100, 100])
            hight = np.array([100, 255, 255])
        if color == "yellow":
            low = np.array([])
            hight = np.array([])

        frame = video_capture.read()[1]
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        blur = cv2.GaussianBlur(hsv, (5, 5), 2)

        # low = np.array([115, 232, 119])
        # hight = np.array([90, 100, 100])

        mask_image = cv2.inRange(hsv, low, hight)
        erode = cv2.erode(mask_image, None, iterations=5)
        dilate = cv2.dilate(erode, None, iterations=10)
        combined_image = cv2.bitwise_and(frame, frame, mask=dilate)

        cnt = cv2.findContours(dilate, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)[0]
        cv2.drawContours(frame, cnt, -1, (0, 255, 0), 2)
        cv2.drawcon
        for c in cnt:
            if cv2.contourArea(c) > 800:
                (x, y, w, h) = cv2.boundingRect(c)
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(
            frame, f"color detected:{color}", (10, 20), font, 0.5, (0, 0, 255), 1
        )
        cv2.imshow("original", frame)
        cv2.imshow("mask", hsv)
        cv2.imshow("combined", combined_image)

        key = cv2.waitKey(1)

        if key == ord("b"):
            color = "blue"
        if key == ord("r"):
            color = "red"
        if key == ord("y"):
            color = "yellow"
        if key == ord("g"):
            color = "green"

        if key == ord("q"):
            video_capture.release()
            cv2.destroyAllWindows()
            break


color_reco("blue")
