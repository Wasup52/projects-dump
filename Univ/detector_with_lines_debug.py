import cv2
import numpy as np
import random
import _scan_mapper
from collections import defaultdict
from numpy.lib.type_check import imag

k_param = 3
line_color = []
for k in range(k_param):
    r,g,b = random.randint(0,255),random.randint(0,255),random.randint(0,255)
    line_color.append((r,g,b))

def segment_by_angle_kmeans(lines, k=k_param, **kwargs):
    """Groups lines based on angle with k-means.

    Uses k-means on the coordinates of the angle on the unit circle 
    to segment `k` angles inside `lines`.
    """

    # Define criteria = (type, max_iter, epsilon)
    default_criteria_type = cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER
    criteria = kwargs.get('criteria', (default_criteria_type, 10, 1.0))
    flags = kwargs.get('flags', cv2.KMEANS_RANDOM_CENTERS)
    attempts = kwargs.get('attempts', 10)

    # returns angles in [0, pi] in radians
    angles = np.array([line[0][1] for line in lines])

    # multiply the angles by two and find coordinates of that angle
    pts = np.array([[np.cos(2*angle), np.sin(2*angle)] for angle in angles], dtype=np.float32)

    # run kmeans on the coords
    labels, centers = cv2.kmeans(pts, k, None, criteria, attempts, flags)[1:]
    labels = labels.reshape(-1)  # transpose to row vec

    # segment lines based on their kmeans label
    segmented = defaultdict(list)
    for i, line in enumerate(lines):
        segmented[labels[i]].append(line)
    segmented = list(segmented.values())
    return segmented


def segment_by_angle(lines):
    angles = np.array([line[0][1]*180/np.pi for line in lines])

    vert = []
    horiz = []
    other = []

    for i, line in enumerate(lines):
        angle = angles[i]
        if 85 < angle < 95:
            horiz.append(line)
        elif 0 < angle < 5 or 175 < angle < 180:
            vert.append(line)
        else:
            other.append(line)
    return (vert, horiz,other)


def intersection(line1, line2):
    """Finds the intersection of two lines given in Hesse normal form.

    Returns closest integer pixel locations.
    See https://stackoverflow.com/a/383527/5087436
    """
    rho1, theta1 = line1[0]
    rho2, theta2 = line2[0]
    A = np.array([
        [np.cos(theta1), np.sin(theta1)],
        [np.cos(theta2), np.sin(theta2)]
    ])
    b = np.array([[rho1], [rho2]])
    x0, y0 = np.linalg.solve(A, b)
    x0, y0 = int(np.round(x0)), int(np.round(y0))
    return [[x0, y0]]


def segmented_intersections(lines, img):
    """Finds the intersections between groups of lines."""

    width = img.shape[1]
    height = img.shape[0]

    up_left = []
    up_right = []
    down_left = []
    down_right = []
    middle = []

    intersections = []
    for i, group in enumerate(lines[:-1]):
        for next_group in lines[i+1:]:
            for line1 in group:
                for line2 in next_group:
                    intersections.append(intersection(line1, line2)) 
    
    for point in intersections:
        x,y = point[0]
        if height//2 - 100 < y < height//2 + 100:
            middle.append(point[0])
        elif width//2 - 100 < x < width//2 + 100:
            middle.append(point[0])
        elif y < height//2 and x < width//2:
            up_left.append(point[0])
        elif y < height//2 and x > width//2:
            up_right.append(point[0])
        elif y > height//2 and x < width//2:
            down_left.append(point[0])
        elif y > height//2 and x > width//2:
            down_right.append(point[0])

    return [up_left, up_right, down_left, down_right, middle]


def rescale(img, scale_percent):
    width = int(img.shape[1] * scale_percent / 100)
    height = int(img.shape[0] * scale_percent / 100)
    dim = (width, height)

    return cv2.resize(img, dim, interpolation=cv2.INTER_AREA)


def avg_point(points):
    try:
        sum_x = 0
        sum_y = 0
        for point in points:
            x,y = point
            sum_x += x
            sum_y += y
        avg_x = sum_x // len(points)
        avg_y = sum_y // len(points)
    except:
        avg_x, avg_y = 0,0

    return (avg_x, avg_y)


def upscale(image):
    lut_in = [0, 127, 255]
    lut_out = [0, 80, 255]

    lut_8u = np.interp(np.arange(0, 256), lut_in, lut_out).astype(np.uint8)
    image_contrasted = cv2.LUT(image, lut_8u)

    return image_contrasted

# img_ = cv2.imread("Univ/cours/20210922_152358.jpg")
# img_ = cv2.imread("Univ/20211005_152542.jpg")
# img_ = cv2.imread("Univ/cours/20211006_132807.jpg")
img_ = cv2.imread("Univ/cours/20210922_151641.jpg")


img_ = upscale(img_)

scale_percent = 20
width = int(img_.shape[1] * scale_percent / 100)
height = int(img_.shape[0] * scale_percent / 100)
dim = (width, height)

large_img = np.copy(img_)
large_img_draw = np.copy(img_)
img = rescale(img_, scale_percent)
img_2 = rescale(img_, scale_percent)
line_img = rescale(img_, scale_percent)
border_img = rescale(img_, scale_percent)

thresh_val = 125
# thresh_val = 155
verified = False

line_thresh_val = 30

thresh_1 = 285
thresh_2 = 150

# thresh_1 = 155
# thresh_2 = 280

it = 5

colors = [(0,255,0), (255,0,0), (0,0,255), (255,255,0)] #green, blue, red, cyan

while True:
    border_img = rescale(img_, scale_percent)
    img_2 = rescale(img_, scale_percent)
    line_img = rescale(img_, scale_percent)
    line_img_draw = rescale(img_, scale_percent)
    # border_img = rescale(img, scale_percent)
    line_gray = cv2.cvtColor(line_img, cv2.COLOR_BGR2GRAY)
    line_thresh_1 = cv2.threshold(line_gray, thresh_val, 255, cv2.THRESH_BINARY)[1]
    dilate = cv2.dilate(line_thresh_1, (5,5), iterations=it)
    blur_gray = cv2.GaussianBlur(line_gray,(5, 5),0)
    line_edges = cv2.Canny(dilate, thresh_1, thresh_2)

    lines_data = cv2.HoughLines(line_edges, 1, np.pi/180, line_thresh_val)

    # segmented = segment_by_angle_kmeans(lines_data)[0:2]

    # for k, categ in enumerate(segmented):
    #     color = line_color[k]
    #     for line in categ:
    #         for r,theta in line:
    #             a = np.cos(theta)
    #             b = np.sin(theta)
    #             x0 = a*r
    #             y0 = b*r
    #             x1 = int(x0 + 1000*(-b))
    #             y1 = int(y0 + 1000*(a))
    #             x2 = int(x0 - 1000*(-b))
    #             y2 = int(y0 - 1000*(a))

    #             cv2.line(line_img_draw,(x1,y1), (x2,y2), color,2)

    segmented = segment_by_angle(lines_data)[0:2]

    for k,lines in enumerate(segmented):
        for line in lines:
            r,theta = line[0]
            a = np.cos(theta)
            b = np.sin(theta)
            x0 = a*r
            y0 = b*r
            x1 = int(x0 + 1000*(-b))
            y1 = int(y0 + 1000*(a))
            x2 = int(x0 - 1000*(-b))
            y2 = int(y0 - 1000*(a))

            cv2.line(line_img_draw,(x1,y1), (x2,y2), colors[k],2)

    # for line in lines_data:
    #     for r,theta in line:
    #         a = np.cos(theta)
    #         b = np.sin(theta)
    #         x0 = a*r
    #         y0 = b*r
    #         x1 = int(x0 + 1000*(-b))
    #         y1 = int(y0 + 1000*(a))
    #         x2 = int(x0 - 1000*(-b))
    #         y2 = int(y0 - 1000*(a))

    #         cv2.line(line_img_draw,(x1,y1), (x2,y2), (0,255,0),2)
    
    up_left, up_right, down_left, down_right, middle = segmented_intersections(segmented, img_2)

    for point in up_left:
        cv2.circle(img_2, point, 1, colors[0], -1) #green
    for point in up_right:
        cv2.circle(img_2, point, 1, colors[1], -1) #blue
    for point in down_left:
        cv2.circle(img_2, point, 1, colors[2], -1) #red
    for point in down_right:
        cv2.circle(img_2, point, 1, colors[3], -1) #cyan

    avg_ul = avg_point(up_left)
    avg_ul_p = (avg_ul[0] / width, avg_ul[1] / height)
    cv2.circle(img_2, avg_ul, 5, colors[0], -1) #green

    avg_ur = avg_point(up_right)
    avg_ur_p = (avg_ur[0] / width, avg_ur[1] / height)
    cv2.circle(img_2, avg_ur, 5, colors[1], -1) #blue

    avg_dl = avg_point(down_left)
    avg_dl_p = (avg_dl[0] / width, avg_dl[1] / height)
    cv2.circle(img_2, avg_dl, 5, colors[2], -1) #red

    avg_dr = avg_point(down_right)
    avg_dr_p = (avg_dr[0] / width, avg_dr[1] / height)
    cv2.circle(img_2, avg_dr, 5, colors[3], -1) #cyan

    cv2.line(border_img, avg_ul, avg_ur, (0,255,0), 2)
    cv2.line(border_img, avg_ul, avg_dl, (0,255,0), 2)
    cv2.line(border_img, avg_dl, avg_dr, (0,255,0), 2)
    cv2.line(border_img, avg_ur, avg_dr, (0,255,0), 2)

    large_width = large_img_draw.shape[1]
    large_height = large_img_draw.shape[0]

    large_avg_ul = (int(avg_ul_p[0] * large_width), int(avg_ul_p[1] * large_height))
    cv2.circle(large_img_draw, large_avg_ul, 5, colors[0], -1) #green

    large_avg_ur = (int(avg_ur_p[0] * large_width), int(avg_ur_p[1] * large_height))
    cv2.circle(large_img_draw, large_avg_ur, 5, colors[1], -1) #blue

    large_avg_dl = (int(avg_dl_p[0] * large_width), int(avg_dl_p[1] * large_height))
    cv2.circle(large_img_draw, large_avg_dl, 5, colors[2], -1) #red

    large_avg_dr = (int(avg_dr_p[0] * large_width), int(avg_dr_p[1] * large_height))
    cv2.circle(large_img_draw, large_avg_dr, 5, colors[3], -1) #cyan

    cv2.line(large_img_draw, large_avg_ul, large_avg_ur, (0,255,0), 2)
    cv2.line(large_img_draw, large_avg_ul, large_avg_dl, (0,255,0), 2)
    cv2.line(large_img_draw, large_avg_dl, large_avg_dr, (0,255,0), 2)
    cv2.line(large_img_draw, large_avg_ur, large_avg_dr, (0,255,0), 2)

    line_thresh = cv2.inRange(large_img_draw, (0,255,0), (0,255,0))
    line_cnt = cv2.findContours(line_thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[0]
    line_cnt = sorted(line_cnt, key=cv2.contourArea, reverse=True)

    for c in line_cnt:
        p = cv2.arcLength(c, True)
        approx = cv2.approxPolyDP(c, 0.02 * p, True)

        if len(approx) == 4:
            target = approx
            break
    if len(approx) == 4:
        approx = _scan_mapper.mapp(target)  # find endpoints of the sheet

        pts = np.float32(
            [[0, 0], [large_width, 0], [large_width, large_height], [0, large_height]]
        )  # map to 800*800 target window

        op = cv2.getPerspectiveTransform(
            approx, pts
        )  # get the top or bird eye view effect
        scanned = cv2.warpPerspective(large_img, op, (large_width, large_height))

        # print(cv2.contourArea(c))
        # cv2.imshow("Scanned", scanned)

    line_contour = cv2.drawContours(img_2, line_cnt, 0, (255, 255, 0), 2)
    
    img_2_width = img_2.shape[1]
    img_2_height = img_2.shape[0]
    cv2.line(img_2, (img_2_width//2 , 0),(img_2_width//2 , img_2_height), (0,0,255),2)
    cv2.line(img_2, (0,img_2_height//2),(img_2_width,img_2_height//2), (0,0,255),2)

    cv2.imshow("linesEdges", line_edges)
    cv2.imshow("linesDetected", line_img_draw)
    cv2.imshow("linesIntersectionAvg", img_2)
    cv2.imshow("border", border_img)
    cv2.imshow("thresh", line_thresh_1)
    cv2.imshow("dilate", dilate)
    # cv2.imshow("linesCnt", line_contour)
    # cv2.imshow("linesCntEdge", line_thresh)

    key = cv2.waitKey(1)

    if key == ord("1"):
        thresh_val -= 10
    if key == ord("7"):
        thresh_val += 10

    if key == ord("2"):
        thresh_1 -= 10
    if key == ord("8"):
        thresh_1 += 10

    if key == ord("3"):
        it -= 1
    if key == ord("9"):
        it += 1

    if key == ord("q"):
        cv2.destroyAllWindows()
        break

# cv2.imwrite(f"Univ/test.jpg", scanned)

# print(intersections)
for line in segmented[2]:
    print(line, line[1]*180/np.pi)