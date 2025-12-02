def factors(n):
    result = set()
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            result.add(i)
            result.add(n // i)
    result.remove(1)
    return result


ranges = [list(map(int, i.split("-"))) for i in open("02.txt").read().split(",")]

part1 = 0
part2 = 0

for i in ranges:
    for y in range(i[0], i[1] + 1):
        id = str(y)
        length = len(id)
        for factor in factors(length):
            size = length // factor
            chunks = [id[i * size:((i * size) + size)] for i in range(factor)]
            if all(chunks[0] == chunk for chunk in chunks):
                if factor == 2:
                    part1 += y
                part2 += y
                break

print(part1)
print(part2)
