"""
ID: aspam1
LANG: PYTHON3
TASK: beads
"""
import sys

fin = open('beads.in', 'r')
fout = open('beads.out', 'w')

numBeads = int(fin.readline())
beadString = fin.readline()

beadArr = [x for x in beadString]
# print(beadArr)
max = 0
for i in range(numBeads):
    beadRight = beadArr[i]
    right = 0
    extent = i
    for x in range(numBeads):
        if i == 0 and right == numBeads-1:
            ret = "{}\n".format(numBeads)
            fout.write(ret)
            quit()
        nextBead = beadArr[(i + x) % numBeads]
        if nextBead != beadRight:
            if beadRight == "w":
                beadRight = nextBead
            elif nextBead != "w":
                extent = x
                break
        extent = (i + x) % numBeads
        right += 1
    print(i, ":", right, "\t", beadArr[i:i+right])
    beadLeft = beadArr[(i - 1) % numBeads]
    # print("Bead left: ", beadLeft)
    left = 0
    for y in range(numBeads):
        ex = (i - 1 - y) % numBeads
        nextBead = beadArr[ex]
        if extent == ex: break
        if nextBead != beadLeft:
            if beadLeft == "w":
                beadLeft = nextBead
            elif nextBead != "w":
                break
        left += 1
    print(i, ":", i-left, "\t", left)
    print(left+right)
    if left + right > max: max = left + right
ret = "{}\n".format(max)
fout.write(ret)
