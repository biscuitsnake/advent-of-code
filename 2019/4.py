from itertools import groupby

# Part 1 = 889
count = 0
for i in range(307237, 769058):
    i = str(i)
    if i[0] <= i[1] <= i[2] <= i[3] <= i[4] <= i[5] and sum(len(tuple(g)) > 1 for k, g in groupby(i)) >= 1:
        count += 1
print(count)

# Part 2 = 589
count = 0
for i in range(307237, 769058):
    i = str(i)
    if i[0] <= i[1] <= i[2] <= i[3] <= i[4] <= i[5] and sum(len(tuple(g)) == 2 for k, g in groupby(i)) >= 1:
        count += 1
print(count)