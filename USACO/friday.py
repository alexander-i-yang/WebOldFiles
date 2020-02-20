"""
ID: aspam1
LANG: PYTHON3
TASK: friday
"""
import sys

def get_day(start, end, start_day): return ((end-start)%7+start_day)%7

fin = open('friday.in', 'r')
fout = open('friday.out', 'w')

numYears = int(fin.readline())
days = [0 for x in range(7)]
year = 1900
date = 1
day = 1 # monday

months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

for y in range(numYears):
    year = 1900+y
    #print(year)
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        months[1] = 29
    else: months[1] = 28
    #print("Feb: ", months[1])
    for m in range(12):
        #print("m: ", m)
        t_day = get_day(date, 13, day)
        #print("13:", t_day)
        days[t_day] += 1
        l_day = get_day(13, months[m], t_day)
        #print("last: ", l_day)
        day = (l_day+1) % 7
        #print("first: ", day)
ret = "{} {} {} {} {} {} {}\n".format(days[6], days[0], days[1], days[2], days[3], days[4], days[5])
fout.write(ret)