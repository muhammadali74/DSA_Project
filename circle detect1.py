import cv2 as cv
import numpy as np


def mid_point(x1, y1, x2, y2):
    x = (x1 + x2) // 2
    y = (y1 + y2) // 2

    return (x, y)


d = {}

count = 0

lower_R = np.array([75, 0, 163])
upper_R = np.array([100, 0, 220])

lower_Y = np.array([30, 194, 194])
upper_Y = np.array([40, 200, 200])

lower_B = np.array([70, 70, 70])
upper_B = np.array([80, 80, 80])

# img = cv.imread('try2.png')
# img = cv.imread('tryyyy.png')
# hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
# blank = np.zeros(img.shape[:], dtype='uint8')
# blank2 = np.zeros(img.shape[:], dtype='uint8')
cap = cv.VideoCapture(0)


while True:
    _, img = cap.read()
    count = 0
    hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
    blank = np.zeros(img.shape[:], dtype='uint8')
    blank2 = np.zeros(img.shape[:], dtype='uint8')

    # mask_R = cv.inRange(img, lower_R, upper_R)
    # mask_Y = cv.inRange(img, lower_Y, upper_Y)
    # mask_B = cv.inRange(img, lower_B, upper_B)
    #Upper boundary
    cv.line(blank, (30, 34), (600, 34), (255, 255, 255), 8) #600
    cv.line(blank2, (70, 34), (1080, 34), (255, 255, 255), 8)

    #Lower boundary
    cv.line(blank, (30, 400), (600, 400), (255, 255, 255), 8)
    cv.line(blank2, (70, 630), (1080, 630), (255, 255, 255), 8)

    #upper left corner
    cv.line(blank, (30, 34), (30, 400), (255, 255, 255), 8)
    cv.line(blank2, (70, 34), (70, 245), (255, 255, 255), 8)

    #upper right corner
    cv.line(blank, (600, 34), (600, 400), (255, 255, 255), 8)
    cv.line(blank2, (1080, 34), (1080, 245), (255, 255, 255), 8)

    #lower left corner
    # cv.line(blank, (70, 430), (70, 630), (255, 255, 255), 8)
    # cv.line(blank2, (70, 430), (70, 630), (255, 255, 255), 8)

    #lower right corner
    cv.line(blank, (1080, 430), (1080, 630), (255, 255, 255), 8)
    cv.line(blank2, (1080, 430), (1080, 630), (255, 255, 255), 8)

    #left goal
    cv.line(blank, (30, 150), (30, 300), (45, 29, 240), 8)
    cv.line(blank2, (70, 245), (70, 430), (45, 29, 240), 8)

    #right goal
    cv.line(blank, (600, 150), (600, 300), (45, 29, 240), 8)
    cv.line(blank2, (1080, 245), (1080, 430), (45, 29, 240), 8)

    mask_R = cv.inRange(hsv, (161, 244, 141), (172, 255, 255))
    mask_Y = cv.inRange(hsv, (24, 177, 187), (33, 247, 217))
    mask_B = cv.inRange(hsv, (93,210,193), (101, 241, 238))

    con_R, contours_R = cv.findContours(
        mask_R, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
    con_Y, contours_Y = cv.findContours(
        mask_Y, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
    con_B, contours_B = cv.findContours(
        mask_B, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)

    # if len(con_Y) == 0:
    #     pass
    # else:
    for cnt in con_R:
        x, y, w, h = cv.boundingRect(cnt)

        md = mid_point(x, y, x+w, y+h)

        d[f'Red{count}'] = md

        count += 1

        cv.circle(img, md, 3, (0, 0, 255), -1)
        cv.circle(blank, md, 10, (0, 0, 255), -1)
        cv.circle(blank2, md, 8, (0, 0, 255), -1)

    count = 0

    for cnt in con_B:
        x, y, w, h = cv.boundingRect(cnt)

        md = mid_point(x, y, x+w, y+h)

        d[f'Blue{count}'] = md

        count += 1

        cv.circle(img, md, 3, (255, 0, 0), -1)
        cv.circle(blank, md, 10, (255, 0, 0), -1)
        cv.circle(blank2, md, 8, (255, 0, 0), -1)

    for cnt in con_Y:

        x_Y, y_Y, w_Y, h_Y = cv.boundingRect(cnt)

        md_Y = mid_point(x_Y, y_Y, x_Y+w_Y, y_Y+h_Y)

        d['ball'] = md_Y

        count += 1

        cv.circle(img, md_Y, 3, (0, 255, 255), -1)
        cv.circle(blank, md_Y, 10, (0, 255, 255), -1)
        cv.circle(blank2, md_Y, 8, (0, 255, 255), -1)

    for i in d:
        for j in d:
            if i != j:
                if i == 'ball':
                    # cv.line(img, d[i], d[j], (0, 255, 255), 1)
                    cv.line(blank, d[i], d[j], (0, 255, 255), 1)
                elif 'Red' in i:
                    # cv.line(img, d[i], d[j], (0, 0, 255), 1)
                    cv.line(blank, d[i], d[j], (0, 0, 255), 1)
                else:
                    # cv.line(img, d[i], d[j], (255, 0, 0), 1)
                    cv.line(blank, d[i], d[j], (255, 0, 0), 1)

    cv.imshow('Orig', img)
    # cv.imshow ('and', mask_R)
    cv.imshow('Graph', blank)
    cv.imshow('nodesOnly', blank2)

    countR = 0
    countB = 0
    countY = 0

    for i in d:
        if 'Red' in i:
            countR += 1
        elif 'Blue' in i:
            countB += 1
        else:
            countY += 1

    # if d['ball'][1] > 100 and d['ball'][0] == 20:
    #     print ('outside')
    # elif d['ball'][1] > 500 and d['ball'][0] == 20:
    #     print ('outside')
    # elif d['ball'][1] > 500 and d['ball'][0] == 20:
    #     print ('upper left corner')


    if countB < 11:
        print('Opponent has the ball')
    elif countR < 11:
        print('player has the ball')

    print(f'Red = {countR}, Blue = {countB}, Ball = {countY}')
    cv.waitKey(1)

    # print (d)
