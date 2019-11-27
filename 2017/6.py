###PART 1###

block = [14, 0, 15, 12, 11, 11, 3, 5, 1, 6, 8, 4, 9, 1, 8, 4]
blocks =  []

cycle = 0

while block not in blocks:
    blocks.append(block)
    new_block = block[:]
    redistbl = max(new_block)
    start = new_block.index(redistbl)
    new_block[start] = 0
    start += 1

    if start > 15:
        start -= 16

    for i in range(redistbl):
        new_block[start] += 1
        start += 1
        if start > 15:
            start -= 16

    cycle += 1
    block = new_block[:]

print (cycle)
block = block[:]
print (block)

###PART 2###

blocks =  []

cycle = 0

while block not in blocks:
    blocks.append(block)
    new_block = block[:]
    redistbl = max(new_block)
    start = new_block.index(redistbl)
    new_block[start] = 0
    start += 1

    if start > 15:
        start -= 16

    for i in range(redistbl):
        new_block[start] += 1
        start += 1
        if start > 15:
            start -= 16

    cycle += 1
    block = new_block[:]


print (cycle)
