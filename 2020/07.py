import re
from collections import defaultdict

puzzle = [i.strip(".\n").split(" bags contain ") for i in open("07.txt").readlines()]
puzzle = {p[0]: {o[1]: int(o[0]) for o in re.findall(r"(\d+) (\w+ \w+)", p[1])} for p in puzzle}

parents = defaultdict(list)
children = defaultdict(list)

found = set()
def find(colour):
    for c in parents[colour]:
        found.add(c)
        find(c)

def count(colour):
    counted = 0
    counted += len(children[colour])
    for c in children[colour]:
        counted += count(c)
    return counted

for i in puzzle:
    for p in puzzle[i].keys():
        parents[p].append(i)
        children[i].extend([p]*puzzle[i][p])

find("shiny gold")
print(len(found))
print(count("shiny gold"))
