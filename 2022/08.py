lines = [[int(j) for j in list(i.strip())] for i in open("08.txt")]

def calc_scenic(dirs, tree):
    score = 1
    for dir in dirs:
        c = 0
        for x in dir:
            if x < tree:
                c += 1
            elif x == tree:
                c += 1
                break
        score *= c
    return score

forest = {}
w = len(lines[0])
h = len(lines)
score = 0
for i, row in enumerate(lines):
    for j, tree in enumerate(row):
        forest[(i,j)] = False

        up = [x[j] for x in lines[0:i]]# rev
        down = [x[j] for x in lines[i+1::]]
        left = row[0:j]# rev
        right = row[j+1:w]

        up.reverse()
        left.reverse()

        dirs = (up, down, left, right)
        if any([all([x < tree for x in dir]) for dir in dirs]):
            forest[(i,j)] = True
        if (res := calc_scenic(dirs, tree)) > score:
            score = res

visible = 0
for i in forest:
    if forest[i]:
        visible += 1

print(visible)    
print(score)
