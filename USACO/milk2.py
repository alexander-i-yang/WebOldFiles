"""
ID: aspam1
LANG: PYTHON3
TASK: milk2
"""


def shrinkList(list):
    leng = len(list) - 1
    i = 0
    while i < leng:
        #print(list[i][1], list[i+1][0])
        while i < leng and list[i][1] >= list[i + 1][0]:
            #print(list[220:228])
            b = list[i][1]
            y = list[i + 1][1]
            # print("Before", list)
            if b <= y:
                list[i][1] = y
            list.pop(i + 1)
            leng = len(list)-1
            # print("After", list)
        if i >= leng: break
        a = list[i][0]
        b = list[i][1]
        x = list[i + 1][0]
        y = list[i + 1][1]
        if a < x:
            if b >= y:
                list.pop(i + 1)
        leng = len(list) - 1
        i += 1
        print(list)


def maxMilk(list):
    max = 0
    for i in list:
        dif = i[1] - i[0]
        if dif > max: max = dif
    return max


def maxNo(list):
    max = 0  # list[0][0]
    for i in range(len(list) - 1):
        dif = list[i + 1][0] - list[i][1]
        if dif > max: max = dif
    return max


fin = open('milk2.in', 'r')
fout = open('milk2.out', 'w')

numFarmers = int(fin.readline())
time = {}

for x in range(numFarmers):
    y, z = map(int, fin.readline().split())
    time[y] = z
time = sorted(time.items(), key=lambda kv: kv[0])
time = [[x[0], x[1]] for x in time]
# print(time)
shrinkList(time)
# print(time)
ret = "{} {}\n".format(maxMilk(time), maxNo(time))
fout.write(ret)
