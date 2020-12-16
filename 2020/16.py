import re
import collections

puzzle = [list(i.split("\n")) for i in open("16.txt").read().split("\n\n")]
rules = [[r.split(":")[0], [int(j) for j in re.search(r'\w+\s*\w*: (\d+)-(\d+) or (\d+)-(\d+)', r).groups()]] for r in puzzle[0]]
my_ticket = [int(m) for m in puzzle[1][1].split(",")]
tickets = [[int(k) for k in list(t.split(","))] for t in puzzle[2][1:]]


def check_ticket(ticket):
    invalid = 0
    count = 0  # screaming
    for t in ticket:
        valid = False
        for r in rules:
            if (r[1][0] <= t <= r[1][1]) or (r[1][2] <= t <= r[1][3]):
                valid = True
        if not valid:
            invalid += t
            count += 1
    return invalid, count


def check_value(value, rule):
    if (rule[0] <= value <= rule[1]) or (rule[2] <= value <= rule[3]):
        return True
    else:
        return False


error = 0
valid_tickets = []
for t in tickets:
    e, num = check_ticket(t)
    if num == 0:
        valid_tickets.append(t)
    else:
        error += e

print(error)

fields = collections.defaultdict(list)
valid_tickets.append(my_ticket)
for i in range(20):
    col = []
    for each in valid_tickets:
        col.append(each[i])
    for r in rules:
        if all([check_value(tok, r[1]) for tok in col]):
            fields[r[0]].append(i)

# Doing the rest manually because I'm not bothered
for k in sorted(fields, key=lambda k: len(fields[k])):
    print(k, fields[k])
# Yes.. I should probably upgrade to Python 3.8
print(my_ticket[1]*my_ticket[5]*my_ticket[7]*my_ticket[9]*my_ticket[12]*my_ticket[15])
