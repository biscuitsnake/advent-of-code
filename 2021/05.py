from collections import defaultdict

puzzle = [i.strip() for i in open("05.txt").readlines()]
points = defaultdict(int)
points2 = defaultdict(int)

for p in puzzle:
    c = [x.split(",") for x in p.split(" -> ")]
    x1, y1 = int(c[0][0]), int(c[0][1])
    x2, y2 = int(c[1][0]), int(c[1][1])

    if x1 == x2:
        for y in range(min(y1, y2), max(y1, y2) + 1):
            points[(x1, y)] += 1
            points2[(x1, y)] += 1
    elif y1 == y2:
        for x in range(min(x1, x2), max(x1, x2) + 1):
            points[(x, y1)] += 1
            points2[(x, y1)] += 1
    else:
        dx = 1 if (x1 < x2) else -1
        dy = 1 if (y1 < y2) else -1
        points2[(x1, y1)] += 1
        while (x1 != x2) or (y1 != y2):
            x1 += dx
            y1 += dy
            points2[(x1, y1)] += 1

print(sum(x > 1 for x in points.values()))
print(sum(x > 1 for x in points2.values()))
