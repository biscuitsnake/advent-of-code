import re
from math import inf
words = [
  ("one", "1"),
  ("two", "2"),
  ("three", "3"),
  ("four", "4"),
  ("five", "5"),
  ("six", "6"),
  ("seven", "7"),
  ("eight", "8"),
  ("nine", "9"),
]

def value(line):
  digits = [(ind, number) for ind, number in enumerate(line) if number.isdigit()]

  return int(digits[0][1] + digits[-1][1])

def translate(line):
  first = (inf, "") # ...
  last = (-1, "")

  for word in words:
    if (ind := line.find(word[0])) != -1:
      if ind <= first[0]:
        first = (ind, word[1])

    if (ind := line.rfind(word[0])) != -1: 
      if ind >= last[0]:
        last = (ind, word[1])

  line = f"{line[:first[0]]}{first[1]}{line[first[0]:]}"
  line = f"{line[:last[0]+1]}{last[1]}{line[last[0]+1:]}"

  return line

def main():
  lines = open("01.txt").read().splitlines()

  part1, part2 = 0, 0
  
  for line in lines:
    part1 += value(line)
    part2 += value(translate(line))

  print(part1, part2)

main()
