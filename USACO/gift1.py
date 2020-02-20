"""
ID: aspam1
LANG: PYTHON3
TASK: gift1
"""
import sys


def print_dict(dict):
    for x in dict:
        sys.stdout.write(x + " : %d\n" % (dict[x]))


def write_dict(file, dict):
    for x in dict:
        ret = "{} {}\n".format(x, dict[x])
        file.write(ret)


def instruc(dict, rec, curName, numMoney, splitNum):
    if numMoney == 0 and splitNum == 0: return
    for name in rec:
        dict[name] += int(numMoney/splitNum)
    dict[curName] += numMoney%splitNum - numMoney

fin = open('gift1.in', 'r')
fout = open('gift1.out', 'w')

numFriends = int(fin.readline())
friends = {fin.readline()[0:-1]: 0 for i in range(numFriends)}
print_dict(friends)
sys.stdout.write("\n")
for i in range(numFriends):
    curName = fin.readline()[0:-1]
    numMoney, splitNum = map(int, fin.readline().split())
    rec = [fin.readline()[0:-1] for x in range(splitNum)]
    instruc(friends, rec, curName, numMoney, splitNum)
print_dict(friends)

write_dict(fout, friends)
fout.close()