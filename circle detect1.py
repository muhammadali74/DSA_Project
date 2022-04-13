import cv2 as cv
import numpy as np


def mid_point(x1, y1, x2, y2):
    x = (x1 + x2) // 2
    y = (y1 + y2) // 2

    return (x, y)


d = {}

count = 0

lower_R = np.array([68, 0, 149])
upper_R = np.array([114, 28, 222])

lower_Y = np.array([0, 193, 222])
upper_Y = np.array([0, 201, 232])

lower_B = np.array([168, 128, 0])
upper_B = np.array([246, 185, 0])

img = cv.imread('try2.png')

cap = cv.VideoCapture(1)

# blank = np.zeros(img.shape[:], dtype='uint8')
# blank2= np.zeros(img.shape[:], dtype='uint8')

while True:
    _, img = cap.read()

    blank = np.zeros(img.shape[:], dtype='uint8')
    blank2 = np.zeros(img.shape[:], dtype='uint8')

    mask_R = cv.inRange(img, lower_R, upper_R)
    mask_Y = cv.inRange(img, lower_Y, upper_Y)
    mask_B = cv.inRange(img, lower_B, upper_B)

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
        cv.circle(blank, md, 3, (0, 0, 255), -1)
        cv.circle(blank2, md, 3, (0, 0, 255), -1)

    count = 0

    for cnt in con_B:
        x, y, w, h = cv.boundingRect(cnt)

        md = mid_point(x, y, x+w, y+h)

        d[f'Blue{count}'] = md

        count += 1

        cv.circle(img, md, 3, (255, 0, 0), -1)
        cv.circle(blank, md, 3, (255, 0, 0), -1)
        cv.circle(blank2, md, 3, (255, 0, 0), -1)
    for cnt in con_Y:

        x_Y, y_Y, w_Y, h_Y = cv.boundingRect(cnt)

        md_Y = mid_point(x_Y, y_Y, x_Y+w_Y, y_Y+h_Y)

        d['ball'] = md_Y

        count += 1

        cv.circle(img, md_Y, 3, (0, 255, 255), -1)
        cv.circle(blank, md_Y, 3, (0, 255, 255), -1)
        cv.circle(blank2, md_Y, 3, (0, 255, 255), -1)

    for i in d:
        for j in d:
            if i != j:
                if i == 'ball':
                    cv.line(img, d[i], d[j], (0, 255, 255), 1)
                    cv.line(blank, d[i], d[j], (0, 255, 255), 1)
                elif 'Red' in i:
                    cv.line(img, d[i], d[j], (0, 0, 255), 1)
                    cv.line(blank, d[i], d[j], (0, 0, 255), 1)
                else:
                    cv.line(img, d[i], d[j], (255, 0, 0), 1)
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

    if countB < 11:
        print('Opponent has the ball')
    elif countR < 11:
        print('player has the ball')

    print(f'Red = {countR}, Blue = {countB}, Ball = {countY}')
    cv.waitKey(1)

    # print (d)
