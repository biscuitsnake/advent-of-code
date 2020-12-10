import collections

puzzle = [int(i.strip()) for i in open("10.txt").readlines()]

puzzle = sorted(puzzle)
puzzle.append(puzzle[-1] + 3)

j = 0
ones, threes = 0, 0
for i in puzzle:
    if i - j == 3:
        threes += 1
    elif i - j == 1:
        ones += 1
    j = i

print(ones * threes)

c = collections.defaultdict(int, {0: 1})
for i in puzzle:
    c[i] = c[i-3] + c[i-2] + c[i-1]

print(c[puzzle.pop()])
