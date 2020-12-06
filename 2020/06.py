puzzle = [i.split("\n") for i in open("06.txt").read().split("\n\n")]

part1, part2 = 0, 0
for p in puzzle:
    q = []
    [q.extend(list(j))for j in p]
    part1 += len(set(q))

    e = [list(k) for k in p]
    part2 += len(set(e[0]).intersection(*e))

print(part1, part2)
