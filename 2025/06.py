# Part 1

def prd(i):
    result = 1
    for num in i:
        result *= num
    return result


input = [i.split() for i in open("06.txt").read().splitlines()]
numbers = input[:-1]
symbols = input[-1]

human = 0
for i in range(len(numbers[0])):
    integers = [int(numbers[j][i]) for j in range(len(numbers))]
    if symbols[i] == "+":
        human += sum(integers)
    elif symbols[i] == "*":
        human += prd(integers)
    else:
        [print("Unknown symbol: " + symbols[i]), exit()]

print(human)

# Part 2

input = open("06.txt").read().splitlines()

cols = len(input[0])
a, b = cols - 1, cols
cephalopod = 0

while a >= 0:
    if input[-1][a] != " ":
        symbol = input[-1][a]
        integers = [i[a:b] for i in input[:-1]]
        transpose = ["".join(i) for i in zip(*integers)]
        if transpose[-1].isspace():
            transpose.pop()
        if symbol == "+":
            cephalopod += sum([int(i) for i in transpose])
        elif symbol == "*":
            cephalopod += prd([int(i) for i in transpose])
        b = a
    a -= 1

print(cephalopod)
