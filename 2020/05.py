puzzle = [i.strip() for i in open("05.txt").readlines()]


def get_id(c):
    c = c.replace("B", "1")
    c = c.replace("F", "0")
    c = c.replace("R", "1")
    c = c.replace("L", "0")
    return int(c, 2)


ids = [get_id(p) for p in puzzle]
print(max(ids))

for i in range(len(ids)):
    if (i not in ids) and (i+1 in ids) and (i-1 in ids):
        print(i)
