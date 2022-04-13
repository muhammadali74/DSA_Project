import cv2 as cv
import numpy as np

def mid_point (x1, y1, x2, y2):
    x = (x1 + x2) // 2
    y = (y1 + y2) // 2

    return (x, y)

def dist (x1, y1, x2, y2):
    a = (x1 + x2) ** 2
    b = (y1 + y2) ** 2

    d = (a + b) ** (1/2)

    return d

cap = cv.VideoCapture(0)

lower_R = np.array ([0, 0, 130])
upper_R = np.array ([80, 80, 255])

lower_Y = np.array ([20, 80, 100])
upper_Y = np.array ([40, 120, 150])

lower_B = np.array ([210, 170, 70])
upper_B = np.array ([255, 200, 95])

while True:
    count = 0
    d = {}

    _, frame = cap.read()

    blank = np.zeros(frame.shape[:2], dtype='uint8')

    # frame = frame[]

    # img = cv.imread('try1.jpg')

    # grayframe = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    # _, thrsh = cv.threshold(grayframe, 240, 255, cv.THRESH_BINARY)

    # con, contours = cv.findContours(thrsh, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)

    # for cnt in con:
    #     x, y, w, h = cv.boundingRect(cnt)

    #     md = mid_point(x, y, x+w, y+h)

    #     d[count] = md

    #     count += 1

    #     cv.circle(frame, md, 8, 255, -1)
    #     cv.circle(blank, md, 8, 255, -1)

    # for i in d:
    #     for j in d:
    #         if i != j:
    #             cv.line(frame, d[i], d[j], (255, 100, 0), 1)
    #             cv.line(blank, d[i], d[j], (255, 100, 200), 1)

    # cv.imshow ('frame', thrsh)
    # cv.imshow ('fameee', frame)
    # cv.imshow ('khalo', blank)
    # img = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
    mask_R = cv.inRange (frame, lower_R, upper_R)
    mask_Y = cv.inRange (frame, lower_Y, upper_Y)
    mask_B = cv.inRange (frame, lower_B, upper_B)

    con_R, contours_R = cv.findContours(mask_R, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
    con_Y, contours_Y = cv.findContours(mask_Y, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
    con_B, contours_B = cv.findContours(mask_B, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)

    if len(con_Y) == 0:
        pass
    else:

        for cnt in con_R:
            x, y, w, h = cv.boundingRect(cnt)

            md = mid_point(x, y, x+w, y+h)

            d[f'Red{count}'] = md

            count += 1

            cv.circle(frame, md, 8, (0, 0, 255), -1)
            cv.circle(blank, md, 8, (0, 0, 255), -1)

        count = 0

        for cnt in con_B:
            x, y, w, h = cv.boundingRect(cnt)

            md = mid_point(x, y, x+w, y+h)

            d[f'Blue{count}'] = md

            count += 1

            cv.circle(frame, md, 8, (255, 0, 0), -1)
            cv.circle(blank, md, 8, (255, 0, 0), -1)


        x_Y, y_Y, w_Y, h_Y = cv.boundingRect(con_Y[0])

        md_Y = mid_point(x_Y, y_Y, x_Y+w_Y, y_Y+h_Y)

        d['ball'] = md_Y

        # count += 1

        cv.circle(frame, md, 8, (0, 255, 255), -1)
        cv.circle(blank, md, 8, (0, 255, 255), -1)

        for i in d:
            for j in d:
                if i != j:
                    if i == 'ball' or j == 'ball':
                        cv.line(frame, d[i], d[j], (0, 255, 255), 1)
                        cv.line(blank, d[i], d[j], (0, 255, 255), 1)
                    elif 'Red' in i or 'Red' in j:
                        cv.line(frame, d[i], d[j], (0, 0, 255), 1)
                        cv.line(blank, d[i], d[j], (0, 0, 255), 1)
                    else:
                        cv.line(frame, d[i], d[j], (255, 0, 0), 1)
                        cv.line(blank, d[i], d[j], (255, 0, 0), 1)

    cv.imshow ('jdf', frame)
    # cv.imshow ('jaja', mask_R)
    # cv.imshow ('f', blank)
    # cv.imshow ('ajdfnds', img)
    cv.waitKey(1)