import imghdr
import cv2 as cv
import time
import numpy as np
import pydirectinput as p


def mid_point(x1, y1, x2, y2):
    x = (x1 + x2) // 2
    y = (y1 + y2) // 2

    return (x, y)


def dist(x1, y1, x2, y2):
    a = (x2 - x1) ** 2
    b = (y2 - y1) ** 2

    d = abs((a + b)) ** (1/2)

    return d


def display_adj_matrix(G, lst, d1):
    # d1 = {}
    # count = 0
    # for m in G:
    #     d1[m] = count
    #     count += 1
    for k in G:
        for l in G:
            lst[d1[k]][d1[l]] = dist(G[k][0], G[k][1], G[l][0], G[l][1])
    return lst

# d = {}

# count = 0

# lower_R = np.array([75, 0, 163])
# upper_R = np.array([100, 0, 220])

# lower_Y = np.array([30, 194, 194])
# upper_Y = np.array([40, 200, 200])

# lower_B = np.array([70, 70, 70])
# upper_B = np.array([80, 80, 80])


# img = cv.imread('try2.png')
# img = cv.imread('try4.png')
# hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
# blank = np.zeros(img.shape[:], dtype='uint8')
# blank2 = np.zeros(img.shape[:], dtype='uint8')
cap = cv.VideoCapture(1)

# cap.set(3, 1280)
# cap.set(4, 720)
d = {'Red0': (628, 545), 'Red1': (723, 537), 'Red2': (589, 422), 'Red3': (665, 408), 'Red4': (763, 387), 'Red5': (1029, 333), 'Red6': (774, 277), 'Red7': (666, 260), 'Red8': (592, 246), 'Red9': (724, 132), 'Red10': (628, 123), 'Blue0': (
    510, 548), 'Blue1': (531, 544), 'Blue2': (524, 535), 'Blue3': (513, 539), 'Blue4': (407, 439), 'Blue5': (402, 430), 'Blue6': (387, 436), 'Blue7': (473, 407), 'Blue8': (493, 407), 'Blue9': (486, 397), 'Blue10': (482, 396), 'ball': (561, 315)}
d1 = {}
lst = [[0 for j in range(len(d))] for i in range(len(d))]
count = 0
for m in d:
    d1[m] = count
    count += 1

while True:
    _, img = cap.read()
    # img = cv.GaussianBlur(img, (11, 11), 0)
    count = 0
    countR = 0
    countB = 0
    countY = 0
    hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
    blank = np.zeros(img.shape[:], dtype='uint8')
    blank2 = np.zeros(img.shape[:], dtype='uint8')

    # mask_R = cv.inRange(img, lower_R, upper_R)
    # mask_Y = cv.inRange(img, lower_Y, upper_Y)
    # mask_B = cv.inRange(img, lower_B, upper_B)
    # Upper boundary
    cv.line(blank, (77, 7), (548, 7), (255, 255, 255), 8)
    cv.line(img, (77, 7), (548, 7), (255, 255, 255), 8)  # 600
    cv.line(blank2, (77, 7), (548, 7), (255, 255, 255), 8)

    # Lower boundary
    cv.line(blank, (77, 460), (548, 460), (255, 255, 255), 8)
    cv.line(img, (77, 460), (548, 460), (255, 255, 255), 8)
    cv.line(blank2, (77, 460), (548, 460), (255, 255, 255), 8)

    # upper left corner
    cv.line(blank, (77, 7), (77, 460), (255, 255, 255), 8)
    cv.line(img, (77, 7), (77, 460), (255, 255, 255), 8)
    cv.line(blank2, (77, 7), (77, 460), (255, 255, 255), 8)

    # upper right corner
    cv.line(blank, (548, 7), (548, 460), (255, 255, 255), 8)
    cv.line(img, (548, 7), (548, 460), (255, 255, 255), 8)
    cv.line(blank2, (548, 7), (548, 460), (255, 255, 255), 8)

    # left goal
    cv.line(blank, (77, 174), (77, 305), (45, 29, 240), 8)
    cv.line(img, (77, 174), (77, 305), (45, 29, 240), 8)
    cv.line(blank2, (77, 174), (77, 305), (45, 29, 240), 8)

    # right goal
    cv.line(blank, (548, 174), (548, 305), (45, 29, 240), 8)
    cv.line(img, (548, 174), (548, 305), (45, 29, 240), 8)
    cv.line(blank2, (548, 174), (548, 305), (45, 29, 240), 8)

    cv.line(img, (202, 7), (202, 460), (255, 255, 255), 2)
    cv.line(img, (423, 7), (423, 460), (255, 255, 255), 2)
    cv.line(img, (313, 7), (313, 460), (255, 255, 255), 1)

    mask_R = cv.inRange(hsv, (161, 244, 141), (172, 255, 255))
    mask_Y = cv.inRange(hsv, (24, 177, 187), (33, 247, 217))
    mask_B = cv.inRange(hsv, (93, 210, 193), (101, 241, 238))
    # mask_B = cv.inRange(hsv, (94, 191, 204), (98, 203, 213))

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

        # if f'Red{count}' in d:
        if countR <= 10:

            d[f'Red{count}'] = md

            count += 1
            countR += 1

            # cv.circle(img, md, 3, (0, 0, 255), -1)
            cv.circle(blank, md, 10, (0, 0, 255), -1)
            # if countR < 3:
            cv.circle(blank2, md, 8, (0, 0, 255), -1)

    count = 0

    for cnt in con_B:
        x, y, w, h = cv.boundingRect(cnt)

        md = mid_point(x, y, x+w, y+h)

        # if f'Blue{count}' in d:
        if countB <= 10:

            d[f'Blue{count}'] = md

            count += 1
            countB += 1

            # cv.circle(img, md, 3, (255, 0, 0), -1)
            cv.circle(blank, md, 10, (255, 0, 0), -1)
            # if countB < 5:
            cv.circle(blank2, md, 8, (255, 0, 0), -1)

    for cnt in con_Y:

        x_Y, y_Y, w_Y, h_Y = cv.boundingRect(cnt)

        md_Y = mid_point(x_Y, y_Y, x_Y+w_Y, y_Y+h_Y)

        if countY <= 1:

            d['ball'] = md_Y

            count += 1
            countY += 1

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

    # print (display_adj_matrix(d))
    adj_mat = display_adj_matrix(d, lst, d1)

    cv.imshow('Orig', img)
    # cv.imshow ('and', mask_R)
    cv.imshow('Graph', blank)
    cv.imshow('nodesOnly', blank2)

    # for i in d:
    #     if 'Red' in i:
    #         countR += 1
    #     elif 'Blue' in i:
    #         countB += 1
    #     elif i == ' ball':
    #         countY += 1

    # if d['ball'][1] > 100 and d['ball'][0] == 20:
    #     print ('outside')
    # elif d['ball'][1] > 500 and d['ball'][0] == 20:
    #     print ('outside')
    # elif d['ball'][1] > 500 and d['ball'][0] == 20:
    #     print ('upper left corner')

    # if countB < 11:
    #     print('Opponent has the ball')
    # elif countR < 11:
    #     print('player has the ball')

    print(f'Red = {countR}, Blue = {countB}, Ball = {countY}')
    cv.waitKey(1)

    print(d)
    # print(adj_mat)
    # time.sleep(1)
    # print (key['Red0'])
    # print(adj_mat[key['Red0']][key['Red0']])
    # print (d['Red0'])
    # print (dist(d['Red0'][0], d['Red0'][1], d['Red0'][0], d['Red0'][1]))
    red_Y = [d[x][0] for x in d if x[0] == 'R' and d[x][0] < 200]
    red_Y2 = [d[x][0] for x in d if x[0] == 'R' and d[x][0] < 325]
    print(red_Y)

    # Defensive Strategy
    if countB > 10 and d['ball'][0] < 423:
        if ((len(red_Y2) > 3) and d['ball'][0] < 423):
            p.keyDown('s')
        elif len(red_Y) >= 2 and d['ball'][0] < 202:
            p.keyDown('s')
            p.keyDown('a')
        else:
            p.keyUp('s')
            p.keyUp('a')
