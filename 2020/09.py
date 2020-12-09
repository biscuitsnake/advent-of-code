import itertools

puzzle = [int(i.strip()) for i in open("09.txt").readlines()]

# Part 1
for i in range(25, len(puzzle)):
    pairs = [sum(j) for j in itertools.combinations(puzzle[i-25:i], 2)]    
    if puzzle[i] not in pairs:
        invalid = puzzle[i]
        print(invalid)
        break

# Part 2
for i in range(len(puzzle)):
    for j in range(i+2, len(puzzle)):
        if sum(puzzle[i:j]) == invalid:
            print(min(puzzle[i:j]) + max(puzzle[i:j]))
