import imghdr
import cv2 as cv
import time
from cv2 import illuminationChange
import numpy as np
import pydirectinput as p
import math
import os
import sys


def enqueue_p(Q, elem, num=2):
    for i in range(len(Q)):
        if Q[i][num] > elem[num]:
            Q.insert(iS    con_R, contours_R=cv.findContours(
        mask_R, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
    con_Y, contours_Y=cv.findContours(
        mask_Y, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
    con_B, contours_B=cv.findContours(
        mask_B, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)

    for cnt in con_R:
        x, y, w, h=cv.boundingRect(cnt)

        md=mid_point(x, y, x+w, y+h)

        # if f'Red{count}' in d:
        if countR <= 10:

            d[f'Red{count}']=md

            count += 1
            countR += 1

            # cv.circle(img, md, 3, (0, 0, 255), -1)
            cv.circle(blank, md, 10, (0, 0, 255), -1)
            # if countR < 3:
            cv.circle(blank2, md, 8, (0, 0, 255), -1)

    count=0

    for cnt in con_B:
        x, y, w, h=cv.boundingRect(cnt)

        md=mid_point(x, y, x+w, y+h)

        # if f'Blue{count}' in d:
        if countB <= 10:

            d[f'Blue{count}']=md

            count += 1
            countB += 1

            # cv.circle(img, md, 3, (255, 0, 0), -1)
            cv.circle(blank, md, 10, (255, 0, 0), -1)
            # if countB < 5:
            cv.circle(blank2, md, 8, (255, 0, 0), -1)

    for cnt in con_Y:

        x_Y, y_Y, w_Y, h_Y=cv.boundingRect(cnt)

        md_Y=mid_point(x_Y, y_Y, x_Y+w_Y, y_Y+h_Y)

        if countY <= 1:

            d['ball']=md_Y

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
    adj_mat=display_adj_matrix(d, lst, d1)

    cv.imshow('Orig', img)
    # cv.imshow ('and', mask_R)
    cv.imshow('Graph', blank)
    cv.imshow('nodesOnly', blank2)

    print(f'Red = {countR}, Blue = {countB}, Ball = {countY}')
    cv.waitKey(1)

    # print(d)

    red_Y=[d[x][0] for x in d if x[0] == 'R' and d[x][0] < 200]
    red_Y2=[d[x][0] for x in d if x[0] == 'R' and d[x][0] < 325]
    print(red_Y)

    # Defensive Strategy
    if countB > 10 and d['ball'][0] < 423:
        if ((len(red_Y2) > 3) and d['ball'][0] < 423):
            p.keyDown('s')
        elif len(red_Y) >= 1 and d['ball'][0] < 202:
            p.keyDown('s')
            p.keyDown('a')
        else:
            p.keyUp('s')
            p.keyUp('a')

    # lst=[left,right,up,down, leftup, leftdown, righup , rightdown]
    # if initx < finalx
    # if inity < final y
    # if initx > final x
    # if init y > final y

    # {'Red0': 0, 'Red1': 1, 'Red2': 2, 'Red3': 3, 'Red4': 4, 'Red5': 5, 'Red6': 6, 'Red7': 7, 'Red8': 8, 'Red9': 9, 'Red10': 10, 'Blue0': 11, 'Blue1': 12, 'Blue2': 13, 'Blue3': 14, 'Blue4': 15, 'Blue5': 16, 'Blue6': 17, 'Blue7': 18, 'Blue8': 19, 'Blue9': 20, 'Blue10': 21, 'ball': 22}
    else:
        teammates=sorted(adj_mat[22][11:22], key=lambda x: x[0])
        opp=sorted(adj_mat[22][0:11], key=lambda y: y[0])
        bhagcount=0
        bhagcount2=0
        # run = True
        x1, y1=d['ball']
        if d['ball'][0] >= 450:
            for i in range(5):
                p.keyDown('a')

        elif d['ball'][0] >= 400:
            list_of_options=goaler()
            if len(list_of_options) == 0:
                # apny pass rakho
                # line
                m1, b1=line(x1, y1-10, x1+60, y1-30)
                m2, b2=line(x1, y1+10, x1+60, y1+30)
                runn=True

                for i in opp[:5]:
                    if d[d2[i[1]]][0] > d['ball'][0]:
                        bhagcount += 1
                    elif x1+100 > d[d2[i[1]]][0] >= x1:
                        if d[d2[i[1]]][0] < (m1*d[d2[i[1]]][0]+b1) or d[d2[i[1]]][0] > (m2*d[d2[i[1]]][0]+b2):
                            bhagcount += 1


                if bhagcount <= 1 or bhagcount2 <= 1:
                    for i in range(10):
                        p.keyDown('shift')
                        p.keyDown('right')

            elif len(list_of_options) == 1:
                x1, y1=d[d2[list_of_options[0][1]]]
                x2, y2=d[d2[list_of_options[0][0]]]
                pass_ball(
                    x1, y1, x2, y2, adj_mat[list_of_options[0][1]][list_of_options[0][0]][0])
                p.keyDown('a')
                print('ball kicked')
                time.sleep(0.3)
                p.keyUp('a')

            elif len(list_of_options) > 1:
                x1, y1=d[d2[list_of_options[-1][1]]]
                x2, y2=d[d2[list_of_options[-1][0]]]
                pass_ball(
                    x1, y1, x2, y2, adj_mat[list_of_options[0][1]][list_of_options[0][0]][0])

        #

        #             # bhag()
        #             pass

        # kepp_ball = True
        else:
            for i in teammates:
                print(f'entering loop {i}')
                node=i[1]
                # print(node)

                # print(adj_mat[11+i][0:11])
                opp_i=min(adj_mat[node][0:11], key=lambda x: x[0])
                # print(opp_i)

                x1, y1=d['ball']
                # print(x1, y1)
                x2, y2=d[d2[node]]
                # print(x2, y2)
                m, b=line(x1, y1, x2, y2)

                should_pass=True
                ynew=m*x2 + b-40  # distance between ball and the next player se ooper wala distance jispe line end horhi hai. parallelogra ki
                diss=dist(x1, y1, x2, ynew)
                # cv.line(blank, (x1, y1), (x2, ynew), (255,0,0), 10)
                if opp_i[0] > 40:
                    for k in adj_mat[22][0:11]:
                        if k[0] < diss:
                            a1, b1=d[d2[k[1]]]
                            if (b1 > 0.9*m*a1 + b+30) or b1 < (1.15*m*a1 + b-30):
                                pass
                            else:
                                should_pass=False
                                break
                    if should_pass:
                        pass_ball(x1, y1, x2, y2, i[0])
                        keepball=False
                        print('passsssssssssssssssssssssssssssssssssssssssssssss')

    # time.sleep(4)
# sssss
