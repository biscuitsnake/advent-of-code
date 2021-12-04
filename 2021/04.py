import numpy as np

with open("04.txt") as f:
    numbers = [int(i) for i in f.readline().split(",")]
    boards = [[int(j) for j in i.strip().split()] for i in f if i.strip()]
    boards = [boards[i:i + 5] for i in range(0, len(boards), 5)]

scores = []

for number in numbers:
    boards = [[[None if (n == number) else n for n in row] for row in board] for board in boards]

    for board in boards:
        w = False
        for row in board:
            if all(i is None for i in row):
                w = True
        for col in np.array(board).T.tolist():
            if all(i is None for i in col):
                w = True
        if w:
            scores.append(sum([sum(filter(None, x)) for x in board]) * number)
            boards.remove(board)  # :(

# Part 1:
print(scores[0])

# Part 2:
print(scores[-1])
