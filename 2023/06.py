from math import prod

document = open("06.txt").read().splitlines()

times = document[0].split()[1:]
distances = document[1].split()[1:]

time = int("".join(times))
distance = int("".join(distances))

times = [int(x) for x in times]
distances = [int(x) for x in distances]

ways = []

for index, t in enumerate(times):
  winnable = 0
  for i in range(1, t):
    d = i * (t - i)
    if d > distances[index]:
      winnable += 1
  ways.append(winnable)

part1 = prod(ways)

part2 = 0

for i in range(1, time):
  d = i * (time - i)
  if d > distance:
    part2 += 1

print(part1, part2)
