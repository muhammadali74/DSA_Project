#Question 1 Noise Recuction from images
##############################################################################
from math import floor

import ast
A = input()
A = ast.literal_eval(A)

def remove_noise(A):
    # print (A)
    p = []
    for i in range(len(A)):
        # q = []
        for j in range (len(A[i])):
            t = []
            No = 0
            top = 'A[i-1][j]'
            bottom = 'A[i+1][j]'
            left = 'A[i][j-1]'
            right = 'A[i][j+1]'
            top_left = 'A[i-1][j-1]'
            top_right = 'A[i-1][j+1]'
            bottom_left = 'A[i+1][j-1]'
            bottom_right = 'A[i+1][j+1]'
            
            if i == 0:
                top = 'No'
                top_left = 'No'
                top_right = 'No'
            if i == len(A)-1:
                bottom = 'No'
                bottom_left = 'No'
                bottom_right = 'No'
                
            if j == 0:
                left = 'No'
                top_left = 'No'
                bottom_left = 'No'
            if j == len(A[i])-1:
                right = 'No'
                top_right = 'No'
                bottom_right = 'No'
                
            t.append(top)
            t.append(bottom)
            t.append(left)
            t.append(right)
            t.append(top_left)
            t.append(top_right)
            t.append(bottom_left)
            t.append(bottom_right)
            
            count = 0
            for k in t:
                if k != 'No':
                    count += 1
                
            # sm = A[i][j] + eval(top) + eval(bottom) + eval(left) + eval(right) + eval(top_left) + eval(top_right) + eval(bottom_left) + eval(bottom_right)
            
            # res = floor(sm/(count+1))
                
            # q.append(res)
            
        # p.append(q)
        
    return p

print(remove_noise(A))

#sample input --> [[10, 20, 20], [10, 10, 10], [20, 10, 20]]
#sample output --> [[12, 13, 15], [13, 14, 15], [12, 13, 12]]