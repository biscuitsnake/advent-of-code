from collections import defaultdict

f = open("14.txt")
polymer = f.readline().strip()
f.readline()
rules = {i.split(" -> ")[0]: i.strip().split(" -> ")[1] for i in f.readlines()}

pairs = defaultdict(int)
chars = defaultdict(int)

for i in range(len(polymer) - 1):
    pairs[polymer[i:i+2]] += 1

for i in polymer:
    chars[i] += 1

def step(ps, cs):
    orig = ps.copy()
    for pair in orig:
        if pair in rules:
            cs[rules[pair]] += orig[pair]
            ps[pair[0] + rules[pair]] += orig[pair]
            ps[rules[pair] + pair[1]] += orig[pair]
            ps[pair] -= orig[pair]
    return ps, cs

for s in range(40):
    pairs, chars = step(pairs, chars)
    if s == 9:
        c = chars.values()
        print(max(c) - min(c))


c = chars.values()
print(max(c) - min(c))
