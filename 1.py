with open('1.txt') as file:
    lines = file.read().splitlines()

lines = list(map(int, lines))

# part 1 = 470

print(sum(map(int, lines)))

# part 2 = 790

total = 0

freqs = []
found = False
i = 0

while not found:
    value = int(lines[i])
    total += value
    if total in freqs:
        print(total)
        found = True
    else:
        freqs.append(total)
    i += 1
    if i == 1014:
        i = 0
