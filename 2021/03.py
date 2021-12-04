from collections import Counter

puzzle = [i.strip() for i in open("03.txt").readlines()]
lp = len(puzzle)
ld = len(puzzle[0])

# Part 1:
gr = ""
for i in range(ld):
    c1 = sum([int(j[i]) for j in puzzle])
    if c1 > lp//2:
        gr += "1"
    else:
        gr += "0"

gr = int(gr, 2)
er = int("1"*ld, 2) ^ gr
print(gr*er)

# Part 2:
def rating(diagnostic, oxygen, ind):
    c = Counter([int(j[ind]) for j in diagnostic])
    mcv = max(c, key=c.get)

    if not oxygen:
        mcv = mcv ^ 1
    if c[0] == c[1]:
        mcv = oxygen * 1

    diagnostic = [n for n in diagnostic if n[ind] == str(mcv)]

    if len(diagnostic) == 1:
        return diagnostic[0]
    else:
        return rating(diagnostic, oxygen, ind+1)

ogr = rating(puzzle, True, 0)
csr = rating(puzzle, False, 0)
print(int(ogr, 2) * int(csr, 2))
