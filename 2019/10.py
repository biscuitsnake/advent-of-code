import collections
import math

data = open("10.txt").readlines()
data = [line.strip() for line in data]

asteroids = {}
for i in range(len(data)):
    for j in range(34):
        if data[i][j] == "#":
            asteroids[j, i] = 0
for asteroid in asteroids.keys():
    angles = []
    for a in asteroids.keys():
        if asteroid == a:
            pass
        else:
            angle = math.atan2(a[1] - asteroid[1], a[0] - asteroid[0])
            angles.append(angle)
    angles = set(angles)
    asteroids[asteroid] = len(angles)

# Part 1 = 267 [at (26, 28)]
print(sorted(asteroids.values())[-1])

# Part 2
dists = collections.defaultdict(list)
for asteroid in asteroids.keys():
    if asteroid == (26, 28):
        pass
    else:
        angle = math.atan2(asteroid[1] - 28, asteroid[0] - 26)
        if angle < 0:
            angle = abs(angle) + math.pi
        distance = math.hypot(28 - asteroid[1], 26 - asteroid[0])
        dists[angle].append([asteroid, distance])
for ang in dists:
    dists[ang] = sorted(dists[ang], key=lambda x: x[1])
dists = {key: dists[key] for key in sorted(dists.keys())}
#print(dists)

for i in range(201):
    idx = i % len(dists)
    if i == 199:
        print(list(dists.values())[idx].pop(0))
    else:
        list(dists.values())[idx].pop(0)

