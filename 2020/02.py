puzzle = [i.strip().split(" ") for i in open("02.txt").readlines()]

valid = 0
for line in puzzle:
    lower = int(line[0].split("-")[0])
    upper = int(line[0].split("-")[1])
    if lower <= line[2].count(line[1][0]) <= upper:
        valid += 1

print(valid)

valid = 0
for line in puzzle:
    lower = int(line[0].split("-")[0]) - 1
    upper = int(line[0].split("-")[1]) - 1
    if (line[2][lower] == line[1][0]) != (line[2][upper] == line[1][0]):
        valid += 1

print(valid)
