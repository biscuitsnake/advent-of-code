puzzle = [int(i) for i in open("01.txt").readlines()]

# Part 1
count = 0
for i in range(1, len(puzzle)):
    if puzzle[i] > puzzle[i - 1]:
        count += 1

print(count)

# Part 2
count2 = 0
for i in range(1, len(puzzle)-2):
    if sum(puzzle[i:i+3]) > sum(puzzle[i-1:i+2]):
        count2 += 1

print(count2)
