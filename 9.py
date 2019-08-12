import collections

# part 1 = 416424

p = 413
last = 71082

players = collections.defaultdict(int)
current_player = 1

current_marble = 0
circle = [0]

for i in range(1, last+1):
    if len(circle) == 1:
        current_marble = 1
        circle.insert(1, i)

    elif i % 23 == 0:
        players[current_player] += i

        if (current_marble - 7) < 0:
            players[current_player] += circle.pop(len(circle) - (7-current_marble))
            current_marble = len(circle) - (7-current_marble) + 1
        else:
            players[current_player] += circle.pop((current_marble) - 7)
            current_marble = current_marble - 7

    else:
        current_marble = current_marble + 2
        if current_marble <= len(circle):
            circle.insert(current_marble, i)
        else:
            current_marble = (current_marble) % len(circle)
            circle.insert(current_marble, i)
    
    i += 1    
    if current_player == p:
        current_player = 1
    else:
        current_player += 1

print (max(players.values()))

