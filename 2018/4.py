import re
from datetime import datetime

file = open('5.txt')
records = [line.strip() for line in file]

sortedRecords = sorted(records, key=lambda x: datetime.strptime(x[1:17], '%Y-%m-%d %H:%M'), reverse=False)

# part 1 = 99911

shifts = {}

for record in sortedRecords:
    min = int(re.search("(:\d+)", record)[0][1:])

    if 'shift' in record:
        start = 0

        if int(re.search("(\d+:)", record)[0][:-1]) == 0:
            start = min

        guard = int(re.search("(#\d+)", record)[0][1:])

        if guard not in shifts:
            shifts[guard] = [0] * 60
    else:
        if 'falls asleep' in record:
            start = min

        if 'wakes up' in record:
            for i in range(start, min):
                shifts[guard][i] += 1

mostsleep = 0

for i in shifts:
    l = shifts[i]
    sleep = sum(l)

    if sleep > mostsleep:
        mostsleep = sleep
        id = i
        maximum = max((v, i) for i, v in enumerate(l))[1]

print(id * maximum)

# part 2 = 65854

mostestsleep = 0

for i in shifts:
    sleep = max(shifts[i])

    if sleep > mostestsleep:
        mostestsleep = sleep
        id = i
        minute = shifts[i].index(mostestsleep)

print(id * minute)
