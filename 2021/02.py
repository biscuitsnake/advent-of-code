puzzle = [i.strip().split(" ") for i in open("02.txt").readlines()]

depth = 0
hpos = 0
aim = 0

for i in puzzle:
    if i[0] == "forward":
        hpos += int(i[1])
        depth += aim*int(i[1])
    elif i[0] == "up":
        aim -= int(i[1])
    elif i[0] == "down":
        aim += int(i[1])

# Part 1:
print(hpos*aim)

# Part 2:
print(hpos*depth)
