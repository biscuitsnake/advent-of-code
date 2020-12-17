import itertools

puzzle = [list(i.strip()) for i in open("17.txt")]

on = set()

for row, y in enumerate(puzzle):
    for col, x in enumerate(y):
        if x == "#":
            on.add((col, row, 0))

for i in range(6):
    new_on = set()
    dim = itertools.product(list(range(-16, 16)), list(range(-16, 16)), list(range(-16, 16)))
    for d in dim:
        active_neighbours = 0
        for ix in [-1, 0, 1]:
            for iy in [-1, 0, 1]:
                for iz in [-1, 0, 1]:
                    if (d[0]+ix, d[1]+iy, d[2]+iz) in on and (ix, iy, iz) != (0, 0, 0):
                        active_neighbours += 1
        if d in on and active_neighbours in [2, 3]:
            new_on.add(d)
        if d not in on and active_neighbours == 3:
            new_on.add(d)
    on = new_on

print(len(on))

# todo; do both parts in one chunk!
# Part 2 takes AGES; fix by checking only cells that need to be checked

on = set()

for row, y in enumerate(puzzle):
    for col, x in enumerate(y):
        if x == "#":
            on.add((col, row, 0, 0))

for i in range(6):
    new_on = set()
    dim = itertools.product(list(range(-16, 16)), list(range(-16, 16)), list(range(-16, 16)), list(range(-16, 16)))
    for (x, y, z, w) in dim:
        active_neighbours = 0
        for ix in [-1, 0, 1]:
            for iy in [-1, 0, 1]:
                for iz in [-1, 0, 1]:
                    for iw in [-1, 0, 1]:
                        if (x+ix, y+iy, z+iz, w+iw) in on and (ix, iy, iz, iw) != (0, 0, 0, 0):
                            active_neighbours += 1
        if (x, y, z, w) in on and active_neighbours in [2, 3]:
            new_on.add((x, y, z, w))
        if (x, y, z, w) not in on and active_neighbours == 3:
            new_on.add((x, y, z, w))
    on = new_on

print(len(on))
