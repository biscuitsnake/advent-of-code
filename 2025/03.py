def joltage(n, bank):
    start = 0
    length = len(bank)
    output = []
    for i in range(n)[::-1]:
        rng = bank[start:length - i]
        maximum = max(rng)
        start += rng.index(maximum) + 1
        output.append(maximum)
    return int(''.join(str(num) for num in output))


banks = open("03.txt").read().splitlines()

part1 = sum(joltage(2, bank) for bank in banks)
part2 = sum(joltage(12, bank) for bank in banks)

print(part1)
print(part2)
