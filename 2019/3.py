import collections

paths = []
for i in open("3.txt").readlines():
    paths.append(i.split(","))

# Part 1 = 709
x = {"R": 1, "L": -1, "U": 0, "D": 0}
y = {"R": 0, "L": 0, "U": 1, "D": -1}


def trace2(path):
    point = (0, 0)
    points = collections.defaultdict(int)
    for p in path:
        for j in range(int(p[1:])):
            points[point] += 1
            point = (point[0] + x[p[0]], point[1] + y[p[0]])
    return points


pointsA = set(trace2(paths[0]))
pointsB = set(trace2(paths[1]))
dists = []
print(pointsA.intersection(pointsB))
for x in pointsA.intersection(pointsB):
    dists.append(abs(x[0]) + abs(x[1]))
print(sorted(dists)[1])

# Part 2
