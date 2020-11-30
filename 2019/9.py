program = open("9.txt").read().split(",")
program = [int(i) for i in program]


def intcode_list(integer):
    intcode = str(integer).zfill(5)
    intcode = [int(i) for i in intcode]
    return intcode


def get_params(r, pointer, program, intcode, base):
    parameters = []
    for i in range(r):
        j = intcode[0:3][::-1][i]
        if j == 0:
            parameters.append(program[program[pointer + 1 + i]])
        elif j == 1:
            parameters.append(program[pointer + 1 + i])
        elif j == 2:
            parameters.append(program[pointer + 1 + i] + base)
    return parameters


def run(program, id, pointer):
    op, base = 0, 0
    while op != 99:
        # print(base)
        intcode = intcode_list(program[pointer])
        op = int(''.join(str(digit) for digit in intcode[3:5]))
        if op == 1:
            parameters = get_params(2, pointer, program, intcode, base)
            program[program[pointer + 3]] = sum(parameters)
            pointer += 4
        if op == 2:
            parameters = get_params(2, pointer, program, intcode, base)
            program[program[pointer + 3]] = parameters[0] * parameters[1]
            pointer += 4
        if op == 3:
            parameters = get_params(1, pointer, program, intcode, base)
            try:
                program[parameters[0]] = id.pop(0)
            except:
                pass
            pointer += 2
        if op == 4:
            if intcode[2] == 1:
                out = program[pointer + 1]
            else:
                out = program[program[pointer + 1]]
            pointer += 2
            return out, pointer, program[:]
        if op == 5:
            parameters = get_params(2, pointer, program, intcode, base)
            if parameters[0] != 0:
                pointer = parameters[1]
            else:
                pointer += 3
        if op == 6:
            parameters = get_params(2, pointer, program, intcode, base)
            if parameters[0] == 0:
                pointer = parameters[1]
            else:
                pointer += 3
        if op == 7:
            parameters = get_params(2, pointer, program, intcode, base)
            if parameters[0] < parameters[1]:
                program[program[pointer + 3]] = 1
            else:
                program[program[pointer + 3]] = 0
            pointer += 4
        if op == 8:
            parameters = get_params(2, pointer, program, intcode, base)
            if parameters[0] == parameters[1]:
                program[program[pointer + 3]] = 1
            else:
                program[program[pointer + 3]] = 0
            pointer += 4
        if op == 9:
            parameters = get_params(1, pointer, program, intcode, base)
            base += parameters[0]
            pointer += 2
    return -1, pointer, program[:]

# it doesn't work.
test1 = [109, 1, 204, -1, 1001, 100, 1, 100, 1008, 100, 16, 101, 1006, 101, 0, 99]
test2 = [1102, 34915192, 34915192, 7, 4, 7, 99, 0]
test3 = [104, 1125899906842624, 99]
test4 = [109, 1, 203, 2, 204, 2, 99]

test1.extend([0 for i in range(4092)])
print(run(test1[:], [], 0)[0])

test2.extend([0 for i in range(4092)])
print(run(test2[:], [], 0)[0])

test3.extend([0 for i in range(4092)])
print(run(test3[:], [], 0)[0])

test4.extend([0 for i in range(4092)])
print(run(test4[:], [], 0)[0])

program.extend([0 for i in range(4092)])
print(run(program[:], [1], 0)[0])