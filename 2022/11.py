import math

monkeys = {}

input = [[y.strip() for y in x.strip().split("\n")] for x in open("11.txt").read().split("\n\n")]

for m in input:
    new = {}
    no = m[0][7:-1]
    new["items"] = [int(x) for x in m[1][16::].split(",")]
    new["op"] = m[2][17::]
    new["test"] = int(m[3][19::])
    new["true"] = m[4][-1]
    new["false"] = m[5][-1]
    monkeys[no] = new

print(monkeys)

for monkey in monkeys:
    print("Monkey {}:".format(monkey))
    c = len(monkeys[monkey]["items"])
    for _ in range(c):
        print("   Monkey inspects an item with a worry level of {}.".format(monkeys[monkey]["items"][-1]))
        old = monkeys[monkey]["items"].pop()
        new = eval(monkeys[monkey]["op"])
        new = math.floor(new / 3)
        if new % monkeys[monkey]["test"]:
            monkeys[monkeys[monkey]["true"]]["items"].append(new)
        else:
            monkeys[monkeys[monkey]["false"]]["items"].append(new)

print(monkeys)