import re

puzzle = [i.strip("/n") for i in open("18.txt").readlines()]
inner = re.compile(r"\([+*\d ]+\)")
addition = re.compile(r"\d+(?: \+ \d+)+")

# Part 2 doesn't work, but it does work for examples and several lines in my input checked. Could debug via line-by-line
# comparison to a working solution then see what goes wrong on the lines that don't match.


def eval_left_to_right(expression):
    if expression.endswith(")") and expression.startswith("("):
        expression = expression[1:len(expression)-1]
    expression = expression.split(" ")
    while len(expression) > 1:
        expression = [str(eval("".join(expression[0:3])))] + expression[3:]
    return expression[0]


def eval_add_before_mul(expression):
    if expression.endswith(")") and expression.startswith("("):
        expression = expression[1:len(expression)-1]
    matches = re.findall(addition, expression)
    new_matches = [eval(i) for i in matches]
    for old, new in zip(matches, new_matches):
        expression = expression.replace(old, str(new))
    return str(eval(expression))


def parse(line):
    matches = re.findall(inner, line)
    # new_matches = [eval_left_to_right(i) for i in matches]
    new_matches = [eval_add_before_mul(i) for i in matches]
    for old, new in zip(matches, new_matches):
        line = line.replace(old, new)
    print(line)
    return line


def evaluate(exp):
    total = 0
    if exp.count("(") > 0:
        total += evaluate(parse(exp))
    else:
        # total += int(eval_left_to_right(exp))
        total += int(eval_add_before_mul(exp))
    return total


s = 0
for i in puzzle:
    s += evaluate(i)
print(s)
