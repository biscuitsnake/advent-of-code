import collections

orbits = collections.defaultdict(list)
for line in open("6.txt").readlines():
    a, b = line.strip().split(")")
    orbits[a].append(b)


def count_children(planet):
    total = 0
    if planet not in orbits:
        return 0
    total += len(orbits[planet])
    for i in orbits[planet]:
        total += count_children(i)
    return total


# Part 1 = 308790
print(sum([count_children(x) for x in orbits.keys()]))

# Part 2?
