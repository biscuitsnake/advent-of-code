import re
from datetime import datetime

file = open('4.txt', 'r')
records = [line.strip() for line in file]

sortedRecords = sorted(records, key=lambda x: datetime.strptime(x[1:17], '%Y-%m-%d %H:%M'), reverse=False)

#part 1 = 99911

shifts = {}

# 1 = sleep
for record in sortedRecords:
    min = int(re.search("(:\d+)", record)[0][1:])
    if 'shift' in record:
        start = 0
        if int(re.search("(\d+:)", record)[0][:-1]) == 0:
            start = min
        guard = int(re.search("(#\d+)", record)[0][1:])
        if guard not in shifts:
            shifts[guard] = [0]*60
    else:
        
        if 'falls asleep' in record:
            start = min

        if 'wakes up' in record:
            for i in range(start, min):
                shifts[guard][i] += 1
    
maxm = 0
id = 0
maxsleep = 0

for i in shifts:
    l = shifts[i]
    sleep = sum(l)
    if sleep > maxsleep:
        maxsleep = sleep
        print (i, l)
        id = i
        maxm =  max( (v, i) for i, v in enumerate(l) )[1]
    
print (id, maxm)
print (id * maxm)
