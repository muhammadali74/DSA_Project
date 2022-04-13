import cv2 as cv
import numpy as np

def mid_point (x1, y1, x2, y2):
    x = (x1 + x2) // 2
    y = (y1 + y2) // 2

    return (x, y)

d = {}

count = 0

lower_R = np.array ([68, 0, 149])
upper_R = np.array ([114, 28, 222])

lower_Y = np.array ([20, 80, 100])
upper_Y = np.array ([40, 120, 150])

lower_B = np.array ([210, 170, 70])
upper_B = np.array ([255, 200, 95])

img = cv.imread ('try2.png')
while True:
    mask_R = cv.inRange (img, lower_R, upper_R)
    mask_Y = cv.inRange (img, lower_Y, upper_Y)
    mask_B = cv.inRange (img, lower_B, upper_B)

    con_R, contours_R = cv.findContours(mask_R, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
    con_Y, contours_Y = cv.findContours(mask_Y, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
    con_B, contours_B = cv.findContours(mask_B, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)

    # if len(con_Y) == 0:
    #     pass
    # else:
    for cnt in con_R:
        x, y, w, h = cv.boundingRect(cnt)

        md = mid_point(x, y, x+w, y+h)

        d[f'Red{count}'] = md

        count += 1

        cv.circle(img, md, 3, (0, 0, 255), -1)
        # cv.circle(blank, md, 8, (0, 0, 255), -1)

    count = 0

    for cnt in con_B:
        x, y, w, h = cv.boundingRect(cnt)

        md = mid_point(x, y, x+w, y+h)

        d[f'Blue{count}'] = md

        count += 1

        # cv.circle(img, md, 3, (255, 0, 0), -1)
        # cv.circle(blank, md, 8, (255, 0, 0), -1)


    # x_Y, y_Y, w_Y, h_Y = cv.boundingRect(con_Y[0])

    # md_Y = mid_point(x_Y, y_Y, x_Y+w_Y, y_Y+h_Y)

    # d['ball'] = md_Y

    # count += 1

    # cv.circle(img, md, 8, (0, 255, 255), -1)
    # cv.circle(blank, md, 8, (0, 255, 255), -1)

    # for i in d:
    #     for j in d:
    #         if i != j:
                # if i == 'ball' or j == 'ball':
                #     cv.line(img, d[i], d[j], (0, 255, 255), 1)
                #     # cv.line(blank, d[i], d[j], (0, 255, 255), 1)
                # elif 'Red' in i or 'Red' in j:
                    # cv.line(img, d[i], d[j], (0, 0, 255), 1)
                    # cv.line(blank, d[i], d[j], (0, 0, 255), 1)
                # else:
                #     cv.line(img, d[i], d[j], (255, 0, 0), 1)
                    # cv.line(blank, d[i], d[j], (255, 0, 0), 1)

    cv.imshow ('jehe', img)
    cv.imshow ('and', mask_R)

    cv.waitKey(1)
    # print (d)