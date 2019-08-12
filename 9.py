import collections

def game(elves, last_marble):
    players = collections.defaultdict(int)
    current_player = 1

    current_marble = 0
    circle = collections.deque([0])

    for i in range(1, last_marble+1):
        if len(circle) == 1:
            current_marble = 1
            circle.insert(1, i)

        elif i % 23 == 0:
            players[current_player] += i
            circle.rotate(7)
            players[current_player] += circle.pop()
            circle.rotate(-1)

        else:
            circle.rotate(-1)
            circle.append(i)
        
        i += 1
        if current_player == elves:
            current_player = 1
        else:
            current_player += 1

    return max(players.values())


# part 1 = 416424

p = 413
last = 71082
print (game(p, last))

# part 2 = 3498287922

p = 413
last = 71082 * 100
print(game(p, last))
