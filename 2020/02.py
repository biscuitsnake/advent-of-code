puzzle = [i.strip().split(" ") for i in open("02.txt").readlines()]

valid1, valid2 = 0, 0
for line in puzzle:
    lower = int(line[0].split("-")[0])
    upper = int(line[0].split("-")[1])
    if lower <= line[2].count(line[1][0]) <= upper:
        valid1 += 1
    if (line[2][lower-1] == line[1][0]) != (line[2][upper-1] == line[1][0]):
        valid2 += 1

print(valid1)
print(valid2)
