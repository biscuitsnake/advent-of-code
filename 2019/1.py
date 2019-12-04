# Part 1 = 3550236
mass = [int(i.strip()) for i in open("1.txt").readlines()]
print(sum([m // 3 - 2 for m in mass]))

# Part 2 = 5322455
total = 0
for m in mass:
    module = 0
    while True:
        m = m // 3 - 2
        if m <= 0:
            break
        else:
            module += m
    total += module

print(total)
