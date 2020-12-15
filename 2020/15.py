import collections
from functools import partial

puzzle = [1, 12, 0, 20, 8, 16]


def game(turns):
    turn = 1
    spoken = collections.defaultdict(partial(collections.deque, maxlen=2))

    for t in puzzle:
        spoken[t].append(turn)
        last_spoken = t
        turn += 1

    while turn <= turns:
        if len(spoken[last_spoken]) == 2:
            last_spoken = spoken[last_spoken][1] - spoken[last_spoken][0]
        else:
            last_spoken = 0
        spoken[last_spoken].append(turn)
        turn += 1
    return last_spoken


print(game(2020))
print(game(30000000))  # slow
