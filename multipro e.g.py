import multiprocess as mp
import random

x = []
for i in range(1, 8000):
    j = random.randint(0, 10000)
    x.append(j)
# print(x)
x1 = x[:]
x2 = x[:]
x3 = x[:]


def s(lst):
    for i in range(len(lst)):
        minimum = i
        for j in range(i+1, len(lst)):
            if lst[j] < lst[minimum]:
                minimum = j
        lst[i], lst[minimum] = lst[minimum], lst[i]
    print('done1')


def b(lst):
    if len(lst) == 1:
        print(lst)
        return
    for i in range(len(lst)-1):
        for j in range(len(lst)-i-1):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
    print('done2')


if __name__ == '__main__':
    jobs = []
    # for i in range(5):
    #     p = mp.Process(target=worker)
    #     jobs.append(p)
    #     p.start()
    # print(mp.cpu_count())
    p1 = mp.Process(target=s, args=(x,))
    p2 = mp.Process(target=s, args=(x1,))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    # s(x2)
    # s(x3)
