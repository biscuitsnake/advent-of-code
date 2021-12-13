import numpy as np
import matplotlib.pyplot as plt

puzzle = [i.split("\n") for i in open("13.txt").read().split("\n\n")]

dots = {tuple([int(j) for j in i.split(",")]) for i in puzzle[0]}
folds = [[i.split("=")[0][-1], int(i.split("=")[1])] for i in puzzle[1]]

def fold(dots, fold):
    new_dots = set()
    if fold[0] == "y":
        for dot in dots:
            if dot[1] > fold[1]:
                new_dots.add((dot[0], fold[1] - (dot[1] - fold[1])))
            else:
                new_dots.add(dot)
    elif fold[0] == "x":
        for dot in dots:
            if dot[0] > fold[1]:
                new_dots.add((fold[1] - (dot[0] - fold[1]), dot[1]))
            else:
                new_dots.add(dot)

    return new_dots

for i in range(len(folds)):
    dots = fold(dots, folds[i])
    if i == 0:
        # Part 1:
        print(len(dots))

# Part 2: REUPUPKR
arr = np.zeros((6, 39))
arr[[i[1] for i in dots], [j[0] for j in dots]] = 1

plt.imshow(arr)
plt.show()
