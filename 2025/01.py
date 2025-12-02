lines = [[i[0], int(i[1:])] for i in open("01.txt").read().splitlines()]

dial = 50
part1 = 0
part2 = 0

for line in lines:
    dir = line[0]
    val = line[1]

    if dir == "R":
        for i in range(0, val):
            dial += 1
            dial %= 100
            if dial == 0:
                part2 += 1
    if dir == "L":
        for i in range(0, val):
            dial -= 1
            dial %= 100
            if dial == 0:
                part2 += 1

    if dial == 0:
        part1 += 1

print(part1)
print(part2)
