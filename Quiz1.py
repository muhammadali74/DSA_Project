# Question 1 Noise Recuction from images
##############################################################################
# from curses.panel import bottom_panel
from math import floor

import ast
# A = input()
# A = ast.literal_eval(A)


def remove_noise(field, i, j):
    i = int(i)
    j = int(j)
    d = {'top': True, 'bottom': True, 'left': True, 'right': True, 'top_left': True,
         'top_right': True, 'bottom_left': True, 'bottom_right': True}
    No = None
    top = 'field[i-1][j]'
    bottom = 'field[i+1][j]'
    left = 'field[i][j-1]'
    right = 'field[i][j+1]'
    top_left = 'field[i-1][j-1]'
    top_right = 'field[i-1][j+1]'
    bottom_left = 'field[i+1][j-1]'
    bottom_right = 'field[i+1][j+1]'
    # print('this')

    if i == 0:
        top = 'No'
        d['top'] = False
        top_left = 'No'
        d['top_left'] = False
        top_right = 'No'
        d['top_right'] = False
    if i == len(field)-1:
        bottom = 'No'
        d['bottom'] = False
        bottom_left = 'No'
        d['bottom_left'] = False
        bottom_right = 'No'
        d['bottom_right'] = False

    if j == 0:
        left = 'No'
        d['left'] = False
        top_left = 'No'
        d['top_left'] = False
        bottom_left = 'No'
        d['bottom_left'] = False
    if j == len(field[i])-1:
        right = 'No'
        d['right'] = False
        top_right = 'No'
        d['top_right'] = False
        bottom_right = 'No'
        d['bottom_right'] = False

    top = eval(top)
    bottom = eval(bottom)
    left = eval(left)
    right = eval(right)
    top_left = eval(top_left)
    top_right = eval(top_right)
    bottom_left = eval(bottom_left)
    bottom_right = eval(bottom_right)

    for i in d:
        if d[i] == True:
            # print(eval(eval(i)))
            d[i] = eval(i)

    # t.append(top)
    # t.append(bottom)
    # t.append(left)
    # t.append(right)
    # t.append(top_left)
    # t.append(top_right)
    # t.append(bottom_left)
    # t.append(bottom_right)

    # count = 0
    # for k in t:
    #     if k != 'No':
    #         count += 1

    # sm = A[i][j] + eval(top) + eval(bottom) + eval(left) + eval(right) + eval(top_left) + eval(top_right) + eval(bottom_left) + eval(bottom_right)

    # res = floor(sm/(count+1))

    # q.append(res)

# p.append(q)

    return d

# print(remove_noise(A))


# A = [[10, 20, 20], [10, 10, 10], [20, 10, 20]]
# # sample output --> [[12, 13, 15], [13, 14, 15], [12, 13, 12]]

# print(remove_noise(A, 0, 0))
