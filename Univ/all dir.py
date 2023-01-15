import cv2
import _scan_mapper
import numpy as np
import os

dir_path = "Univ/cours"
directory = os.listdir(dir_path)
need_verif = False

def scale_down(img, scale_percent):
    width = int(img.shape[1] * scale_percent / 100)
    height = int(img.shape[0] * scale_percent / 100)
    dim = (width, height)

    return cv2.resize(img, dim, interpolation=cv2.INTER_AREA)

for img_name in directory:
    print(img_name)
    good = False

    img_ = cv2.imread(f"{dir_path}/{img_name}")

    width = int(img_.shape[1])
    height = int(img_.shape[0])
    dim = (width, height)

    img = cv2.resize(img_, dim, interpolation=cv2.INTER_AREA)
    img_2 = cv2.resize(img_, dim, interpolation=cv2.INTER_AREA)

    thresh_val = 155

    while not good:
        grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        thresh = cv2.threshold(grey, thresh_val, 255, cv2.THRESH_BINARY)[1]
        cnt = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[0]

        img_2 = cv2.resize(img_, dim, interpolation=cv2.INTER_AREA)

        cnt = sorted(cnt, key=cv2.contourArea, reverse=True)

        # the loop extracts the boundary contours of the page
        for c in cnt:
            p = cv2.arcLength(c, True)
            approx = cv2.approxPolyDP(c, 0.02 * p, True)

            if len(approx) == 4:
                target = approx
                break
        if len(approx) == 4:
            approx = _scan_mapper.mapp(target)  # find endpoints of the sheet

            pts = np.float32(
                [[0, 0], [width, 0], [width, height], [0, height]]
            )  # map to 800*800 target window

            op = cv2.getPerspectiveTransform(
                approx, pts
            )  # get the top or bird eye view effect
            scanned = cv2.warpPerspective(img, op, (width, height))

            # cv2.imshow("Scanned", scanned)

        contour = cv2.drawContours(img_2, cnt, 0, (0, 255, 0), 10)
        
        scanned_grey = cv2.cvtColor(scanned, cv2.COLOR_BGR2GRAY)
        scanned_thresh = cv2.threshold(scanned_grey, thresh_val, 255, cv2.THRESH_BINARY)[1]
        average = scanned_thresh.mean(axis=0).mean(axis=0)

        if average < 200:
            need_verif = True
        elif need_verif == False:
            good = True
        
        if need_verif:
            show_scanned = scale_down(scanned, 20)
            show_contour = scale_down(contour, 20)
            cv2.imshow("scanned", show_scanned)
            cv2.imshow("cnt", show_contour)
        
        print(thresh_val)

        key = cv2.waitKey(1)

        if key == ord("1"):
            thresh_val -= 10
        if key == ord("7"):
            thresh_val += 10

        if key == ord("q"):
            cv2.destroyAllWindows()
            need_verif = False
            good = True
            
    img_name_without_jpg = img_name.strip(".jpg")
    cv2.imwrite(f"Univ/scanned/{img_name_without_jpg}_scanned.jpg", scanned)

# cnt = sorted(cnt, key=cv2.contourArea, reverse=True)
# for c in cnt:
#     print(cv2.contourArea(c))
