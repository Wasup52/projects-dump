import cv2
import scan_mapper
import numpy as np
import os

dir_path = "Dropbox\\ENSEM\\cours"
directory = os.listdir(dir_path)

for img_name in directory:
    print(img_name)

    img_ = cv2.imread(f"{dir_path}\\{img_name}")

    scale_percent = 100
    width = int(img_.shape[1] * scale_percent / 100)
    height = int(img_.shape[0] * scale_percent / 100)
    dim = (width, height)

    img = cv2.resize(img_, dim, interpolation=cv2.INTER_AREA)
    img_2 = cv2.resize(img_, dim, interpolation=cv2.INTER_AREA)

    thresh_val = 155

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

        cv2.imshow("Scanned", dst)

    img_name_without_jpg = img_name.strip(".jpg")
    cv2.imwrite(f"Univ\\{img_name_without_jpg}_scanned.jpg", dst)

# cnt = sorted(cnt, key=cv2.contourArea, reverse=True)
# for c in cnt:
#     print(cv2.contourArea(c))
