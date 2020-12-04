import re
puzzle = [list(i.replace("\n", " ").split(" ")) for i in open("04.txt").read().split("\n\n")]


def check_passport(pport):
    if not 1920 <= int(pport['byr']) <= 2002:
        return False
    if not 2010 <= int(pport['iyr']) <= 2020:
        return False
    if not 2020 <= int(pport['eyr']) <= 2030:
        return False
    if not (pport['hgt'][-2::] == "cm" and 150 <= int(pport['hgt'][0:-2]) <= 193):
        if not (pport['hgt'][-2::] == "in" and 59 <= int(pport['hgt'][0:-2]) <= 76):
            return False
    if not re.match(r"^#[0-9a-f]{6}$", pport['hcl']):
        return False
    if pport['ecl'] not in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
        return False
    if not re.match(r"^[0-9]{9}$", pport['pid']):
        return False
    return True


part1 = 0
part2 = 0
for each in puzzle:
    passport = {}
    for p in each:
        v = p.split(":")
        passport[v[0]] = v[1]
    if (len(passport) == 8) or (len(passport) == 7 and "cid" not in passport.keys()):
        part1 += 1
        if check_passport(passport):
            part2 += 1

print(part1, part2)
