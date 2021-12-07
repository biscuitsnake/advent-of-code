from statistics import median, mean
from math import ceil, floor

puzzle = [int(i) for i in open("07.txt").readline().split(",")]

# Part 1:
m1 = round(median(puzzle))
fuel = 0
for i in puzzle:
    fuel += abs(i - m1)

print(fuel)

# Part 2:
m2 = mean(puzzle)
m = [floor(m2), ceil(m2)]
fuel = [0, 0]

def crab(n):
    return n*(n + 1) // 2

for i in puzzle:
    fuel[0] += crab(abs(i - m[0]))
    fuel[1] += crab(abs(i - m[1]))

print(min(fuel))
