program = open("5.txt").read().split(",")
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


def run(program, id):
    pointer = 0
    op = 0
    while op != 99:
        intcode = intcode_list(program[pointer])
        op = intcode[4]
        if op == 1:
            parameters = get_params(2, pointer, program, intcode)
            program[program[pointer+3]] = sum(parameters)
            pointer += 4
        if op == 2:
            parameters = get_params(2, pointer, program, intcode)
            program[program[pointer+3]] = parameters[0] * parameters[1]
            pointer += 4
        if op == 3:
            program[program[pointer+1]] = id
            pointer += 2
        if op == 4:
            if intcode[2] == 1:
                out = program[pointer+1]
            else:
                out = program[program[pointer + 1]]
            if out != 0:
                print(out)
                break
            pointer += 2
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


# Part 1 = 7566643
run(program[:], 1)

# Part 2 = 9265694
run(program[:], 5)
