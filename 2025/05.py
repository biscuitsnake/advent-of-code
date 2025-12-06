ranges, ids = open("05.txt").read().split("\n\n")
ranges = [list(map(int, r.split("-"))) for r in ranges.splitlines()]
ids = [int(i) for i in ids.splitlines()]

# Part 1

fresh = 0
for id in ids:
    for r in ranges:
        if r[0] <= id <= r[1]:
            fresh += 1
            break

print(fresh)

# Part 2

ranges.sort()

idx = 1
total = 0
while idx < len(ranges):
    curr = ranges[idx]
    prev = ranges[idx - 1]

    if curr[0] <= prev[1]:
        prev[1] = max(prev[1], curr[1])
        ranges[idx - 1] = prev
        ranges.pop(idx)
    else:
        total += prev[1] - prev[0] + 1
        idx += 1

total += ranges[-1][1] - ranges[-1][0] + 1
print(total)
