DIRS = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]
GRID = [list(i) for i in open("04.txt").read().splitlines()]
WIDTH = len(GRID[0])
HEIGHT = len(GRID)


def access(i, j):
    rolls = 0
    for dir in DIRS:
        y = i + dir[0]
        x = j + dir[1]
        if (0 <= y < HEIGHT) and (0 <= x < WIDTH):
            if GRID[y][x] == "@":
                rolls += 1
    return rolls


# Part 1

accessible = 0
for i, row in enumerate(GRID):
    for j, col in enumerate(row):
        if col == "@":
            rolls = access(i, j)
            if rolls < 4:
                accessible += 1
print(accessible)

# Part 2

removable = 0
more = True
while more:
    more = False
    for i, row in enumerate(GRID):
        for j, col in enumerate(row):
            if col == "@":
                rolls = access(i, j)
                if rolls < 4:
                    GRID[i][j] = "."
                    removable += 1
                    more = True
print(removable)
