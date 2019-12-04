import collections

wires = []
for i in open("3.txt").readlines():
    wires.append(i.split(","))

# Part 1 = 709
x = {"R": 1, "L": -1, "U": 0, "D": 0}
y = {"R": 0, "L": 0, "U": 1, "D": -1}


def get_points(wire):
    point = (0, 0)
    points = collections.defaultdict(int)
    for w in wire:
        for i in range(int(w[1:])):
            points[point] += 1
            point = (point[0] + x[w[0]], point[1] + y[w[0]])
    return points


def get_steps(wire):
    s = 0
    point = (0, 0)
    steps = collections.defaultdict(list)
    for w in wire:
        for j in range(int(w[1:])):
            s += 1
            point = (point[0] + x[w[0]], point[1] + y[w[0]])
            if point in common:
                steps[point[0], point[1]].append(s)
    return steps


# Part 1 = 709
pointsA = set(get_points(wires[0]))
pointsB = set(get_points(wires[1]))
common = pointsA.intersection(pointsB)
distances = []
for c in common:
    distances.append(abs(c[0]) + abs(c[1]))
print(sorted(distances)[1])

# Part 2 = 13836
stepsA = get_steps(wires[0])
stepsB = get_steps(wires[1])
combined = []
for k in stepsB.keys():
    combined.append(stepsA[k][0] + stepsB[k][0])
print(sorted(combined)[0])
