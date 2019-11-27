file = open("4.txt.")

###PART 1###

validPasses = 0

for line in file:
    line = line.strip("\n")
    words = line.split(" ")
    if len(words) == len(set(words)):
        validPasses += 1

print (validPasses)

###PART 2###

validPasses = 0

for line in open("4.txt."):
    line = line.strip("\n")
    words = line.split(" ")
    valid = True
    ind = 0
    for x in words:
        for y in words[(ind+1):len(words)]:
            if set(x) == set(y):
                valid = False
        ind += 1        
    if valid:
        validPasses += 1

print (validPasses)


