# Part 1 = 3550236
mass = [int(i.strip()) for i in open("1.txt").readlines()]

total = 0
for m in mass:
    total += m // 3 - 2

print(total)

# Part 2 = 5322455
total = 0
for m in mass:
    module = 0
    while True:
        fuel = m // 3 - 2
        if fuel <= 0:
            break
        else:
            module += fuel
            m = fuel
    total += module

print(total)
