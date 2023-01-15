import cv2
import scan_mapper
import numpy as np

# directory = os.listdir("Dropbox\\ENSEM\\cours")

# for img_path in directory:
#     print(img_path)

img_ = cv2.imread("Dropbox\\ENSEM\\cours\\20210922_152358.jpg")

scale_percent = 30
width = int(img_.shape[1] * scale_percent / 100)
height = int(img_.shape[0] * scale_percent / 100)
dim = (width, height)

img = cv2.resize(img_, dim, interpolation=cv2.INTER_AREA)
img_2 = cv2.resize(img_, dim, interpolation=cv2.INTER_AREA)

thresh_val = 145

while True:
    grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    thresh = cv2.threshold(grey, thresh_val, 255, cv2.THRESH_BINARY)[1]
    cnt = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[0]

    cnt = sorted(cnt, key=cv2.contourArea, reverse=True)

    # the loop extracts the boundary contours of the page
    for c in cnt:
        p = cv2.arcLength(c, True)
        approx = cv2.approxPolyDP(c, 0.02 * p, True)

        if len(approx) == 4:
            target = approx
            break
    if len(approx) == 4:
        approx = scan_mapper.mapp(target)  # find endpoints of the sheet

        pts = np.float32(
            [[0, 0], [width, 0], [width, height], [0, height]]
        )  # map to 800*800 target window

        op = cv2.getPerspectiveTransform(
            approx, pts
        )  # get the top or bird eye view effect
        dst = cv2.warpPerspective(img, op, (width, height))

        print(cv2.contourArea(c))
        cv2.imshow("Scanned", dst)

    contour = cv2.drawContours(img_2, cnt, 0, (0, 255, 0), 2)

    cv2.imshow("thresh", thresh)
    cv2.imshow("contour", contour)

    key = cv2.waitKey(1)

    if key == ord("1"):
        thresh_val -= 10
    if key == ord("7"):
        thresh_val += 10

    if key == ord("q"):
        cv2.destroyAllWindows()
        break

for c in cnt:
    print(cv2.contourArea(c))

# cnt = sorted(cnt, key=cv2.contourArea, reverse=True)
# for c in cnt:
#     print(cv2.contourArea(c))
