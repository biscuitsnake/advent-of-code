import numpy

# parse input

file = open('3.txt', 'r')
claims = [id.strip() for id in file]

data = [[]] * 1347
ind = 0

for i in claims:
    a = i.split('@')
    b = a[1].split(':')

    id = a[0].strip('#')
    pos = b[0].strip().split(',')
    size = b[1].strip().split('x')

    pos = [int(j) for j in pos]
    size = [int(k) for k in size]

    data[ind] = [pos, size, id]

    ind += 1

# assumes fabric is 1000x1000 or less

fabric = numpy.zeros((1000, 1000))

# part 1 = 114946

for i in data:
    posx = i[0][0]
    posy = i[0][1]
    width = i[1][0]
    length = i[1][1]

    for j in range(posx, (posx + width)):
        for k in range(posy, (posy + length)):
            fabric[j, k] += 1

print(numpy.count_nonzero(fabric > 1))

# part 2 = 877

for i in data:
    posx = i[0][0]
    posy = i[0][1]
    width = i[1][0]
    length = i[1][1]

    valid = 0
    size = width * length

    for j in range(posx, (posx + width)):
        for k in range(posy, (posy + length)):
            if fabric[j, k] == 1:
                valid += 1
    if valid == size:
        print(i[2])
