import os
import cv2

def sort_box(boxes):
    def x_(boxe):
        return boxe[0]
    def y_(boxe):
        return boxe[1]

    boxes_col_1 = sorted(boxes, key=x_)[0:2]
    boxes_col_2 = sorted(boxes, key=x_)[2:4]

    boxes_col_1_sort = sorted(boxes_col_1, key=y_)[0:2]
    boxes_col_2_sort = sorted(boxes_col_2, key=y_)[0:2]

    return [boxes_col_1_sort[0], boxes_col_2_sort[0], boxes_col_1_sort[1], boxes_col_2_sort[1]]

dir_path = "get_diapo/ilovepdf_pages-to-jpg-compta/"
img_names = sorted(os.listdir(dir_path))

k = 0
for img_name in img_names:
    img_path = dir_path + img_name
    img = cv2.imread(img_path)

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    thresh = cv2.threshold(gray, 50, 255, cv2.THRESH_BINARY_INV)[1]
    cnts = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[0]
    cnts_img = img.copy()
    cv2.drawContours(cnts_img, cnts, -1, (0, 255, 0), 3)

    cv2.imshow("gray", gray)
    cv2.imshow("thresh", thresh)
    cv2.imshow("cnts", cnts_img)
    keys = cv2.waitKey(0)

    if keys == ord("q"):
        break
    elif keys == ord("n"):
        pass
    else:
        pass

    imgs_box = []
    for cnt in cnts:
        x,y,width,height = cv2.boundingRect(cnt)
        if width > 300 and height > 300:
            imgs_box.append((x,y,width,height))

    imgs_box = sort_box(imgs_box)

    imgs = []
    for x, y, rect_width, rect_height in imgs_box:
        imgs.append(img[y:y+rect_height, x:x+rect_width])

    for img_ in imgs:
        cv2.imwrite(f"get_diapo/diapos-compta/{k}.jpg", img_)
        print(k)
        k += 1