puzzle = [i.strip() for i in open("10.txt").readlines()]
pair = {"(": ")", "{": "}", "[": "]", "<": ">"}
table1 = {")": 3, "]": 57, "}": 1197, ">": 25137}
table2 = {"(": 1, "[": 2, "{": 3, "<": 4}

score1 = 0
score2 = []

for p in range(len(puzzle)):
    stack = []
    i = 0
    corrupt = False
    while i < len(puzzle[p]):
        stack.append(puzzle[p][i])
        i += 1
        if len(stack[-2::]) == 2:
            if stack[-2] in pair.keys() and stack[-1] == pair[stack[-2]]:
                stack.pop()
                stack.pop()
            elif (stack[-2] in pair.keys()) and (stack[-1] in pair.values()):
                score1 += table1[stack[-1]]
                corrupt = True
    if not corrupt:
        score = 0
        for s in reversed(stack):
            score = score * 5
            score += table2[s]
        score2.append(score)

print(score1)
print(sorted(score2)[len(score2)//2])
