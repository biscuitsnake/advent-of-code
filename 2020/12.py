puzzle = [[i[0], int(i[1:])] for i in open("12.txt").readlines()]
dirs = {'N': [0, 1], 'E': [1, 0], 'S': [0, -1], 'W': [-1, 0]}
comp = {0: 'N', 1: 'E', 2: 'S', 3: 'W'}


def move(instructions):
    position = [1, 0, 0]
    for i in instructions:
        cmd = i[0]
        if cmd == 'R':
            position[0] = (position[0] + int(i[1]/90)) % 4
        if cmd == 'L':
            position[0] = (position[0] - int(i[1]/90)) % 4
        if cmd == 'F':
            cmd = comp[position[0]]
        if cmd in dirs:
            position[1] += dirs[cmd][0] * i[1]
            position[2] += dirs[cmd][1] * i[1]
    return position


def move2(instructions):
    position = [1, 0, 0]
    waypoint = [10, 1]
    for i in instructions:
        cmd = i[0]
        if cmd == 'R':
            for j in range(int(i[1]/90) % 4):
                waypoint[0], waypoint[1] = waypoint[1], -waypoint[0]
        if cmd == 'L':
            for j in range(int(i[1] / 90) % 4):
                waypoint[0], waypoint[1] = -waypoint[1], waypoint[0]
        if cmd == 'F':
            position[1] += waypoint[0] * i[1]
            position[2] += waypoint[1] * i[1]
        if cmd in dirs:
            waypoint[0] += dirs[cmd][0] * i[1]
            waypoint[1] += dirs[cmd][1] * i[1]
    return position


part1 = move(puzzle)
print(abs(part1[1]) + abs(part1[2]))

part2 = move2(puzzle)
print(abs(part2[1]) + abs(part2[2]))
