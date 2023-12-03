import re

engine = [row.strip() for row in open("03.txt").readlines()]

neighbours = [
    (-1, -1),
    (-1, 0),
    (-1, 1),
    (0, 1),
    (0, -1),
    (1, 1),
    (1, 0),
    (1, -1),
]

def get_adjacent(cell):
  return [(cell[0] + n[0], cell[1] + n[1]) for n in neighbours]

adj = []
gears = {}
part1 = 0

for (i, row) in enumerate(engine):
  for (j, cell) in enumerate(list(row)):
    if not cell.isdigit() and cell != ".":
      adj.extend(get_adjacent((i, j)))
    if cell == "*":
      gears[(i, j)] = []

for (i, row) in enumerate(engine):
  numbers = re.findall(r'\d+', row)
  start = 0
  for num in numbers:
    ind = row.find(num, start)
    start = ind + len(num)
    for j in range(ind, ind + len(num)):
      for a in get_adjacent((i, j)):
        if (a[0], a[1]) in gears:
          gears[(a[0], a[1])].append(num)
          break

      if ((i, j)) in adj:
        part1 += int(num)
        break

part2 = sum([int(x[0]) * int(x[1]) if len(x) == 2 else 0 for x in gears.values()])

print(part1, part2)    
