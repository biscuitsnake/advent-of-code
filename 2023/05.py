lines = open("05.txt").read().split("\n\n")

seeds = [int(x) for x in lines[0].split(":")[1].split()]
maps = [[[int(z) for z in y.split()] for y in  x.split("\n")[1::]] for x in lines[1::]]

sources = {}

for seed in seeds:
  sources[seed] = [seed]
  for i, table in enumerate(maps):
    v = False
    for line in table:
      if sources[seed][i] in range(line[1], (line[1] + line[2])):
        sources[seed].append(sources[seed][i] - (line[1] - line[0]))
        v = True
    if not v:
      sources[seed].append(sources[seed][i])

part1 = min([x[-1] for x in sources.values()])

print(part1)
