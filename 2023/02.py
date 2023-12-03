from math import prod

lines = [i.split(": ") for i in open("02.txt").read().splitlines()]

part1 = 0
part2 = 0

for line in lines:
  game = int(line[0].split(" ")[1])
  valid = True
  sets = line[1].split(";")

  min_rgb = {"red": 0, "green": 0, "blue": 0}

  for set in sets:
    rgb = {"red": 0, "green": 0, "blue": 0}
    cubes = set.strip().split(", ")
    
    for cube in cubes:
      s = cube.split(" ")
      rgb[s[1]] += int(s[0])
    
    if not ((rgb["red"] <= 12) and (rgb["green"] <= 13) and (rgb["blue"] <= 14)):
      valid = False
    
    for colour in min_rgb.keys():
      if rgb[colour] >= min_rgb[colour]:
        min_rgb[colour] = rgb[colour]
  
  if valid:
    part1 += game

  part2 += prod(min_rgb.values())

print(part1, part2)
