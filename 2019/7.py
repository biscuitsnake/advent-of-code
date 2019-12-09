import itertools

program = open("7.txt").read().split(",")
program = [int(i) for i in program]


def intcode_list(integer):
    intcode = str(integer).zfill(5)
    intcode = [int(i) for i in intcode]
    return intcode


def get_params(r, pointer, program, intcode):
    parameters = []
    for i in range(r):
        if intcode[0:3][::-1][i] == 0:
            parameters.append(program[program[pointer + 1 + i]])
        else:
            parameters.append(program[pointer + 1 + i])
    return parameters


def run(program, id, pointer):
    op = 0
    while op != 99:
        intcode = intcode_list(program[pointer])
        op = int(''.join(str(digit) for digit in intcode[3:5]))
        if op == 1:
            parameters = get_params(2, pointer, program, intcode)
            program[program[pointer+3]] = sum(parameters)
            pointer += 4
        if op == 2:
            parameters = get_params(2, pointer, program, intcode)
            program[program[pointer+3]] = parameters[0] * parameters[1]
            pointer += 4
        if op == 3:
            program[program[pointer+1]] = id.pop(0)
            pointer += 2
        if op == 4:
            if intcode[2] == 1:
                out = program[pointer+1]
            else:
                out = program[program[pointer + 1]]
            pointer += 2
            return out, pointer, program[:]
        if op == 5:
            parameters = get_params(2, pointer, program, intcode)
            if parameters[0] != 0:
                pointer = parameters[1]
            else:
                pointer += 3
        if op == 6:
            parameters = get_params(2, pointer, program, intcode)
            if parameters[0] == 0:
                pointer = parameters[1]
            else:
                pointer += 3
        if op == 7:
            parameters = get_params(2, pointer, program, intcode)
            if parameters[0] < parameters[1]:
                program[program[pointer+3]] = 1
            else:
                program[program[pointer+3]] = 0
            pointer += 4
        if op == 8:
            parameters = get_params(2, pointer, program, intcode)
            if parameters[0] == parameters[1]:
                program[program[pointer+3]] = 1
            else:
                program[program[pointer+3]] = 0
            pointer += 4
    return -1, pointer, program[:]


def amplifier(program, phase):
    s = 0
    for i in phase:
        s, p, pro = run(program[:], [i, s], 0)
        del p, pro
    return s


def amplifier2(program, phase):
    s = 0
    m = 0
    pointers = [0, 0, 0, 0, 0]
    programs = [program.copy() for _ in range(5)]
    for i in phase:
        s, pointers[m % 5], programs[m % 5] = run(programs[m % 5], [i, s], pointers[m % 5])
        m += 1
    last = 0
    while True:
        s, pointers[m % 5], programs[m % 5] = run(programs[m % 5], [s], pointers[m % 5])
        if (m % 5) == 4:
            last = s
        m += 1
        if s == -1:
            return last


# Part 1 = 273814
signal = 0
for p in itertools.permutations(range(5)):
    val = amplifier(program[:], p)
    if val > signal:
        signal = val
print(signal)

# Part 2 = 34579864
signal = 0
for p in itertools.permutations(range(5, 10)):
    val = amplifier2(program[:], p)
    if val > signal:
        signal = val
print(signal)
