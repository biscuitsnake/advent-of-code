puzzle = [int(i) for i in open("06.txt").readline().split(",")]
states = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0}

for fish in puzzle:
    states[fish] += 1

for day in range(1, 257):
    pass
    zeros = states[0]
    states[0] = 0
    for i in range(1, 9):
        states[i-1] = states[i]
    states[8] = 0
    states[6] += zeros
    states[8] += zeros

    if day == 80:
        print("Day {}:".format(day), sum(states.values()))
    if day == 256:
        print("Day {}".format(day), sum(states.values()))
