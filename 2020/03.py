import numpy as np

puzzle = [list(i.strip()) for i in open("03.txt").readlines()]
h = 7*len(puzzle)
m = np.array([np.array(l * h) for l in puzzle]) # build largest map beforehand for speed


def traverse(right, down):
    trees = 0
    y, x = 0, 0
    while y < len(puzzle) - 1:
        x += right
        y += down
        if m[y, x] == '#':
            trees += 1
    return trees


print(traverse(3, 1))
print(traverse(1, 1)*traverse(3, 1)*traverse(5, 1)*traverse(7, 1)*traverse(1, 2))
