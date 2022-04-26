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
        # if Q[i][num] > elem[num]:S    con_R, contours_R = cv.findContours(
        if Q[i][num] > elem[num]:
            Q.insert(i, elem)
            return
    Q.append(elem)
    return


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
    for k in G:
        for l in G:
            lst[d1[k]][d1[l]] = (
                dist(G[k][0], G[k][1], G[l][0], G[l][1]), d1[l])
    return lst


def line(x1, y1, x2, y2):
    if x2-x1 == 0:
        x2 += 1
    m = (y2-y1)/(x2-x1)
    b = y1-m*x1
    return m, b


def an (x1, y1, x2, y2):
    mag_v1 = 100
    mag_v2 = dist(x1, y1, x2, y2)

    val = (100*(x2-x1)) / (mag_v1*mag_v2)

    ang = math.acos(val)

    if y2 > y1:
      return (2*math.pi) - ang

    else:
      return ang



def run(x1,y1):
    pass
    



def pass_ball(x1, y1, x2, y2, dis):
    r_n = dist(y1, x1, y2, x2)
    if y2-y1 == 0:
        y2 = 1

    # angle = math.atan((x2-x1) / (y2-y1))
    angle = an (x1, y1, x2, y2)

    if dis > 140:
        hold = 0.4
    else:
        hold = dis/325

    if dis < 200:
        hold2 = 0.4
    else:
        hold2 = ((dis-200)*(3/500)) + (dis/500)

    if 0 < angle < (math.pi)/6:
        #  print(math.atan(x2-x1/(y2-y1))
        print('passdownnew')
        p.keyDown('down')
        p.keyDown('right')
        p.keyDown('s')
        time.sleep(hold)
        p.keyUp('right')
        p.keyUp('down')
        p.keyUp('s')
    elif (math.pi/6) < angle < (math.pi) / 3:
        print('downright')
        p.keyDown('down')
        p.keyDown('right')
        p.keyDown('s')
        time.sleep(hold)
        p.keyUp('right')
        p.keyUp('down')
        p.keyUp('s')
    elif (math.pi/3) < angle < (math.pi)/2:
        print('passright')
        p.keyDown('right')
        p.keyDown('s')
        time.sleep(hold)
        p.keyUp('right')
        p.keyUp('s')
    elif (math.pi/2) < angle < 2*(math.pi)/3:
        print('passright')
        p.keyDown('right')
        p.keyDown('s')
        time.sleep(hold)
        p.keyUp('right')
        p.keyUp('s')
    elif 2*(math.pi/3) < angle < 5*(math.pi)/6:
        print('upright')
        p.keyDown('up')
        p.keyDown('right')
        p.keyDown('s')
        time.sleep(hold)
        p.keyUp('right')
        p.keyUp('up')
        p.keyUp('s')

    elif 5*(math.pi/6) < angle < (math.pi):
        print('passup')
        p.keyDown('up')
        p.keyDown('s')
        time.sleep(hold)
        p.keyUp('up')
        p.keyUp('s')

    elif math.pi < angle < 7*(math.pi)/6:
        print('passup')
        p.keyDown('up')
        p.keyDown('s')
        time.sleep(hold)
        p.keyUp('up')
        p.keyUp('s')

    elif 7*(math.pi/6) < angle < 4*(math.pi)/3:
        print('passupleft')
        p.keyDown('up')
        p.keyDown('left')
        p.keyDown('s')
        time.sleep(hold)
        p.keyUp('left')
        p.keyUp('up')
        p.keyUp('s')

    else:
        p.keyDown('s')
        time.sleep(hold)
        print('SUIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII')
        p.keyUp('s')
    time.sleep(hold2)
# agr two specfic line se bahor hai to dont kick
# agr koi bhi nhi aspas to phr aony pass rakhni
# atleast some distance ry har banday se or total distanc eki cost maximium rhay...
# if akela or koi bnada spas nhi to dorect goal


def goaler():
    m1, b1 = line(548, 174, 381, 7)
    m2, b2 = line(548, 305, 381, 460)

    destination = None
    list = []
    for i in d:
        if d[i][0] >= 430:
            if d[i][1] > (m1*d[i][0] + b1) and d[i][1] < (m2*d[i][0] + b2) and 'Blue' in i:
                enqueue_p(list, (i, d1[i], 548-d[i][0]))
            # elif 'Red' in i:
            #     enqueue_p(enemy,(i, d1[i]))

    destination = False

    for l in list:
        opp_lst = [x for x in adj_mat[l[1]][0:11] if x[0] < 22]
        if len(opp_lst) > 1:
            pass
        else:
            destination = l
            break

    if destination:
        dx, dy = dijkstra(adj_mat, destination[1])
        print(dx, dy)
        print('Garmi dekho rozay choro nasahy karo..............................')
        return dy

    return []


def dijkstra(graph, start):
    # we can also make seperate lists/dictionaries ofr red and blue nodes
    nodes_to_take = []
    for q in d:
        if d[q][0] > 400 and 'Blue' in q:
            nodes_to_take.append(d1[q])
    nodes_to_take.append(22)

    print(nodes_to_take)

    back_path = []

    distances = [float("inf") for _ in range(len(graph))]
    distancenode = {}

    # This contains whether a node was already visited
    visited = []
    for i in range(len(graph)):
        # if i in nodes_to_take:
        visited.append(False)
        # else:
        #     visited.append(True)

    print(visited)

    # The distance from the start node to itself is of course 0
    distances[start] = 0

    # While there are nodes left to visit...
    while True:
        # find the node with the currently shortest distance from the start node...
        shortest_distance = float("inf")
        shortest_index = -1
        for i in range(len(graph)):
            # ... by going through all nodes that haven't been visited yet
            # print (distances[i], shortest_distance)
            if distances[i] < shortest_distance and not visited[i]:
                shortest_distance = distances[i]
                shortest_index = i
            # print (distances)

        # print("Visiting node " + str(shortest_index) + " with current distance " + str(shortest_distance))

        if shortest_index == -1:
            # a = True
            # for i in visited:
            #     if i == False:
            #         a = False
            # There was no node not yet visited --> We are done
            # if a :
            path = []
            parent = 22
            while parent != start:
                path.insert(0, (distancenode[parent], parent))
                parent = distancenode[parent]

            return distances, path

        # ...then, for all neighboring nodes that haven't been visited yet....
        for i in range(11, len(graph[shortest_index])):
            if i in nodes_to_take:
                # ...if the path over this edge is shorter...
                opps = get_enemy(graph, i)
                if graph[shortest_index][i][0] != 0 and distances[i] > distances[shortest_index] + graph[shortest_index][i][0]:
                    # ...Save this path as new shortest path.
                    distances[i] = distances[shortest_index] + \
                        graph[shortest_index][i][0]
                    distancenode[i] = shortest_index

                    print("Updating distance of node " +
                          str(i) + " to " + str(distances[i]))

        # Lastly, note that we are finished with this node.
        visited[shortest_index] = True
        # print("Visited nodes: " + str(visited))
        # print("Currently lowest distances: " + str(distances))'


def get_enemy(graph, node):
    opp_lst = [x for x in graph[node][0:11] if x[0] < 22]
    return opp_lst


# d = {}
# count = 0ssssssssssssssss
# lower_R = np.array([75, 0, 163])sssssssssssssssssssss
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
d2 = {}
lst = [[0 for j in range(len(d))] for i in range(len(d))]
count = 0
for m in d:
    d1[m] = count
    d2[count] = m
    count += 1

print(d1)
print(d2)

while True:
    _, img = cap.read()
    count = 0
    countR = 0
    countB = 0
    countY = 0
    hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
    blank = np.zeros(img.shape[:], dtype='uint8')
    blank2 = np.zeros(img.shape[:], dtype='uint8')
    blank3 = np.zeros(img.shape[:], dtype='uint8')

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

    cv.line(img, (548, 174), (381, 7), (255, 255, 255), 10)
    cv.line(img, (548, 305), (381, 460), (255, 255, 255), 10)

    mask_R = cv.inRange(hsv, (161, 244, 141), (172, 255, 255))
    mask_Y = cv.inRange(hsv, (24, 177, 187), (33, 247, 217))
    mask_B = cv.inRange(hsv, (93, 210, 193), (101, 241, 238))
    # mask_B = cv.inRange(hsv, (94, 191, 204), (98, 203, 213))

    # cv.circle(blank,(300,300),25,(0,0,80),3)

    con_R, contours_R = cv.findContours(
        mask_R, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
    con_Y, contours_Y = cv.findContours(
        mask_Y, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
    con_B, contours_B = cv.findContours(
        mask_B, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)

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

    print(f'Red = {countR}, Blue = {countB}, Ball = {countY}')
    cv.waitKey(1)

    # print(d)

    red_Y = [d[x][0] for x in d if x[0] == 'R' and d[x][0] < 200]
    red_Y2 = [d[x][0] for x in d if x[0] == 'R' and d[x][0] < 325]
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
        teammates = sorted(adj_mat[22][11:22], key=lambda x: x[0])
        opp = sorted(adj_mat[22][0:11], key=lambda y: y[0])
        bhagcount = 0
        bhagcount2=0
        # run = True
        x1, y1 = d['ball']
        if d['ball'][0] >= 450:
            for i in range(5):
                p.keyDown('a')

        elif d['ball'][0] >= 400:
            list_of_options = goaler()
            if len(list_of_options) == 0:
                # apny pass rakho
                # line
                m1,b1 = line(x1,y1-10, x1+60,y1-30)
                m2,b2 = line(x1,y1+10, x1+60, y1+30)
                runn=True

                for i in opp[:5]:
                    if d[d2[i[1]]][0] > d['ball'][0]:
                        bhagcount += 1
                    elif x1+100 > d[d2[i[1]]][0] >= x1:
                        if d[d2[i[1]]][0] < (m1*d[d2[i[1]]][0]+b1) or d[d2[i[1]]][0] > (m2*d[d2[i[1]]][0]+b2):
                            bhagcount+=1

                    
                if bhagcount <= 1 or bhagcount2<=1:
                    for i in range(10):
                        p.keyDown('shift')
                        p.keyDown('right')

            elif len(list_of_options) == 1:
                x1, y1 = d[d2[list_of_options[0][1]]]
                x2, y2 = d[d2[list_of_options[0][0]]]
                pass_ball(
                    x1, y1, x2, y2, adj_mat[list_of_options[0][1]][list_of_options[0][0]][0])
                p.keyDown('a')
                print('ball kicked')
                time.sleep(0.3)
                p.keyUp('a')

            elif len(list_of_options) > 1:
                x1, y1 = d[d2[list_of_options[-1][1]]]
                x2, y2 = d[d2[list_of_options[-1][0]]]
                pass_ball(
                    x1, y1, x2, y2, adj_mat[list_of_options[0][1]][list_of_options[0][0]][0])

        #

        #             # bhag()
        #             pass

        # kepp_ball = True
        else:
            for i in teammates:
                print(f'entering loop {i}')
                node = i[1]
                # print(node)

                # print(adj_mat[11+i][0:11])
                opp_i = min(adj_mat[node][0:11], key=lambda x: x[0])
                # print(opp_i)

                x1, y1 = d['ball']
                # print(x1, y1)
                x2, y2 = d[d2[node]]
                # print(x2, y2)
                m, b = line(x1, y1, x2, y2)

                should_pass = True
                ynew = m*x2 + b-40  # distance between ball and the next player se ooper wala distance jispe line end horhi hai. parallelogra ki
                diss = dist(x1, y1, x2, ynew)
                # cv.line(blank, (x1, y1), (x2, ynew), (255,0,0), 10)
                if opp_i[0] > 40:
                    for k in adj_mat[22][0:11]:
                        if k[0] < diss:
                            a1, b1 = d[d2[k[1]]]
                            if (b1 > 0.9*m*a1 + b+30) or b1 < (1.15*m*a1 + b-30):
                                pass
                            else:
                                should_pass = False
                                break
                    if should_pass:
                        pass_ball(x1, y1, x2, y2, i[0])
                        keepball = False
                        print('passsssssssssssssssssssssssssssssssssssssssssssss')

    # time.sleep(4)
# sssss
