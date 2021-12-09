import numpy as np
from scipy.ndimage import measurements

puzzle = [[int(j) for j in i.strip()] for i in open("09.txt").readlines()]
a = np.zeros(shape=(len(puzzle), len(puzzle[0])))
part1 = 0

for r in range(len(puzzle)):
    for c in range(len(puzzle[0])):
        current = puzzle[r][c]
        adj = []
        if r > 0:
            adj.append(puzzle[r-1][c])
        if r < len(puzzle) - 1:
            adj.append(puzzle[r+1][c])
        if c > 0:
            adj.append(puzzle[r][c-1])
        if c < len(puzzle[0]) - 1:
            adj.append(puzzle[r][c+1])

        if all(current < x for x in adj):
            part1 += (current + 1)
        if current != 9:
            a[r][c] = 1

lw, num = measurements.label(a)
area = sorted(measurements.sum(a, lw, index=range(lw.max() + 1)), reverse=True)
part2 = int(area[0]*area[1]*area[2])

print(part1)
print(part2)
