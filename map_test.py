x_map = {7: 0, 8: 0, 9: 0, 10: 0}
y_map = {77: 0, 78: 0, 79: 0, 80: 0}

w = 11
i = 0
while i < 25:
    increment = w+18
    for k in range(w, increment):
        x_map[k] = i

    w = increment
    i += 1

w = 81
i = 0
while i < 26:
    increment = w+18
    for k in range(w, increment):
        y_map[k] = i

    w = increment
    i += 1

# print(y_map)