from PIL import Image, ImageGrab
import numpy as np
import pytesseract
import cv2
import time


def ocr(img):
    gray = cv2.cvtColor(im_in, cv2.COLOR_BGR2GRAY)
    thresh = cv2.threshold(gray, 220, 255, cv2.THRESH_BINARY_INV)[1]
    frame = Image.fromarray(thresh)
    string = pytesseract.image_to_string(
        frame, config="-c tessedit_char_whitelist=0123456789,."
    )
    return string


while True:

    img_balance = ImageGrab.grab(bbox=(470, 230, 605, 290))
    im_in = np.array(img_balance)
    # gray = cv2.cvtColor(im_in, cv2.COLOR_BGR2GRAY)
    # blured = cv2.medianBlur(gray, 3)
    # thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
    # kernel = np.ones((3, 3), np.uint8)
    # dilate = cv2.dilate(thresh, kernel, iterations=1)
    # erode = cv2.erode(dilate, kernel, iterations=1)

    # Threshold.
    # Set values equal to or above 220 to 0.
    # Set values below 220 to 255.

    # th, im_th = cv2.threshold(gray, 220, 255, cv2.THRESH_BINARY_INV)

    # cv2.imshow("Thresholded Image", im_th)
    black_bg = cv2.imread(
        "cv2\\Color detector\\Black.jpg"
    )

    balance = ocr(im_in)

    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(
        black_bg, f"balance = {balance}", (10, 100), font, 0.5, (255, 255, 255), 2
    )

    cv2.imshow("Info", black_bg)

    key = cv2.waitKey(1)

    if key == ord("q"):
        cv2.destroyAllWindows()
        break

print("done")
