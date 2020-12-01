import itertools
import math

puzzle = [int(i) for i in open("01.txt").readlines()]

# Part 1 = 927684
[print(math.prod(i)) for i in itertools.combinations(puzzle, 2) if sum(i) == 2020]

# Part 2 = 292093004
[print(math.prod(i)) for i in itertools.combinations(puzzle, 3) if sum(i) == 2020]