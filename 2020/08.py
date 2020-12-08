import copy

puzzle = [i.strip().split(" ") for i in open("08.txt").readlines()]
puzzle = [[i[0], int(i[1])] for i in puzzle]

# Part 1
pointer = 0
acc = 0
ran = set()
while True:
    if pointer in ran:
        print(acc)
        break
    ran.add(pointer)
    if puzzle[pointer][0] == 'acc':
        acc += puzzle[pointer][1]
    if puzzle[pointer][0] == 'jmp':
        pointer += puzzle[pointer][1]
        continue
    pointer += 1

def run(prog):
    pointer = 0
    acc = 0
    ran = set()
    while True:
        if pointer == len(prog):
            return acc
        if pointer in ran:
            return False
        ran.add(pointer)
        if prog[pointer][0] == 'acc':
            acc += prog[pointer][1]
        if prog[pointer][0] == 'jmp':
            pointer += prog[pointer][1]
            continue
        pointer += 1

# Part 2
for i in range(len(puzzle)):
    # TIL you can't slice/.copy a list of lists properly
    modified = copy.deepcopy(puzzle)
    if puzzle[i][0] == 'jmp':
        modified[i][0] = 'nop'
    elif puzzle[i][0] == 'nop':
        modified[i][0] = 'jmp'
    x = run(modified)
    if x:
        print(x)
