puzzle = [[b.split(" ") for b in a.strip().split(" | ")] for a in open("08.txt").readlines()]

freq = {4: "e", 6: "b", 8: "c", 9: "f"}
nums = {"abcefg": 0, "cf": 1, "acdeg": 2, "acdfg": 3, "bcdf": 4,
        "abdfg": 5, "abdefg": 6, "acf": 7, "abcdefg": 8, "abcdfg": 9}

part1 = 0
part2 = 0

for p in puzzle:
    # Part 1:
    part1 += sum(x in [2, 4, 3, 7] for x in map(len, p[1]))

    # Part 2:
    seg = {"a": None, "b": None, "c": None, "d": None, "e": None, "f": None, "g": None}
    signal = sorted(p[0], key=len)
    joined = "".join(signal)

    seg["a"] = list(set(signal[1]) - set(signal[0]))[0]
    for letter in list(set("abcdefg") - set(seg.values())):
        if joined.count(letter) in freq:
            seg[freq[joined.count(letter)]] = letter
    a = set(signal[2])
    b = set("abcdefg") - set(seg.values())
    seg["d"] = list(a.intersection(b))[0]
    seg["g"] = list(set("abcdefg") - set(seg.values()))[0]

    seg = dict((v, k) for k, v in seg.items())
    value = ""

    for digit in p[1]:
        actual = "".join(sorted([seg[i] for i in digit]))
        value += str(nums[actual])

    part2 += int(value)

print(part1)
print(part2)
