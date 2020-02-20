"""
ID: aspam1
LANG: PYTHON3
TASK: test
"""
import sys
fin = open ('test.in', 'r')
fout = open ('test.out', 'w')
x,y = map(int, fin.readline().split())
sum = x+y
fout.write(str(sum) + '\n')
fout.close()
sys.stderr.write('message')