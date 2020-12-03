puzzle = [list(i.strip()) for i in open("03.txt").readlines()]
L = len(puzzle)
W = len(puzzle[0])


def traverse(right, down):
    trees = 0
    y, x = 0, 0
    while y < L - 1:
        x += right
        y += down
        if puzzle[y][x % W] == '#':
            trees += 1
    return trees


print(traverse(3, 1))
print(traverse(1, 1)*traverse(3, 1)*traverse(5, 1)*traverse(7, 1)*traverse(1, 2))
