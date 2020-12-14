import itertools

puzzle = [i.strip() for i in open('14.txt').readlines()]


def mad(mask, address):
    # this function is disgusting. do not look
    address = bin(address)[2:].zfill(36)
    addresses = []
    new_addr = ''
    for i in zip(mask, address):
        if i[0] == '1':
            new_addr += '1'
        if i[0] == '0':
            new_addr += i[1]
        if i[0] == 'X':
            new_addr += 'X'
    perms = [''.join(p) for p in itertools.product('10', repeat=new_addr.count('X'))]
    for k in perms:
        k = list(k)
        addresses.append(int(''.join([k.pop() if z == 'X' else z for z in new_addr]), 2))
    return addresses


memory = {}
for line in puzzle:
    if line.startswith('mask'):
        mask = line[7:]
    else:
        a = line.split('] = ')
        addr = int(a[0][4:])
        val = int(a[1])
        # Part 1
        # memory[addr] = (int(mask.replace('X', '0'), 2) | val) & (int(mask.replace('X', '1'), 2))
        # End part 1

        # Part 2
        for ad in mad(mask, addr):
            memory[ad] = val
        # End part 2

print(sum(memory.values()))
