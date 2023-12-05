lines = [line.strip() for line in open("04.txt").read().splitlines()]

part1 = 0
count = [1]*len(lines)

for index, line in enumerate(lines):
  _, tail = line.split(":")  
  a, b = tail.split("|")

  chosen = [int(i) for i in a.split()]
  winning = [int(i) for i in b.split()]

  score = 0
  for c in chosen:
    if c in winning:
      score += 1

  if score > 0:
    part1 += 2**(score - 1)
  
  for j in range(score):
    count[index + j + 1] += count[index]  

part2 = sum(count)

print(part1, part2)
