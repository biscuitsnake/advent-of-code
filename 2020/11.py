import copy

puzzle = [list(i.strip()) for i in open("11.txt").readlines()]


def do_round(grid):
    new_grid = copy.deepcopy(grid)
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if grid[row][col] == '.':
                continue
            adj = []
            for x in (-0, 1, -1):
                for y in (0, 1, -1):
                    if x == y == 0:
                        continue
                    # Begin Part 1:
                    # adj.extend(grid[row+x][col+y])
                    # End Part 1
                    # Begin Part 2:
                    z = 1
                    while 0 <= row+z*x < len(grid) and 0 <= col+z*y < len(grid[row]):
                        check = grid[row+z*x][col+z*y]
                        if check != '.':
                            adj.append(check)
                            break
                        z += 1
                    # End Part 2
            if grid[row][col] == 'L' and adj.count('#') == 0:
                new_grid[row][col] = '#'
            # if grid[row][col] == '#' and adj.count('#') >= 4:  # Part 1
            if grid[row][col] == '#' and adj.count('#') >= 5:
                new_grid[row][col] = 'L'
    return new_grid


[i.insert(0, '.') for i in puzzle]
[i.append('.') for i in puzzle]
new_len = len(puzzle[0])
puzzle.insert(0, ['.']*new_len)
puzzle.append(['.']*new_len)

grid = puzzle
while True:
    new = do_round(grid)
    if new == grid:
        flat = [sleep for nope in new for sleep in nope]
        print(flat.count('#'))
        break
    grid = new
