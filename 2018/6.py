import numpy

file = open("6.txt")
coords = [] #string coordinates, no spaces
for i in file.readlines():
    i = i.replace(" ", "")
    i = i.strip()
    coord = list(i.split(","))
    coords.append(list(i.split(",")))

# part 1 = 3006

grid = numpy.zeros((400, 400))

# numpy sucks

label = 1
for c in coords:
    grid[int(c[0]), int(c[1])] = label
    label += 1

for i in range(400):    
    for j in range(400):
        shortestDistance = 1000
        x = 1
        for c in coords:
            distance = abs(i - int(c[0])) + abs(j - int(c[1]))
            if distance == shortestDistance:
                marker = 0
            if distance < shortestDistance:
                shortestDistance = distance
                marker = x            
            x += 1
        grid[i, j] = marker

sizes = {}
for i in range(0, 51):
    sizes[i] = numpy.count_nonzero(grid == i)

for i in range(400):
    if grid[i, 0] in sizes:
        del sizes[grid[i, 0]]
    if grid[0, i] in sizes:
        del sizes[grid[0, i]]
    if grid[i, 399] in sizes:
        del sizes[grid[i, 399]]
    if grid[399, i] in sizes:
        del sizes[grid[399, i]]

print(sizes[max(sizes.keys(), key=(lambda x: sizes[x]))])

# part 2 = 42998

grid = numpy.zeros((400, 400))

for i in range(400):    
    for j in range(400):
        totalDistance = 0
        for c in coords:
            totalDistance += abs(i - int(c[0])) + abs(j - int(c[1]))
        if totalDistance < 10000:
            grid[i, j] = 1

print(numpy.count_nonzero(grid == 1))           
