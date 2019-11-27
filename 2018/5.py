import string

# part 1 = 9900

file = open('5.txt')
polymer = list(file.read())
polymer.pop()

reaction = True
totalDes = 0

while reaction:
    destroyed = False
    i = 0
    r = True

    while r:
        f = polymer[i]
        s = polymer[i + 1]
        if (f.isupper() != s.isupper()) and (f.lower() == s.lower()):
            del polymer[i:i + 2]
            destroyed = True
            totalDes += 2
        i += 1
        if i >= (len(polymer)) - 1:
            r = False

    if not destroyed:
        print(len(polymer))
        reaction = False

# part 2 = 4992
# hashtag slow

types = {}

for letter in string.ascii_lowercase:
    unit = letter.upper() + letter  # Aa
    new_polymer = [x for x in polymer if x not in unit]

    reaction = True
    totalDes = 0

    while reaction:
        destroyed = False
        i = 0
        r = True

        while r:
            f = new_polymer[i]
            s = new_polymer[i + 1]
            if (f.isupper() != s.isupper()) and (f.lower() == s.lower()):
                del new_polymer[i:i + 2]
                destroyed = True
                totalDes += 2
            i += 1
            if (i >= (len(new_polymer)) - 1):
                r = False

        if not destroyed:
            types[unit] = (len(new_polymer))
            reaction = False

print(min(types.values()))
