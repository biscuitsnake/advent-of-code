###PART 1###

import operator as op

ops = { "<": op.lt, "<=": op.le, ">": op.gt, ">=": op.ge, "==": op.eq, "!=": op.ne}

file = open("8.txt")

instructions = []

for line in file:
    instruction = []
    line = line.strip("\n")
    line = line.replace("if ", "")
    line = line.split(" ")
    for i in line:
        instruction.append(i)
    instructions.append(instruction)

    
registers = {}

for instr in instructions:
    if instr[0] not in registers:
        registers[instr[0]] = 0

highest = 0

for instr in instructions:
    if ops[instr[4]](registers[instr[3]], int(instr[5])):
        if instr[1] == "inc":
            registers[instr[0]] += int(instr[2])
        else:
            registers[instr[0]] -= int(instr[2])
    if registers[instr[0]] > highest:
        highest = int(registers[instr[0]])

maximum = max(registers, key=registers.get)
print ("Largest value after completing instructions: "+ str(registers[maximum]))

###PART 2###

print ("Largest value during process: " +  str(highest))


    

    

        

        
