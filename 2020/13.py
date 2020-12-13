import math

puzzle = [i.strip() for i in open("13.txt").readlines()]
earliest = int(puzzle[0])
ts = puzzle[1].split(",")

p1 = {}
nox = [int(i) for i in ts if (i != 'x')]
for num in nox:
    m = math.ceil(earliest/num)
    p1[m * num] = num

print((min(p1) - earliest) * p1[min(p1)])

# Chinese Remainder Theorem
def crt(a, b):
    N = math.prod(a)
    x = 0
    for b_i, n in zip(b, a):
        # pow(a, -1, n) is inverse modulo
        x += b_i * (N // n) * pow(N // n, -1, n)
    return x % N

ind = [(int(i[1]) - i[0]) for i in enumerate(ts) if i[1] != 'x']
print(crt(nox, ind))
