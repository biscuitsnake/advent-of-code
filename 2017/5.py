###PART 1###

file = open("5.txt")

maze = []
for line in file:
    maze.append(int(line.strip("\n")))

n = 0
step = 0
while 0 <= n <= (len(maze)-1):
    jump = maze[n]
    maze[n] += 1
    n += jump
    step += 1

print (step)

###PART 2###

print ("This takes a while...")

file = open("5.txt")

maze = []
for line in file:
    maze.append(int(line.strip("\n")))

n = 0
step = 0
while 0 <= n <= (len(maze)-1):
    jump = maze[n]
    if jump >= 3:
        maze[n] -= 1
    else:
        maze[n] += 1
    n += jump
    step += 1

print (step)
