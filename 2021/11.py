puzzle = [[int(j) for j in i.strip()] for i in open("11.txt").readlines()]

def adjacent(octopi, row, col):
    adj = [(row-1, col-1), (row-1, col), (row-1, col+1), (row, col-1),
           (row, col+1), (row+1, col-1), (row+1, col), (row+1, col+1)]

    for o in adj:
        if (0 <= o[0] <= 9) and (0 <= o[1] <= 9) and (octopi[o[0]][o[1]] != -1):
            octopi[o[0]][o[1]] += 1
    return octopi

def flash(octopi, flashes):
    if all([all([x <= 9 for x in row]) for row in octopi]):
        return octopi, flashes
    else:
        for row in range(10):
            for col in range(10):
                if octopi[row][col] > 9:
                    flashes += 1
                    octopi = adjacent(octopi, row, col)
                    octopi[row][col] = -1
        return flash(octopi, flashes)

def step(octopi, flashes):
    simultaneous = False
    initial_flashes = flashes
    octopi = [[o + 1 for o in p] for p in octopi]
    octopi, flashes = flash(octopi, flashes)
    if (flashes - initial_flashes) == 100:
        simultaneous = True
    octopi = [[0 if (o == -1) else o for o in p] for p in octopi]
    return octopi, flashes, simultaneous

f = 0

# Obviously, this range is specific to my input.
for s in range(490):
    puzzle, f, sim = step(puzzle, f)
    if s == 99:
        part1 = f
    if sim:
        part2 = s + 1

print(part1)
print(part2)

