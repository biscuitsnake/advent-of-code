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
        else:
            parameters.append(program[program[base + pointer + 1 + i]])
    return parameters


def run(program, id, pointer):
    op, base = 0, 0
    while op != 99:
        #print(base)
        intcode = intcode_list(program[pointer])
        if intcode == [0, 0, 2, 0, 3]:
            print(program[pointer], program[pointer+1])
        op = int(''.join(str(digit) for digit in intcode[3:5]))
        if op == 1:
            parameters = get_params(2, pointer, program, intcode)
            program[program[pointer+3]] = sum(parameters)
            pointer += 4
        if op == 2:
            parameters = get_params(2, pointer, program, intcode, base)
            program[program[pointer+3]] = parameters[0] * parameters[1]
            pointer += 4
        if op == 3:
            parameters = get_params(1, pointer, program, intcode, base)
            print(parameters[0], program[parameters[0]])
            program[program[parameters[0]]] = id.pop(0)
            pointer += 2
        if op == 4:
            if intcode[2] == 1:
                out = program[pointer+1]
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
                program[program[pointer+3]] = 1
            else:
                program[program[pointer+3]] = 0
            pointer += 4
        if op == 8:
            parameters = get_params(2, pointer, program, intcode, base)
            if parameters[0] == parameters[1]:
                program[program[pointer+3]] = 1
            else:
                program[program[pointer+3]] = 0
            pointer += 4
        if op == 9:
            parameters = get_params(1, pointer, program, intcode, base)
            base += parameters[0]
            pointer += 2
    return -1, pointer, program[:]


test = [1102,34915192,34915192,7,4,7,99,0]
test.extend([0 for i in range(4096)])
program.extend([0 for i in range(4096)])
print(run(program[:], [1], 0)[0])
print(run(test[:], [], 0)[0])